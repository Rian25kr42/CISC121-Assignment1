def solution(A):
    # keep track of how many times num appears
    count = {}
    #count each num in list
    for number in A:
        count[number] = count.get(number,0) +1
    #find number with odd count
    for number in count:
        if count[number] % 2 != 0:
            return number
