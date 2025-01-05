#Check The Number is even or odd

num = int(input("Enter Any Number"))

if num%2==0:
    print("The Number is Even")

else:
    print("The Number is Odd")

#Check the Number is Positive Negative or zero

check = int(input("Enter Any Number"))

if check>=1:
    print("The Number is Positive Number")

elif check==0:
    print("The Number is Zero")

elif check<0:
    print("The Number is negative")

    #Check User Can Vote or Not

age = int(input("Enter Your Age"))

if age>=18:
    print("You Can Vote Bro")

else:
    print("Sorry, You Can't Vote")

    #Check The Triangle is Equlateral,Isosceles,Scalane

side1 = int(input("Enter Side 1"))
side2 = int(input("Enter Side 2"))
side3 = int(input("Enter Side 3"))

if side1 == side2 and side2 == side3:
    print("Equalateral Triangle")

elif side1 == side2 or side2 != side3 or side1 == side2 or side1 != side3:
    print("Isoscles Triangle")

elif side1 != side2 and side2 !=  side3 and side1 !=  side3:
    print("Scalene Triangle")

#Check Password

p = input("Enter a Password")

if p == "python123":
    print("The Password is Correct")

else:
     print("The Password is InCorrect")