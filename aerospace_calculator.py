import math
import csv
rocket_specs={'SLV':
              {'dry_mass':400,                  #all dry masses are in kilograms
               'max_propellant':310,            #all maximum propellants are in kilograms
               'exhaust_velocity':2530},        #all exhaust velocities are in meters per second
                'ASLV':
               {'dry_mass':900,
                'max_propellant':700,
                'exhaust_velocity':2600,
                },
                'PSLV':
                {'dry_mass':3200,
                 'max_propellant':2500,
                 'exhaust_velocity':3120},
                 'GSLV':
                 {'dry_mass':4500,
                  'max_propellant':12800,
                  'exhaust_velocity':4450
                  },
                  'LVM3':
                  {'dry_mass':6000,
                   'max_propellant':28000,
                   'exhaust_velocity':4340
                   },
                   'SSLV':
                   {'dry_mass':1100,
                    'max_propellant':300,
                    'exhaust_velocity':2800}}

def description():
    print('Aero Fuel and Range Calculator')
    print('\n')
    print('Description')
    print('This tool allows you to choose an aircraft registered in its database and once you input the vehicle type, name and the Target Delta-V boost, gives you the follwiing:-')
    print('Total Fuel Required')
    print('Maximum Tank Capacity')
    print('Leftover propellant reserve')
    print('Mission Status')
    
def run_mission_search():
    print("Input the following values:")
    print("Please choose the satelitle family you want to simulate from the given list(1-6):")
    print('1. SLV (Satellite Launch Vehicle):  Strictly Low Earth Orbit (LEO). It was only designed to deploy tiny, experimental tech-demonstrator satellites (like the Rohini series) weighing around 40 kg into low-altitude paths. It does not have the power for deep-space maneuvers.')
    print('2. ASLV (Augmented Satellite Launch Vehicle): Strictly Low Earth Orbit (LEO). It could carry payloads up to 150 kg into near-Earth tracks but lacked the heavy velocity stages required for lunar or escape trajectories.')
    print('3. PSLV (Polar Satellite Launch Vehicle): Highly versatile. It primary deploys Sun-Synchronous Polar Orbits (SSPO) for Earth-observation and climate monitoring. Crucially, its specialized "XL" configuration has the extreme structural accuracy needed to push payloads into Lunar Trajectories (Chandrayaan-1) and Martian Interplanetary Trajectories (Mangalyaan).')
    print('4. GSLV (Geosynchronous Satellite Launch Vehicle): Optimised for Geosynchronous Transfer Orbits (GTO) and Geostationary Orbits (GEO) for heavy communications, weather mapping, and navigation networks. It possesses high engine efficiency (high Exhaust Velocity) capable of deep-space operations.')
    print('5. LVM3 (Launch Vehicle Mark 3): Heaviest deployment bands. It injects heavy multi-ton commercial communication clusters into GTO and possesses the massive lifting capacity required to place heavy planetary rovers directly into Lunar Injection Vectors (Chandrayaan-3).')
    print('6. SSLV (Small Satellite Launch Vehicle): Strictly customized Low Earth Orbit (LEO) and planar circular orbits up to 500 km. It is designed entirely for low-altitude earth observation, internet constellations, and student science modules.')
    print('\nEnter you choice(numerical-1,2,3,4,5 or 6)')
    menu_choice=input()
    match menu_choice:
        case "1":
            selected_family="SLV"
        case "2":
            selected_family="ASLV"
        case "3":
            selected_family="PSLV"
        case "4":
            selected_family="GSLV"
        case "5":
            selected_family="LVM3"
        case "6":
            selected_family="SSLV"
        case _:
              print("Invalid choice selection")
    unique_vehicles=[]
    with open('isro_database.csv','r') as file:
                reader=csv.reader(file)
                for row in reader:
                    launcher_text=row[3].upper().strip()
                    satellite_name=row[1].strip()
                    if selected_family=='SLV':
                          if "SLV" in launcher_text and "ASLV" not in launcher_text and "PSLV" not in launcher_text and "GSLV" not in launcher_text:
                                 if satellite_name not in unique_vehicles:
                                    unique_vehicles.append(satellite_name) 
                    elif selected_family in launcher_text:
                        if satellite_name not in unique_vehicles:
                            unique_vehicles.append(satellite_name)
    for index, rocket_name in enumerate(unique_vehicles, start=1):
        print(f"{index}. {rocket_name}")
    print("\nSelect the exact vehicle number which you want to simulate: ")
    sub_choice=int(input())
    final_rocket=unique_vehicles[sub_choice-1]
    print(final_rocket)
                                                              #Actual physics engine and Tsiolkovsky Rocket Equation
    specs=rocket_specs[selected_family]
    dry_mass=specs["dry_mass"]
    max_propellant=specs["max_propellant"]
    exhaust_velocity=specs["exhaust_velocity"]
    delta_v = float(input("\nEnter your Target Delta-V boost for the simulation (in m/s): "))
    fuel_needed = dry_mass * (math.exp(delta_v / exhaust_velocity) - 1)
    print(f"\n=================== MISSION REPORT ===================")
    print(f"Simulating Profile for Satellite: {final_rocket}")
    print(f"Vehicle Family Utilized: {selected_family}")
    print(f"Calculated Fuel Required: {fuel_needed:.2f} kg")
    print(f"Maximum Tank Capacity: {max_propellant} kg")

         # Run the comparative check
    if fuel_needed > max_propellant:
        print("\n❌ MISSION FAILED: The vehicle's tanks are too small! The rocket ran out of fuel mid-maneuver.")
    else:
        remaining_fuel = max_propellant - fuel_needed
        print(f"\n✅ MISSION SUCCESSFUL: Vector achieved! Leftover propellant reserve: {remaining_fuel:.2f} kg.")
        print(f"=======================================================")



description()
run_mission_search()