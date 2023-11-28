# Print a # staircase with base and height equal to n

n = int(input())

for value in range(1, n + 1, 1):
    print(('#'*value).rjust(n))