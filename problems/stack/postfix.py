from data_structures.stack.stack import Stack

def postfix_evaluation(lst):
      tokens = Stack()
      result = 0
      for token in lst:

            if token.isdigit():
                  tokens.push(int(token))
            else:
                  right = tokens.pop()
                  left = tokens.pop()
                  if token == "+":
                        result = left+right
                  elif token == "-":
                        result = left-right
                  elif token == "*":
                        result = left*right
                  elif token == "/":
                        result = left/right

                  tokens.push(result)
      return tokens.pop()
 

