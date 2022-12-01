pos = 0 #horizontal position
depth = 0
aim = 0

with open("Day 2 raw_data.txt") as file:
    input = [line.strip() for line in file.readlines()]

#print(input)

for i in input:
    if "forward" in i:
        temp = i.split() 
        pos += int(temp[1])
        depth += aim * int(temp[1])   
        #print(pos, depth , aim) 

    if "down" in i:
        temp = i.split() 
        aim += int(temp[1])
        #print(pos, depth , aim)

    if "up" in i:
        temp = i.split() 
        aim -= int(temp[1])
        #print(pos, depth , aim) 

print(pos * depth)






