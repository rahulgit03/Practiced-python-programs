n=371
sum=0
for i in str(n):
    sum+=int(i)**len(str(n))
if sum==n:
    print(True)
else:
    print(False)
    
