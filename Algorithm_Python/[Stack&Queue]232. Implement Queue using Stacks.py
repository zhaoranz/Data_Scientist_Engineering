'''
1. push1向pop1中压入，一定要压入push1中全部的元素
2. 如果pop1不为空，push1 绝对不能向其中压入元素
3. 掌握以上两点，在push pop peek中，都可以压入元素

'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push1=[]
        self.pop1=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.pop1:
            while self.push1:
                self.pop1.append(self.push1.pop())
        return self.pop1.pop()
                

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.pop1:
            while self.push1:
                self.pop1.append(self.push1.pop())
        return self.pop1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        
        """
        return not self.push1 and not self.pop1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
