"""
ALyssa Dunn
Data Strcutures Course Project
Option 1
"""
#Comfy Deveations
import math
sum = 0

#Input
t = list(map(float, input("Please enter 10 temperatures: ").split()))
#testing the list that was entered
#print(t)

#Standard Deviation Equation
for i in range(len(t)):
    sum += t[i]
mean = sum/len(t)

sum_of_sd = 0
for i in range(len(t)):
    sum_of_sd += (t[i] - mean) ** 2
stdev = ((sum_of_sd)/len(t)) ** 0.5
#testing the equation
#print("Stdev is", stdev) 

#Output
if stdev <= 1.0:
    print("COMFY")
else:
    print("NOT COMFY")



