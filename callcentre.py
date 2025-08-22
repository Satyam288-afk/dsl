from collections import deque

class Call:
    def __init__(self, customer_id, call_time):
        self.customer_id = customer_id
        self.call_time = call_time

    def __repr__(self):
        return f"[Customer: {self.customer_id}, Time: {self.call_time}min]"


class Operator:
    def __init__(self, operator_id):
        self.operator_id = operator_id
        self.queue = deque()
        self.total_time = 0
        self.call_log = []

    def add_call(self, call):
        self.queue.append(call)
        self.total_time += call.call_time

    def answer_call(self):
        if self.queue:
            call = self.queue.popleft()
            self.total_time -= call.call_time
            self.call_log.append(call)
            return call
        return None

    def average_wait_time(self):
        return self.total_time / len(self.queue) if self.queue else 0

    def is_empty(self):
        return not self.queue

    def next_available_time(self):
        return self.total_time

    def queue_snapshot(self):
        return list(self.queue)

    def call_history(self):
        return self.call_log

    def __repr__(self):
        return f"Operator {self.operator_id}"


class CallCenter:
    def __init__(self, num_operators):
        self.operators = [Operator(i + 1) for i in range(num_operators)]

    def addCall(self, customer_id, call_time):
        new_call = Call(customer_id, call_time)
        selected_operator = min(self.operators, key=lambda op: op.total_time)
        selected_operator.add_call(new_call)
        print(f"Call {new_call} assigned to Operator {selected_operator.operator_id}")

    def answerCall(self):
        for operator in self.operators:
            if not operator.is_empty():
                call = operator.answer_call()
                print(f"Operator {operator.operator_id} answered call {call}")
                return
        print("No calls to answer at the moment.")

    def viewQueue(self):
        print("\n--- Current Call Queues ---")
        for operator in self.operators:
            queue = operator.queue_snapshot()
            print(f"Operator {operator.operator_id}: {queue if queue else 'No calls'}")

    def isQueueEmpty(self):
        return all(operator.is_empty() for operator in self.operators)

    def viewCallLogs(self):
        print("\n--- Call Logs ---")
        for operator in self.operators:
            logs = operator.call_history()
            print(f"Operator {operator.operator_id}: {logs if logs else 'No calls answered yet'}")

    def averageWaitTimes(self):
        print("\n--- Average Wait Times ---")
        for operator in self.operators:
            avg_time = operator.average_wait_time()
            print(f"Operator {operator.operator_id}: {avg_time:.2f} minutes")

    def nextAvailableTimes(self):
        print("\n--- Next Available Operator Times ---")
        for operator in self.operators:
            time_remaining = operator.next_available_time()
            print(f"Operator {operator.operator_id}: Free in {time_remaining} minutes")


def main_loop():
    center = CallCenter(num_operators=3)
    print("📞 Welcome to the Call Center Simulation!")
    print("Available commands:")
    print("add [customerID] [callTime]")
    print("answer")
    print("queue")
    print("logs")
    print("average")
    print("next")
    print("empty")
    print("quit")

    while True:
        command = input("\n> ").strip().lower()

        if command.startswith("add"):
            parts = command.split()
            if len(parts) != 3:
                print("Usage: add [customerID] [callTime]")
            else:
                customer_id = parts[1]
                try:
                    call_time = int(parts[2])
                    center.addCall(customer_id, call_time)
                except ValueError:
                    print("Call time must be a number.")
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
            print("Exiting simulation. Goodbye!")
            break
        else:
            print("Unknown command. Try: add, answer, queue, logs, average, next, empty, quit.")


if __name__ == "__main__":
    main_loop()
