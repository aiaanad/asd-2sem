import unittest
import random
import time
import tracemalloc
from lab_3.src.task12 import colorLabyrinth


class TestColorLabyrinth(unittest.TestCase):
    def setUp(self) -> None:
        self.n = 10**5
        self.m = 10**5
        self.k = 10**5
        self.colors = [random.choice(range(1, 101)) for _ in range(self.k)]
        self.edges = [[i+1, i+2, random.choice(range(1, 101))] for i in range(self.m)]

    def test_func_with_max_args(self):
        expected_time = 1
        expected_memory = 16*1024*1024

        start = time.perf_counter()
        colorLabyrinth(self.n, self.m, self.edges, self.k, self.colors)
        end = time.perf_counter() - start

        self.assertLessEqual(end, expected_time)

        tracemalloc.start()

        # Сохраняем текущий снимок памяти перед вызовом функции
        snapshot_before = tracemalloc.take_snapshot()
        # Вызываем функцию
        colorLabyrinth(self.n, self.m, self.edges, self.k, self.colors)
        # Снимаем снимок после вызова
        snapshot_after = tracemalloc.take_snapshot()
        # Вычисляем разницу в памяти
        memory = sum(stat.size for stat in snapshot_after.compare_to(snapshot_before, 'lineno'))
        tracemalloc.stop()

        self.assertLessEqual(memory, expected_memory)

