#Part B: Statistics

count = 0
total = 0
target = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

marks = int(input("Enter Mark: "))
maximum = int()
minimum = marks

while marks >= 0:
    if marks <= 100 and marks >= 0:
        count = count + 1
        total = total + marks
        if maximum <= marks:
            maximum = marks
        elif minimum >= marks:
            minimum = marks
 
    if marks >= 40:
        target = target + 1

    if marks >= 0 and marks <= 29:
        count1 = count1 + 1
    elif marks >= 30 and marks <= 39:
        count2 = count2 + 1
    elif marks >= 40 and marks <= 69:
        count3 = count3 + 1
    elif marks >= 70 and marks <= 100:
        count4 = count4 + 1
    marks = int(input("Enter Mark: "))

print("\n0-29     ",end="")
for i in range(0,count1):
    print("*",end="")
print("\r")

print("30-39    ",end="")
for j in range(0,count2):
    print("*",end="")
print("\r")

print("40-69    ",end="")
for k in range(0,count3):
    print("*",end="")
print("\r")

print("70-100   ",end="")
for m in range(0,count4):
    print("*",end="")
print("\n")

average = total / count
print(count,"students in total.")
print("Average Mark: ",average)
print("Number of Students with a Pass Mark: ",target)
print("Highest Mark: ",maximum)
print("Lowest Mark: ",minimum)
