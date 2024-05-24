from graph import Graph, Vertex
import random


class IHeuristic:
    def __init__(self, graph: Graph, id: int) -> None:
        self.graph = graph
        self.id = id
        self.name = "IHeuristic"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        raise NotImplementedError("This Function has not been implemented")


class RandomHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)
        self.name = "Random"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        return random.randrange(0, len(self.graph.vertexes))


class HasVisitedHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)
        self.name = "Has Visited"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        if next_vertex_id in visited:
            return -1
        else:
            return 1


class DistanceHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)
        self.name = "Distance"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        current_vertex: Vertex | None = self.graph.vertexes.get(current_vertex_id)
        if current_vertex is None:
            return float("inf")

        next_vertex: Vertex | None = self.graph.vertexes.get(next_vertex_id)
        if next_vertex is None:
            return float("inf")

        return current_vertex.position.distance_to(next_vertex.position)


class DirectionChangeHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)
        self.name = "Direction Change"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        current_vertex: Vertex | None = self.graph.vertexes.get(current_vertex_id)
        if current_vertex is None:
            return float("inf")

        next_vertex: Vertex | None = self.graph.vertexes.get(next_vertex_id)
        if next_vertex is None:
            return float("inf")

        previos_vertex: Vertex | None = self.graph.vertexes.get(previous_vertex_id)
        if previos_vertex is None:
            return float("inf")

        previous_angle = previos_vertex.position.angle_to(current_vertex.position)
        current_angle = current_vertex.position.angle_to(next_vertex.position)

        return abs(current_angle - previous_angle)


class AngleDeltaHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)
        self.name = "Angle Delta"

    def get_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int,
        visited: list[int],
    ) -> float:
        vertexes_copy: dict[int, Vertex] = self.graph.vertexes

        for vertex_id in visited:
            try:
                vertexes_copy.pop(vertex_id)
            except:
                pass

        try:
            vertexes_copy.pop(next_vertex_id)
        except:
            pass

        if len(vertexes_copy) <= 0:
            return float("inf")

        current_vertex: Vertex | None = self.graph.vertexes.get(current_vertex_id)
        if current_vertex is None:
            return float("inf")

        next_vertex: Vertex | None = self.graph.vertexes.get(next_vertex_id)
        if next_vertex is None:
            return float("inf")

        init_angle = current_vertex.position.angle_to(next_vertex.position)

        angle_count: int = len(vertexes_copy)
        angle_sum: float = 0

        for vertexes_id in vertexes_copy.keys():
            vertex = self.graph.vertexes.get(vertexes_id)
            if vertex is None:
                continue
            current_angle = current_vertex.position.angle_to(vertex.position)
            angle_sum = angle_sum + abs(init_angle - current_angle)

        return angle_sum / angle_count
