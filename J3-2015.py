input = raw_input()
output = []
vowels = ['a','e','i','o','u']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def isVowel(letter):
    for index in range(0,len(vowels)):
        if letter == vowels[index]:
            return True
        else:
            pass
    return False

def getNextC(letter):
    if letter == 'z':
        return 'z'
    for index in range(0,len(cons)):
        if letter == cons[index]:
            return cons[index+1]

def doIt(letter):
    temp = ['','','']
    temp[0] = letter
    temp[1] = 'z'
    temp[2] = getNextC(letter)
    final = ",".join(temp)
    return final

for index, char in enumerate(input):
    if isVowel(input[index]):
        output.append(input[index])
    else:
        output.append(doIt(input[index]))
finalString = ",".join(output)
print(finalString)
