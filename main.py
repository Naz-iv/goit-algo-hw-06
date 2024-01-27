import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph: nx.Graph, title="Graph") -> None:
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw(graph, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue", font_size=8)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()


def describe_graph(graph: nx.Graph) -> None:
    print(f"Кількість вузлів: {graph.number_of_nodes()}")
    print(f"Кількість ребер: {graph.number_of_edges()}")

    print("Список вузлів:", graph.nodes())
    print("Список ребер:", graph.edges())

    for node, degree in graph.degree():
        print(f"Ступінь вершини {node}: {degree}")


def task_1():
    cities = {
        "Київ": {"Чернігів": 145, "Житомир": 132, "Черкаси": 198, "Полтава": 345},
        "Чернігів": {"Київ": 145, "Суми": 230, "Черкаси": 180},
        "Житомир": {"Київ": 132, "Рівне": 245, "Вінниця": 310},
        "Черкаси": {"Київ": 198, "Кропивницький": 250, "Чернігів": 180},
        "Полтава": {"Київ": 345, "Харків": 290, "Суми": 220},
        "Суми": {"Чернігів": 230, "Харків": 150, "Полтава": 220},
        "Рівне": {"Луцьк": 270, "Житомир": 245, "Тернопіль": 315},
        "Вінниця": {"Житомир": 310, "Хмельницький": 180, "Чернівці": 420},
        "Кропивницький": {"Черкаси": 250, "Миколаїв": 160, "Дніпро": 310},
        "Харків": {"Суми": 150, "Полтава": 290, "Дніпро": 345},
        "Луцьк": {"Рівне": 270, "Житомир": 390, "Тернопіль": 340},
        "Хмельницький": {"Вінниця": 180, "Тернопіль": 120, "Чернівці": 220},
        "Чернівці": {"Львів": 385, "Івано-Франківськ": 250, "Хмельницький": 220},
        "Тернопіль": {"Луцьк": 340, "Рівне": 315, "Хмельницький": 120},
    }

    districts_map = nx.Graph()

    for city, connections in cities.items():
        districts_map.add_node(city)
        for connected_city, distance in connections.items():
            districts_map.add_edge(city, connected_city, weight=distance)

    return districts_map


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    country_graph = task_1()

    describe_graph(country_graph)

    visualize_graph(country_graph)

    # DFS
    dfs_paths = list(nx.dfs_edges(country_graph, source="Київ"))
    print(f"DFS шлях: {dfs_paths}")

    # BFS
    bfs_paths = list(nx.bfs_edges(country_graph, source="Київ"))
    print(f"BFS шлях: {bfs_paths}")

    print("\nШляхи відрізняються, так як: \nПошук у глибину (DFS) виконується шляхом відвідування вершини, а потім "
          "рекурсивного відвідування всіх сусідніх вершин, які ще не були відвідані.\nПошук у ширину (BFS) відрізняється "
          "від DFS тим, що він відвідує всі вершини на певному рівні перед тим, як перейти до наступного рівня. \n")

    for start_city in country_graph.nodes:
        shortest_paths = dijkstra(country_graph, start_city)
        print(f"Найкоротші шляхи від `{start_city}`: {shortest_paths}")
