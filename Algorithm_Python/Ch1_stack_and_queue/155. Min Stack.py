'''
假设当前数据为newNum，先将其压入stackData。然后判断stackMin 是否为空。
如果为空，则newNum 也压入stackMin；#math.inf# 如果不为空，则比较newNum 和stackMin 的栈顶
元素中哪一个更小。
如果newNum 更小或两者相等，则newNum 也压入stackMin；如果stackMin 中栈顶元素
小，则把stackMin 的栈顶元素重复压入stackMin，即在栈顶元素上再压入一个栈顶元素
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

