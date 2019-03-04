def calculate(pilesArray, numOfpiles):
    
    # initial value 0
    xorResult =0 
    for i in range(numOfpiles): 
        #Firstly Convert each number into binary
        pileBin = bin(pilesArray[i])[2:].zfill(5)
        # Show the player the binary equivalent of each pile...  
        print("-------")
        print("In pile " + str(i+1) + " you have " + str(pileBin)+ "("+ str(pilesArray[i]) + ")" +" sticks.")
         #We calcute XOR
        xorResult^=pilesArray[i]
        print("xor: ", xorResult)
        
    #if first player is winner as xor resuls is zero
    if(xorResult == 0 or numOfpiles%2 ==0):
        return "Player1 is winner :)"
    
    #if player2 is winner, xor result is nonzero
    else:
        return "Player2 is winner"
    
    
#main codes
pilesArray = []
numOfpiles = int(input("How many piles are in the nim-game? "))
for i in range(0, numOfpiles):
    x = input('Enter the number for initially coins: ')
    pilesArray.append(int(x))
print(pilesArray)
print(calculate(pilesArray, numOfpiles))
