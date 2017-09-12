i = 0
t = 10
numbers = []

for i in range(0,t,2):
    print("At the top i is %d" % i)
    numbers.append(i)


    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % (i+2))


print("The numbers: ")

for num in numbers:
    print num
# at the top i is 0
# numbers now: [0]
# at the bottom i is 1
