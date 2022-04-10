

def FizzBuzz(start, finish):
    n= finish-start+1
    outlist = []
    for i in range(0,n):
        index = start + i
        if index % 3 == 0 and index % 5 == 0:
            outlist.append("fizzbuzz")
            continue
        elif index % 3 == 0:
            outlist.append("fizz")
            continue
        elif index % 5 == 0:
            outlist.append("buzz")
            continue
        else:
            outlist.append(index)

    return(outlist)    
