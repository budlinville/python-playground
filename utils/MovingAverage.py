#  https://www.youtube.com/watch?v=FFX6bz4RCGU&list=WL&index=9

class MovingAverage:
    def __init__(self, size:int):
        """
        Initialize your data strucutre here.
        """
        self.array = []
        self.size = size

    def next(self, val: int) -> float:
        self.array.append(val)
        return sum(self.array[-self.size:]) / min(len(self.array), self.size)

