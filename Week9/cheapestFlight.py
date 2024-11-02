import heapq
from collections import defaultdict
def cheapest_flight(flights, start, end):
    
    # graph initialization
    graph = defaultdict(list)
    for (src, dest, cost) in flights:
        graph[src].append((dest, cost))
    
    # init a priority queue a dictionary for tracking min cost
    min_heap = [(0, start)]  # (cost, city)
    min_cost = {start: 0}
    
    while min_heap:
        curr_cost, curr_city = heapq.heappop(min_heap)
        
        # if we find a cheaper way to a city, we continue
        if min_cost.get(curr_city, float('inf')) < curr_cost:
            continue
            
        # Explore neighbors
        for neighbor, price in graph[curr_city]:
            new_cost = curr_cost + price
            
            # Only push to heap is a cheaper path to neight is found
            if new_cost < min_cost.get(neighbor, float('inf')):
                min_cost[neighbor] = new_cost
                heapq.heappush(min_heap, (new_cost, neighbor))
    return min_cost.get(end, -1)

flights = [
    ('A', 'B', 100),
    ('A', 'C', 200),
    ('B', 'C', 50),
    ('B', 'D', 200),
    ('C', 'D', 30),
    ('D', 'E', 100)
]

print(cheapest_flight(flights, 'A', 'E'))