from os import popen
from sys import stdin

ps = popen('C:/Windows/system32/tasklist.exe', 'r')
pp = ps.readlines()
ps.close()

pp.pop(0)
ph = pp.pop(0)
pp.pop(0)

print(f'{len(ph)} process reported')
print("first process in list:")
print(pp[0])
