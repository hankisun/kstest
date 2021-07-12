from anytree import AnyNode, RenderTree
from collections import deque
from random import randrange

root = AnyNode(id='0', ch='a')
ch = ord('a')
q = deque()
q.append(root)
t_cnt = 0

root.ch = 'z'

while q:
    child_no = randrange(1,4)
    papa = q.popleft()
    for _ in range(child_no):
        ch += 1
        t_cnt += 1
        child = AnyNode(id=str(t_cnt), parent = papa, ch=chr(ch))
        q.append(child)
#     print(q)
    if t_cnt > 26:
        break
        
q.clear()

print(RenderTree(root))
    
    
