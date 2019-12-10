"""
Main generic object classes:

- 1. Quay_wall
- 2. Berth
- 3. Cyclic_Unloader
    - STS crane
- 4. Horizontal transport
    - Tractor trailer
- 5. Commodity
    - TEU
- 6. Containers
    - Laden
    - Reefer
    - Empty
    - OOG
- 7. Laden and reefer stack
- 8. Stack equipment
- 9. Empty stack
- 10. OOG stack
- 11. Gates
- 12. Empty handler
- 13. Vessel
- 14. Labour
- 15. Energy
- 16. General
- 17. Indirect Costs
"""

# package(s) for data handling
import pandas as pd

# *** Default inputs: Quay_Wall class *** todo add values of RHDHV or general (e.g. PIANC)

quay_wall_data = {"name": 'Quay',
                  "ownership": 'Port authority',
                  "delivery_time": 2,
                  "lifespan": 50,
                  "mobilisation_min": 2_500_000,
                  "mobilisation_perc": 0.02,
                  "maintenance_perc": 0.01,
                  "insurance_perc": 0.01,
                  "freeboard": 4,  # m todo vragen of dit realistisch is
                  "Gijt_constant": 757.8,  # USD/m (if 1.0 EUR = 1.12 USD, 670.45 EUR = 757.8 USD)
                  "Gijt_coefficient": 1.2729,
                  "max_sinkage": 0.5,
                  "wave_motion": 0.5,
                  "safety_margin": 0.5,
                  "apron_width": 65.5,  # m
                  "apron_pavement": 125}  # all values from Ijzermans, 2019, P 91

# *** Default inputs: Berth class *** #todo add min_cranes

berth_data = {"name": 'Berth',
              "crane_type": 'Mobile cranes',
              "delivery_time": 1,
              "max_cranes": 3}  # STS cranes

channel_data = {"name": 'Channel',
                "ownership": 'Port authority',
                "delivery_time": 2,                 # years
                "lifespan": 50,                     # years
                "capital_dredging_rate": 7.0,       # USD per m3
                "infill_dredging_rate": 5.5,        # USD per m3
                "maintenance_dredging_rate": 4.5,   # USD per m3
                "mobilisation_min": 2_500_000,
                "mobilisation_perc": 0.02,
                "maintenance_perc": 0.10,
                "insurance_perc": 0.01}

bridge_data = {"name": 'Bridge',
               "ownership": 'Port authority',
               "delivery_time": 3,
               "lifespan": 50,                      # years
               "unit_rate": 100_000_000,            # USD per km
               "maintenance_perc": 0.025,
               "insurance_perc": 0.01}

reclamation_data = {"name": 'Reclamation',
                    "ownership": 'Port authority',
                    "delivery_time": 2,             # years
                    "lifespan": 50,                 # years
                    "reclamation_rate": 12.50,      # USD per m3
                    "maintenance_perc": 0.02,
                    "insurance_perc": 0.00}

revetment_data = {"name": 'Revetment',
                  "ownership": 'Port authority',
                  "delivery_time": 2,               # years
                  "lifespan": 50,                   # years
                  "revetment_rate": 180_000,        # USD per m
                  "quay_length_rate": 1.5,
                  "maintenance_perc": 0.01,
                  "insurance_perc": 0.00}

breakwater_data = {"name": 'Breakwater',
                   "ownership": 'Port authority',
                   "delivery_time": 2,              # years
                   "lifespan": 50,                  # years
                   "breakwater_rate":  275_000,     # USD per m
                   "quay_length_rate": 1.5,
                   "maintenance_perc": 0.01,
                   "insurance_perc": 0.00}

# *** Default inputs: Cyclic_Unloader class *** todo check sources sts_crane_data and add small sts_crane_data for the barge berths

