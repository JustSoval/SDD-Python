list1 = [1,7,3,20,42,12,2,4,17,23]

def numcheck(numlist):
    num = 0
    for i in numlist:
        if i > num:
            num = i

    return(num)

print(numcheck(list1))