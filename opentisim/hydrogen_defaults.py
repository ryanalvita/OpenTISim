"""Defaults for following objects:

- 1. Jetty
- 2. Berth
- 3. Unloader
    - Liquid hydrogen
    - Ammonia
    - MCH
- 4. Pipelines
    - jetty
    - hinterland
- 5. Storage
    - Liquid hydrogen
    - Ammonia
    - MCH
- 6. H2 retrieval
    - Ammonia
    - MCH
- 6. Commodity
    - Liquid hydrogen
    - Ammonia
    - MCH
- 7. Vessel
    - smallhydrogen
    - largehydrogen
    - smallammonia
    - largeammonia
    - Handysize
    - Panamax
    - VLCC
- 8. Labour

Default values are based on Claes 2018; Corbeau 2018; Daas 2018; Juha 2018;
Kranendonk 2018; Schutz 2018; Schuurmans 2018 and Verstegen 2018

"""

# package(s) for data handling
import pandas as pd


# *** Default inputs: Jetty class ***

jetty_data = {"name": 'Jetty_01',
                  "ownership": 'Port authority',
                  "delivery_time": 2,
                  "lifespan": 50,
                  "mobilisation_min": 1_000_000,
                  "mobilisation_perc": 0.02,
                  "maintenance_perc": 0.01,
                  "insurance_perc": 0.01,
                  "Gijt_constant_jetty": 2000, #based on personal communation with de Gijt
                  "jettywidth": 16,
                  "jettylength": 30,
                  "mooring_dolphins":250_000,
                  "catwalkwidth": 5,
                  "catwalklength":100,
                  "Catwalk_rate": 1000,
                            } # all values from P. Quist personnal communication

# *** Default inputs: Berth class ***

berth_data = {"name": 'Berth_01',
              "crane_type": 'Mobile cranes',
              "delivery_time": 1}  # all values from Ijzermans, 2019, P 92


# *** Default inputs: Pipeline class ***

jetty_pipeline_data = {"name": 'jetty_pipeline_01',
                      "type": 'jetty_pipeline',
                      "length": 600,
                      "ownership": 'Terminal operator',
                      "delivery_time": 1,
                      "lifespan": 26,
                      "unit_rate_factor": 193_000,
                      "mobilisation": 30_000,
                      "maintenance_perc": 0.01,
                      "insurance_perc": 0.01,
                      "consumption_coefficient": 80, #kwh/ton
                      "crew": 1,
                      "utilisation": 0.80,
                      "capacity": 4000}

hinterland_pipeline_data = {"name": 'hinterland_pipeline_01',
                            "type": 'hinterland_pipeline',
                            "length": 400,
                            "ownership": 'Terminal operator',
                            "delivery_time": 1,
                            "lifespan": 26,
                            "mobilisation": 30_000,
                            "unit_rate_factor": 193_000,
                            "maintenance_perc": 0.01,
                            "insurance_perc": 0.01,
                            "consumption_coefficient": 80, #in kwh/ton
                            "crew": 1,
                            "utilisation": 0.80,
                            "capacity": 4000} #ton/hr


# *** Default inputs: Storage class ***

"Liquid hydrogen"

storage_lh2_data = {"name": 'HTank_01',
             "type": 'HydrogenTank',
             "ownership": 'Terminal operator',
             "delivery_time": 1,
             "lifespan": 30,
             "unit_rate": 200_000_000,
             "mobilisation_min": 200_000,
             "mobilisation_perc": 0.003,
             "maintenance_perc": 0.01,
             "crew_min": 3,
             "crew_for5": 1,
             "insurance_perc": 0.01,
             "storage_type": 'tank',
             "consumption": 610,
             "capacity": 3_540} # all input values from Ijzermans, 2019, P 102

"Ammonia"
storage_nh3_data = {"name": 'ATank_01',
                  "type": 'AmmoniaTank',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 30,
                  "unit_rate": 60_000_000,
                  "mobilisation_min": 200_000,
                  "mobilisation_perc": 0.003,
                  "maintenance_perc": 0.01,
                  "crew_min": 3,
                  "crew_for5": 1,
                  "insurance_perc": 0.01,
                  "storage_type": 'tank',
                  "consumption": 100, #in kwh/ton
                  "capacity": 34_130}

"MCH"
storage_MCH_data = {"name": 'MCHTank_01',
                  "type": 'MCHTank',
                  "ownership": 'Terminal operator',
                  "delivery_time": 1,
                  "lifespan": 50,
                  "unit_rate": 35_000_000,
                  "mobilisation_min": 200_000,
                  "mobilisation_perc": 0.003,
                  "maintenance_perc": 0.01,
                  "crew_min": 3,
                  "crew_for5": 1,
                  "insurance_perc": 0.01,
                  "storage_type": 'tank',
                  "consumption": 10,
                  "capacity": 38_500}


# *** Default inputs: H2Conversion class ***

"Liquid hydrogen"
h2retrieval_lh2_data = {"name": 'H2retrieval_LH2_01',
                  "type": 'HydrogenTank',
                  "ownership": 'Terminal operator',
                  "delivery_time": 2,
                  "lifespan": 10,
                  "unit_rate": 18_000_000,
                  "mobilisation_min": 200_000,
                  "mobilisation_perc": 0.003,
                  "maintenance_perc": 0.015,
                  "crew_min": 3,
                  "crew_for5": 1,
                  "insurance_perc": 0.01,
                  "h2retrieval_type": 'tank',
                  "consumption": 600, #in kwh/ton
                  "capacity": 171} #in ton/hr

