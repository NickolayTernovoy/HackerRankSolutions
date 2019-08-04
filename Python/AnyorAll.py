# https://www.hackerrank.com/challenges/any-or-all/problem
# solution, Python 3
n, a = (input(), input().split(" "))# input list
print((any([j == j[::-1] for j in a]) and (all((int)(x) > 0 for x in (a)))))