from collections import deque

from numpy import empty

graph = {}
graph['you'] = ['kyaw', 'william', 'R gyi', 'Htet', 'nobody']
graph['kyaw'] = ['E', 'F']
graph['william'] = ['G', 'H', 'arkar']
graph['Htet'] = ['arkar', 'A', 'B']
graph['R gyi'] = ['C', 'D']
graph['nobody'] = []
graph['E'] = []
graph['F'] = []
graph['G'] = []
graph['H'] = []
graph['arkar'] = []
graph['A'] = []
graph['B'] = []
graph['C'] = []
graph[
    'D'
] = []



def is_mango_seller(someone):
    return someone == 'C'


def search_queue(person):
    search_queue = deque(graph[person])
    while search_queue:
        someone = search_queue.popleft()
        searched = []
        if someone not in searched:
            if is_mango_seller(someone):
                print(f"{someone} is mango seller")
                return True
            else:
                search_queue += graph[someone]
                searched.append(someone)
                print(searched)
    return False


print("Search queue: ", search_queue('you'))