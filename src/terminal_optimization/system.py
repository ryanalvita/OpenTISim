# package(s) for data handling
import pandas as pd
import numpy as np

# Used for making the graph to visualize our problem
import networkx as nx

# terminal_optimization package
from terminal_optimization.objects import *
from terminal_optimization import defaults


class System:
    def __init__(self, startyear=2019, lifecycle=20, operational_hours=4680, elements=[], supply_chains=[],
                 supply_graph=[], cargo_type=[],
                 cargo_forecast=[],
                 traffic_forecast=[]):
        # time inputs
        self.startyear = startyear
        self.lifecycle = lifecycle
        self.operational_hours = operational_hours

        # status terminal @ T=startyear
        self.supply_chains = supply_chains
        self.supply_graph = supply_graph
        self.elements = elements

        # cargo and traffic inputs
        self.cargo_type = cargo_type
        self.cargo_forecast = cargo_forecast
        self.traffic_forecast = traffic_forecast

    def simulate(self, startyear=2019, lifecycle=20):
        """ Terminal design optimization

        Based on:
        - Ijzermans, W., 2019. Terminal design optimization. Adaptive agribulk terminal planning
          in light of an uncertain future. Master's thesis. Delft University of Technology, Netherlands.
          URL: http://resolver.tudelft.nl/uuid:7ad9be30-7d0a-4ece-a7dc-eb861ae5df24.
        - Van Koningsveld, M. and J. P. M. Mulder. 2004. Sustainable Coastal Policy Developments in the
          Netherlands. A Systematic Approach Revealed. Journal of Coastal Research 20(2), pp. 375-385

        Apply frame of reference style decisions while stepping through each year of the terminal
        lifecycle and check if investment is needed (in light of strategic objective, operational objective,
        QSC, decision recipe, intervention method):
        1. step through investment decisions
        2. collect cash flows
        3. collect revenues
        4. calculate profits
        5. apply WACC to cashflows and revenues
        6. aggregate to NPV

        """

        # 1. step through investment decisions
        for year in range(startyear, startyear + lifecycle):
            """
            strategic objective: create a profitable enterprise (NPV > 0)
            operational objective: provide infrastructure of just sufficient quality
            """
            print('')
            print('Simulate year: {}'.format(year))

            # estimate traffic from commodity scenarios
            handysize, handymax, panamax, total_calls, total_vol = self.calculate_vessel_calls(year)
            print('  Total vessel calls: {}'.format(total_calls))
            print('     Handysize calls: {}'.format(handysize))
            print('     Handymax calls: {}'.format(handymax))
            print('     Panamax calls: {}'.format(panamax))
            print('  Total cargo volume: {}'.format(total_vol))

            allowable_berth_occupancy = .4  # is 40 %
            self.berth_invest(year, allowable_berth_occupancy, handysize, handymax, panamax)

            # NB: quay_conveyor, storage, hinterland_conveyor and unloading_station follow from berth
            # self.conveyor_invest(year, 1000)
            #
            # self.storage_invest(year, 10000)
            #
            # self.conveyor_invest(year, 1000)
            #
            # # self.calculate_train_calls(year)
            # self.unloading_station_invest(year, 1000)

        # 2. collect cash flows

        # 3. collect revenues

        # 4. calculate profits

        # 5. apply WACC to cashflows and revenues

        # 6. aggregate to NPV

    def create_data_dict(self, obj):
        """Function to create a dict with important capex and opex data."""

        # add cash flow information to quay_wall object in a dataframe
        data = {}

        data['year'] = list(range(self.startyear, self.startyear + self.lifecycle))
        try:
            data['capex'] = list(np.multiply(0, range(self.startyear, obj.year_online - 1))) + [
                obj.capex] + list(
                np.multiply(0, range(obj.year_online, self.startyear + self.lifecycle)))
        except:
            pass

        try:
            data['maintenance'] = list(np.multiply(0, range(self.startyear, obj.year_online - 1))) + \
                                  list(np.multiply(obj.maintenance,
                                                   len(range(obj.year_online - 1, self.startyear + self.lifecycle)) * [
                                                       1]))
        except:
            pass

        try:
            data['insurance'] = list(np.multiply(0, range(self.startyear, obj.year_online - 1))) + \
                                list(np.multiply(obj.maintenance,
                                                 len(range(obj.year_online - 1, self.startyear + self.lifecycle)) * [
                                                     1]))
        except:
            pass

        try:
            data['energy'] = list(np.multiply(0, range(self.startyear, obj.year_online - 1))) + \
                             list(np.multiply(obj.energy,
                                              len(range(obj.year_online - 1, self.startyear + self.lifecycle)) * [
                                                  1]))
        except:
            pass

        try:
            data['labour'] = list(np.multiply(0, range(self.startyear, obj.year_online - 1))) + \
                             list(np.multiply(obj.labour,
                                              len(range(obj.year_online - 1, self.startyear + self.lifecycle)) * [
                                                  1]))
        except:
            pass

        return data

    def calculate_vessel_calls(self, year=2019):
        """Calculate volumes to be transported and the number of vessel calls (both per vessel type and in total) """

        # intialize values to be returned
        handysize_vol = 0
        handymax_vol = 0
        panamax_vol = 0
        total_vol = 0

        # gather volumes from each commodity scenario and calculate how much is transported with which vessel
        commodities = self.find_elements(Commodity)
        for commodity in commodities:
            # todo: check what commodity.utilisation means (Wijnands multiplies by utilisation)
            volume = commodity.scenario_data.loc[commodity.scenario_data['year'] == year]['volume'].item()
            handysize_vol += volume * commodity.handysize_perc / 100
            handymax_vol += volume * commodity.handymax_perc / 100
            panamax_vol += volume * commodity.panamax_perc / 100
            total_vol += volume

        # gather vessels and calculate the number of calls each vessel type needs to make
        vessels = self.find_elements(Vessel)
        for vessel in vessels:
            if vessel.type == 'Handysize':
                handysize_calls = int(np.ceil(handysize_vol / vessel.call_size))
            elif vessel.type == 'Handymax':
                handymax_calls = int(np.ceil(handymax_vol / vessel.call_size))
            elif vessel.type == 'Panamax':
                panamax_calls = int(np.ceil(panamax_vol / vessel.call_size))
        total_calls = np.sum([handysize_calls, handymax_calls, panamax_calls])

        return handysize_calls, handymax_calls, panamax_calls, total_calls, total_vol

    def calculate_berth_occupancy(self, handysize, handymax, panamax):
        """
        - Find all cranes and sum their effective_capacity to get service_capacity
        - Divide callsize_per_vessel by service_capacity and add mooring time to get total time at berth
        - Occupancy is total_time_at_berth divided by operational hours
        """

        # list all crane objects in system
        list_of_elements_1 = self.find_elements(Cyclic_Unloader)
        list_of_elements_2 = self.find_elements(Continuous_Unloader)
        list_of_elements = list_of_elements_1 + list_of_elements_2

        # find the total service rate and determine the time at berth (in hours, per vessel type and in total)
        if list_of_elements != []:
            service_rate = 0
            for element in list_of_elements:
                service_rate += element.effective_capacity

            time_at_berth_handysize = handysize * (
                    (defaults.handysize_data["call_size"] / service_rate) + defaults.handysize_data["mooring_time"])
            time_at_berth_handymax = handymax * (
                    (defaults.handymax_data["call_size"] / service_rate) + defaults.handymax_data["mooring_time"])
            time_at_berth_panamax = panamax * (
                    (defaults.panamax_data["call_size"] / service_rate) + defaults.panamax_data["mooring_time"])

            total_time_at_berth = np.sum([time_at_berth_handysize, time_at_berth_handymax, time_at_berth_panamax])

            # berth_occupancy is the total time at berth devided by the operational hours
            berth_occupancy = total_time_at_berth / self.operational_hours
        else:
            # if there are no cranes the berth occupancy is 'infinite' so a berth is certainly needed
            berth_occupancy = float("inf")

        return berth_occupancy

    def check_crane_slot_available(self):
        list_of_elements = self.find_elements(Berth)
        slots = 0
        for element in list_of_elements:
            slots += element.max_cranes

        list_of_elements_1 = self.find_elements(Cyclic_Unloader)
        list_of_elements_2 = self.find_elements(Continuous_Unloader)
        list_of_elements = list_of_elements_1 + list_of_elements_2

        # when there are more slots than installed cranes ...
        if slots > len(list_of_elements):
            return True
        else:
            return False

    def find_elements(self, obj):
        """return elements of type obj part of self.elements"""

        list_of_elements = []
        if self.elements != []:
            for element in self.elements:
                if isinstance(element, obj):
                    list_of_elements.append(element)

        return list_of_elements

    def report_element(self, Element, year):
        elements = 0
        elements_online = 0
        element_name = []
        list_of_elements = self.find_elements(Element)
        if list_of_elements != []:
            for element in list_of_elements:
                element_name = element.name
                elements += 1
                if year >= element.year_online:
                    elements_online += 1

        print('     a total of {} {} is online; {} total planned'.format(elements_online, element_name, elements))

        return elements_online, elements

    def berth_invest(self, year, allowable_berth_occupancy, handysize, handymax, panamax):
        """
        Given the overall objectives of the terminal

        Decision recipe Berth:
        QSC: berth_occupancy
        Problem evaluation: there is a problem if the berth_occupancy > allowable_berth_occupancy
            - allowable_berth_occupancy = .40 # 40%
            - a berth needs:
               - a quay
               - cranes (min:1 and max: max_cranes)
            - berth occupancy depends on:
                - total_calls and total_vol
                - total_service_capacity as delivered by the cranes
        Investment decisions: invest enough to make the berth_occupancy < allowable_berth_occupancy
            - adding quay and cranes decreases berth_occupancy_rate
        """

        # report on the status of all berth elements
        berths_online, berths = self.report_element(Berth, year)
        self.report_element(Quay_wall, year)
        self.report_element(Cyclic_Unloader, year)
        self.report_element(Continuous_Unloader, year)
        print('')
        print('  Start analysis:')

        # calculate berth occupancy
        berth_occupancy = self.calculate_berth_occupancy(handysize, handymax, panamax)
        print('     Berth occupancy (@ start of year): {}'.format(berth_occupancy))

        while berth_occupancy > allowable_berth_occupancy:

            # add a berth when no crane slots are available
            if not (self.check_crane_slot_available()):
                print('  *** add Berth to elements')
                berth = Berth(**defaults.berth_data)
                berth.year_online = year + berth.delivery_time
                self.elements.append(berth)

                berth_occupancy = self.calculate_berth_occupancy(handysize, handymax,
                                                                 panamax)
                print('     Berth occupancy (after adding berth): {}'.format(berth_occupancy))

            # check if a quay is needed
            berths = len(self.find_elements(Berth))
            quay_walls = len(self.find_elements(Quay_wall))
            if berths > quay_walls:
                length = max(defaults.handysize_data["LOA"], defaults.handymax_data["LOA"],
                             defaults.panamax_data["LOA"])
                draft = max(defaults.handysize_data["draft"], defaults.handymax_data["draft"],
                            defaults.panamax_data["draft"])
                max_sinkage = 0.5
                wave_motion = 0.5
                safety_margin = 0.5
                depth = np.sum([draft, max_sinkage, wave_motion, safety_margin])
                self.quay_invest(year, length, depth)

                berth_occupancy = self.calculate_berth_occupancy(handysize, handymax, panamax)
                print('     Berth occupancy (after adding quay): {}'.format(berth_occupancy))

            # check if a crane is needed
            if self.check_crane_slot_available():
                self.crane_invest(year)

                berth_occupancy = self.calculate_berth_occupancy(handysize, handymax, panamax)
                print('     Berth occupancy (after adding crane): {}'.format(berth_occupancy))

    def quay_invest(self, year, length, depth):
        """
        *** Decision recipe Quay: ***
        QSC: quay_per_berth
        problem evaluation: there is a problem if the quay_per_berth < 1
        investment decisions: invest enough to make the quay_per_berth = 1
            - adding quay will increase quay_per_berth
            - quay_wall.length must be long enough to accommodate largest expected vessel
            - quay_wall.depth must be deep enough to accommodate largest expected vessel
            - quay_wall.freeboard must be high enough to accommodate largest expected vessel
        """

        print('  *** add Quay to elements')
        quay_wall = Quay_wall(**defaults.quay_wall_data)

        # - capex
        unit_rate = int(
            quay_wall.Gijt_constant * (depth * 2 + quay_wall.freeboard) ** quay_wall.Gijt_coefficient)
        mobilisation = int(max((length * unit_rate * quay_wall.mobilisation_perc), quay_wall.mobilisation_min))
        quay_wall.capex = int(length * unit_rate + mobilisation)

        # - opex
        quay_wall.insurance = quay_wall.capex * quay_wall.insurance_perc
        quay_wall.maintenance = quay_wall.capex * quay_wall.maintenance_perc
        quay_wall.year_online = year + quay_wall.delivery_time

        # add cash flow information to quay_wall object in a dataframe
        data = self.create_data_dict(quay_wall)
        quay_wall.df = pd.DataFrame(data=data)

        self.elements.append(quay_wall)

    def crane_invest(self, year):
        """current strategy is to add cranes as soon as a service trigger is achieved
        - find out how much service capacity is online
        - find out how much service capacity is planned
        - find out how much service capacity is needed
        - add service capacity until service_trigger is no longer exceeded
        """

        # # from all Crane objects sum online length
        # service_capacity = 0
        # service_capacity_online = 0
        # list_of_elements_1 = self.find_elements(Cyclic_Unloader)
        # list_of_elements_2 = self.find_elements(Continuous_Unloader)
        # list_of_elements = list_of_elements_1 + list_of_elements_2
        # if list_of_elements != []:
        #     for element in list_of_elements:
        #         service_capacity += element.lifting_capacity * element.hourly_cycles * element.eff_fact * self.operational_hours
        #         if year >= element.year_online:
        #             service_capacity_online += element.lifting_capacity * element.hourly_cycles * element.eff_fact * self.operational_hours
        #
        # print('a total of {} ton of crane service capacity is online; {} ton total planned'.format(
        #     service_capacity_online,
        #     service_capacity))
        #
        # # check if total planned length is smaller than target length, if so add a quay
        # while service_capacity < service_capacity_trigger:
        print('  *** add Harbour crane to elements')
        crane = Cyclic_Unloader(**defaults.harbour_crane_data)

        # - capex
        delta = 1
        unit_rate = crane.unit_rate
        mobilisation = delta * unit_rate * crane.mobilisation_perc
        crane.capex = int(delta * unit_rate + mobilisation)

        # - opex
        crane.insurance = crane.capex * crane.insurance_perc
        crane.maintenance = crane.capex * crane.maintenance_perc

        occupancy = 0.8  # todo: Figure out occupancy
        consumption = crane.consumption
        hours = self.operational_hours * occupancy
        crane.energy = consumption * hours

        labour = Labour(**defaults.labour_data)
        crane.labour = crane.crew * self.operational_hours / labour.shift_length
        crane.year_online = year + crane.delivery_time

        # add cash flow information to quay_wall object in a dataframe
        data = self.create_data_dict(crane)
        crane.df = pd.DataFrame(data=data)

        self.elements.append(crane)

        # service_capacity += crane.lifting_capacity * crane.hourly_cycles * crane.eff_fact * self.operational_hours

        # print('a total of {} ton of crane service capacity is online; {} ton total planned'.format(
        #     service_capacity_online,
        #     service_capacity))

    def storage_invest(self, year, storage_trigger):
        """current strategy is to add storage as long as target storage is not yet achieved
        - find out how much storage is online
        - find out how much storage is planned
        - find out how much storage is needed
        - add storage until target is reached
        """

        # from all Quay objects sum online length
        storage = 0
        storage_online = 0
        list_of_elements = self.find_elements(Storage)
        if list_of_elements != []:
            for element in list_of_elements:
                storage += element.capacity
                if year >= element.year_online:
                    storage_online += element.capacity

        print('a total of {} ton of storage capacity is online; {} ton total planned'.format(storage_online, storage))

        # check if total planned length is smaller than target length, if so add a quay
        while storage < storage_trigger:
            print('add Storage to elements')
            silo = Storage(**defaults.silo_data)

            # - capex
            silo.capex = silo.unit_rate * silo.capacity + silo.mobilisation_min

            # - opex
            silo.insurance = silo.capex * silo.insurance_perc
            silo.maintenance = silo.capex * silo.maintenance_perc
            silo.energy = silo.consumption * silo.capacity * self.operational_hours

            occupancy = 0.8  # todo: Figure out occupancy
            consumption = silo.consumption
            capacity = silo.capacity
            hours = self.operational_hours
            silo.energy = consumption * capacity * hours

            silo.year_online = year + silo.delivery_time

            # add cash flow information to quay_wall object in a dataframe
            data = self.create_data_dict(silo)
            silo.df = pd.DataFrame(data=data)

            self.elements.append(silo)

            storage += silo.capacity

        print('a total of {} ton of storage capacity is online; {} ton total planned'.format(storage_online, storage))

    def conveyor_invest(self, year, service_capacity_trigger):
        """current strategy is to add conveyors as soon as a service trigger is achieved
        - find out how much service capacity is online
        - find out how much service capacity is planned
        - find out how much service capacity is needed
        - add service capacity until service_trigger is no longer exceeded
        """

        # from all Conveyor objects sum online capacity
        service_capacity = 0
        service_capacity_online = 0
        list_of_elements = self.find_elements(Conveyor)
        if list_of_elements != []:
            for element in list_of_elements:
                service_capacity += element.capacity_steps
                if year >= element.year_online:
                    service_capacity_online += element.capacity_steps
        # todo: understand conveyors capacity formulation

        print('a total of {} ton of conveyor service capacity is online; {} ton total planned'.format(
            service_capacity_online,
            service_capacity))

        # check if total planned length is smaller than target length, if so add a quay
        while service_capacity < service_capacity_trigger:
            print('add Conveyor to elements')
            conveyor = Conveyor(**defaults.quay_conveyor_data)

            # - capex
            delta = conveyor.capacity_steps
            unit_rate = 6.0 * conveyor.length
            mobilisation = conveyor.mobilisation
            conveyor.capex = int(delta * unit_rate + mobilisation)

            # - opex
            conveyor.insurance = conveyor.capex * conveyor.insurance_perc
            conveyor.maintenance = conveyor.capex * conveyor.maintenance_perc
            occupancy = 0.8  # todo: Figure out occupancy
            consumption = conveyor.capacity_steps * conveyor.consumption_coefficient + conveyor.consumption_constant
            hours = self.operational_hours * occupancy
            conveyor.energy = consumption * hours

            conveyor.year_online = year + conveyor.delivery_time

            # add cash flow information to quay_wall object in a dataframe
            data = self.create_data_dict(conveyor)
            conveyor.df = pd.DataFrame(data=data)

            self.elements.append(conveyor)

            service_capacity += conveyor.capacity_steps

        print('a total of {} ton of conveyor service capacity is online; {} ton total planned'.format(
            service_capacity_online,
            service_capacity))

    def unloading_station_invest(self, year, service_capacity_trigger):
        """current strategy is to add unloading stations as soon as a service trigger is achieved
        - find out how much service capacity is online
        - find out how much service capacity is planned
        - find out how much service capacity is needed
        - add service capacity until service_trigger is no longer exceeded
        """

        # from all Conveyor objects sum online capacity
        service_capacity = 0
        service_capacity_online = 0
        list_of_elements = self.find_elements(Unloading_station)
        if list_of_elements != []:
            for element in list_of_elements:
                service_capacity += element.production
                if year >= element.year_online:
                    service_capacity_online += element.production
        # todo: understand conveyors capacity formulation

        print('a total of {} ton of conveyor service capacity is online; {} ton total planned'.format(
            service_capacity_online,
            service_capacity))

        # check if total planned length is smaller than target length, if so add a quay
        while service_capacity < service_capacity_trigger:
            print('add Unloading_station to elements')
            hinterland_station = Unloading_station(**defaults.hinterland_station_data)

            # - capex
            delta = hinterland_station.production
            unit_rate = hinterland_station.unit_rate
            mobilisation = hinterland_station.mobilisation
            hinterland_station.capex = int(delta * unit_rate + mobilisation)

            # - opex
            hinterland_station.insurance = hinterland_station.capex * hinterland_station.insurance_perc
            hinterland_station.maintenance = hinterland_station.capex * hinterland_station.maintenance_perc
            hinterland_station.energy = hinterland_station.consumption * hinterland_station.production * self.operational_hours

            hinterland_station.year_online = year + hinterland_station.delivery_time

            # add cash flow information to quay_wall object in a dataframe
            data = self.create_data_dict(hinterland_station)
            hinterland_station.df = pd.DataFrame(data=data)

            self.elements.append(hinterland_station)

            service_capacity += hinterland_station.production

        print('a total of {} ton of conveyor service capacity is online; {} ton total planned'.format(
            service_capacity_online,
            service_capacity))

    def plot_system(self):
        pass

    def NPV(self):
        pass

    def supply_chain(self, nodes, edges):
        """Create a supply chain of example objects:
        the graph contains all available paths the cargo can take to travel through the terminal
        each path needs at least 1 of each of the indicated objects to make a navigable route
        if terminal elements do not make up a graph with a full path through no revenue can be obtained
        """
        # create a graph
        FG = nx.DiGraph()

        labels = {}
        for node in nodes:
            labels[node.name] = (node.name, node.name)
            FG.add_node(node.name, Object=node)

        for edge in edges:
            FG.add_edge(edge[0].name, edge[1].name, weight=1)

        self.supply_graph = FG

        # inspect all paths
        self.supply_chains = list([p for p in nx.all_shortest_paths(FG, nodes[0].name, nodes[-1].name)])
