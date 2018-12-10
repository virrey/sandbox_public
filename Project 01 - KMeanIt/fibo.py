fibdict = {}
def  fibosum(n,rdict=0):
    '''
    set rdict=1 to return the fibo dictionary as well
    '''
    if n == 0:
        fibdict[n] = 0
        return fibdict[n]
    elif n == 1:
        fibdict[n] = 1
        return fibdict[n]
    else:
        nleft = 0
        nright = 0
        if n-2 in fibdict.keys():
            nleft += fibdict[n-2]
        else:
            nleft += fibosum(n-2)
            fibdict[n-2] = nleft
        if n-1 in fibdict.keys():
            nright += fibdict[n-1]
        else:
            nright += fibosum(n-1)
            fibdict[n-1] = nright
    ans = nleft + nright
    if rdict == 1:
        return ans, fibdict
    return ans