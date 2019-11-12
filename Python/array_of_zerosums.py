def solution(N):
    out = list()
    if N % 2 == 1:
        out.append(0)
        N = N - 1
    i = 1
    while i <= (N/2):
        out.append(i)
        out.append(i*-1)
        i += 1
    return out
    
print(solution(7))
    

    