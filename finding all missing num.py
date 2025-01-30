arr=[2,5,7,8,6]
target_sum=9
dicti={}
for i in arr:
    if target_sum-i in arr:
        dicti[i]=[i-target_sum]
print(dicti)
        
    
