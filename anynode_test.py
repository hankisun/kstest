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

##########################
# fusion type
class CutRange:
    def __init__(self, cur_line, typ):
        self.cur_line = cur_line
        self.typ = typ
        self.tr_idx = 0
    
    def cut_range(self, tr):
        ret = []
        tr_s = tr[0]
        tr_e = tr[1]
        for idx in range(self.tr_idx, len(self.cur_line)):
            ctyp = self.typ[idx]
            if ctyp == 'd':
                continue
            cr = self.cur_line[idx]
            cr_s = cr[0]
            cr_e = cr[1]

            if tr_s > cr_e:
                continue

            if tr_e < cr_s:
                break

            if tr_s >= cr_s:
                # tr  --- | ----
                # cr ---  | ---          
                if tr_e > cr_e:
                    if ctyp == 'c':
                        ret.append([tr_s, cr_e])
                    tr_s = cr_e + 1
                    continue
                # tr  --  | --- | ---  |  ---
                # cr ---- | --- | ---- | ----              
                else:
                    if ctyp == 'c':
                        ret.append([cr_s, cr_e])
                    break

            # tr ---  | ----
            # cr  --- |  ---      
            if tr_s < cr_s:
                ret.append([tr_s, cr_s-1])
                tr_s = cr_s
                # tr --- 
                # cr --  
                if tr_e > cr_e:
                    if ctyp == 'c':
                        ret.append([tr_s, cr_e])
                    tr_s = cr_e + 1
                    continue
                # tr --  | --- 
                # cr --- | ---
                else:
                    if ctyp == 'c':
                        ret.append([tr_s, cr_e])
                    break

        print(ret)
        
        self.tr_idx = idx if idx > 0 else idx -1
        return ret

trace_line = [[4,11],[15,19]]
cur = [[1,2],[3,6],[8,9],[11,15],[17,17],[19,20]]
typ = ['c','a','c','a','d','c']
# cur = [[2,21]]

cut_list = []
next_idx = 0

cr = CutRange(cur, typ)
for tr in trace_line:
    cut = cr.cut_range(tr)
    if cut_list:
        if cut_list[-1] == cut[0]:
            cut.pop(0)
        cut_list.extend(cut)
    else:
        cut_list = cut

print(cut_list)

##########################
# fusion type
def cut_range(tr, cur, typ, start_idx):
    ret = []
    tr_s = tr[0]
    tr_e = tr[1]
    for idx in range(start_idx, len(cur)):
        ctyp = typ[idx]
        if ctyp == 'd':
            continue
        cr = cur[idx]
        cr_s = cr[0]
        cr_e = cr[1]

        if tr_s > cr_e:
            continue

        if tr_e < cr_s:
            break
                        
        if tr_s >= cr_s:
            # tr  --- | ----
            # cr ---  | ---          
            if tr_e > cr_e:
                if ctyp == 'c':
                    ret.append([tr_s, cr_e])
                tr_s = cr_e + 1
                continue
            # tr  --  | --- | ---  |  ---
            # cr ---- | --- | ---- | ----              
            else:
                if ctyp == 'c':
                    ret.append([cr_s, cr_e])
                break
    
        # tr ---  | ----
        # cr  --- |  ---      
        if tr_s < cr_s:
            ret.append([tr_s, cr_s-1])
            tr_s = cr_s
            # tr --- 
            # cr --  
            if tr_e > cr_e:
                if ctyp == 'c':
                    ret.append([tr_s, cr_e])
                tr_s = cr_e + 1
                continue
            # tr --  | --- 
            # cr --- | ---
            else:
                if ctyp == 'c':
                    ret.append([tr_s, cr_e])
                break

    print(ret)
    return ret, idx if idx > 0 else idx -1

trace_line = [[4,11],[15,19]]
cur = [[1,2],[3,6],[8,9],[11,15],[17,17],[19,20]]
typ = ['c','a','c','a','d','c']
# cur = [[2,21]]

cut_list = []
next_idx = 0
for tr in trace_line:
    cut, next_idx = cut_range(tr, cur, typ, next_idx)
    if cut_list:
        if cut_list[-1] == cut[0]:
            cut.pop(0)
        cut_list.extend(cut)
    else:
        cut_list = cut

print(cut_list)
    
