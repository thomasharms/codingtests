# count the amount of messages given a message string S and the max amount of letters in
# a single message K: return the number of messages need to be sent
def solution(S, K):
    msg_count = 0
    words = S.split()
    # could also be while words: since empty list equals false
    while len(words) > 0:
        msg_char_count = 0
        msg_text=""
        if len(words[0]) > K:
            return -1

        while msg_char_count < K and len(words)>0:
            if len(words)>0:
                if msg_char_count == 0 and (msg_char_count+len(words[0]))<=K:
                    word = words.pop(0)
                elif (msg_char_count+len(words[0])+1)<=K:
                    word = " "+words.pop(0)
                msg_text += word
                msg_char_count += len(word)
        msg_count += 1
    
    if msg_count>0 & msg_count <= 500:
        return msg_count
    else:
        return -1



test = "east an element in the list is wrong, one might want to get notified."

r = 10
print(solution(test, r))
print(len(test))

