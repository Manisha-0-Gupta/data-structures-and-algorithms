from data_structures.stack.stack import Stack

def reverse(s):

      stack = Stack()
      result = ""
      for char in s:
            stack.push(char)

      while not stack.is_empty():
            result += stack.pop()

      return result

print(reverse('hello'))