# gantry_crane_data = {"name": 'Gantry_crane',
#                      "ownership": 'Terminal operator',
#                      "delivery_time": 1,
#                      "lifespan": 40,
#                      "unit_rate": 9_750_000,
#                      "mobilisation_perc": 0.15,
#                      "maintenance_perc": 0.02,
#                      "consumption": 561,
#                      "insurance_perc": 0.01,
#                      "crew": 3,
#                      "crane_type": 'Gantry crane',
#                      "lifting_capacity": 50,
#                      "hourly_cycles": 50,
#                      "eff_fact": 0.50}  # all values from Ijzermans, 2019, P 100
#
# harbour_crane_data = {"name": 'Harbour_crane',
#                       "ownership": 'Terminal operator',
#                       "delivery_time": 1,
#                       "lifespan": 40,
#                       "unit_rate": 7_880_000,
#                       "mobilisation_perc": 0.15,
#                       "maintenance_perc": 0.02,
#                       "consumption": 210,
#                       "insurance_perc": 0.01,
#                       "crew": 3,
#                       "crane_type": 'Harbour crane',
#                       "lifting_capacity": 25,
#                       "hourly_cycles": 40,
#                       "eff_fact": 0.40}  # all values from Ijzermans, 2019, P 100
#
# mobile_crane_data = {"name": 'Mobile_crane',
#                      "ownership": 'Terminal operator',
#                      "delivery_time": 1,
#                      "lifespan": 40,
#                      "unit_rate": 3_325_000,
#                      "mobilisation_perc": 0.15,
#                      "maintenance_perc": 0.02,
#                      "consumption": 485,
#                      "insurance_perc": 0.01,
#                      "crew": 3,
#                      "crane_type": 'Mobile crane',
#                      "lifting_capacity": 30,
#                      "hourly_cycles": 25,
#                      "eff_fact": 0.35}  # all values from Ijzermans, 2019, P 100

sts_crane_data = {"name": 'STS_crane',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,  # years
                  "lifespan": 40,  # years
                  "unit_rate": 10_000_000,  # USD per unit
                  "mobilisation_perc": 0.15,  # percentage
                  "maintenance_perc": 0.02,  # percentage
                  "insurance_perc": 0.01,  # percentage
                  "consumption": 8,  # Source: Peter Beamish (RHDHV)
                  "crew": 5.5,  # 1.5 crane driver, 2 quay staff, 2 twistlock handler (per shift)
                  "crane_type": 'STS crane',
                  "lifting_capacity": 2.13,  # weighted average of TEU per lift
                  "hourly_cycles": 25,  # PIANC wg135
                  "eff_fact": 0.75}


# Default inputs: Horizontal_Transport class *** #todo add sources

tractor_trailer_data = {"name": 'Tractor-trailer',
                        "type": 'tractor_trailer',
                        "ownership": 'Terminal operator',
                        "delivery_time": 0,
                        "lifespan": 10,
                        "mobilisation": 1_000,
                        "unit_rate": 85_000,
                        "maintenance_perc": 0.10,
                        "insurance_perc": 0.01,
                        "crew": 1,
                        "salary": 30_000,  # dummy
                        "utilisation": 0.80,
                        "fuel_consumption": 2,  # liter per box move
                        "productivity": 1,
                        "required": 5,
                        "non_essential_moves": 1.2}  # todo input value for tractor productivity

# *** Default inputs: Container class #todo add sources

laden_container_data = {"name": 'Laden container',
                        "type": 'laden_container',
                        "teu_factor": 1.60,
                        "dwell_time": 3,
                        "peak_factor": 1.2,
                        "stack_occupancy": 0.8}

reefer_container_data = {"name": 'Empty container',
                         "type": 'empty_container',
                         "teu_factor": 1.75,
                         "dwell_time": 3,
                         "peak_factor": 1.2,
                         "stack_occupancy": 0.8}

empty_container_data = {"name": 'Empty container',
                        "type": 'empty_container',
                        "teu_factor": 1.55,
                        "dwell_time": 10,
                        "peak_factor": 1.2,
                        "stack_occupancy": 0.7}

