
def median(x):
    x.sort()
    n=len(x)
    mid=int(n/2);
    if(n%2==1):
        return x[mid]
    else:
        return (x[mid]+x[mid+1])/2

def mode(x):
    res = max(set(x), key = x.count)
    return res

def mean(x):
    n=len(x)
    sumofa=0
    for i in x:
        sumofa=sumofa+i;
    return sumofa/n


from stats import x 

print(median(x))
print(mode(x))
print(mean(x))