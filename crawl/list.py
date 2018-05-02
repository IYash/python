# -*- coding: utf-8 -*-
# 列表求积

def product_list(list_of_numbers):
    total = 1
    for i in list_of_numbers:
        total *= i
    return total

# 最大值

def greatest(list_of_numbers):
    result = 0
    for e in list_of_numbers:
        if e > result:
            result = e
    return result

# 列表操作

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(usa_univs):
    num = 0
    tuition = 0
    for name,student,tui in usa_univs:
        num += student
        tuition += student * tui
        
    return num,tuition 