oog_container_data = {"name": 'OOG container',
                      "type": 'oog_container',
                      "teu_factor": 1.55,
                      "dwell_time": 4,
                      "peak_factor": 1.2,
                      "stack_occupancy": 0.9}

# *** Default inputs: Laden_Stack class

rtg_stack_data = {"name": 'RTG Stack',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 40,
                  "mobilisation": 25_000,
                  "maintenance_perc": 0.1,
                  "width": 6,  # TEU
                  "height": 5,  # TEU
                  "length": 30,  # TEU
                  "capacity": 900,  # TEU
                  "gross_tgs": 18,
                  "area_factor": 2.04,  # m2/TEU (based on grasshopper layout P. Koster)
                  "pavement": 200,  # DUMMY
                  "drainage": 50,  # DUMMY
                  "household": 0.1,  # moves
                  "digout_margin": 1.2,  # percentage
                  "reefer_factor": 2.33,  # RHDHV
                  "consumption": 4,  # kWh per active reefer
                  "reefer_rack": 3500,
                  "reefers_present": 0.5}  # per reefer spot

rmg_stack_data = {"name": 'RMG Stack',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 40,
                  "mobilisation": 50_000,
                  "maintenance_perc": 0.1,
                  "width": 6,  # TEU
                  "height": 5,  # TEU
                  "length": 40,  # TEU
                  "capacity": 1200,  # TEU
                  "gross_tgs": 18.67,
                  "area_factor": 2.79,  # m2/TEU (based on grasshopper layout P. Koster)
                  "pavement": 200,  # DUMMY
                  "drainage": 50,  # DUMMY
                  "household": 0.1,  # moves
                  "digout_margin": 1.2,  # percentage
                  "reefer_factor": 2.33,  # RHDHV
                  "consumption": 4,  # kWh per active reefer
                  "reefer_rack": 3500,
                  "reefers_present": 0.5}  # per reefer spot

sc_stack_data = {"name": 'SC Stack',
                 "ownership": 'Terminal operator',
                 "delivery_time": 1,
                 "lifespan": 40,
                 "mobilisation": 50_000,
                 "maintenance_perc": 0.1,
                 "width": 48,  # TEU
                 "height": 4,  # TEU
                 "length": 20,  # TEU
                 "capacity": 3840,  # TEU
                 "gross_tgs": 26.46,
                 "area_factor": 1.45,  # m2/TEU (based on grasshopper layout P. Koster)
                 "pavement": 200,  # DUMMY
                 "drainage": 50,  # DUMMY
                 "household": 0.1,  # moves
                 "digout_margin": 1.2,  # percentage
                 "reefer_factor": 2.33,  # RHDHV
                 "consumption": 4,  # kWh per active reefer
                 "reefer_rack": 3500,
                 "reefers_present": 0.5}  # per reefer spot

rs_stack_data = {"name": 'RS Stack',
                 "ownership": 'Terminal operator',
                 "delivery_time": 1,
                 "lifespan": 40,
                 "mobilisation": 10_000,
                 "maintenance_perc": 0.1,
                 "width": 4,  # TEU
                 "height": 4,  # TEU
                 "length": 20,  # TEU
                 "capacity": 320,  # TEU
                 "gross_tgs": 18,
                 "area_factor": 3.23,  # m2/TEU (based on grasshopper layout P. Koster)
                 "pavement": 200,  # DUMMY
                 "drainage": 50,  # DUMMY
                 "household": 0.1,  # moves
                 "digout_margin": 1.2,  # percentage
                 "reefer_factor": 2.33,  # RHDHV
                 "consumption": 4,  # kWh per active reefer
                 "reefer_rack": 3500,
                 "reefers_present": 0.5}  # per reefer spot

# #*** Default inputs: Reefer data
# reefer_rack_data = {"reefer_factor":2.33, #RHDHV
#                  "consumption":4, #kWh per active reefer
#                  "reefer_rack": 3500} #per reefer spot

