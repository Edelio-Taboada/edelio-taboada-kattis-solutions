p= input()
s = input()
def ifNum(x):
    return x.isnumeric()
        
def checkPrepend():
    global s
    global p
    if p[1:len(p)] == s:
        if ifNum(p[0]):
            return True
    return False
    
    
def checkAppend():
    global s
    global p
    if p[0:len(p)-1] == s:
        if ifNum(p[-1]):
            return True
    return False

    
    
def checkCaseSwap():
    global s
    global p
    caseSwappedP = ""
    for each in p:
        if not ifNum(each):
            if each.islower():
                caseSwappedP += each.upper()
            elif each.isupper():
                caseSwappedP += each.lower()
        else:
            caseSwappedP += each
            
    if caseSwappedP == s:
        return True
    

if s == p:
    print("Yes")
elif checkPrepend():
    print("Yes")
elif checkAppend():
    print("Yes")
elif checkCaseSwap():
    print("Yes")
else:
    print("No")
