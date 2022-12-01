"""
* File Name:           Day 1 part two: Sonar Sweep.py
* Author:              Deep Shah
* Date:                1st Dec 2022

"""

with open("Day 1 raw_data.txt") as file:
    Arr = [line.strip() for line in file.readlines()] 

i, j = 0, 0
res, sum = 0, 0
count = 0

#sliding window technique

while(j < len(Arr)):  
            sum = sum + int(Arr[j])
            if j - i + 1 < 3:   #check if window size is hit
                j += 1
            elif j - i + 1 == 3:
                if res == 0:    #this will be the first result (no previous sum)
                    res = sum
                elif sum > res: #compare with previous sum
                    count += 1
                res = sum
                sum = sum - int(Arr[i])
                i += 1          #now slide the window
                j += 1

print(count)