from data_structures.stack.stack import Stack

class BrowserHistory:

      def __init__(self,homepage):
            self.back_stack = Stack()
            self.forward_stack = Stack()
            self.current = homepage

      def visit(self,url):
            self.back_stack.push(self.current)

            while not self.forward_stack.is_empty():
                  self.forward_stack.pop()

            self.current = url

      def back(self):
            if self.back_stack.is_empty():
                  return self.current
            
            self.forward_stack.push(self.current)
            self.current = self.back_stack.pop()

            return self.current

      def forward(self):
            if self.forward_stack.is_empty():
                  return self.current
            
            self.back_stack.push(self.current)
            self.current = self.forward_stack.pop()

            return self.current
      def current_page(self):
            return self.current




