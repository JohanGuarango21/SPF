
import heapq

graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

def dijkstra(graph, start):
    distances = {}
    parents = {}

    for location in graph:
        distances[location] = float("inf")
        parents[location] = None

    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current = heapq.heappop(queue)

        if current_distance > distances[current]:
            continue

        for neighbor in graph[current]:
            weight = graph[current][neighbor]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, parents

def find_path(parents, start, destination):
    path = []
    current = destination

    while current is not None:
        path.insert(0, current)
        current = parents[current]

    if path[0] == start:
        return path
    else:
        return []

print("Available Locations: A, B, C, D, E, F")

start = input("Enter starting location: ").strip().upper()
destination = input("Enter destination: ").strip().upper()

if start not in graph or destination not in graph:
    print("Invalid location!")

else:
    distances, parents = dijkstra(graph, start)
    path = find_path(parents, start, destination)

    if path:
        print("Shortest Path:", " -> ".join(path))
        print("Total Distance:", distances[destination])
    else:
        print("No path found!")
