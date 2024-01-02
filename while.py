#this program calculates the mean average of user integer input
numtotal = []

while True:
    num_input = int(input("please enter a number: "))
    numtotal.append(num_input)
    if num_input == -1:
        break

numtotal.remove(-1)

numaverage = sum(numtotal)/len(numtotal)

print(numaverage)