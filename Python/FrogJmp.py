def solution(X, Y, D):
    # Find distance 
    distance = Y - X
    # Calculate Number of jumps 
    jumps = distance // D
    #  if distance is not reached add jump to go past distance
    if distance % D != 0:
        jumps += 1
    return jumps
