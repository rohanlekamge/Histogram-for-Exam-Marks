#Part D: Vertical Histogram (Extension)

count = 0   #this count is used to print the total number of students who had written the exam.
total = 0   #this is used to find the average marks of these students
target = 0  #i have used this count to print number of students who got marks above 40
histogram = 0
count1 = 0  #To count the students who take marks in between 0 and 29
count2 = 0  #To count the students who take marks in between 30 and 39
count3 = 0  #To count the students who take marks in between 40 and 69
count4 = 0  #To count the students who take marks in between 70 and 100
while True:
    try:
        marks = int(input("Enter Mark: "))
    except ValueError: #this checks is there a runtime Error called "ValueError"
        print("You Have Entered a Non-Numerical Character. Please Enter a Valid Character\n")
        continue       #goes straight to the first line
    else:
        #you have entered a numerical character
        #you're ready to exit the loop.
        break          #this will end the loop and break from here
    
maximum = int()        #This is also equals to marks = 0
minimum = marks
while marks >= 0:      #i have repeated following loop using marks >= 0
    if marks <= 100 and marks >= 0:
        if marks >= 40:
            target = target + 1
        count = count + 1
        total = total + marks
        if maximum <= marks:
            maximum = marks
        elif minimum >= marks:
            minimum = marks   
    elif marks > 100:
        print("Entered Number is Not Valid. Please Try Again\n")
 

    if marks >= 0 and marks <= 29:
        count1 = count1 + 1
    elif marks >= 30 and marks <= 39:
        count2 = count2 + 1
    elif marks >= 40 and marks <= 69:
        count3 = count3 + 1
    elif marks >= 70 and marks <= 100:
        count4 = count4 + 1


    while True:  #this is repeat of same loop in the above
        try:
            marks = int(input("Enter Mark: "))
        except ValueError:
            print("You Have Entered a Non-Numerical Character. Please Enter a Valid Character\n")
            continue
        else:
            break
        
print("\n: 0-29 : 30-39 : 40-69 : 70-100 :")

list = [count1, count2, count3, count4] #i have used a List called "list" to include counts in each mark catagory

while max(list) >= histogram:           #i have used max(list) to find the maximum in that list
    if count1 > histogram:              #i have initially diclared histogram = 0    
        print("   *   ", end="")
    elif count1 <= histogram:
        print("       ", end="")
        
    if count2 > histogram:
        print("    *    ", end="")
    elif count2 <= histogram:
        print("         ", end="")
    
    if count3 > histogram:
        print("   *    ", end="")
    elif count3 <= histogram:
        print("        ", end="")
        
    if count4 > histogram:
        print("   *    ", end="")
    elif count4 <= histogram:
        print("        ", end="")

    histogram = histogram + 1
    print("\n")

average = total / count             #Calculating the Average
print(count,"students in total.")   #Printing the total number of students who wrote the exam
print("Average Mark: ",average)     #print Average marks obtain by students in the exam
print("Number of Students with a Pass Mark: ",target) #Number of students who got marks above 40
print("Highest Mark: ",maximum)     #Highest mark obtained in the exam
print("Lowest Mark: ",minimum)      #Lowest mark obtained in the exam
 
