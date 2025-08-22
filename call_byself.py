from collections import deque

class call_pick:
    def __init__(self):
        self.queue = deque()

    def add_call(self, name, time):
        self.queue.append((name, time))
        print(f"added a name: {name} with a time {time} min.")

    def view_queue(self):
        if not self.queue:
            print("queue is empty")
        else:
            print("current queue")
            count = 1
            for call in self.queue:
                name = call[0]
                time = call[1]
                print(f"{count}. {name} - {time} minutes")
                count += 1

    def answer_call(self):
        if not self.queue:
            print("queue is empty")
        else:
            call = self.queue.popleft()
            print(f"Answered call from {call[0]} with time {call[1]} minutes.")

    def is_empty(self):
        return len(self.queue) == 0


def main():
    cp = call_pick()
    while True:
        cmd = input("Enter command (add/view/answer/quit): ").lower()
        if cmd == "add":
            name = input("Name: ")
            time = int(input("Call time (min): "))
            cp.add_call(name, time)
        elif cmd == "view":
            cp.view_queue()
        elif cmd == "answer":
            cp.answer_call()
        elif cmd == "quit":
            print("Bye!")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
