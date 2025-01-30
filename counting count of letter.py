arr=[1,5,7,8,9,6,4,5,5,5,2,1,4,7]
dicti={}
for item in arr:
    if item in dicti:
        dicti[item]+=1
    else:
        dicti[item]=1
for item,count in dicti.items():
    print(item,':',count)
