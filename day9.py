# Write a recursive function to find the sum of digits of a positive integer.
sumnum=0
def sum_of_digits(num):
    global sumnum
    if num==0:
        print(f"The sum of digits is {sumnum}.")
    else:
        digit=num%10
        sumnum=sumnum+digit
        sum_of_digits(num//10)
        

number=int(input("Enter a positive number:"))
sum_of_digits(number)

# Write a recursive function to reverse a string.
rev=""
def rev_string(str):
    global rev
    if len(str)==0:
        print(rev)
    else:
        rev=rev+str[-1]
        str=str[:-1]
        rev_string(str)
str1=input("Enter a string:")
rev_string(str1)

# How would you write a recursive function to calculate the power of a number
def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
num=int(input("Enter a number:"))
exp=int(input("Enter power:"))
result= power(num,exp)
print(f"{num}^{exp}={result}")