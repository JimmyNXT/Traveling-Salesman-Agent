import random
from datetime import datetime

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
        random.seed(datetime.now().timestamp())
        should_mutate:bool = random.uniform(0, 1) > -1
        if should_mutate:
            self.weight = self.weight + random.uniform(-1, 1)
