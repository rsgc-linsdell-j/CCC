input = raw_input()
output = []
vowels = [a,e,i,o,u]
alphabet = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
cons = [b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z]
def isVowel(letter):
    for index in range(0,len(vowels)):
        if letter == vowels[index]:
            return true
        else:
            pass
    return false

def doIt(letter):
    

for index, char in enumerate(input):
    if isVowel(input[index]):
        output[-1] = input[index]
    else:
        doIt(input[index])
print(output)
