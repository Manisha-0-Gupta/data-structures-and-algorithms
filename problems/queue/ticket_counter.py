from data_structures.queue.queue import Queue

class TicketCounter:

      def __init__(self):
            self.customers = Queue()

      def take_ticket(self,customer):
            self.customers.enqueue(customer)

      def serve_customer(self):
            if self.customers.is_empty():
                  print("No customer is waiting")
                  return 
            
            return self.customers.dequeue()

      def next_customer(self):
            if self.customers.is_empty():
                  print("No customer is waiting")
                  return 

            return self.customers.peek()

      def waiting_count(self):
            return self.customers.size()



