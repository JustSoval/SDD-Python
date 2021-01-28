list1 = ["straw", "car", "stand", "cold", "table", "stone", "plate"]

def scheck(wordlist):
    returnlist = []
    for i in wordlist:
        if i[0] == "s":
            returnlist.append(i)
    return(returnlist)

print(scheck(list1))