#time = O(Nlog(N) + Mlog(M))
#space = O(1) constant
#if you are given two arrays, how do you find the smallest difference between the two.

def smallestDifference(arrayOne, arrayTwo):
    # before you sort the arrays, you should ask your interviewer if you it's ok to sort the initial arrays allocated or to create copy's to preserve data. **Note this will change your space/time complexities.
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
        # firstNum is calling the integer at a certain index
        # We are looping through arrayOne and arrayTwo - if the index of arrayOne and arrayTwo are less than the length of their respective array's, then it will keep looping. 
        # Once the firstNum and secondNum have gone through both arrays, the loop will finish.
        #while it's looping...
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        # if the firstNum (-1) is less than the secondNum (15)
        # This is correct, so in this iterable, it will move on to the next number in the loop and forget elif and else.
        # this will call the answer of 15 --1 = 16 = current
        # and then it will move the index up one in arrayOne
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        # if the secondNum is less than the firstNum 
        # this will call the answer the new current number = current
        # and then it will move the index up one in arrayTwo
        else:
            return [firstNum, secondNum]
        # this will print the answer it has found our answer and doesn't need to keep looping. 
        # this is important because we have sorted our list. If we didn't sort our list in this instance, this condition would be a viable option.
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
        # this is still within the loop and is a secondary condition
        # if we have found that the smallest is greater than the current, which will always be true as this inf is infinity is always the largest. 
        # the smallest will now the the current number
    return smallestPair
    # we have looped through all we have needed to to get our answer. 
    # you'll noticed that the current number was always updated to get the new best answer.
    # the second condition(line42) makes sure that we have both integers "answers" logged to then call the final answer(line 48)
    
blah = smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17])
print(blah)
