graph = {}
graph['start'] = {}
graph['start']['a'] = 10
graph['a'] = {}
graph['a']['b'] = 20
graph['b'] = {}
graph['b']['fin'] = 30
graph['b']['c'] = 1  
graph['c'] = {} #
graph['c']['a'] = 1
graph['fin'] = {}
print(f"graph: {graph}")

inifity = float('inf')
costs = {}
costs['a'] = 10 
costs['b'] = inifity 
costs['c'] = inifity
costs['fin'] = inifity
print(f"costs: {costs}")

parents = {}
parents['a'] = 'start'
parents['b'] = 'a'
parents['c'] = 'b'
parents['fin'] = inifity 
print(f"parents: {parents}")

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
print(f"costs: {costs}")
print(costs['fin'])


