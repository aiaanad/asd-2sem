import unittest
import random
import time
import tracemalloc
from lab_4.src.task7 import find_longest_sub, main


class TestFindLongestSub(unittest.TestCase):
    def test_args1_from_task(self):
        input_data = 'cool toolbox'
        res = find_longest_sub(input_data)
        self.assertEqual(res, (1, 1, 3))

    def test_args2_from_task(self):
        input_data = 'aaa bb'
        res = find_longest_sub(input_data)
        self.assertEqual(res[2], 0)

    def test_args3_from_task(self):
        input_data = 'aabaa babbaab'
        res = find_longest_sub(input_data)
        self.assertIn(res, [(0, 4, 3), (2, 3, 3)])

    def test_main_performance(self):
        max_length = 100000
        s = ''.join(random.choice('abcdefghij') for _ in range(max_length-1000))
        t = ''.join(random.choice('abcdefghij') for _ in range(max_length-1000))
        common_part = 'x' * 1000
        s_mid = (max_length-1000) // 2
        t_mid = (max_length-1000) // 2
        s = s[:s_mid] + common_part + s[s_mid + 1000:]
        t = t[:t_mid] + common_part + t[t_mid + 1000:]
        pairs = [f"{s} {t}"]

        tracemalloc.start()
        start_time = time.time()
        main(pairs)
        elapsed_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.assertLess(elapsed_time, 15, "Превышено ограничение времени (15 сек)")
        self.assertLess(peak, 512 * 1024 * 1024, "Превышено ограничение памяти (512 MB)")


if __name__ == "__main__":
    unittest.main()
