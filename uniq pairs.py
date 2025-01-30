nums=input().split(',')
sum_num=int(input())
new_list=[]
unique_pairs=set()
for i in nums:
    new_list+=[int(i)]
index_num=len(new_list)-1
for curr_index in range(index_num):
    num_1=new_list[curr_index]
    num_2=sum_num-num_1
    remain_list=new_list[curr_index-1:]
    if num_2 in remain_list:
       pair=(num_1,num_2)
       #print(pair)
       sorted_pair=tuple(sorted(pair))
       #unique_pairs.add(sorted_pair)
       print(sorted_pair)
        
