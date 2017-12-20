#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L


btCounter = 0
fcCounter = 0


#This function calculates indices for a given array
def getPos(ruler):
    result = list()
    for i in range(len(ruler)):
        if ruler[i] == 1:
            result.append(i)
    return result

#Your backtracking function implementation

#This function checks whether constraints are satisfied for a given scale configuration
def isValid(L, M, ruler):
    global fcCounter
    fcCounter += 1
    global btCounter
    btCounter += 1
    dist = list()

    for i in range(0, len(ruler)-1):
        if ruler[i] == 1:
            for j in range(i+1,len(ruler)):
                if ruler[j] == 1:
                    dist.append(j-i)

    #Check if distances are same
    for i in range(0, len(dist)-1):
        for j in range(i+1, len(dist)):
            if dist[i] == dist[j]:
                return False

    return True



def BT(L, M):

    #init ruler as an array
    ruler = list()
    for i in range(L+1):
        ruler.append(0)

    tempM = M
    ruler1 = ruler[:]

    #place one marker at L to mark the length of the marker
    ruler1[L] = 1
    M = M - 1
    res = []

    #find a solution for the given config
    resultRec = BTHelper(L, M, res, ruler1, 0)

    #if solution does not exist, return -1,[]
    if (resultRec[0] == False):
        return -1, []

    #if solution exists, store that in some temp var (prevRec), and calculate for optimal length
    prevRec = resultRec
    temp = list()
    temp.append(resultRec)
    L -= 1

    #call BTHelper ecursively on L-1 for calculation of optimal length
    while L >= tempM:
        M = tempM
        ruler1 = ruler[0:L+1]
        ruler1[L] = 1
        M = M - 1
        res = []
        resultRec = BTHelper(L, M, res, ruler1, 0)
        if resultRec[0] == True:
            prevRec = resultRec
        else:
            pos = getPos(prevRec[1])
            return L+1, pos
        L -= 1

    pos = getPos(prevRec[1])
    return L+1, pos


'''
This function calculates a solution for ruler of length L and M markers and appends to res.
It checks if for a given config the constraints are consistent or not, if not consistent, then
backtrack, else go on iterating over the remaining ruler until number of markers are not 0
'''
def BTHelper(L, M, res, ruler, curr):
    ruler1 = ruler[:]
    ruler1[curr] = 1

    if isValid(L, M, ruler1):
        M -= 1
        if M > 0:
            for i in range(curr+1, L):

                val, ruler2 = BTHelper(L, M, res, ruler1, i)
                if(val == True):
                    return True, ruler2
                else:
                    continue
            if res:
                return True, res
            else:
                return False, []

        else:
            res.append(ruler1)
            return True, ruler1

    else:
        return False,[]




#Your backtracking+Forward checking function implementation

'''
This function does forward checking for a given ruler configuration. We maintain a list called
domain which stores the values of all the lengths which have been calculated for previous configs,
and another list called dist which stores the length from a marker to all the other marker for that
instance. If the union of dist list and the domain list is the same, then it means that there is an
inconsistency, hence we return False, domain in that case, else, we return an updated domain (domain+dist)
and True
'''
def constraintConsistent(domain, ruler, curr):

    dist = list()
    for i in range(len(ruler)):
        if ruler[i] == 1:
            if i == curr:
                continue
            else:
                dist.append(abs(curr-i))

    dist1 = list(set(dist))

    #Check if distances in domain and dist are the same
    for i in range(len(dist1)):
        for j in range(len(domain)):
            if dist1[i] == domain[j]:
                return False, domain
    #if dist and domain are not the same, then update the domain by appending dist to it
    for i in dist1:
        domain.append(i)
    return True, domain



'''
This function performs the forward check once, to see if a solution exists or not, if it exists, then
we call recursively FCHelper on L-1 to get the optimal solution
'''
def FC(L, M):
    ruler = list()
    #contains all possible lengths
    domain = list()
    for i in range(L+1):
        ruler.append(0)
    domain.append(0)
    tempM = M
    ruler1 = ruler[:]
    domain1 = domain[:]
    ruler1[L] = 1
    M = M - 1
    res = []
    resultRec = FCHelper(L, M, res, ruler1, 0, domain1)
    if (resultRec[0] == False):
        return -1, []
    prevRec = resultRec
    temp = list()
    temp.append(resultRec)
    L -= 1

    #continue calling recursively until L >=tempM
    while L >= tempM:
        M = tempM
        ruler1 = ruler[0:L+1]
        domain1 = domain[:]
        ruler1[L] = 1
        M = M - 1
        res = []
        resultRec = FCHelper(L, M, res, ruler1, 0, domain1)
        #if there exists a solution for smaller len, store it in prevRec
        if resultRec[0] == True:
            prevRec = resultRec
        else:
            pos = getPos(prevRec[1])
            return L+1, pos
        L -= 1

    pos = getPos(prevRec[1])

    return L+1, pos


'''
This function calculates a solution for ruler of length L and M markers and appends to res.
It first checks one step ahead to see if consistent solution is possible or not (constraintConsistent),
if constraintConsistent returns True, then we can continue with normal process of selecting one value
from the domain. Else, we return False,[], thereby reducing the number of checks performed
'''
def FCHelper(L, M, res, ruler, curr, domain):
    ruler1 = ruler[:]
    domain1 = domain[:]
    tempRuler = ruler1[:]
    tempRuler[curr] = 1
    flag, domain1 = constraintConsistent(domain1, ruler1, curr)
    if(flag == True):
        ruler1[curr] = 1
        if isValid(L, M, ruler1):
            M -= 1
            if M > 0:
                for i in range(curr+1, L):
                    val, ruler2 = FCHelper(L, M, res, ruler1, i, domain1)
                    if(val == True):
                        return True, ruler2
                    else:
                        continue
                if res:
                    return True, res
                else:
                    return False, []
            else:
                res.append(ruler1)
                return True, ruler1
        else:
            return False, []
    else:
        return False,[]



#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]
