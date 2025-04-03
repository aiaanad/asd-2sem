from lab_1.src.task15 import delSeq
import unittest
import random
import time
import tracemalloc


class TestDelSeq(unittest.TestCase):
    def setUp(self):
        seq = ['(', ')', '{', '}', '[', ']']
        self.s = ''.join([random.choice(seq) for _ in range(100)])

    def test_time_and_memory(self):
        # given
        expected_time = 2
        expected_memory = 256

        # when
        start_time = time.perf_counter()
        delSeq((self.s + ',')[:-1])
        result_time = time.perf_counter() - start_time

        tracemalloc.start()
        delSeq((self.s + '.')[:-1])
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertLessEqual(result_time, expected_time, f"Значение {result_time} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def tearDown(self):
        del self.s


if __name__ == "__main__":
    unittest.main()
