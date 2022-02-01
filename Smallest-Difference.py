#time = O(Nlog(N) + Mlog(M))
#space = O(1) constant
#if you are given two arrays, how do you find the smallest difference between the two.

def smallestDifference(arrayOne, arrayTwo):
    # before you sort the arrays, you should ask your interviewer if you it's ok to sort the initial arrays allocated or to create copy's to preserve data. Note this will change your space time complexities.
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    
    # so far we've sorted both arrays and we've stated multiple variables to be called on in the next while loop 
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        #something to be clear on
        # idxOne is calling the index
        # firstNum is the integer
        # We are looping through arrayOne and arrayTwo - if the index of arrayOne and arrayTwo are less than the length of their respective array's, then it will keep looping. Once the firstNum and secondNum have gone through both arrays, the loop will finish.
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        # if the firstNum(the integer (-1)) is less than the secondNum(the integer (15))
        # in this case it is
        # it will call the the answer of 15 --1 = 16 = current
        # and then it will move the index up one in arrayOne
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair



blah = smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17])
print(blah)