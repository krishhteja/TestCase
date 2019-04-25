import sys

def readInp():
    readVal = input("Enter String : ")
    compute(readVal)

def compute(readVal):
    wordToPrint = ''
    count = 0
    for eachLetter in readVal:
        try:
            if eachLetter.isalpha():
                if count % 2 == 0:
                    wordToPrint += eachLetter.upper()
                else:
                    wordToPrint += eachLetter.lower()
                count = count + 1
            elif eachLetter.isdigit():
                if int(eachLetter) % 2 == 0:
                    if count % 2 == 0:
                        wordToPrint += "E"
                    else:
                        wordToPrint += "e"
                else:
                    if count % 2 == 0:
                        wordToPrint += "O"
                    else:
                        wordToPrint += "o"
                count = count + 1
            else:
                wordToPrint += eachLetter
        except:
            print("Failed to finish the task.")
    print("Output is - " + wordToPrint)
    return wordToPrint

if __name__ == '__main__':
    readInp()