"Ammonia"
h2retrieval_nh3_data = {"name": 'H2retrieval_NH3_01',
             "type": 'AmmoniaTank',
             "ownership": 'Terminal operator',
             "delivery_time": 2,
             "lifespan": 20,
             "unit_rate": 100_000_000,
             "mobilisation_min": 200_000,
             "mobilisation_perc": 0.003,
             "maintenance_perc": 0.015,
             "crew_min": 3,
             "crew_for5": 1,
             "insurance_perc": 0.01,
             "h2retrieval_type": 'tank',
             "consumption": 5889,#in kwh/ton
             "capacity": 55}  #in ton/hr

"MCH"
h2retrieval_MCH_data = {"name": 'H2retrieval_MCH_01',
             "type": 'MCHTank',
             "ownership": 'Terminal operator',
             "delivery_time": 2,
             "lifespan": 20,
             "unit_rate": 200_000_000,
             "mobilisation_min": 200_000,
             "mobilisation_perc": 0.003,
             "maintenance_perc": 0.015,
             "crew_min": 3,
             "crew_for5": 1,
             "insurance_perc": 0.01,
             "h2retrieval_type": 'tank',
             "consumption": 9360,#in kwh/ton
             "capacity": 57}  #in ton/hr


# *** Default inputs: Commodity class ***

commodity_lhydrogen_data = {"name": 'Liquid hydrogen',
                            "type": 'Liquid hydrogen',
                  "handling_fee": 490,
                  "smallhydrogen_perc": 30,
                  "largehydrogen_perc": 70,
                  "smallammonia_perc": 0,
                  "largeammonia_perc": 0,
                  "handysize_perc": 0,
                  "panamax_perc": 0,
                  "vlcc_perc": 0,
                  "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
                                                  'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}

commodity_ammonia_data = {"name": 'Ammonia',
                "type": 'Ammonia',
                "handling_fee": 150,
                "smallhydrogen_perc": 0,
                "largehydrogen_perc": 0,
                "smallammonia_perc": 40,
                "largeammonia_perc": 60,
                "handysize_perc": 0,
                "panamax_perc": 0,
                "vlcc_perc": 0,
                "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
                                                'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}
commodity_MCH_data = {"name": 'MCH',
            "type": 'MCH',
            "handling_fee": 1000,
            "smallhydrogen_perc": 0,
            "largehydrogen_perc": 0,
            "smallammonia_perc": 0,
            "largeammonia_perc": 0,
            "handysize_perc": 30,
            "panamax_perc": 40,
            "vlcc_perc": 30,
            "historic_data": pd.DataFrame(data={'year': [2014, 2015, 2016, 2017, 2018],
                                                  'volume': [1_000_000, 1_100_000, 1_250_000, 1_400_000, 1_500_000]})}

# *** Default inputs: Vessel class ***

"Liquid hydrogen:"

smallhydrogen_data = {"name": 'smallhydrogen_1',
                  "type": 'Smallhydrogen',
                  "call_size": 10_000,
                  "LOA": 200,
                  "draft": 10,
                  "beam": 24,
                  "max_cranes": 3,
                  "all_turn_time": 20,
                  "pump_capacity": 1_000,
                  "mooring_time": 3,
                  "demurrage_rate": 600}

largehydrogen_data = {"name": 'largehydrogen_1',
                  "type": 'Largehydrogen',
                  "call_size": 30_000,
                  "LOA": 300,
                  "draft": 12,
                  "beam": 43,
                  "max_cranes": 3,
                  "all_turn_time": 30,
                  "pump_capacity": 3_000,
                  "mooring_time": 3,
                  "demurrage_rate": 700}

"Ammonia:"

smallammonia_data = {"name": 'smallammonia_1',
                 "type": 'Smallammonia',
                 "call_size": 20_000,
                 "LOA": 170,
                 "draft": 9.5,
                 "beam": 22,
                 "max_cranes": 2,
                 "all_turn_time": 24,
                 "pump_capacity": 2_000,
                 "mooring_time": 3,
                 "demurrage_rate": 750}

largeammonia_data = {"name": 'largeammonia_1',
                 "type": 'Largeammonia',
                 "call_size": 55_000,
                 "LOA": 230,
                 "draft": 11,
                 "beam": 40,
                 "max_cranes": 2,
                 "all_turn_time": 24,
                 "pump_capacity": 5_500,
                 "mooring_time": 3,
                 "demurrage_rate": 750}

"MCH:"
handysize_data = {"name": 'Handysize_1',
                  "type": 'Handysize',
                  "call_size": 35_000,
                  "LOA": 130,
                  "draft": 10,
                  "beam": 24,
                  "max_cranes": 2,
                  "all_turn_time": 24,
                  "pump_capacity": 3_500,
                  "mooring_time": 3,
                  "demurrage_rate": 600}

panamax_data = {"name": 'Panamax_1',
                "type": 'Panamax',
                "call_size": 65_000,
                "LOA": 220,
                "draft": 13,
                "beam": 32.2,
                "max_cranes": 3,
                "all_turn_time": 36,
                "pump_capacity": 6_500,
                "mooring_time": 3,
                "demurrage_rate": 730}

vlcc_data = {"name": 'VLCC_1',
             "type": 'VLCC',
             "call_size": 200_000,
             "LOA": 300,
             "draft": 18.5,
             "beam": 55,
             "max_cranes": 3,
             "all_turn_time": 40,
             "pump_capacity": 20_000,
             "mooring_time": 3,
             "demurrage_rate": 1000}


# *** Default inputs: Labour class ***

labour_data = {"name": 'Labour',
               "international_salary": 105_000,
               "international_staff": 4,
               "local_salary": 18_850,
               "local_staff": 10,
               "operational_salary": 46_000,
               "shift_length": 8,
               "annual_shifts": 200}

# *** Default inputs: Energy class ***

energy_data = {"name": 'Energy',
               "price": 0.09}

