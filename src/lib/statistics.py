# src/lib/statistics.py

from math import sqrt
from typing import List


def mean(data: List[float]) -> float:
    return sum(data) / len(data)


def variance(data: List[float]) -> float:
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def standard_deviation(data: List[float]) -> float:
    return sqrt(variance(data))
