from  temperatureAnalze import  temperature
def setp(x):
    return (x/100)*100


def Max(*a):
    Max_num = 0
    current_num = 0
    for i in a:
        for num in i:
            current_num = num
            if current_num > num:
                Max_num = current_num
    return Max_num
def Min(*a):
    Min_num : int = 0
    current_num : int = 0
    for i in a:
        for b in i:
            if b < b-1:
                current_num = b
                Min_num =+ current_num

    return Min_num


def Sum(*a):
    total_sum = 0
    for n in a:
        for k in n:
            total_sum+=k
    return total_sum


nums = [100,23,23]

print(f"The min is {Min(nums)}. The max is {Max(nums)}.  The sum is {Sum(nums)}")









