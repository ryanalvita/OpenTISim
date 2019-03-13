quay_data 	  = {"name": 'quay_01',
                     "t0_length": 0, 
          	     "ownership": 'Port authority', 
          	     "delivery_time": 2, 
          	     "lifespan": 50, 
          	     "mobilisation_min": 2500000,
          	     "mobilisation_perc": 0.02, 
          	     "maintenance_perc": 0.01, 
          	     "insurance_perc": 0.01,
          	     "length": 400, 
          	     "depth": 14,
          	     "freeboard": 4, 
          	     "Gijt_constant": 757.20, 
          	     "Gijt_coefficient": 1.2878} 

berth_data 	  = {"name": 'berth_01',
                     "t0_quantity": 0, 
           	     "crane_type": 'Mobile cranes', 
           	     "max_cranes": 3}

gantry_crane_data = {"name": 'gantry_crane_01',
                     "t0_quantity": 0, 
                     "ownership": 'Terminal operator', 
                     "delivery_time": 1, 
                     "lifespan": 40, 
                     "unit_rate": 19500000,
                     "mobilisation_perc": 0.15, 
                     "maintenance_perc": 0.02, 
                     "insurance_perc": 0.01, 
                     "crew": 3, 
                     "crane_type": 'Gantry crane', 
                     "lifting_capacity": 70, 
                     "hourly_cycles": 60, 
                     "eff_fact": 0.55,
                     "utilisation": 0.80}

harbour_crane_data = {"name": 'harbour_crane_01',
                      "t0_quantity": 0, 
                      "ownership": 'Terminal operator', 
                      "delivery_time": 1, 
                      "lifespan": 40, 
                      "unit_rate": 14000000, 
                      "mobilisation_perc": 0.15, 
                      "maintenance_perc": 0.02, 
                      "insurance_perc": 0.01, 
                      "crew": 3, 
                      "crane_type": 'Harbour crane crane', 
                      "lifting_capacity": 40, 
                      "hourly_cycles": 40, 
                      "eff_fact": 0.55,
                      "utilisation": 0.80}

mobile_crane_data  = {"name": 'mobile_crane_01',
                      "t0_quantity": 0, 
                      "ownership": 'Terminal operator', 
                      "delivery_time": 1, 
                      "lifespan": 20, 
                      "unit_rate": 3325000,
                      "mobilisation_perc": 0.15, 
                      "maintenance_perc": 0.031,
                      "insurance_perc": 0.01, 
                      "crew": 3, 
                      "crane_type": 'Mobile crane',
                      "lifting_capacity": 60, 
                      "hourly_cycles": 30, 
                      "eff_fact": 0.55,
                      "utilisation": 0.80}

continuous_screw_data = {"name": 'continuous_loader_01',
                         "t0_quantity": 0, 
                         "ownership": 'Terminal operator', 
                         "delivery_time": 1, 
                         "lifespan": 30, 
                         "unit_rate": 6900000, 
                         "mobilisation_perc": 0.15, 
                         "maintenance_perc": 0.02, 
                         "insurance_perc": 0.01, 
                         "crew": 2,
                         "crane_type": 'Screw unloader', 
                         "peak_capacity": 700, 
                         "eff_fact": 0.55, 
                         "utilisation": 0.80}

silo_data      	   = {"name": 'silo_01',
                      "t0_capacity": 0, 
                      "ownership": 'Terminal operator',
               	      "delivery_time": 1, 
               	      "lifespan": 30, 
               	      "unit_rate": 60, 
               	      "mobilisation_min": 200000, 
               	      "mobilisation_perc": 0.003, 
               	      "maintenance_perc": 0.02, 
               	      "crew": 1, 
               	      "insurance_perc": 0.01, 
               	      "storage_type": 'Silos', 
               	      "consumption": 0.002, 
               	      "silo_capacity": 6000}

warehouse_data 	   = {"name": 'warehouse_01',
                      "t0_capacity": 0, 
               	      "ownership": 'Terminal operator', 
               	      "delivery_time": 1, 
               	      "lifespan": 30, 
               	      "unit_rate": 140,
               	      "mobilisation_min": 200000, 
               	      "mobilisation_perc": 0.001, 
               	      "maintenance_perc": 0.01, 
               	      "crew": 3, 
               	      "insurance_perc": 0.01, 
               	      "storage_type": 'Warehouse', 
               	      "consumption": 0.002, 
               	      "silo_capacity": 'n/a'}

hinterland_station_data = {"name": 'hinterland_station_01',
                           "t0_capacity": 0, 
                           "ownership": 'Terminal operator', 
                           "delivery_time": 1, 
                           "lifespan": 15, 
                           "unit_rate": 4000, 
                           "mobilisation": 100000, 
                           "maintenance_perc": 0.02, 
                           "consumption": 0.25, 
                           "insurance_perc": 0.01, 
                           "crew": 2, 
                           "utilisation": 0.80, 
                           "capacity_steps": 300}

quay_conveyor_data = {"name": 'quay_converyor_01',
                      "t0_capacity": 0, 
                      "length": 500, 
                      "ownership": 'Terminal operator', 
                      "delivery_time": 1, 
                      "lifespan": 10, 
                      "unit_rate": 6, 
                      "mobilisation": 30000,
                      "maintenance_perc": 0.10, 
                      "insurance_perc": 0.01, 
                      "consumption_constant": 81,
                      "consumption_coefficient": 0.08, 
                      "crew": 1, 
                      "utilisation": 0.80, 
                      "capacity_steps": 400}

hinterland_conveyor_data = {"name": 'hinterland_conveyor_01',
                            "t0_capacity": 0, 
                            "length": 500, 
                            "ownership": 'Terminal operator', 
                            "delivery_time": 1, 
                            "lifespan": 10, 
                            "mobilisation": 30000, 
                            "unit_rate": 6, 
                            "maintenance_perc": 0.10, 
                            "insurance_perc": 0.01, 
                            "consumption_constant": 81, 
                            "consumption_coefficient": 0.08, 
                            "crew": 1, 
                            "utilisation": 0.80, 
                            "capacity_steps": 400}