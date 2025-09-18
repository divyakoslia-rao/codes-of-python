
# ASSIGNMENT 2 


#1 print hello world
print("Hello , World!")


#2 take input from user as name
name = input("Enter name : ")
print(f"Hello, {name}")


#3 swapping numbers 
x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
x = x+y
y = x-y
x = x-y
print("after swapping x is : ",x)
print("after swapping y is : ",y)


#4 even oddd number 
number = int(input("Enter number: "))
if number%2 == 0 :
    print("even number")
else :
    print("odd number")


#5 positive,negative or zero
num = int(input("enter a number: "))
if num>0 :
    print("positive number")
elif num<0 :
    print("negative number")
else :
    print("zero")


#6 largest of two numbers
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1>num2 :
    print("largest number is ",num1)
elif num2>num1 :
    print("largest number is ",num2)
else :
    print("both numbers are equal .")


#7 smallest of three numbers 
num_1 = input("enter 1st number: ")
num_2 = input("enter 2nd number: ")
num_3 = input("enter 3rd number: ")
if num_1<num_2 :
    if num_1<num_3 :
        print("smallest number is ",num_1)
elif num_2<num_1 :
    if num_2<num_3 :
        print("smallest number is ",num_2)
else :
    print("smallest number is ",num_3)


#8 square and cube of a number 
x = int(input("enter number: "))
print("square is ",x*x)
print("cube is ",x*x*x)


#9 sum of digits of a given number 
b = int(input("enter number: "))
output = sum(int(x) for x in str(b))
print("sum of digits is : ",output)


#10 print all numbers from 1 to 10 
for i in range(1,11) :
    print(i)


#11 factorial of a number 
num = int(input("enter a number : "))
factorial = 1
if num<0 :
    print("no factorial exist ")
elif num==0 :
    print("factorial is 1")
else :
    for i in range (1,num+1):
        factorial = factorial*i
print( "factorial is ",factorial)


#12 reverse 
d = input("enter number : ")
print(d[::-1])


#13 print 10 fibonacci numbers
a = 0
b = 1
c = 0
for i in range(10):
    print(c)
    a=b
    b=c
    c = a+b


#14 palindrome string
s1 = input("enter a string: ")
if s1[::]==s1[::-1] :
    print("string is palindrome")
else :
    print("string is not palindrome")


#15 charracters in a given string
text1 = input("Enter a string: ")
print("No. of characters: ",len(text1))


#16 sum of n natural numbers 
n = int(input("enter value of n : "))
print(n*(n+1)/2)


#17 multiplication table of a number
y = int(input("enter table of : "))
table = []
for x in range(1,11):
    table.append(x*y)
print(table)


#17 using list comprehension (table)
z = int(input("enter table of :"))
table_of=[x*z for x in range(1,11)]
print(table_of)


#18 count vowels and consonants in a string 
str1 = input("enter a string : ")
str1.lower()
count = 0
for i in str1:
    if i in ["a","e","i","o","u"]:
        count += 1
print("vowels in string are : ",count)
print("consonants are : ",len(str1)-count)

#19 printing numbers between two numbers 
starting = int(input("Enter the start number: "))
ending = int(input("Enter the end number: "))
for numbers in range(starting + 1, ending):
    print(numbers)


#20 right angled traingle using stars 
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("*" * i)


#21 sort a list 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Example usage
my_list = [5, 2, 9, 1, 5, 6]
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)



#22 maximum and minumum numbers
list1 = [32,43,23,54,56,35]
max = list1[0]
min = list1[0]
for i in list1:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f"maximum number is {max}")
print(f"minimum number is {min}")


#23 remove duplicate item
list2 = [4,5,4,5,2,3,4,8]
newlist = []
for i in list2 :
    if i not in newlist :
        newlist.append(i)
print(list2)
print(newlist)


#24 anagrams strings
string1 = input("enter first string: ")
string2 = input("enter second string: ")
if len(string1) != len(string2):
    print("not anagrams")
else:
    sorted1 = sorted(string1.lower())
    sorted2 = sorted(string2.lower())
    if sorted1 == sorted2 :
        print("anagrams")
    else:
        print("not anagrams ")


#25 count frequency of each element 
def frequency(lst):
    freq = {}
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
    return freq
my_list = [1, 2, 2, 3, 1, 4, 2]
frequencies = frequency(my_list)
print("Frequencies:", frequencies)


#26 second largest number
my_list = [10,23,45,2,32,9]
my_list.sort()
print(my_list)
print("second largest number is : ",my_list[-2])


#27 prime numbers from 1 to 100
n=1
while n<=100:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
        print(n,end=" ")
    n+=1


#28 n prime numbers 
number = int(input("enter first n prime numbers: "))
c = 2
while number!=0:
    for i in range(2,c):
        if c%i==0:
            break
    else:
        print(c,end=" ")
        number-=1
    c+=1


#29 find longest word in a sentence 
def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print("Longest word:", find_longest_word(sentence))


#30 reverse a string
string = input("enter a string : ")
reversed_str = ""
for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
print(reversed_str)