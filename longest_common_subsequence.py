"""
Problem: find the longest common subsequence for given two strings.
Subsequence doesn't need to be contiguous block.
"""
#           B   D    C   A    B    A
#        0  0   0    0   0    0    0
# A      0  0   0    0   1    0    1
# B      0  1   1    1   1    2    2
# C      0  1   1    2   2    2    2
# B      0  1   1    1   1    3    3
# D      0  1   2    2   2    3    3
# A      0  1   2    2   3    3    3
# B      0  1   2    2   3    4    4


def find_longest_subsequence(str1, str2):
    """Find the longest subsequence."""
    memory = [[0 for _ in range(len(str1) + 1)]]
    common_subsequence = ""
    for i in range(len(str2)):
        memory.append([0 for _ in range(len(str1) + 1)])
    for i in range(1, len(memory)):
        for j in range(1, len(memory[0])):
            if str2[i-1] == str1[j-1]:
                memory[i][j] = memory[i-1][j-1] + 1
                common_subsequence += str2[i-1]
            else:
                memory[i][j] = max(memory[i-1][j], memory[i][j-1])

    print(common_subsequence)
    return memory[len(str2)][len(str1)]


def test_find_longest_subsequence(func):
    test_cases = (
        (("ZXVVYZW", "XKYKZPW"), 4),
        (("", ""), 0),
        (("ABCDEFG", ""), 0),
        (("ABCDEFG", "ABCDEFG"), 7)
    )
    for test_case in test_cases:
        args, result = test_case
        actual = func(*args)
        assert actual == result, f"Actual {actual} expected {result}"


if __name__ == '__main__':
    test_find_longest_subsequence(find_longest_subsequence)
