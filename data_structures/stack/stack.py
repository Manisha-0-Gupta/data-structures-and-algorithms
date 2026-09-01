class Stack:
      def __init__(self):
            self.st = []

      def push(self,element):
            self.st.append(element)
            
      def pop(self):
            if not self.st:
                  return -1 
            return self.st.pop()
            
      def peek(self):
            if not self.st:
                  return -1
            return self.st[-1]
      
      def is_empty(self):
            return len(self.st) ==0
      
      def size(self):
            return len(self.st)
      def view(self):
            print(self.st)

