import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def h(s, p, x) -> int:
    return sum([(ord(s[i]) - 97) * (x ** i % p) for i in range(len(s))]) % p


def precompute_hashes(s, k, p, x) -> list:
    res = [0 for _ in range(len(s) - k + 1)]
    res[len(s) - k] = h(s[len(s) - k:], p, x)
    y = 1
    for i in range(1, k + 1):
        y = (y * x) % p
    for i in range(len(s) - k - 1, -1, -1):
        res[i] = (x * res[i + 1] + (ord(s[i]) - 97) - y * (ord(s[i + k]) - 97)) % p

    return res


def had_sub_len_k(s, t, k) -> tuple:
    p = 10 ** 7 + 9
    x = random.randint(1, p - 1)
    hashes = precompute_hashes(s, k, p, x)
    for i in range(len(t) - k + 1):
        if h(t[i:i + k], p, x) in hashes:
            return True, s.find(t[i:i + k]), i
    return False, -1, -1


def find_longest_sub(input_data: str) -> tuple:
    s, t = input_data.split()
    s, t = min(s, t), max(s, t)
    if s in t:
        return 0, t.find(s), len(s)
    low = 1
    high = len(s)
    k = len(s) // 2
    i, j = -1, -1
    while high >= low:
        check, cur_i, cur_j = had_sub_len_k(s, t, k)
        if check:
            low = k + 1
            i, j = cur_i, cur_j
        else:
            high = k - 1
        k = (low + high) // 2
    if i < 0:
        return -1, -1, 0
    return i, j, k


def main(pairs):
    res = []
    for pair in pairs:
        res.append(find_longest_sub(pair))
    return res


if __name__ == "__main__":
    pairs = []
    input_path = '\\'.join(dir_path.split('\\')[:-1]) + '\\txtf\\input.txt'
    with open(input_path, 'r') as f:
        for line in f:
            pairs.append(line)
    output_path = '\\'.join(dir_path.split('\\')[:-1]) + '\\txtf\\output.txt'
    with open(output_path, 'w') as f:
        res = main(pairs)
        f.write('\n'.join(res))

