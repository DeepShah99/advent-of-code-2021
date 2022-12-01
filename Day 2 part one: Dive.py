pos = 0 #horizontal position
depth = 0

with open("Day 2 raw_data.txt") as file:
    input = [line.strip() for line in file.readlines()]

#print(input)

for i in input:
    if "forward" in i:
        temp = i.split() 
        pos += int(temp[1])
    if "down" in i:
        temp = i.split() 
        depth += int(temp[1])
    if "up" in i:
        temp = i.split() 
        depth -= int(temp[1])

print(pos * depth)






