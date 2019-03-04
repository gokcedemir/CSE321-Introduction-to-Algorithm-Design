#program to find out if string follows a given pattern or not
def check(pattern, text, myMap):
    ptt = len(pattern)
    txt= len(text)  #length of given string 
    #If both string and pattern reach their end 
    if(ptt == 0 and txt== 0):
        return True
    # If either string or pattern reach their end 
    if(ptt== 0 or txt== 0):
        return False
    # if character is seen before
    if(pattern[0] in myMap):
        tmp = myMap[pattern[0]]
        if(len(tmp)>txt or text[:len(tmp)] != tmp):
            return False
        else:
            #recursive call
            return check(pattern[1:], text[len(tmp):], myMap)
    else:
        for i in range(1,txt):
            myMap[pattern[0]] = text[:i]
            if check(pattern[1:], text[i:], myMap):
                return True
            # if not, remove from map 
            del myMap[pattern[0]]

    return False
#driver codes

myMap={}
print("Pattern: abcdab  Text: tobeornottobet --> " + str(check('abcdab', 'tobeornottobet', myMap)))
print("Pattern: abcdab  Text: tobeornottobe --> " + str(check('abcdab', 'tobeornottobe', myMap)))