# *** Default inputs: Other_Stack class

empty_stack_data = {"name": 'Empty Stack',
                    "ownership": 'Terminal operator',
                    "delivery_time": 1,
                    "lifespan": 40,
                    "mobilisation": 25_000,
                    "maintenance_perc": 0.1,
                    "width": 8,  # TEU
                    "height": 6,  # TEU
                    "length": 10,  # TEU
                    "capacity": 480,  # TEU
                    "gross_tgs": 18,
                    "area_factor": 2.04,  # Based on grasshopper layout
                    "pavement": 200,  # DUMMY
                    "drainage": 50,
                    "household": 1.05,
                    "digout": 1.05}  # DUMMY

oog_stack_data = {"name": 'OOG Stack',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 40,
                  "mobilisation": 25_000,
                  "maintenance_perc": 0.1,
                  "width": 10,  # TEU
                  "height": 1,  # TEU
                  "length": 10,  # TEU
                  "capacity": 100,  # TEU
                  "gross_tgs": 64,
                  "area_factor": 1.05,  # m2/TEU (based on grasshopper layout P. Koster)
                  "pavement": 200,  # DUMMY
                  "drainage": 50}  # DUMMY

# *** Default inputs: Stack_Equipment class #todo add eRTG

rtg_data = {"name": 'RTG',
            "type": 'rtg',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 1_400_000,
            "mobilisation": 5000,
            "maintenance_perc": 0.1,  # dummy
            "insurance_perc": 0,
            "crew": 1,  # dummy
            "salary": 50_000,  # dummy
            "required": 3,
            "fuel_consumption": 1,  # dummy
            "power_consumption": 0
            }

rmg_data = {"name": 'RMG',
            "type": 'rmg',
            "ownership": 'Terminal operator',
            "delivery_time": 0,
            "lifespan": 10,
            "unit_rate": 2_500_000,
            "mobilisation": 5000,
            "maintenance_perc": 0.1,  # dummy
            "insurance_perc": 0,
            "crew": 0,  # dummy
            "salary": 50_000,  # dummy
            "required": 1,  # one per stack
            "fuel_consumption": 0,  # dummy
            "power_consumption": 15  # kWh/box move
            }

sc_data = {"name": 'Straddle carrier',
           "type": 'sc',
           "ownership": 'Terminal operator',
           "delivery_time": 0,
           "lifespan": 10,
           "unit_rate": 2_000_000,  # dummy
           "mobilisation": 5000,
           "maintenance_perc": 0.1,  # dummy
           "insurance_perc": 0,
           "crew": 0,  # dummy
           "salary": 50_000,  # dummy
           "required": 5,
           "fuel_consumption": 0,  # dummy
           "power_consumption": 30
           }

rs_data = {"name": 'Reach stacker',
           "type": 'rs',
           "ownership": 'Terminal operator',
           "delivery_time": 0,
           "lifespan": 10,
           "unit_rate": 500_000,
           "mobilisation": 5000,
           "maintenance_perc": 0.1,  # dummy
           "insurance_perc": 0,
           "crew": 2,  # dummy
           "salary": 50_000,  # dummy
           "required": 4,
           "fuel_consumption": 1,  # dummy
           "power_consumption": 0
           }

# *** Default inputs: Gate class ***

gate_data = {"name": 'Gate',
             "type": 'gate',
             "ownership": "Terminal operator",
             "delivery_time": 1,  # years
             "lifespan": 15,  # years
             "unit_rate": 30_000,  # USD/gate
             "mobilisation": 5000,  # USD/gate
             "maintenance_perc": 0.02,  # percentage
             "crew": 2,  # crew
             "salary": 30_000,  # dummy
             "canopy_costs": 250,  # USD/m2
             "area": 288.75,  # PIANC WG135
             "staff_gates": 1,  #
             "service_gates": 1,  #
             "design_capacity": 0.98,  #
             "exit_inspection_time": 2,  # min #dummy
             "entry_inspection_time": 2,  # min #dummy
             "peak_hour": 0.25,  # dummy
             "peak_day": 0.1,  # dummy
             "peak_factor": 1.2,  #
             "truck_moves": 0.75,  #
             "operating_days": 6,  #
             "capacity": 60}

