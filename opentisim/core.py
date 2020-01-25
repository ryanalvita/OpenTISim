# package(s) for data handling
import pandas as pd
import numpy as np


# *** General functions
def report_element(Terminal, Element, year):
    elements = 0
    elements_online = 0
    element_name = []
    list_of_elements = find_elements(Terminal, Element)
    if list_of_elements != []:
        for element in list_of_elements:
            element_name = element.name
            elements += 1
            if year >= element.year_online:
                elements_online += 1

    if Terminal.debug:
        if elements_online or elements:
            print('     a total of {} {} is online; a total of {} is still pending'.format(elements_online, element_name, elements - elements_online))

    return elements_online, elements


def find_elements(Terminal, obj):
    """return elements of type obj part of Terminal.elements"""

    list_of_elements = []
    if Terminal.elements != []:
        for element in Terminal.elements:
            if isinstance(element, obj):
                list_of_elements.append(element)

    return list_of_elements


def occupancy_to_waitingfactor(occupancy=.3, nr_of_servers_chk=4, poly_order=6):
    """Waiting time factor (E2/E2/n Erlang queueing theory using 6th order polynomial regression)"""

    # Create dataframe with data from Groenveld (2007) - Table V
    utilisation = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .9])
    nr_of_servers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    data = np.array([
        [0.0166, 0.0006, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.0604, 0.0065, 0.0011, 0.0002, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.1310, 0.0235, 0.0062, 0.0019, 0.0007, 0.0002, 0.0001, 0.0000, 0.0000, 0.0000],
        [0.2355, 0.0576, 0.0205, 0.0085, 0.0039, 0.0019, 0.0009, 0.0005, 0.0003, 0.0001],
        [0.3904, 0.1181, 0.0512, 0.0532, 0.0142, 0.0082, 0.0050, 0.0031, 0.0020, 0.0013],
        [0.6306, 0.2222, 0.1103, 0.0639, 0.0400, 0.0265, 0.0182, 0.0128, 0.0093, 0.0069],
        [1.0391, 0.4125, 0.2275, 0.1441, 0.0988, 0.0712, 0.0532, 0.0407, 0.0319, 0.0258],
        [1.8653, 0.8300, 0.4600, 0.3300, 0.2300, 0.1900, 0.1400, 0.1200, 0.0900, 0.0900],
        [4.3590, 2.0000, 1.2000, 0.9200, 0.6500, 0.5700, 0.4400, 0.4000, 0.3200, 0.3000]
    ])
    df = pd.DataFrame(data, index=utilisation, columns=nr_of_servers)

    # Create a 6th order polynomial fit through the data (for nr_of_stations_chk)
    target = df.loc[:, nr_of_servers_chk]
    p_p = np.polyfit(target.index, target.values, poly_order)

    waiting_factor = np.polyval(p_p, occupancy)
    # todo: when the nr of servers > 10 the waiting factor should be set to inf (definitively more equipment needed)

    # Return waiting factor
    return waiting_factor


def waitingfactor_to_occupancy(factor=.3, nr_of_servers_chk=4, poly_order=6):
    """Waiting time factor (E2/E2/n Erlang queueing theory using 6th order polynomial regression)"""

    # Create dataframe with data from Groenveld (2007) - Table V
    utilisation = np.array([.1, .2, .3, .4, .5, .6, .7, .8, .9])
    nr_of_servers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    data = np.array([
        [0.0166, 0.0006, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.0604, 0.0065, 0.0011, 0.0002, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000],
        [0.1310, 0.0235, 0.0062, 0.0019, 0.0007, 0.0002, 0.0001, 0.0000, 0.0000, 0.0000],
        [0.2355, 0.0576, 0.0205, 0.0085, 0.0039, 0.0019, 0.0009, 0.0005, 0.0003, 0.0001],
        [0.3904, 0.1181, 0.0512, 0.0532, 0.0142, 0.0082, 0.0050, 0.0031, 0.0020, 0.0013],
        [0.6306, 0.2222, 0.1103, 0.0639, 0.0400, 0.0265, 0.0182, 0.0128, 0.0093, 0.0069],
        [1.0391, 0.4125, 0.2275, 0.1441, 0.0988, 0.0712, 0.0532, 0.0407, 0.0319, 0.0258],
        [1.8653, 0.8300, 0.4600, 0.3300, 0.2300, 0.1900, 0.1400, 0.1200, 0.0900, 0.0900],
        [4.3590, 2.0000, 1.2000, 0.9200, 0.6500, 0.5700, 0.4400, 0.4000, 0.3200, 0.3000]
    ])
    df = pd.DataFrame(data, index=utilisation, columns=nr_of_servers)

    # Create a 6th order polynomial fit through the data (for nr_of_stations_chk)
    target = df.loc[:, nr_of_servers_chk]
    p_p = np.polyfit(target.values, target.index, poly_order)
    print(p_p)

    occupancy = np.polyval(p_p, factor)

    # Return occupancy
    return occupancy


