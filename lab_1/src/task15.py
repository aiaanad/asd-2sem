def is_match(a, b):
    return (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']')


def delSeq(s: str) -> str:
    n = len(s)
    dp = [['' for _ in range(n)] for _ in range(n)]
    for _len in range(1, n + 1):
        r = _len - 1
        for l in range(n):
            if r >= n or l > r:
                continue

            if _len == 2:
                if is_match(s[l], s[r]):
                    dp[l][r] = s[l]+s[r]

            elif _len > 2:
                if is_match(s[l], s[r]):
                    dp[l][r] = s[l] + dp[l+1][r-1] + s[r]

                else:
                    for m in range(l+1, r):
                        dp[l][r] = max(dp[l][r], (dp[l][m]+dp[m+1][r]), key=len)
            r += 1
    return dp[0][n-1]


if __name__ == "__main__":
    s = '({{{{{[)})]'
    print(delSeq(s))

