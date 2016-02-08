input = raw_input()

happy = 0
sad = 0

for index, char in enumerate(input):
    if char == ':' and input[index+1] == '-':
        if input[index+2] == ')':
            happy += 1
        elif input[index+2] == '(':
            sad += 1
    pass

if happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
elif happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
