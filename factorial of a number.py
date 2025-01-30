number=int(input('enter a number :'))
if number < 0:
    print('Factorial is not defined for -ve numbers ')
   
factorial=1
for current_number in range(number,1,-1):
    factorial*=current_number
print(factorial)