# *** Default inputs: Barge_Berth class ***

barge_berth_data = {"name": 'Barge_Berth',
                    "type": 'barge_berth',
                    "ownership": "Terminal operator",
                    "delivery_time": 2,                 # years
                    "lifespan": 50,                     # equal to quay wall OGV
                    "unit_rate": 30_000,                # USD/barge_berth
                    "mobilisation": 5000,               # USD/barge_berth
                    "maintenance_perc": 0.02,           # percentage
                    "nom_crane_productivity": 15.0,     # moves per hour
                    "utilisation": 0.90,                # rate
                    "efficiency": 0.75,                 # rate
                    "crane_per_berth": 1.30,            # rate
                    "handling_time_ratio": 0.90,        # handling time to berthing time ratio
                    "peak_factor": 1.10}

# *** Default inputs: ECH class***

empty_handler_data = {"name": 'Empty Handler',
                      "type": 'empty_handler',
                      "ownership": "Terminal operator",
                      "delivery_time": 1,
                      "lifespan": 15,
                      "unit_rate": 500_000,
                      "mobilisation": 5000,
                      "maintenance_perc": 0.02,
                      "crew": 1,
                      "salary": 35_000,  # dummy
                      "fuel_consumption": 1.5,
                      "required": 5}

# *** Default inputs: Commodity class ***

container_data = {"name": 'Laden',
                  "handling_fee": 150,
                  "fully_cellular_perc": 0,
                  "panamax_perc": 0,
                  "panamax_max_perc": 0,
                  "post_panamax_I_perc": 0,
                  "post_panamax_II_perc": 0,
                  "new_panamax_perc": 100,
                  "VLCS_perc": 0,
                  "ULCS_perc": 0}

# *** Default inputs: Vessel class *** (Source: i) The Geography of Transport Systems, Jean-Paul Rodrigue (2017), ii) UNCTAD)

fully_cellular_data = {"name": 'Fully_Cellular_1',
                       "type": 'Fully_Cellular',
                       "starting_time": 0,  # years
                       "call_size": 2500/8,  # TEU
                       "LOA": 215,  # m
                       "draught": 10.0,  # m
                       "beam": 20.0,  # m
                       "max_cranes": 4,  # STS cranes
                       "all_turn_time": 31,  # todo source
                       "mooring_time": 6,  # berthing + deberthing time
                       "demurrage_rate": 730,  # USD todo edit
                       "transport_costs": 200}  # USD per TEU

panamax_data = {"name": 'Panamax_1',
                "type": 'Panamax',
                "starting_time": 0,  # years
                "call_size": 3400/8,  # TEU
                "LOA": 250,  # m
                "draught": 12.5,  # m
                "beam": 32.2,  # m
                "max_cranes": 4,  # STS cranes
                "all_turn_time": 31,  # todo source [hr]
                "mooring_time": 6,  # berthing + deberthing time [hr]
                "demurrage_rate": 730,  # USD todo edit
                "transport_costs": 180}  # USD per TEU

panamax_max_data = {"name": 'Panamax_Max_1',
                    "type": 'Panamax_Max',
                    "starting_time": 0,  # years
                    "call_size": 4500/8,  # TEU
                    "LOA": 290,  # m
                    "draught": 12.5,  # m
                    "beam": 32.0,  # m
                    "max_cranes": 4,  # STS cranes
                    "all_turn_time": 31,  # todo source [hr]
                    "mooring_time": 2,  # berthing + deberthing time [hr]
                    "demurrage_rate": 730,  # USD todo edit
                    "transport_costs": 160}  # USD per TEU

