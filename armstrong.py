n=153
l=len(str(n))
sum=0
for i in str(n):
    sum+=int(i)**l
if sum==n:
    print('True')
else:
    print('False')
    
