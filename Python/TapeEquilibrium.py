def solution(A):
    # find sum of list
    tot = sum(A)
    left_sum = 0
    smallest = None

    # try each split
    for i in range(1, len(A)):
        # move next num to left side
        left_sum += A[i -1]
        right_sum = tot - left_sum

        # find difference between both sums
        diff = abs(left_sum - right_sum)
        # update smallest diff found
        if smallest is None or diff < smallest:
            smallest = diff


    return smallest
