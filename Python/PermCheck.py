def solution(A):
    # find how many num are in list
    length = len(A)
    #keep track of already checked numbers
    check = set()
    #check each number in list
    for number in A:
        #return 0 if num is outside range or repeated
        if number < 1 or number > length or number in check:
            return 0
        #keep track of num
        check.add(number)

    #return 1 if all num passed checks
    return 1
