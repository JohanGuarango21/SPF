
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
    Still working......

