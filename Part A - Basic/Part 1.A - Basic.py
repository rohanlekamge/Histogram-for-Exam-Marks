#Part A: Basic Program 

count = 0       #this count is used to print the total number of students who had written the exam.
count1 = 0      #To count the students who take marks in between 0 and 29
count2 = 0      #To count the students who take marks in between 30 and 39
count3 = 0      #To count the students who take marks in between 40 and 69
count4 = 0      #To count the students who take marks in between 70 and 100
marks = int()   #This is also equals to marks = 0
while marks >= 0: #i have repeated following loop using marks >= 0
    marks = int(input("Enter Mark: "))
    
    if marks >= 0 and marks <= 29:
        count1 = count1 + 1
    elif marks >= 30 and marks <= 39:
        count2 = count2 + 1
    elif marks >= 40 and marks <= 69:
        count3 = count3 + 1
    elif marks >= 70 and marks <= 100:
        count4 = count4 + 1
    
    
    if marks <= 100 and marks >= 0:
        count = count + 1
    

print("\n0-29     ",end="")
for i in range(0,count1):
    print("*",end="") #by using end='' . i have printed "*" in same line.
print("\r")         #Without the use of end='' . it will print "*" vertically.

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

print(count,"students in total.")
