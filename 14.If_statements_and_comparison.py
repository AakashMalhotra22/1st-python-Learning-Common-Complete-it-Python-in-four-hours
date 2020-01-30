# It can be used to compare strings, bulleins, and other datatypes
'''
Some signs; != not equal
             == equals to
             >= greate than
             <= less than

'''


'''
Type I
'''

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2>= num1 and num2>=num3:
        print(num2)
    else:
        print(num3)

max_num(3,4,5)

'''
TypeII
'''

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return (num1)
    elif num2>= num1 and num2>=num3:
        return(num2)
    else:
        return(num3)

print(max_num(3,4,5))

