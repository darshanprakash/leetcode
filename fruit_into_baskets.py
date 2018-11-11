def solution(tree):
    res = cur = count_b = a = b = 0

    for c in tree:
        cur = cur + 1 if c in (a, b) else count_b + 1
        count_b = count_b + 1 if c == b else 1
        if b != c: a, b = b, c
        res = max(res, cur)

    return res


if __name__ == "__main__":
    row = [1, 2, 1, 3, 4, 3, 5, 1, 2]
    print(solution(row))
