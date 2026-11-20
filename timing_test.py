
import heapq
import random
import time

def dijkstra_heap(graph, start):
    distances = {}

    for location in graph:
        distances[location] = float("inf")

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
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

def dijkstra_array(graph, start):
    distances = {}
    visited = {}

    for location in graph:
        distances[location] = float("inf")

    distances[start] = 0

    for i in range(len(graph)):
        current = None
        smallest = float("inf")

        for location in graph:
            if location not in visited:
                if distances[location] < smallest:
                    smallest = distances[location]
                    current = location

        if current is None:
            break

        visited[current] = True

        for neighbor in graph[current]:
            weight = graph[current][neighbor]
            new_distance = distances[current] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

def create_graph(size):
    graph = {}

    for i in range(size):
        graph[i] = {}

    for i in range(size - 1):
        weight = random.randint(1, 20)
        graph[i][i + 1] = weight
        graph[i + 1][i] = weight

    for i in range(size * 2):
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)

        if a != b:
            weight = random.randint(1, 20)
            graph[a][b] = weight
            graph[b][a] = weight

    return graph

print("Size | Heap Time (seconds) | Array Time (seconds)")

for size in [10, 100, 1000]:
    graph = create_graph(size)

    start_time = time.perf_counter()
    heap_result = dijkstra_heap(graph, 0)
    heap_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    array_result = dijkstra_array(graph, 0)
    array_time = time.perf_counter() - start_time

    print(size, "|", round(heap_time, 6), "|", round(array_time, 6))

    if heap_result == array_result:
        print("Both algorithms gave the same distances.")
    else:
        print("Results do not match!")
