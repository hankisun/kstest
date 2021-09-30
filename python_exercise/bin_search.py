def call_api(s, e, er):
    for error in er:
        if error in range(s, e+1):
            return False
    return True

def bin_search(s, e, er):
    if s == e:
        if call_api(s, e, er):
            print(s)
        else:
            print(str(s) + ' error found')
        return 1
    # call api , exception occurred -> bin search
    if call_api(s, e, er):
        print(s, e)
        return 1
    m = int((s + e) / 2)
    call1 = bin_search(s, m, er)
    call2 = bin_search(m+1, e, er)
    return call1 + call2
    
bin_search(1,100,[37, 38, 51])
