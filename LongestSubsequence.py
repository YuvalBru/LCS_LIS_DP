#Let A be a sequence of integers length n
#and B sequence of integers of length m
#and C a sequence of integers either 0 or 1 of length n.
#where n,m >= 1 n != m or n=m.
# I will be identifying the first  problem as the longest common sub sequence problem or in short LCS
#And the second problem as the longest increasing sub sequence problem or in short LIS


A = [3,4,3,1,2,5]
B = [1,2,4,3,3]
C = [1,1,0,1,1,1]

#Question 1 section A
def number_of_lcs(A, B):
    if not A or not B:
        return "One of the lists are empty therefore there is no Longest Common Sub Sequence."

    m, n = len(A), len(B)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]  # Defining the Matrix

    for i in range(1, m + 1): #Filling up the matrix according to the rules I explained above
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    # Backtracking the matrix to find the amount of longest common sub sequences and the common sub sequences them selves.
    def backtrack(i, j, path, seen, indices):
        if matrix[i][j] == 0:
            lcs_tuple = tuple(path[::-1])
            indices_tuple = tuple(indices[::-1])
            if (lcs_tuple, indices_tuple) not in seen:
                seen.add((lcs_tuple, indices_tuple))
                return [path[::-1]]
            return []

        sequences = []

        if i > 0 and j > 0 and A[i - 1] == B[j - 1]:
            sequences.extend(backtrack(i - 1, j - 1, path + [A[i - 1]], seen, indices + [(i - 1, j - 1)]))
        else:
            if i > 0 and matrix[i - 1][j] == matrix[i][j]:
                sequences.extend(backtrack(i - 1, j, path, seen, indices))
            if j > 0 and matrix[i][j - 1] == matrix[i][j]:
                sequences.extend(backtrack(i, j - 1, path, seen, indices))

        return sequences

    seen = set()

    lcs_sequences = backtrack(m, n, [], seen, [])



    return len(lcs_sequences)


print(f"1.A: {number_of_lcs(A,B)}")

#Question 1.B
def all_lcs(A, B, theta=None):
    if not A or not B:
        return "One of the lists are empty therefore there is no Longest Common Sub Sequence."

    m, n = len(A), len(B)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    def backtrack(i, j, path, seen, indices):
        if matrix[i][j] == 0:
            lcs_tuple = tuple(path[::-1])
            indices_tuple = tuple(indices[::-1])
            if (lcs_tuple, indices_tuple) not in seen:
                seen.add((lcs_tuple, indices_tuple))
                return [path[::-1]]
            return []

        sequences = []

        if i > 0 and j > 0 and A[i - 1] == B[j - 1]:
            sequences.extend(backtrack(i - 1, j - 1, path + [A[i - 1]], seen, indices + [(i - 1, j - 1)]))
        else:
            if i > 0 and matrix[i - 1][j] == matrix[i][j]:
                sequences.extend(backtrack(i - 1, j, path, seen, indices))
            if j > 0 and matrix[i][j - 1] == matrix[i][j]:
                sequences.extend(backtrack(i, j - 1, path, seen, indices))

        return sequences

    seen = set()

    lcs_sequences = backtrack(m, n, [], seen, [])

    if theta is not None:
        lcs_sequences = lcs_sequences[:theta]

    for item in lcs_sequences:
        item.sort()


    return lcs_sequences

print(f"1.B: {all_lcs(A, B, theta=4)}")


#Question 1 Section C
def all_unique_lcs(A, B, theta=None):
    if not A or not B:
        return "One of the lists are empty therefore there is no Longest Common Sub Sequence."

    m, n = len(A), len(B)

    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    def backtrack(i, j, path, seen, indices):
        if matrix[i][j] == 0:
            lcs_tuple = tuple(path[::-1])
            indices_tuple = tuple(indices[::-1])
            if (lcs_tuple, indices_tuple) not in seen:
                seen.add((lcs_tuple, indices_tuple))
                return [path[::-1]]
            return []

        sequences = []

        if i > 0 and j > 0 and A[i - 1] == B[j - 1]:
            sequences.extend(backtrack(i - 1, j - 1, path + [A[i - 1]], seen, indices + [(i - 1, j - 1)]))
        else:
            if i > 0 and matrix[i - 1][j] == matrix[i][j]:
                sequences.extend(backtrack(i - 1, j, path, seen, indices))
            if j > 0 and matrix[i][j - 1] == matrix[i][j]:
                sequences.extend(backtrack(i, j - 1, path, seen, indices))

        return sequences

    seen = set()

    lcs_sequences = backtrack(m, n, [], seen, [])

    lcs_sequences = list(set(tuple(seq) for seq in lcs_sequences))
    lcs_sequences = [list(seq) for seq in lcs_sequences]

    for item in lcs_sequences:
        item.sort()

    if theta is not None:
        lcs_sequences = lcs_sequences[:theta]


    return lcs_sequences

