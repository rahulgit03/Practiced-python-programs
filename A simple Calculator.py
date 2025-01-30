print('---- A simple Calculator ----')
num_1=int(input('Enter num 1 : '))
num_2=int(input('Enter num 1 : '))
operator=input('enter operation for addition(+),substaraction(-),multiplication(*),division(/) :')
if operator == '+':
    print(' sum of 2 num : ',num_1+num_2)
elif operator == '-':
    print('the result is :', num_1-num_2)
elif operator =='*':
    print('the result is :', num_1*num_2)
else:
    if num_2==0 :
        print(' Error not divisible by zero ')
    else:
        print(' the result is :', num_1/num_2)
