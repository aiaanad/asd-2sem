from lab_2.src.task9 import delSubTree
import unittest
import random
import time
import tracemalloc


class TestDelSubTree(unittest.TestCase):
    def test_del_subtree_args1(self):
        # given
        n, m = 6, 4
        rel = [[-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]
        nodes = [6, 9, 7, 8]
        expected_result = [5, 4, 4, 1]
        # when
        result = delSubTree(n, rel, m, nodes)
        # then
        self.assertEqual(result, expected_result)

    def test_del_subtree_args2(self):
        # given
        n, m = 6, 4
        rel = [[-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]
        nodes = [6, 9, 0, 8]
        expected_result = [5, 4, 3, 1]
        # when
        result = delSubTree(n, rel, m, nodes)
        # then
        self.assertEqual(result, expected_result)

    def test_time_and_memory(self):
        # given
        expected_time = 2
        expected_memory = 256
        n, m = 2*10**5, 2*10**5
        rel = []
        for i in range(1, n + 1):
            left = 2 * i if 2 * i <= n else 0
            right = 2 * i + 1 if 2 * i + 1 <= n else 0
            rel.append((i, left, right))
        nodes = random.sample(range(1, 2*10**5+1), 2*10**5)
        # when
        start_time = time.perf_counter()
        delSubTree(n, rel, m, nodes)
        result_time = time.perf_counter() - start_time
        tracemalloc.start()
        delSubTree(n, rel, m, nodes)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()
        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")


if __name__ == "__main__":
    unittest.main()
