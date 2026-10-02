wordList = [] #word list will be filled up using the loadFile function below.
numbersList = [189,29,55.7,-4.9,8901,-36.76,74.8, 33, -9, 60.3221, 19, -222, 41,
37, -12, 9.6, -0.33, 2, 21]

def saveFile(filename):
    file = open(filename,"w")
    for word in wordList:
        file.write(word)
    file.close()

def loadFile(filename):
    file = open(filename,"r")
    for line in file:
        word = line.strip("\n")
        wordList.append(word)
    file.close()


#BOOLEAN FUNCTIONS
#len(wordList) returns the length of the list
#list[0] returns the first letter in list
#list[2] returns the third letter in list
#and: means both left and right conditions must be true for the entire expression to be true
#or: means only one or the other (or both) conditions must be true for the entire expression to be true
#example boolean function.  You may want to make more to use in your filter below

def isInteger(number):
  return number == int(number)

# boolean function for working with words  
# You can replace the return condition with whatever you need.
# example:  return len(x) == 6 and x[0] == "r" and x[2] == "d"
def keepWordCondition(x):
    return len(x) == 6 and x[0] == "r" and x[2] == "d"

# boolean function for working with numbers 
# You can replace the return condition with whatever you need.
# example:  return isInteger(x) and x > 0 
def keepNumberCondition(x):
    return isInteger(x) and x > 0 

#MAIN SCRIPT

loadFile("word-puzzle-list.txt")
print (len(wordList) , " total words in list.")

#FILTERING WORD LIST
print("FILTERING WORD LIST")
result = filter(lambda x: keepWordCondition(x), wordList) 
result = list(result) #convert result of filter to a list.
#to filter the list differently, change the condition in keepWordCondition(x) above.
print(result)
print (len(result) , " results in filtered word list.")

print("")

#FILTERING NUMBER LIST
print("FILTERING NUMBER LIST")
result2 = filter(lambda x: keepNumberCondition(x), numbersList)
result2 = list(result2) #convert result of filter to a list.
print(result2)
print (str(len(result2)) + " results in filtered number list.")