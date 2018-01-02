def LongestCommonSubsequence(A, B):
    """Find longest common subsequence of iterables A and B."""
    A = list(A)
    B = list(B)

    # Fill dictionary lcsLen[i,j] with length of LCS of A[:i] and B[:j]
    lcsLen = {} #dev
    directions = {}
    fillDictionaryWithOperations(A, B, directions, lcsLen)

    # Produce actual sequence by backtracking through pairs (i,j),
    # using computed lcsLen values to guide backtracking
    i = len(A)
    j = len(B)
    operations = []
    deriveLCSFromDictionaryOperations(A, B, directions, i, j, operations)
    operations.reverse()
    # print operations
    return operations


def deriveLCSFromDictionaryOperations(A, B, directions, i, j, operations):
    while True:
        if i <= 0 and j <= 0:
            break

        if directions[i, j] == 'D':
            # print 'LCS char', A[i-1]
            operations.append('LCS ' + A[i - 1])
            i -= 1
            j -= 1
        elif directions[i, j] == 'U':
            # print 'add', B[j-1]
            operations.append('ADD ' + B[j - 1])
            j -= 1
        elif directions[i, j] == 'L':
            # print 'remove', A[i-1]
            operations.append('REM ' + A[i - 1])
            i -= 1
        elif directions[i, j] == 'E':
            if i == 0:
                # print 'add', B[j-1]
                operations.append('ADD ' + B[j - 1])
                j -= 1
            elif j == 0:
                # print 'remove', A[j-1]
                operations.append('REM ' + A[j - 1])
                i -= 1


def fillDictionaryWithOperations(A, B, directions, lcsLen):
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i == 0 or j == 0:
                lcsLen[i, j] = 0
                directions[i, j] = "E" #empty
            elif A[i - 1] == B[j - 1]:
                lcsLen[i, j] = lcsLen[i - 1, j - 1] + 1
                directions[i, j] = "D" #diagonal
            else:
                if lcsLen[i - 1, j] >= lcsLen[i, j - 1]:
                    lcsLen[i, j] = lcsLen[i - 1, j]
                    directions[i, j] = "L" #left
                else:
                    lcsLen[i, j] = lcsLen[i, j - 1]
                    directions[i, j] = "U" #up


if __name__ == "__main__":
    print LongestCommonSubsequence('BDCABA', 'ABCBDAB')
    # LongestCommonSubsequence('ABCABBA', 'CBABAC')
