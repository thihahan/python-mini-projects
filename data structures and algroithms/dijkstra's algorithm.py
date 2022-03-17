graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
graph['fin'] = {}
print(f"graph: {graph}")

costs = {}
inifity = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['fin'] = inifity
print(f'costs: {costs}')

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = inifity
print(f"parents: {parents}")

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if (costs[node] < lowest_cost) and (node not in processed):
            lowest_cost = costs[node]
            lowest_cost_node = node
    print('lowest_cost_node: ', lowest_cost_node)
    return lowest_cost_node
    
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    print(f"neighbors: {neighbors}")
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
print(costs['fin'])
