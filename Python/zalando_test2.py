def solution(S):
    
    found = True
    pos_pattern = ['AB', 'BA', 'CD', 'DC']
    while found:
        found = False
        i = 0
        last = -1
        for i in range(len(S)-1):
            
            if S[i:i+2] in pos_pattern:
                found = True
                last = i
            print(last)
        if last==0 and found:
            S = S[2:]
        elif found:
            S = S[0:last]+S[last+2:]
        print(S)
    return S


a = "CABABD"
print(solution(a))
