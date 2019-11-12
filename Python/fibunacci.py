import time
def fibr(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-2) + fibr(n-1)

def fibarr(n):
    count = 2
    out = dict()
    out[0] = 0
    out[1] = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        while count<=n:
            out[count] = out[count-2]+ out[count-1]
            count += 1
        return out[n]

n= 5
start = time.time()
f=fibr(n)
end = time.time()
ctime = end-start
print("Fib is: %f and  takes %f seconds to compute" % (f, ctime))
