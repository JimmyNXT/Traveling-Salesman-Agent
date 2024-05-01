from heuristic import IHeuristic

class WeightedHeuristic:
    def __init__(self, weight:float, heuristic:IHeuristic) -> None:
        self.weight:float = weight
        self.heuristic:IHeuristic = heuristic