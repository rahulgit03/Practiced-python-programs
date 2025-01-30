nums=[1,5,8,9,-1,11]
target=10
def finding_indeces_of_target_pair_sum(nums,target):
    num_dict={}
    pairs=[]
    for i,num in enumerate(nums):
        complement=target-num
        if complement in num_dict:
            pairs.append([num_dict[complement],i])
        num_dict[num]=i
    return pairs
result=finding_indeces_of_target_pair_sum(nums,target)
print(result)
