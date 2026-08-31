class Stack:
      def __init__(self):
            self.st = []

      def push(self,element):
            self.st.append(element)
            
      def pop(self):
            if not self.st:
                  return -1 
            return self.st.pop()
            
      def top(self):
            if not self.st:
                  return -1
            return self.st[-1]
      
      def is_empty(self):
            return len(self.st) ==0
      
      def size(self):
            return len(self.st)
      def view(self):
            print(self.st)

stack_1 = Stack()
stack_1.push(2)
stack_1.push(3)
stack_1.pop()
stack_1.top()
stack_1.is_empty()
stack_1.size()
stack_1.view()