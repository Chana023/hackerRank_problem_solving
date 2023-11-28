
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

def miniMaxSum(arr):
    # Write your code here
    arr = list(arr)
    min_value = min(arr)
    max_value = max(arr)

    copy_list = list(arr)
    copy_list.remove(min_value)

    max_sum = 0
    for value in copy_list:
        max_sum = max_sum + value
    
    arr.remove(max_value)
    min_sum = 0
    for value in arr:
        min_sum = min_sum + value

    print(min_sum, max_sum)

    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)