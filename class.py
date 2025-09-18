# class Animal:
#     def eat(self):
#         print("i eat")
# class Dog(Animal):
#     def bark(self):
#         pass

# my_dog=Dog("Rex")
# my_dog.eat()
# my_dog.bark()
 
lst = [1, 2, 2, 3, 3, 3, 4] 
freq = {}
for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1
print("frequencies : ",freq)