n = 26
def enc(m,k):
    return (m+k)%26

def dec(m,k):
    global n
    return (m-k)%n

def xenc(m,k):
    return (m*k)%26

def xdec(m,k):
    global n
    return (m/k)%n
