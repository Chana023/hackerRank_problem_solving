# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

number_of_candles = int(input())
list_of_candles = list(map(int, input().split(' ')))

max_candle = max(list_of_candles)

count = 0

count = len([ x for x in list_of_candles if x == max_candle ])

print(count)