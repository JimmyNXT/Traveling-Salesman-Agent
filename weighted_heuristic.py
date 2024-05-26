import random
from heuristic import IHeuristic


class WeightedHeuristic:
    def __init__(self, weight: float, heuristic: IHeuristic) -> None:
        self.weight: float = weight
        self.heuristic: IHeuristic = heuristic

    def get_weighted_edge_value(
        self,
        current_vertex_id: int,
        next_vertex_id: int,
        previous_vertex_id: int|None,
        visited: list[int],
    ) -> float:

        return self.weight * self.heuristic.get_edge_value(
            current_vertex_id, next_vertex_id, previous_vertex_id, visited
        )

    def mutate(self):
        should_mutate:bool = random.uniform(0, 1) < 0.2
        if not should_mutate:
            return

        self.weight = self.weight + random.uniform(-0.5, 0.5)

