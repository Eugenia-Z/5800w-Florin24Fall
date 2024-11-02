import heapq
from collections import defaultdict

def min_cost_path_with_split_nodes(flights, airport_taxes, start, end):
    # Create the expanded graph
    graph = defaultdict(list)
    
    # Add flight edges (u_out to v_in with flight cost)
    for u, v, cost in flights:
        graph[f"{u}_out"].append((f"{v}_in", cost))
    
    # Add tax edges (v_in to v_out with airport tax cost)
    for city, tax in airport_taxes.items():
        graph[f"{city}_in"].append((f"{city}_out", tax))
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, f"{start}_in")]  #(cost, node)
    min_cost = {f"{start}_in": 0}
    
    while pq:
        curr_cost, node = heapq.heappop(pq)
        
        # If we've reached the destination out node, return the cost
        if node == f"{end}_out":
            return curr_cost

        # Relax edges:
        for neighbor, edge_cost in graph[node]:
            new_cost = curr_cost + edge_cost
            if new_cost < min_cost.get(neighbor, float('inf')):
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
                
    # if the destination is not reachable
    return float('inf')

if __name__ == "__main__":
    flights = [
    ("A", "B", 100),
    ("A", "C", 200),
    ("B", "C", 50),
    ("B", "D", 150),
    ("C", "D", 100)
    ]
    airport_taxes = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 40
    }
    start, end = "A", "D"
    print("Minimum cost from A to D (With Split Nodes and Taxes):", min_cost_path_with_split_nodes(flights, airport_taxes, start, end))