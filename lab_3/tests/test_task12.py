import unittest
import time
import tracemalloc
from lab_3.src.task12 import colorLabyrinth


class TestColorLabyrinth(unittest.TestCase):
    def setUp(self) -> None:
        self.n = 10**5
        self.m = 10**5
        self.k = 10**5
        self.edges = []
        # Создаем максимальное количество коридоров между комнатами
        # с разными цветами (цвета от 1 до 100)
        for i in range(1, self.m + 1):
            u = (i % self.n) + 1  # равномерно распределяем по комнатам
            v = ((i + 1) % self.n) + 1  # следующая комната
            c = (i % 100) + 1  # цвет от 1 до 100
            self.edges.append([u, v, c])

        # Генерируем максимальное описание пути (цвета от 1 до 100)
        self.colors = [(i % 100) + 1 for i in range(self.k)]

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