def add_cashflow_data_to_element(Terminal, element):
    """Place cashflow data in element dataframe
    Elements that take two years to build are assign 60% to year one and 40% to year two."""

    # years
    years = list(range(Terminal.startyear, Terminal.startyear + Terminal.lifecycle))

    # capex
    capex = element.capex

    # opex
    maintenance = element.maintenance
    insurance = element.insurance
    labour = element.labour

    # year online
    year_online = element.year_online
    year_delivery = element.delivery_time

    df = pd.DataFrame()

    # years
    df["year"] = years

    # capex
    if year_delivery > 1:
        df.loc[df["year"] == year_online - 2, "capex"] = 0.6 * capex
        df.loc[df["year"] == year_online - 1, "capex"] = 0.4 * capex
    else:
        df.loc[df["year"] == year_online - 1, "capex"] = capex

    # opex
    if maintenance:
        df.loc[df["year"] >= year_online, "maintenance"] = maintenance
    if insurance:
        df.loc[df["year"] >= year_online, "insurance"] = insurance
    if labour:
        df.loc[df["year"] >= year_online, "labour"] = labour

    df.fillna(0, inplace=True)

    element.df = df

    return element


def add_cashflow_elements(Terminal, labour):
    """Cycle through each element and collect all cash flows into a pandas dataframe."""

    cash_flows = pd.DataFrame()

    # initialise cash_flows
    cash_flows['year'] = list(range(Terminal.startyear, Terminal.startyear + Terminal.lifecycle))
    cash_flows['capex'] = 0
    cash_flows['maintenance'] = 0
    cash_flows['insurance'] = 0
    cash_flows['energy'] = 0
    cash_flows['labour'] = 0
    cash_flows['demurrage'] = Terminal.demurrage
    cash_flows['revenues'] = Terminal.revenues

    # add labour component for years were revenues are not zero
    cash_flows.loc[cash_flows[
                       'revenues'] != 0, 'labour'] = labour.international_staff * labour.international_salary + labour.local_staff * labour.local_salary

    for element in Terminal.elements:
        if hasattr(element, 'df'):
            for column in cash_flows.columns:
                if column in element.df.columns and column != "year":
                    cash_flows[column] += element.df[column]

    cash_flows.fillna(0)

    # calculate WACC real cashflows
    cash_flows_WACC_real = pd.DataFrame()
    cash_flows_WACC_real['year'] = cash_flows['year']
    for year in range(Terminal.startyear, Terminal.startyear + Terminal.lifecycle):
        for column in cash_flows.columns:
            if column != "year":
                cash_flows_WACC_real.loc[cash_flows_WACC_real['year'] == year, column] = \
                    cash_flows.loc[
                        cash_flows[
                            'year'] == year, column] / (
                            (1 + WACC_real()) ** (
                            year - Terminal.startyear))

    return cash_flows, cash_flows_WACC_real


def WACC_nominal(Gearing=60, Re=.10, Rd=.30, Tc=.28):
    """Nominal cash flow is the true dollar amount of future revenues the company expects
    to receive and expenses it expects to pay out, including inflation.
    When all cashflows within the model are denoted in real terms and including inflation."""

    Gearing = Gearing
    Re = Re  # return on equity
    Rd = Rd  # return on debt
    Tc = Tc  # income tax
    E = 100 - Gearing
    D = Gearing

    WACC_nominal = ((E / (E + D)) * Re + (D / (E + D)) * Rd) * (1 - Tc)

    return WACC_nominal


def WACC_real(inflation=0.02):  # old: interest=0.0604
    """Real cash flow expresses a company's cash flow with adjustments for inflation.
    When all cashflows within the model are denoted in real terms and have been
    adjusted for inflation (no inlfation has been taken into account),
    WACC_real should be used. WACC_real is computed by as follows:"""

    WACC_real = (WACC_nominal() + 1) / (inflation + 1) - 1

    return WACC_real


def NPV(Terminal, labour):
    """Gather data from Terminal elements and combine into a cash flow overview"""

    # add cash flow information for each of the Terminal elements
    cash_flows, cash_flows_WACC_real = add_cashflow_elements(Terminal, labour)

    # prepare years, revenue, capex and opex for plotting
    years = cash_flows_WACC_real['year'].values
    revenue = Terminal.revenues
    capex = cash_flows_WACC_real['capex'].values
    opex = cash_flows_WACC_real['insurance'].values + \
           cash_flows_WACC_real['maintenance'].values + \
           cash_flows_WACC_real['energy'].values + \
           cash_flows_WACC_real['demurrage'].values + \
           cash_flows_WACC_real['labour'].values

    # collect all results in a pandas dataframe
    df = pd.DataFrame(index=years, data=-capex, columns=['CAPEX'])
    df['OPEX'] = -opex
    df['REVENUE'] = revenue
    df['PV'] = - capex - opex + revenue
    df['cum-PV'] = np.cumsum(- capex - opex + revenue)

    return df
