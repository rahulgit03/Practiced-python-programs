arr=[1,5,7,8,9,6,4,5,5,5,2,1,4,7]
duplicates=[]
new_arr=[]
for i in arr:
    if i not in new_arr:
        new_arr=new_arr + [i]
    else:
        duplicates=duplicates+[i]
print(duplicates)
