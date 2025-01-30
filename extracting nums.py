string='c0d1n8'
nums=[]
for i in string:
    if i.isdigit():
        nums+=[int(i)]
print(nums)
print('sum of digits in given string :',sum(nums))
print(' minimum num of digits in given string :',min(nums))
