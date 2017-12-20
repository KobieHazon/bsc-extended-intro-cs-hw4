#Skeleton file for HW4 - Fall 2017-2018 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

import random
import math

############
# QUESTION 1
############


def acc(f, v, lst):
    if len(lst) == 0:
        return v
    return acc(f, f(lst[0], v), lst[1:])
    

def myProd(lst):
    if not lst:
        return 0
    return acc(lambda x, y: x*y, 1, lst)


def g(f1, f2):
    return lambda x: f2(f1(x))


def h(x):
    return x


def compose(lst):
	return acc(g, h, lst)




############
# QUESTION 2
############

def profit(value,size):
    max_p, tmp = 0, 0
    for i in range(size):
        tmp += value[i] + profit(value, size - (i + 1))
        if tmp > max_p:
            max_p = tmp
        tmp = 0
    return max_p


def profit2(value,size):
    d = {}
    return profit_mem(value,size,d)


def profit_mem(value,size,d):
    if size not in d:
        d[size], tmp = 0, 0
        for i in range(size):
            if size - (i + 1) not in d:
                d[size - (i + 1)] = profit_mem(value, size - (i + 1), d)
            tmp += value[i] + d[size - (i + 1)]
            if tmp > d[size]:
                d[size] = tmp
            tmp = 0
    return d[size]


def profit3(value, size):
    n = len(value)
    return profit_rec(value, n, size)


def profit_rec(value, i, size):
    if size==0 or i==0:
        return 0
    if size==1:
        return value[0]
    left = value[min(i-1, size-1)] + profit_rec(value, i, max(0, size-i))
    right = profit_rec(value, i-1, size)
    return max(left, right)


############
# QUESTION 3
############

# do not modify the code's structure or change any of the existing code

def win(num, moves):
    for move in moves:
        if (num - move) == 0 or ((num - move) > 0 and not win(num - move, moves)):
            return True #We prevent unneeded recursive calls by not calling if num - move <= 0
    return False


def win2(num, moves):
    d = {}
    return win_mem(num, moves, d)


def win_mem(num, moves,d):
    if num not in d:
        for move in moves:
            if (num - move) == 0 or ((num - move) > 0 and not win(num - move, moves)):
                d[num] = True
        if num not in d:
            d[num] = False
    return d[num]
    
############
# QUESTION 6
############

def walk(run_length, d): 
    loc = [0 for i in range(d)]
    back_to_origin = False
    for step in range(run_length):
        for cor in range(d):
            loc[cor] += random.choice([-1,1])
        if loc == [0 for i in range(d)]:
            back_to_origin = True
    dist = math.sqrt(sum([x**2 for x in loc]))
    return dist, back_to_origin


def rw_stats(run_length, d, number_runs=10**3):
    sum_dist = 0
    max_dist = 0
    sum_origin = 0
    min_dist = run_length
    for run in range(number_runs):
        dist, back_to_origin = walk(run_length, d)
        sum_dist += dist
        if back_to_origin:
            sum_origin += 1
        if dist > max_dist:
            max_dist = dist
        elif dist < min_dist:
            min_dist = dist
    average_dist = sum_dist/number_runs
    origin_frequency = sum_origin/number_runs
    return run_length, average_dist, average_dist/(run_length**0.5),\
            min_dist, max_dist, origin_frequency


    
########
# Tester
########

def test():

    # Q1 basic tests
    def mySum(lst):
    	return acc((lambda x,y: x + y), 0, lst)
    lst = [i for i in range(1,25)]
    if mySum(lst) != sum(lst):
        print("error in acc()")
    if myProd(lst) != 620448401733239439360000:
        print("error in myProd()")
    if compose([lambda x: x-1, lambda x: x*2, lambda x: x+1]) == None or \
       compose([lambda x: x-1, lambda x: x*2, lambda x: x+1])(5) != 11 or \
       compose([])(5) != 5:
        print("error in compose()")

    # Q2 basic tests
    value1, size1 = [1, 5, 8, 9], 4
    value2, size2 = [2, 3, 7, 8, 9], 5
    if profit(value1,size1) != 10 or profit(value2,size2) != 11:
        print("error in profit()")
    if profit2(value1,size1) != 10 or profit2(value2,size2) != 11:
        print("error in profit2()")
    if profit3(value1,size1) != 10 or profit3(value2,size2) != 11:
        print("error in profit3()")
    
    # Q3 basic tests
    moves = [1,4,2]
    if win(9,moves) != False or win(8,moves) != True \
       or win(10,moves) != True:
        print("error in win()")
    if win2(9,moves) != False or win2(8,moves) != True \
       or win2(10,moves) != True:
        print("error in win2()")
