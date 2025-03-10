from pynput.keyboard import Key

stratagems = {"MG-43 Machine Gun": [[Key.down, Key.left, Key.down, Key.up, Key.right],
                                    "stratagems/Machine_Gun_Stratagem_Icon.png"],
              "APW-1 Anti-Materiel Rifle": [[Key.down, Key.left, Key.right, Key.up, Key.down],
                                            "stratagems/Anti-Materiel_Rifle_Stratagem_Icon.png"],
              "M-105 Stalwart": [[Key.down, Key.left, Key.down, Key.up, Key.up, Key.left],
                                 "stratagems/Stalwart_Stratagem_Icon.png"],
              "EAT-17 Expendable Anti-Tank": [[Key.down, Key.down, Key.left, Key.up, Key.right],
                                              "stratagems/Expendable_Anti-Tank_Stratagem_Icon.png"],
              "GR-8 Recoilless Rifle": [[Key.down, Key.left, Key.right, Key.right, Key.left],
                                        "stratagems/Recoilless_Rifle_Stratagem_Icon.png"],
              "FLAM-40 Flamethrower": [[Key.down, Key.left, Key.up, Key.down, Key.up],
                                       "stratagems/Flamethrower_Stratagem_Icon.png"],
              "AC-8 Autocannon": [[Key.down, Key.left, Key.down, Key.up, Key.up, Key.right],
                                  "stratagems/Autocannon_Stratagem_Icon.png"],
              "MG-206 Heavy Machine Gun": [[Key.down, Key.left, Key.up, Key.down, Key.down],
                                           "stratagems/Heavy_Machine_Gun_Stratagem_Icon.png"],
              "RL-77 Airburst Rocket Launcher": [[Key.down, Key.up, Key.up, Key.left, Key.right],
                                                 "stratagems/RL-77_Airburst_Rocket_Launcher_Stratagem_Icon.png"],
              "MLS-4X Commando": [[Key.down, Key.left, Key.up, Key.down, Key.right],
                                  "stratagems/Commando_Stratagem_Icon.png"],
              "RS-422 Railgun": [[Key.down, Key.right, Key.down, Key.up, Key.left, Key.right],
                                 "stratagems/Railgun_Stratagem_Icon.png"],
              "FAF-14 Spear": [[Key.down, Key.down, Key.up, Key.down, Key.down], "stratagems/Spear_Stratagem_Icon.png"],
              "StA-X3 W.A.S.P. Launcher": [[Key.down, Key.down, Key.up, Key.down, Key.right],
                                           "stratagems/StA-X3_W.A.S.P._Launcher_Stratagem_Icon.png"],
              "Orbital Gatling Barrage": [[Key.right, Key.down, Key.left, Key.up, Key.up],
                                          "stratagems/Orbital_Gatling_Barrage_Stratagem_Icon.png"],
              "Orbital Airburst Strike": [[Key.right, Key.right, Key.right],
                                          "stratagems/Orbital_Airburst_Strike_Stratagem_Icon.png"],
              "Orbital 120mm HE Barrage": [[Key.right, Key.right, Key.down, Key.left, Key.right, Key.down],
                                           "stratagems/Orbital_120mm_HE_Barrage_Stratagem_Icon.png"],
              "Orbital 380mm HE Barrage": [[Key.right, Key.down, Key.up, Key.up, Key.left, Key.down, Key.down],
                                           "stratagems/Orbital_380mm_HE_Barrage_Stratagem_Icon.png"],
              "Orbital Walking Barrage": [[Key.right, Key.down, Key.right, Key.down, Key.right, Key.down],
                                          "stratagems/Orbital_Walking_Barrage_Stratagem_Icon.png"],
              "Orbital Laser": [[Key.right, Key.down, Key.up, Key.right, Key.down],
                                "stratagems/Orbital_Laser_Stratagem_Icon.png"],
              "Orbital Napalm Barrage": [[Key.right, Key.right, Key.down, Key.left, Key.right, Key.up],
                                         "stratagems/Orbital_Napalm_Barrage_Stratagem_Icon.png"],
              "Orbital Railcannon Strike": [[Key.right, Key.up, Key.down, Key.down, Key.right],
                                            "stratagems/Orbital_Railcannon_Strike_Stratagem_Icon.png"],
              "Eagle Strafing Run": [[Key.up, Key.right, Key.right],
                                     "stratagems/Eagle_Strafing_Run_Stratagem_Icon.png"],
              "Eagle Airstrike": [[Key.up, Key.right, Key.down, Key.right],
                                  "stratagems/Eagle_Airstrike_Stratagem_Icon.png"],
              "Eagle Cluster Bomb": [[Key.up, Key.right, Key.down, Key.down, Key.right],
                                     "stratagems/Eagle_Cluster_Bomb_Stratagem_Icon.png"],
              "Eagle Napalm Airstrike": [[Key.up, Key.right, Key.down, Key.up],
                                         "stratagems/Eagle_Napalm_Airstrike_Stratagem_Icon.png"],
              "LIFT-850 Jump Pack": [[Key.down, Key.up, Key.up, Key.down, Key.up],
                                     "stratagems/Jump_Pack_Stratagem_Icon.png"],
              "Eagle Smoke Strike": [[Key.up, Key.right, Key.up, Key.down],
                                     "stratagems/Eagle_Smoke_Strike_Stratagem_Icon.png"],
              "Eagle 110mm Rocket Pods": [[Key.up, Key.right, Key.up, Key.left],
                                          "stratagems/Eagle_110mm_Rocket_Pods_Stratagem_Icon.png"],
              "Eagle 500kg Bomb": [[Key.up, Key.right, Key.down, Key.down, Key.down],
                                   "stratagems/Eagle_500kg_Bomb_Stratagem_Icon.png"],
              "M-102 Fast Recon Vehicle": [[Key.left, Key.down, Key.right, Key.down, Key.right, Key.down, Key.up],
                                           "stratagems/M-102_Fast_Recon_Vehicle_Stratagem_Icon.png"],
              "Orbital Precision Strike": [[Key.right, Key.right, Key.up],
                                           "stratagems/Orbital_Precision_Strike_Stratagem_Icon.png"],
              "Orbital Gas Strike": [[Key.right, Key.right, Key.down, Key.right],
                                     "stratagems/Orbital_Gas_Strike_Stratagem_Icon.png"],
              "Orbital EMS Strike": [[Key.right, Key.right, Key.left, Key.down],
                                     "stratagems/Orbital_EMS_Strike_Stratagem_Icon.png"],
              "Orbital Smoke Strike": [[Key.right, Key.right, Key.down, Key.up],
                                       "stratagems/Orbital_Smoke_Strike_Stratagem_Icon.png"],
              "E/MG-101 HMG Emplacement": [[Key.down, Key.up, Key.left, Key.right, Key.right, Key.left],
                                           "stratagems/HMG_Emplacement_Stratagem_Icon.png"],
              "FX-12 Shield Generator Relay": [[Key.down, Key.down, Key.left, Key.right, Key.left, Key.right],
                                               "stratagems/Shield_Generator_Relay_Stratagem_Icon.png"],
              "A/ARC-3 Tesla Tower": [[Key.down, Key.up, Key.right, Key.up, Key.left, Key.right],
                                      "stratagems/Tesla_Tower_Stratagem_Icon.png"],
              "MD-6 Anti-Personnel Minefield": [[Key.down, Key.left, Key.up, Key.right],
                                                "stratagems/Anti-Personnel_Minefield_Stratagem_Icon.png"],
              "B-1 Supply Pack": [[Key.down, Key.left, Key.down, Key.up, Key.up, Key.down],
                                  "stratagems/Supply_Pack_Stratagem_Icon.png"],
              "GL-21 Grenade Launcher": [[Key.down, Key.left, Key.up, Key.left, Key.down],
                                         "stratagems/Grenade_Launcher_Stratagem_Icon.png"],
              "LAS-98 Laser Cannon": [[Key.down, Key.left, Key.down, Key.up, Key.left],
                                      "stratagems/Laser_Cannon_Stratagem_Icon.png"],
              "MD-I4 Incendiary Mines": [[Key.down, Key.left, Key.left, Key.down],
                                         "stratagems/Incendiary_Minefield_Stratagem_Icon.png"],
              "AX/LAS-5 \"Guard Dog\" Rover": [[Key.down, Key.up, Key.left, Key.up, Key.right, Key.right],
                                               "stratagems/Guard_Dog_Rover_Stratagem_Icon.png"],
              "SH-20 Ballistic Shield Backpack": [[Key.down, Key.left, Key.down, Key.down, Key.up, Key.left],
                                                  "stratagems/Ballistic_Shield_Backpack_Stratagem_Icon.png"],
              "ARC-3 Arc Thrower": [[Key.down, Key.right, Key.down, Key.up, Key.left, Key.left],
                                    "stratagems/Arc_Thrower_Stratagem_Icon.png"],
              "MD-17 Anti-Tank Mines": [[Key.down, Key.left, Key.up, Key.up],
                                        "stratagems/MD-17_Anti-Tank_Mines_Stratagem_Icon.png"],
              "LAS-99 Quasar Cannon": [[Key.down, Key.down, Key.up, Key.left, Key.right],
                                       "stratagems/Quasar_Cannon_Stratagem_Icon.png"],
              "SH-32 Shield Generator Pack": [[Key.down, Key.up, Key.left, Key.right, Key.left, Key.right],
                                              "stratagems/Shield_Generator_Pack_Stratagem_Icon.png"],
              "MD-8 Gas Mines": [[Key.down, Key.left, Key.left, Key.right],
                                 "stratagems/Gas_Minefield_Stratagem_Icon.png"],
              "A/MG-43 Machine Gun Sentry": [[Key.down, Key.up, Key.right, Key.right, Key.up],
                                             "stratagems/Machine_Gun_Sentry_Stratagem_Icon.png"],
              "A/G-16 Gatling Sentry": [[Key.down, Key.up, Key.right, Key.left],
                                        "stratagems/Gatling_Sentry_Stratagem_Icon.png"],
              "A/M-12 Mortar Sentry": [[Key.down, Key.up, Key.right, Key.right, Key.down],
                                       "stratagems/Mortar_Sentry_Stratagem_Icon.png"],
              "AX/AR-23 \"Guard Dog\"": [[Key.down, Key.up, Key.left, Key.up, Key.right, Key.down],
                                         "stratagems/Guard_Dog_Stratagem_Icon.png"],
              "A/AC-8 Autocannon Sentry": [[Key.down, Key.up, Key.right, Key.up, Key.left, Key.up],
                                           "stratagems/Autocannon_Sentry_Stratagem_Icon.png"],
              "A/MLS-4X Rocket Sentry": [[Key.down, Key.up, Key.right, Key.right, Key.left],
                                         "stratagems/Rocket_Sentry_Stratagem_Icon.png"],
              "A/M-23 EMS Mortar Sentry": [[Key.down, Key.up, Key.right, Key.down, Key.right],
                                           "stratagems/AM-23_EMS_Mortar_Sentry_Stratagem_Icon.png"],
              "EXO-45 Patriot Exosuit": [[Key.left, Key.down, Key.right, Key.up, Key.left, Key.down, Key.down],
                                         "stratagems/EXO-45_Patriot_Exosuit_Stratagem_Icon.png"],
              "EXO-49 Emancipator Exosuit": [[Key.left, Key.down, Key.right, Key.up, Key.left, Key.down, Key.up],
                                             "stratagems/EXO-49_Emancipator_Exosuit_Stratagem_Icon.png"],
              "TX-41 Sterilizer": [[Key.down, Key.left, Key.up, Key.down, Key.left],
                                   "stratagems/Sterilizer_Stratagem_Icon.png"],
              "AX/TX-13 \"Guard Dog\" Dog Breath": [[Key.down, Key.up, Key.left, Key.up, Key.right, Key.up],
                                                    "stratagems/Guard_Dog_Dog_Breath_Stratagem_Icon.png"],
              "SH-51 Directional Shield": [[Key.down, Key.up, Key.left, Key.right, Key.up, Key.up],
                                           "stratagems/SH-51_Directional_Shield_Stratagem_Icon.png"],
              "E/AT-12 Anti-Tank Emplacement": [[Key.down, Key.up, Key.left, Key.right, Key.right, Key.right],
                                                "stratagems/E_AT-12_Anti-Tank_Emplacement_Stratagem_Icon.png"],
              "A/FLAM-40 Flame Sentry": [[Key.down, Key.up, Key.right, Key.down, Key.up, Key.up],
                                         "stratagems/A_FLAM-40_Flame_Sentry_Stratagem_Icon.png"],
              "B-100 Portable Hellbomb": [[Key.down, Key.right, Key.up, Key.up, Key.up],
                                          "stratagems/Portable_Hellbomb_Stratagem_Icon.png"],
              "Reinforce": [[Key.up, Key.down, Key.right, Key.left, Key.up], "stratagems/Reinforce_Stratagem_Icon.png"],
              "Resupply": [[Key.down, Key.down, Key.up, Key.right], "stratagems/Resupply_Stratagem_Icon.png"],
              "Hellbomb": [[Key.down, Key.up, Key.left, Key.down, Key.up, Key.right, Key.down, Key.up],
                           "stratagems/Hellbomb_Stratagem_Icon.png"]}