post_panamax_I_data = {"name": 'Post_Panamax_I_1',
                       "type": 'Post_Panamax_I',
                       "starting_time": 0,  # years
                       "call_size": 6000/8,  # TEU
                       "LOA": 300,  # m
                       "draught": 13.0,  # m
                       "beam": 40.0,  # m
                       "max_cranes": 4,  # STS cranes
                       "all_turn_time": 31,  # todo source [hr]
                       "mooring_time": 2,  # berthing + deberthing time [hr]
                       "demurrage_rate": 730,  # USD todo edit
                       "transport_costs": 150}  # USD per TEU

post_panamax_II_data = {"name": 'Post_Panamax_II_1',
                        "type": 'Post_Panamax_II',
                        "starting_time": 0,  # years
                        "call_size": 8500/8,  # TEU
                        "LOA": 340,  # m
                        "draught": 14.5,  # m
                        "beam": 43.0,  # m
                        "max_cranes": 4,  # STS cranes
                        "all_turn_time": 31,  # todo source [hr]
                        "mooring_time": 2,  # berthing + deberthing time [hr]
                        "demurrage_rate": 730,  # USD todo edit
                        "transport_costs": 140}  # USD per TEU

new_panamax_data = {"name": 'New_Panamax_1',
                    "type": 'New_Panamax',
                    "starting_time": 0,  # years
                    "call_size": 12500/8,  # TEU
                    "LOA": 366,  # m
                    "draught": 15.2,  # m
                    "beam": 49.0,  # m
                    "max_cranes": 4,  # STS cranes
                    "all_turn_time": 31,  # todo source [hr]
                    "mooring_time": 6,  # berthing + deberthing time [hr]
                    "demurrage_rate": 730,  # USD todo edit
                    "transport_costs": 120}  # USD per TEU

VLCS_data = {"name": 'VLCS_1',
             "type": 'VLCS',
             "starting_time": 0,  # years
             "call_size": 15000/8,  # TEU
             "LOA": 397,  # m
             "draught": 15.5,  # m
             "beam": 56.0,  # m
             "max_cranes": 4,  # STS cranes
             "all_turn_time": 31,  # todo source [hr]
             "mooring_time": 6,  # berthing + deberthing time [hr]
             "demurrage_rate": 730,  # USD todo edit
             "transport_costs": 80}  # USD per TEU

ULCS_data = {"name": 'ULCS_1',
             "type": 'ULCS',
             "starting_time": 0,  # years
             "call_size": 21000/8,  # TEU
             "LOA": 400,  # m
             "draught": 16.0,  # m
             "beam": 59.0,  # m
             "max_cranes": 4,  # STS cranes
             "all_turn_time": 31,  # todo source [hr]
             "mooring_time": 6,  # berthing + deberthing time [hr]
             "demurrage_rate": 730,  # USD todo edit
             "transport_costs": 60}  # USD per TEU

# *** Default inputs: Barge class *** # todo add sources

small_barge_data = {"name": 'Small_Barge_1',
                    "type": 'small',
                    "ownership": 'Port authority',
                    "delivery_time": 1,  # years
                    "lifespan": 10,  # years
                    "call_size": 200,  # TEU
                    "LOA": 90,  # m
                    "draught": 4.5,  # m
                    "beam": 12.0,  # m
                    "unit_rate": 1_000_000,  # USD per barge
                    "operations_perc": 0.10,
                    "maintenance_perc": 0.10,
                    "insurance_perc": 0.01,
                    "max_cranes": 1,  # small STS cranes
                    "mooring_time": 6,  # berthing + deberthing time
                    "transport_costs": 200}  # USD per TEU

