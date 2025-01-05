#For Loops

    #Multiplication of 5

for multi in range(5,51,5):
    print(multi)

    #Count Vowels

count = "vowels"
vowles = "aeiou"
v_count = 0

for char in count:
    if char in vowles:
        v_count +=1
        print(v_count)

        #Sum of Evene Numbers from a list

even_number = [2,5,8,3]
sum = 0

for num in even_number:
    if num%2==0:
        sum += num
        print(sum)

        #Find Largest and smallest number in list 

number = [10,20,5,8]

for num2 in number:
    if num2 == 20:
        print(f"Largest Number is 20")

    elif num2 == 5:
        print(f"Smallest Number is 5")

        #sum of digits using loop

n = int(input("Enter Number")) #1234
total = 0

for digit in str(n):
    total += int(digit)
    print(f"Total is {total}")

    #Reverse 

for rev in reversed("PYTHON"):
    print(rev)