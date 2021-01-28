list1 = [1,7,3,20,42,12,2,4,17,23]

def numcheck(numlist):
    total = 0

    for i in numlist:
        total += i

    avg = total / len(numlist)

    return(avg)

print(numcheck(list1))