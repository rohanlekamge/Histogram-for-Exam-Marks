#Part D: Vertical Histogram (Extension)

count = 0
total = 0
target = 0
histogram = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
while True:
    try:
        marks = int(input("Enter Mark: "))
    except ValueError:
        print("You Have Entered a Non-Numerical Character. Please Enter a Valid Character\n")
        continue
    else:
        #you have entered a numerical character
        #you're ready to exit the loop.
        break
    
maximum = int()
minimum = marks
while marks >= 0:
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


    while True:
        try:
            marks = int(input("Enter Mark: "))
        except ValueError:
            print("You Have Entered a Non-Numerical Character. Please Enter a Valid Character\n")
            continue
        else:
            break
        
print("\n: 0-29 : 30-39 : 40-69 : 70-100 :")

list = [count1, count2, count3, count4]

while max(list) >= histogram:
    if count1 > histogram:
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

average = total / count
print(count,"students in total.")
print("Average Mark: ",average)
print("Number of Students with a Pass Mark: ",target)
print("Highest Mark: ",maximum)
print("Lowest Mark: ",minimum)
