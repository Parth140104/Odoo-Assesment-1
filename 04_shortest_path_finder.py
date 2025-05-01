import heapq

def dijkstra(graph, start, end):
    # Priority queue: (distance, city)
    heap = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {}

    while heap:
        current_distance, current_city = heapq.heappop(heap)

        if current_city == end:
            break

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(heap, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    if distances[end] == float('inf'):
        return f"No path from {start} to {end}.", None

    return path, distances[end]


# --- Example input ---
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

# --- Run the function ---
path, distance = dijkstra(cities, start_city, destination_city)

# --- Output ---
if path:
    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")
else:
    print(distance)
