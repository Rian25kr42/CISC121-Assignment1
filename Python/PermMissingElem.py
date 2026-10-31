def solution(A):
    # find largest expected number
    largest = len(A) + 1
    #calc expected sum
    expected_sum = largest * (largest + 1) // 2
    #add number to list
    tot = 0
    for number in A:
        tot += number
    #subtract to find missing num
    return expected_sum - tot
