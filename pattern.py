# this program creates an increasing then decreasing star pattern within the for loop range
COUNTER = 0 
STAR = "*"

for i in range(0, 10):
    COUNTER += 1 # keeps track each iteration of the for loop
    if COUNTER < 6:
        print(STAR)
        STAR = STAR+"*"
    elif COUNTER > 6:
        index = 10-i
        print(STAR[0:index]) # as index gets smaller, less stars are printed to achieve a decreasing pattern