def getAndRemoveLastElement(stack):
    result= stack.pop()
    if not stack:
        return result
    else:
        last = getAndRemoveLastElement(stack)
        stack.append(result)
        return last
def reverseStack(stack):
    if not stack:
        return
    i = getAndRemoveLastElement(stack)
    reverseStack(stack)
    stack.append(i)


def main1(stack):
    reverseStack(stack)
    res=[]
    while stack:
        res.append(stack.pop(0))
    return res
    