medium_barge_data = {"name": 'Medium_Barge_1',
                     "type": 'medium',
                     "ownership": 'Port authority',
                     "delivery_time": 1,  # years
                     "lifespan": 10,  # years
                     "call_size": 250,  # TEU
                     "LOA": 100,  # m
                     "draught": 5.0,  # m
                     "beam": 13.0,  # m
                     "unit_rate": 1_000_000,  # USD per barge
                     "operations_perc": 0.10,
                     "maintenance_perc": 0.10,
                     "insurance_perc": 0.01,
                     "max_cranes": 1,  # small STS cranes
                     "mooring_time": 6,  # berthing + deberthing time
                     "transport_costs": 200}  # USD per TEU

large_barge_data = {"name": 'Large_Barge_1',
                    "type": 'large',
                    "ownership": 'Port authority',
                    "delivery_time": 1,  # years
                    "lifespan": 10, # years
                    "call_size": 300,  # TEU
                    "LOA": 120,  # m
                    "draught": 5.5,  # m
                    "beam": 14.0,  # m
                    "unit_rate": 1_000_000,  # USD per barge
                    "operations_perc": 0.10,
                    "maintenance_perc": 0.10,
                    "insurance_perc": 0.01,
                    "max_cranes": 1,  # small STS cranes
                    "mooring_time": 6,  # berthing + deberthing time
                    "transport_costs": 200}  # USD per TEU

truck_data = {"name": 'Truck',
              "ownership": 'Port authority',
              "delivery_time": 1,
              "lifespan": 10,
              "unit_rate": 10_000,  # USD per truck
              "operations_perc": 0.10,
              "maintenance_perc": 0.10,
              "insurance_perc": 0.01}

# *** Default inputs: Labour class ***

labour_data = {"name": 'Labour',
               "international_salary": 105_000,
               "international_staff": 4,
               "local_salary": 18_850,
               "local_staff": 10,
               "operational_salary": 16_750,
               "shift_length": 6.5,  # hr per shift
               "annual_shifts": 200,
               "daily_shifts": 5,  # shifts per day
               "blue_collar_salary": 25_000,  # USD per crew per day
               "white_collar_salary": 35_000}  # USD per crew per day

# *** Default inputs: Energy class ***

energy_data = {"name": 'Energy',
               "price": 0.10}

# *** Default inputs: General_Services class ***

general_services_data = {"name": 'General_Services"',
                         "type": 'general_services',
                         "office": 2400,
                         "office_cost": 1500,
                         "workshop": 2400,
                         "workshop_cost": 1000,
                         "fuel_station_cost": 500_000,
                         "scanning_inspection_area": 2700,
                         "scanning_inspection_area_cost": 1000,
                         "lighting_mast_required": 1.2,  # masts per ha
                         "lighting_mast_cost": 30_000,
                         "firefight_cost": 2_000_000,
                         "maintenance_tools_cost": 10_000_000,
                         "terminal_operating_software_cost": 10_000_000,
                         "electrical_station_cost": 2_000_000,
                         "repair_building": 100,
                         "repair_building_cost": 1000,
                         "ceo": 1,  # FTE per 500 k TEU
                         "secretary": 1,  # FTE per 500 k TEU
                         "administration": 3,  # FTE per 500 k TEU
                         "hr": 2,  # FTE per 500 k TEU
                         "commercial": 1,  # FTE per 500 k TEU
                         "operations": 4,  # FTE/shirt per 500 k TEU
                         "engineering": 2,  # FTE/shift per 500 k TEU
                         "security": 2,  # FTE/shift per 500 k TEU
                         "general_maintenance": 0.015,
                         "crew_required": 500_000,  # for each 500_k TEU an additional crew team is added
                         "delivery_time": 1,
                         "lighting_consumption": 1,
                         "general_consumption": 1000}

# *** Default inputs: Indirect_Costs class ***

indirect_costs_data = {"name": 'Indirect_Costs',
                       "preliminaries": 0.15,
                       "engineering": 0.05,
                       "miscellaneous": 0.15,
                       "electrical_works_fuel_terminal": 0.12,
                       "electrical_works_power_terminal": 0.15}

