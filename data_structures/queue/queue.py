class Queue:

      def __init__(self):
            self.qu = []
            self.front =0

      def enqueue(self,item):
            self.qu.append(item)

      def dequeue(self):
            if len(self.qu) == self.front:
                  return -1
            dq = self.qu[self.front]
            self.front +=1
            return dq
      
      def peek(self):
            if len(self.qu) == self.front:
                  return -1
            pk =  self.qu[self.front]
            return pk
      
      def is_empty(self):
            return len(self.qu) == self.front
      
      def size(self):
            return len(self.qu) - self.front

