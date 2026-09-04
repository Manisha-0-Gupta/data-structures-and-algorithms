from data_structures.queue.queue import Queue
class PrinterQueue:

      def __init__(self):
            self.printer = Queue()

      def receive_job(self,name):
            self.printer.enqueue(name)

      def print_next(self):
            if self.printer.is_empty():
                  print("The queue is empty")
                  return
            return self.printer.dequeue()
      
      def next_job(self):
            return self.printer.peek()
      
      def pending_jobs(self):
            return self.printer.size()

