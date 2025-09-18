
# ASSIGNMENT 1

#1 first character
a = ("divya")
print("first character: ",a[0])


#2 last character
b = ("yadav")
print("last character: ",b[4])
print(b[4:6:1])
print(b[-1:-2:-1])


#3 first three characters
c = input("enter a word1: ")
print(c[0:3:1])


#4 reverse 
d = input(" enter string: ")
print(d[::-1])


#5 enter every second character
e = input("string is:") 
print(e[0::2])


#6 larger one 
f = input("enter 1st number: ")
g = input("enter 2nd number: ")
if f > g :
    print("largest number is: ",f)
else :
    print("largest number is: ",g)


#7 odd/even
num = int(input("enter a number: "))
if num % 2 == 0 :
   print("even")
else :
    print("odd")   


#8 having letter a or not 
d_rao = input("Enter a string: ")
if 'a' in d_rao:
    print("string have 'a'.")
else:
    print("string does not have 'a'.")


#9 positive negative zero
number = int(input("enter any number: "))
if number > 0 :
    print("number is positive ")
elif number < 0 :
    print("number is negative ")
else :
    print("number is zero ")


#10 printing middle characters 
word = input("enter a word: ")
length = len(word)
mid = length // 2
if length % 2 == 0 :
    print("middle numbers:",word[mid-1:mid+1] )
else :
    print("middle character: ",word[mid])


#11 uppercase and lowercase
k = input("enter a string: ")
print(k[0::1].upper())
k = k.lower()
print(k)


#12 first half and second half using slicing
sentence = input("enter a sentence: ")
lenth = len(sentence)
mid = lenth // 2
first_half = sentence[:mid]
second_half = sentence[mid:]
print("first half is ", first_half)
print("second half is ",second_half)


#13 divisible by 5 
h = int(input("random number is: "))
if h % 5 == 0 :
    print("buzz")
else :
    print("not buzz")


#14 password check 
password = input("enter password: ")
if len(password)>= 8 :
    print("strong")
else :
    print("weak")


#15 first and last character match ?
string = input("string: ")
if len(string)<2:
    print("invalid input ")
elif string[0]==string[-1] :
   print("match")
else :
    print("no match")


#16 pass or fail
i = int(input("enter marks: "))
if i >= 33 :
    print("pass")
else :
    print("fail")


#17 palindrome 
word = input("enter a word: ")
if word == word[::-1] :
    print("palindrome")
else :
    print("not palindrome")


#18 teenager and adult 
j = int(input("enter age "))
if 0<j< 13 :
    print("child")
elif 13<j<=19 :
    print("teenager")
elif j>19 :
    print("adult")
else :
    print("invalid age ")


#19 even indexed number 
name = input("enter name : ")
print(name[::2])


#20 dictionary order 
first_string = input("enter a string: ")
second_string = input("enter other string: ")
a = first_string
b = second_string
if a>b :
    print("preceding word is ",b)
elif b>a :
    print("preceding word is ",a)
else :
    print("both string are equal ")