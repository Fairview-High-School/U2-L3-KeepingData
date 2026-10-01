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

#here is an example predicate block.  You may want to make more to use in your filter below
def isInteger(number):
  return number == int(number)
  
    
#MAIN SCRIPT
#setup()
loadFile("word-puzzle-list.txt")
print (str(len(wordList)) + " total words in list.")
#len(wordList) returns the length of the list
#list[0] returns the first letter in list
#list[2] returns the third letter in list
#and: means both left and right conditions must be true for the entire expression to be true
#or: means only one or the other (or both) conditions must be true for the entire expression to be true


#EXAMPLE OF FILTERING WORD LIST
print("FILTERING WORD LIST")
result = filter(lambda x: len(x) == 6 and x[0] == "r" and x[2] == "d" , wordList)  # 6 letter word and 1st letter is "r" and 3d letter is "d"
#to filter the list differently, change the condition.  (The condition above is len(x) == 6 and x[0] == "r" and x[2] == "d"
print(result)
print (str(len(result)) + " results in filtered word list.")

print("")
print("")

#EXAMPLE OF FILTERING NUMBER LIST
print("FILTERING NUMBER LIST")
result2 = filter(lambda x: isInteger(x) and x > 0, numbersList) # integers that are greater than 0
print(result2)
print (str(len(result2)) + " results in filtered number list.")



#Here were the initial examples in case you modified them:

#result = filter(lambda x: len(x) == 6 and x[0] == "r" and x[2] == "d" , wordList)  # 6 letter word and 1st letter is "r" and 3d letter is "d"

#result2 = filter(lambda x: isInteger(x) and x > 0, numbersList) # integers that are greater than 0