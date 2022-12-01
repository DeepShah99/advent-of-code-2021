"""
* File Name:           Day 1 part one: Sonar Sweep.py
* Author:              Deep Shah
* Date:                1st Dec 2022

"""

"""
Tried to web scrap the input data. But I guess advent of code doesn't authorize HTTP GET requests without session cookie.  

from bs4 import BeautifulSoup
import requests

url = "https://adventofcode.com/2021/day/1/input"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser") 

print(result.text)  

The following authorization error was received:
Puzzle inputs differ by user.  Please log in to get your puzzle input.

Also, many attempts of GET requests might get me blocked. So proceeded with creating a local text file as raw input.
"""




with open("Day 1 raw_data.txt") as file:
    depth = [line.strip() for line in file.readlines()] 


#print(depth)
#print(len(depth))
count = 0

for i in range(0, len(depth) - 1):   
    if int(depth[i]) < int(depth[i + 1]): #compare with previous data
        count += 1
   

 

print(count)

