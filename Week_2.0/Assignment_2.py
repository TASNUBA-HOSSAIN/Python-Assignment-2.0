# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 01:32:33 2018

@author: TASNUBA
"""
## Part 1

gradient_func_x = lambda x: 2*x + 12
gradient_func_y = lambda y: 2*y + 4

X_0 = 3
Y_0 = 3

#initially X_old is X_init, that's the point we start from
X_old = X_0
Y_old = Y_0

#Learning rate to do the shifting of slope
learning_rate = 0.1

#Diff between X_old and X_new
threshold = 100
threshold1 = 100

iteration_no = 0

limit = 500

while threshold > 0.000001:
    X_new = X_old - (learning_rate * gradient_func_x(X_old))
    Y_new = Y_old - (learning_rate * gradient_func_y(Y_old))
        
    threshold = abs(X_new - X_old)
    threshold1 = abs(Y_new - Y_old)
        
    X_old = X_new
    Y_old = Y_new
        
    iteration_no += 1
    
    if iteration_no == limit:
        break
        
    print("Iteration no: "+str(iteration_no)+", Value of X = "+str(X_new) +", Value of Y = "+str(Y_new))

# When iteration no. is set to 1000, the code runs upto 600 iterations only. So I set the limit of iterations to 500.
    
# The most convenient learning rate for me is 0.1 since this value generates the lowest values of x and y.

## PART 2:

list_1 = [] 

print ('Enter five integer numbers to generate first list (list_1)')

for i in range(0, 4): # set up loop to run 5 times
	number = int(input('Please enter a number: ')) 
	list_1.append(number) 

print ('list_1 = '+str(list_1))

list_2 = [] 

print ('Enter five integer numbers to generate second list (list_2)')

for i in range(0, 4): # set up loop to run 5 times
	number_2 = int(input('Please enter a number: ')) 
	list_2.append(number_2) 

print ('list_2 = '+str(list_2))


import modules as mods

mods.Average(list_1)
mods.Average(list_2)

mods.median(list_1)
mods.median(list_2)



