fibdict = {}
def  fibosum(nth,rdict=0):
    '''
    Builds the Fibonacci Sum and Dictionary.
    In effect it starts by looking to see if the two prior numbers
    in the fibonacci sequence already exist in our dictionary
    and if they do not it recurses until we find our nth=0 and nth=1
    then it whips back out through the recurrsion adding everything up.
    Optional: Set rdict=1 to return the fibo dictionary as well
    '''
    if nth == 0:
        fibdict[nth] = 0 # if nth == 0 then add idx=0 and ans=0 to dict
        return fibdict[nth]
    elif nth == 1:
        fibdict[nth] = 1 # if nth == 1 then add idx=1 and ans=1 to dict
        return fibdict[nth]
    else: # happens when nth not in [0,1]
        a = 0 # init first value
        b = 0 # init second value
        if nth-2 in fibdict.keys(): # if we already have value from nth-2 then that's our left number
            a += fibdict[nth-2]
        else: # otherwise we're pushing this missing dict value through into the fibo function
            a += fibosum(nth-2) 
            fibdict[nth-2] = a
        if nth-1 in fibdict.keys(): # if we already have value from nth-1 then that's our right number
            b += fibdict[nth-1]
        else: # otherwise we're pushing this missing dict value through into the fibo function
            b += fibosum(nth-1)
            fibdict[nth-1] = b
    ans = a + b
    if rdict == 1:
        return ans, fibdict
    return ans