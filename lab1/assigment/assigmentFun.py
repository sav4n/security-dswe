n = 256
def enc(m,k):
    global n
    return (m+k)%n

def dec(m,k):
    global n
    return (m-k)%n