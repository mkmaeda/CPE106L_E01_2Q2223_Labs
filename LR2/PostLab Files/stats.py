def mean(numbers):
    if len(numbers)==0:
        return 0
    return sum(numbers)/len(numbers)

def median(numbers):
    if len(numbers)==0:
        return 0
    numbers.sort()
    n=len(numbers)
    if n%2==0:
        return (numbers[n//2]+numbers[n//2-1])/2
    else:
        return numbers[n//2]
    
def mode(numbers):
    if len(numbers)==0:
        return 0
    count=0
    mode=0
    numbers.sort()
    for i in numbers:
        if numbers.count(i)>count:
            cnt=numbers.count(i)
            mode=i
    return mode

def main():
    numbers=[1,2,3,3,4,5,5,6,5,10]
    print("Mean:",mean(numbers))
    print("Median:",median(numbers))
    print("Mode:",mode(numbers))
main()