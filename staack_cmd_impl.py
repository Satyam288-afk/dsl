document = ""
undo_stack = []
redo_stack = []
original_document = ""

def make_change(new_text):
    global document, undo_stack, redo_stack
    undo_stack.append(document)
    redo_stack.clear()
    document = new_text

def undo():
    global document, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
    else:
        print("Nothing to undo.")

def redo():
    global document, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
    else:
        print("Nothing to redo.")

def save():
    global original_document, document
    original_document = document
    print("Document saved.")

def revert_to_original():
    global document, undo_stack, redo_stack, original_document
    undo_stack.append(document)
    document = original_document
    redo_stack.clear()
    print("Reverted to original document.")

def show_undo_history():
    print("Undo History (oldest to latest):")
    for i, state in enumerate(undo_stack):
        print(f"{i+1}: {repr(state)}")

def show_redo_history():
    print("Redo History (oldest to latest):")
    for i, state in enumerate(redo_stack):
        print(f"{i+1}: {repr(state)}")

def show_document():
    print(f"Current Document: {repr(document)}")

# --- Command Loop ---
def main():
    print("Simple Document Editor")
    print("Commands: show, undo, redo, save, revert, undo_history, redo_history, change <your text>, quit")
    
    while True:
        command = input(">> ").strip()

        if command == "show":
            show_document()
        elif command == "undo":
            undo()
        elif command == "redo":
            redo()
        elif command == "save":
            save()
        elif command == "revert":
            revert_to_original()
        elif command == "undo_history":
            show_undo_history()
        elif command == "redo_history":
            show_redo_history()
        elif command.startswith("change "):
            new_text = command[7:].strip()
            make_change(new_text)
        elif command == "quit":
            print("Exiting.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
