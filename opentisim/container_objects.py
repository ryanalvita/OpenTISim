"""Main generic object classes:

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

from opentisim import container_mixins

# The generic Quay_wall class
Quay_Wall = type('Quay_Wall', (container_mixins.identifiable_properties_mixin,  # Give it a name
                               container_mixins.quay_wall_properties_mixin,
                               container_mixins.history_properties_mixin,  # Give it procurement history
                               container_mixins.hascapex_properties_mixin,  # Give it capex info
                               container_mixins.hasopex_properties_mixin,  # Give it opex info
                               container_mixins.hasrevenue_properties_mixin,  # Give it revenue info
                               container_mixins.hastriggers_properties_mixin,  # Give it investment triggers
                               container_mixins.hasland_properties_mixin),
                 {})  # The dictionary is empty because the site type is generic

# The generic Berth class
Berth = type('Berth', (container_mixins.identifiable_properties_mixin,      # Give it a name
                       container_mixins.history_properties_mixin,           # Give it procurement history
                       container_mixins.berth_properties_mixin,             # Give it berth properties
                       container_mixins.hascapex_properties_mixin,          # Give it capex info
                       container_mixins.hasopex_properties_mixin,           # Give it opex info
                       container_mixins.hasrevenue_properties_mixin,        # Give it revenue info
                       container_mixins.hastriggers_properties_mixin),      # Give it investment triggers
             {})                                                            # The dictionary is empty because the site type is generic

# The generic Channel class
Channel = type('Channel', (container_mixins.identifiable_properties_mixin,  # Give it a name
                           container_mixins.history_properties_mixin,       # Give it procurement history
                           container_mixins.channel_properties_mixin,       # Give it channel properties
                           container_mixins.hascapex_properties_mixin,      # Give it capex info
                           container_mixins.hasopex_properties_mixin,       # Give it opex info
                           container_mixins.hasrevenue_properties_mixin,    # Give it revenue info
                           container_mixins.hastriggers_properties_mixin),  # Give it investment triggers
               {})                                                          # The dictionary is empty because the site type is generic

# The generic Cyclic_Unloader class
Cyclic_Unloader = type('Cyclic_Unloader', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                           container_mixins.history_properties_mixin,  # Give it procurement history
                                           container_mixins.cyclic_properties_mixin,
                                           container_mixins.hascapex_properties_mixin,  # Give it capex info
                                           container_mixins.hasopex_properties_mixin,  # Give it opex info
                                           container_mixins.hasrevenue_properties_mixin,  # Give it revenue info
                                           container_mixins.hastriggers_properties_mixin),  # Give it investment triggers
                       {})  # The dictionary is empty because the site type is generic

# The generic Horizontal transport class
Horizontal_Transport = type('Horizontal_Transport', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                                     container_mixins.history_properties_mixin,  # Give it procurement history
                                                     container_mixins.transport_properties_mixin,
                                                     container_mixins.hascapex_properties_mixin,  # Give it capex info
                                                     container_mixins.hasopex_properties_mixin,  # Give it opex info
                                                     container_mixins.hastriggers_properties_mixin),  # Give it investment triggers
                            {})  # The dictionary is empty because the site type is generic

# The generic Commodity class
Commodity = type('Commodity', (container_mixins.identifiable_properties_mixin,  # Give it a name
                               container_mixins.commodity_properties_mixin,
                               container_mixins.hasscenario_properties_mixin),
                 {})  # The dictionary is empty because the site type is generic

# The generic container class
Container = type('Container', (container_mixins.identifiable_properties_mixin,  # Give it a name
                               container_mixins.container_properties_mixin),
                 {})  # The dictionary is empty because the site type is generic

# The generic laden and reefer stack class
Laden_Stack = type('Laden_Stack', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                   container_mixins.history_properties_mixin,
                                   container_mixins.laden_stack_properties_mixin,
                                   container_mixins.hasopex_properties_mixin,
                                   container_mixins.hascapex_properties_mixin,  # Give it capex info
                                   container_mixins.hastriggers_properties_mixin,  # Give it investment triggers
                                   container_mixins.hasland_properties_mixin),
                   {})  # The dictionary is empty because the site type is generic

# The generic stack equipment class
Stack_Equipment = type('Stack_Equipment', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                           container_mixins.history_properties_mixin,
                                           container_mixins.stack_equipment_properties_mixin,
                                           container_mixins.hascapex_properties_mixin,  # Give it capex info
                                           container_mixins.hasopex_properties_mixin,  # Give it opex info
                                           container_mixins.hastriggers_properties_mixin),  # Give it investment triggers
                       {})  # The dictionary is empty because the site type is generic

# Empty_stack class
Empty_Stack = type('Empty_Stack', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                   container_mixins.history_properties_mixin,
                                   container_mixins.empty_stack_properties_mixin,
                                   container_mixins.hasopex_properties_mixin,
                                   container_mixins.hascapex_properties_mixin,  # Give it capex info
                                   container_mixins.hastriggers_properties_mixin,  # Give it investment triggers
                                   container_mixins.hasland_properties_mixin),
                   {})  # The dictionary is empty because the site type is generic

# OOG_stack class
OOG_Stack = type('Empty_Stack', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                 container_mixins.history_properties_mixin,
                                 container_mixins.oog_stack_properties_mixin,
                                 container_mixins.hasopex_properties_mixin,
                                 container_mixins.hascapex_properties_mixin,  # Give it capex info
                                 container_mixins.hastriggers_properties_mixin,  # Give it investment triggers
                                 container_mixins.hasland_properties_mixin),
                 {})  # The dictionary is empty because the site type is generic

# The general Gates class
Gate = type('Gate', (container_mixins.identifiable_properties_mixin,    # Give it a name
                     container_mixins.history_properties_mixin,
                     container_mixins.gate_properties_mixin,
                     container_mixins.hascapex_properties_mixin,        # Give it capex info
                     container_mixins.hasopex_properties_mixin,         # Give it opex info
                     container_mixins.hastriggers_properties_mixin,     # Give it investment triggers
                     container_mixins.hasland_properties_mixin),
            {})  # The dictionary is empty because the site type is generic

# The general Barge Berth class
Barge_Berth = type('Barge_Berth', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                   container_mixins.history_properties_mixin,
                                   container_mixins.gate_properties_mixin,
                                   container_mixins.hascapex_properties_mixin,  # Give it capex info
                                   container_mixins.hasopex_properties_mixin,  # Give it opex info
                                   container_mixins.hastriggers_properties_mixin,  # Give it investment triggers
                                   container_mixins.hasland_properties_mixin),
                   {})  # The dictionary is empty because the site type is generic

# The general Empty Container Handler (ECH) class
Empty_Handler = type('Empty_Handler', (container_mixins.identifiable_properties_mixin,  # Give it a name
                                       container_mixins.history_properties_mixin,
                                       container_mixins.empty_handler_properties_mixin,
                                       container_mixins.hascapex_properties_mixin,  # Give it capex info
                                       container_mixins.hasopex_properties_mixin,  # Give it opex info
                                       container_mixins.hastriggers_properties_mixin),  # Give it investment triggers
                     {})  # The dictionary is empty because the site type is generic

# The general Vessel class
Vessel = type('Vessel', (container_mixins.identifiable_properties_mixin,
                         container_mixins.vessel_properties_mixin),
              {})  # The dictionary is empty because the site type is generic

# The general Labour class
Labour = type('Labour', (container_mixins.identifiable_properties_mixin,
                         container_mixins.labour_properties_mixin),
              {})  # The dictionary is empty because the site type is generic

# The general Energy class
Energy = type('Energy', (container_mixins.identifiable_properties_mixin,
                         container_mixins.energy_properties_mixin),
              {})  # The dictionary is empty because the site type is generic

# The general services class
General_Services = type('General_Services', (container_mixins.identifiable_properties_mixin,
                                             container_mixins.hasland_properties_mixin,
                                             container_mixins.hasopex_properties_mixin,
                                             container_mixins.hascapex_properties_mixin,
                                             container_mixins.general_services_mixin,
                                             container_mixins.history_properties_mixin),
                        {})  # The dictionary is empty because the site type is generic

# The indirect costs class
Indirect_Costs = type('Indirect Costs', (container_mixins.identifiable_properties_mixin,
                                         container_mixins.indirect_costs_mixin),
                      {})  # The dictionary is empty because the site type is generic

# The land costs class
Land_Price = type('Land Price', (container_mixins.identifiable_properties_mixin,
                                 container_mixins.hascapex_properties_mixin),
                  {})  # The dictionary is empty because the site type is generic