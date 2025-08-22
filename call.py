from collections import deque

class Call:
    def __init__(self, customer_id, call_time):
        self.customer_id = customer_id
        self.call_time = call_time

    def __str__(self):
        return f"Customer {self.customer_id}, Time {self.call_time}min"

class Operator:
    def __init__(self, operator_id):
        self.operator_id = operator_id
        self.queue = deque()
        self.total_time = 0
        self.call_log = []

    def add_call(self, call):
        self.queue.append(call)
        self.total_time += call.call_time

    def remove_call(self, call):
        self.queue.remove(call)
        self.total_time -= call.call_time
        self.call_log.append(call)
        return call

    def is_empty(self):
        return len(self.queue) == 0

    def average_wait_time(self):
        if len(self.queue) == 0:
            return 0
        return self.total_time / len(self.queue)

    def next_available_time(self):
        return self.total_time

class CallCenter:
    def __init__(self, num_operators):
        self.operators = []
        for i in range(num_operators):
            self.operators.append(Operator(i + 1))

    def addCall(self, customer_id, call_time):
        call = Call(customer_id, call_time)
       
        selected_operator = self.operators[0]
        for op in self.operators:
            if op.total_time < selected_operator.total_time:
                selected_operator = op
        selected_operator.add_call(call)
        print(f"Added call {call} to Operator {selected_operator.operator_id}")

    def answerCall(self):
        shortest_call = None
        selected_operator = None

        for op in self.operators:
            for call in op.queue:
                if shortest_call is None or call.call_time < shortest_call.call_time:
                    shortest_call = call
                    selected_operator = op

        if shortest_call is not None:
            selected_operator.remove_call(shortest_call)
            print(f"Operator {selected_operator.operator_id} answered call {shortest_call}")
        else:
            print("No calls to answer.")

    def viewQueue(self):
        for op in self.operators:
            print(f"Operator {op.operator_id} queue:")
            if op.is_empty():
                print("  No calls")
            else:
                for call in op.queue:
                    print(f"  {call}")

    def viewCallLogs(self):
        for op in self.operators:
            print(f"Operator {op.operator_id} call log:")
            if len(op.call_log) == 0:
                print("  No calls answered yet")
            else:
                for call in op.call_log:
                    print(f"  {call}")

    def averageWaitTimes(self):
        for op in self.operators:
            avg = op.average_wait_time()
            print(f"Operator {op.operator_id} average wait time: {avg:.2f} minutes")

    def nextAvailableTimes(self):
        for op in self.operators:
            print(f"Operator {op.operator_id} will be free in {op.next_available_time()} minutes")

    def isQueueEmpty(self):
        for op in self.operators:
            if not op.is_empty():
                return False
        return True

def main_loop():
    center = CallCenter(3)
    print("Welcome to Call Center!")
    print("Commands:")
    print(" add [customerID] [callTime]")
    print(" answer")
    print(" queue")
    print(" logs")
    print(" average")
    print(" next")
    print(" empty")
    print(" quit")

    while True:
        command = input("> ").strip().lower()
        if command.startswith("add"):
            parts = command.split()
            if len(parts) != 3:
                print("Usage: add [customerID] [callTime]")
                continue
            customer_id = parts[1]
            try:
                call_time = int(parts[2])
            except:
                print("Call time must be a number")
                continue
            center.addCall(customer_id, call_time)
        elif command == "answer":
            center.answerCall()
        elif command == "queue":
            center.viewQueue()
        elif command == "logs":
            center.viewCallLogs()
        elif command == "average":
            center.averageWaitTimes()
        elif command == "next":
            center.nextAvailableTimes()
        elif command == "empty":
            print("Queue empty:", center.isQueueEmpty())
        elif command == "quit":
            print("Bye!")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main_loop()
