#Write a Python program to count the number of even and odd numbers from a series of numbers.

# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, ) 
count_odd = 0
count_even = 0
for i in numbers:
       
 if  (i % 2 == 0):
     count_even=count_even + 1

else:
    count_odd = count_even + 1

print("Total  of even numbers is :",count_even)
print("Total  of odd numbers is :",count_odd)