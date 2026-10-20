def my_sum(*args):
    #args will be a tuple of all the arguments passed to the function.

    total = 0
    for num in args:
        total += num
    return total

result = my_sum(7567, 9272, 9383)
print(result) 
#Can also be used for multiplication, division, etc. Just change the operator in the for loop. This is the basic use case of args.