from data_structures.stack.stack import Stack

def is_balanced(expression):
      stack = Stack()

      pairs = {'(':')',
               '{':'}',
               '[':']'
      }
      for char in expression:
            if char in pairs:
                  stack.push(pairs[char])
            else:
                  if stack.is_empty():
                        return False

                  if stack.top() != char:
                        return False

                  stack.pop()

      return stack.size()== 0

print(is_balanced("[{()}]"))