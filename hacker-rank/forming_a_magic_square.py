# https://www.hackerrank.com/challenges/magic-square-forming/problem


def formingMagicSquare(s):

    return 1


if __name__ == "__main__":
    test_cases = [
        ([5, 3, 4,
         1, 5, 8,
         6, 4, 2], 7),

        ([4, 9, 2,
         3, 5, 7,
         8, 1, 5], 1),

         ([4, 8, 2,
          4, 5, 7,
          6, 1, 6], 4)
    ]
    for test in test_cases:
        print("PASS" if formingMagicSquare(test[0]) == test[1] else "FAIL")
