states_needed = set(['id','nv', 'ut','wa','mt','or','ca','az'])
stations = {}
stations['Kone'] = set(['id','nv','ut'])
stations['Ktwo'] = set(['wa','id','mt'])
stations['Kthree'] = set(['or','nv','ca'])
stations['Kfour'] = set(['nv', 'ut'])
stations['Kfive'] = set(['ca', 'az'])
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for state, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = state
            states_covered = covered
            print(state)
        #print("I here")
            
        final_stations.add(best_station)
        states_needed -= states_covered

print(final_stations)
        