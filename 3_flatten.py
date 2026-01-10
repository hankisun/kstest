def flatten(data):
    res=[]
    for i in data:
        if type(i) is list:
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

example=[[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))
    