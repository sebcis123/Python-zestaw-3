import heapq


def dijkstra(graph, start):
    # Inicjalizacja
    distances = {vertex: float('inf') for vertex in graph}  # odległości do wszystkich wierzchołków
    distances[start] = 0  # odległość do wierzchołka startowego to 0
    priority_queue = [(0, start)]
    visited = set()  # zbiór odwiedzonych wierzchołków

    while priority_queue:
        # pobranie wierzchołka o najniższej odległości z kolejki
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # przetwarzanie sąsiadów bieżącego wierzchołka
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # jeśli znaleziono krótszą ścieżkę do sąsiada
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    print(f"Najkrótsze odległości od wierzchołka {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")
