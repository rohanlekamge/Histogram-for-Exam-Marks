#Part B: Statistics

count = 0   #this count is used to print the total number of students who had written the exam.
total = 0   #this is used to find the average marks of these students
target = 0  #i have used this count to print number of students who got marks above 40
count1 = 0  #To count the students who take marks in between 0 and 29
count2 = 0  #To count the students who take marks in between 30 and 39
count3 = 0  #To count the students who take marks in between 40 and 69
count4 = 0  #To count the students who take marks in between 70 and 100

marks = int(input("Enter Mark: "))
maximum = int()     #This is also equals to marks = 0
minimum = marks

while marks >= 0:   #i have repeated following loop using marks >= 0
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
    print("*",end="")   #by using end='' . i have printed "*" in same line.
print("\r")             #Without the use of end='' . it will print "*" vertically.

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

average = total / count             #Calculating the Average
print(count,"students in total.")   #Printing the total number of students who wrote the exam
print("Average Mark: ",average)     #Average marks obtain by students in the exam
print("Number of Students with a Pass Mark: ",target) #Number of students who got marks above 40
print("Highest Mark: ",maximum)     #Highest mark obtained in the exam
print("Lowest Mark: ",minimum)      #Lowest mark obtained in the exam
