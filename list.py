#Create a list of 5 numbers and print the largest number.
#Find the sum of all elements in a list.
#Count how many times a specific number appears in a list.
#Remove duplicate elements from a list.
#Reverse a list without using reverse().
#Find the second largest element in a list.
#Merge two lists into one.
#Sort a list in ascending and descending order.
#Find all even numbers in a list.
#Rotate a list by k positions

#question 1:
a=[1,2,3,4,5]
print(max(a))

#question 2:
a=[1,2,3,4,5]
print(sum(a))

#question 3:
a=[1,2,3,4,5,2,2]
print(a.count(2))

#question 4:
a=[1,2,3,4,5,2,2]
b=list(set(a))
print(b)

#question 5:
a=[1,2,3,4,5]
b=a[::-1]
print(b)

#question 6:
a=[1,2,3,4,5]
a.sort()
print(a)
print(a[-2])

#question 7:
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

#question 8:
a=[5,2,9,1,5,6]
a.sort()
print(a)
a.sort(reverse=True)
print(a)  

#question 9:
a=[1,2,3,4,5,6,7,8,9]
even_numbers=[num for num in a if num%2==0] 
print(even_numbers)

#question 10:
a=[1,2,3,4,5,6,7,8,9]
k=3 
rotated_list=a[k:]+a[:k]
print(rotated_list) 
