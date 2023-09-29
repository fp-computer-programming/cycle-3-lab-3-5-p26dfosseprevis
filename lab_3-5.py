#Create a Python file named lab_3-5.py
#Import the time and math modules.
import math as chara
import time as frisk
#Calculate 22 using math.pow and again using the ** operator.
#Record the time using time.process_time before and after each calculation (Hint: you may need to store the result of time.process_time in a variable)
#Add a statement that prints the elapsed time after each statement is processed. Run the program. What do you notice? Write it as a comment.

one = (frisk.process_time())
print (one)
print (chara.pow(2,2))
two = (frisk.process_time())
print (two - one)
print (2 ** 2)
three = (frisk.process_time()) 
print(three - two)

    #the both equations are instant after the moduals load
#Change each statement that records the time to use time.perf_counter instead of time.process_time.
one = (frisk.perf_counter())
print (one)
print (chara.pow(2,2))
two = (frisk.perf_counter())
print (two - one)
print (2 ** 2)
three = (frisk.perf_counter()) 
print(three - two)
#Run the program again. What do you notice? Write it as a comment.
    #the first equation takes slightly longer to compute