print(f"1.C: {all_unique_lcs(A, B, theta=None)}")



#Question 2
#We solve this problem using a list which tracks and updates the amount of numbers which comply with being part of a sub sequence of the sequence A
# with correspondence to the indices of C.


# Question 2 Section A
def length_of_lis(A,C):
    if (1 in C) == False:
        return "There are no ones in C or A is an empty list therefore there is no Longest Increasing Sequence."

    n = len(A)
    mat = [0] * n
    max_length = 0

    for i in range(n):
        if C[i] == 1:
            mat[i] = 1
            for j in range(i):
                if A[j] <A[i] and C[j] == 1:
                    mat[i] = max(mat[i], mat[j] + 1)
            max_length = max(max_length, mat[i])

    return max_length

print("2.A:", length_of_lis(A,C))

# Question 2 Section B
def number_of_lis(A, C):
    if (1 in C) == False:
        return "There are no ones in C or A is an empty list therefore there is no Longest Increasing Sequence."

    n = len(A)
    mat = [0] * n
    count = [1] * n
    max_length = 0

    for i in range(n):
        if C[i] == 1:
            mat[i] = 1
            for j in range(i):
                if A[j] < A[i] and C[j] == 1:
                    if mat[j] + 1 > mat[i]:
                        mat[i] = mat[j] + 1
                        count[i] = count[j]
                    elif mat[j] + 1 == mat[i]:
                        count[i] += count[j]
            max_length = max(max_length,mat[i])

    return sum(count[i] for i in range(n) if mat[i] == max_length)



print("2.B:", number_of_lis(A, C))


# Question 2 Section C
def all_lis(A, C,theta=None):
    if ((1 in C) == False) or not A:
        return "There are no ones in C or A is an empty list therefore there is no Longest Increasing Sequence."

    n = len(A)
    mat = [0] * n
    max_length = 0
    paths = {}

    for i in range(n):
        if C[i] == 1:
            mat[i] = 1
            paths[i] = [[A[i]]]
            for j in range(i):
                if A[j] < A[i] and C[j] ==1:
                    if mat[j] + 1 >mat[i]:
                        mat[i] = mat[j] + 1
                        paths[i] = [seq + [A[i]] for seq in paths[j]]
                    elif mat[j] + 1 == mat[i]:
                        paths[i].extend(seq + [A[i]] for seq in paths[j])
            max_length = max(max_length, mat[i])

    lis_sequences = []
    for i in range(n):
        if mat[i] == max_length:
            lis_sequences.extend(paths[i])

    for seq in lis_sequences:
        seq.sort()

    if theta is not None:
        lis_sequences = lis_sequences[:theta]

    return lis_sequences, len(lis_sequences)

print("2.c:", all_lis(A, C,theta=4))

# Question 2 Section D
def all_unique_lis(A, C, theta=None):
    if ((1 in C) == False) or not A:
        return "There are no ones in C or A is an empty list therefore there is no Longest Increasing Sequence."



    n = len(A)
    mat = [0] * n
    max_length = 0
    paths = {}

    for i in range(n):
        if C[i] == 1:
            mat[i] = 1
            paths[i] = [[A[i]]]
            for j in range(i):
                if A[j] < A[i] and C[j] == 1:
                    if mat[j] + 1 > mat[i]:
                        mat[i] = mat[j] + 1
                        paths[i] = [seq + [A[i]] for seq in paths[j]]
                    elif mat[j] + 1 == mat[i]:
                        paths[i].extend(seq + [A[i]] for seq in paths[j])
            max_length = max(max_length, mat[i])

    lis_sequences = []
    for i in range(n):
        if mat[i] == max_length:
            lis_sequences.extend(paths[i])

    for seq in lis_sequences:
        seq.sort()

    unique_sequences = list(set(tuple(seq) for seq in lis_sequences))
    unique_sequences = [list(seq) for seq in unique_sequences]

    if theta is not None:
        unique_sequences = unique_sequences[:theta]

    return unique_sequences, len(unique_sequences)

print("2.d:", all_unique_lis(A, C, theta=None))