from data_structures.stack.stack import Stack

class TextEditor():

      def __init__(self):
            self.forward = Stack()
            self.back = Stack()
            self.current = ""

      def write(self,word):
            self.back.push(self.current)

            while not self.forward.is_empty():
                  self.forward.pop()
            self.current += word


      def undo(self):
            if self.back.is_empty():
                  return self.current
            self.forward.push(self.current)
            self.current = self.back.pop()
            return self.current

      def redo(self):
            if self.forward.is_empty():
                  return self.current

            self.back.push(self.current)
            self.current = self.forward.pop()
            return self.current

      def current_text(self):
            return self.current
