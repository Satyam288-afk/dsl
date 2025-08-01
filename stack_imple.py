from datetime import datetime

document = ""
undo_stack = []
redo_stack = []
original_document = ""
MAX_HISTORY = 20

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def make_change(new_text):
    global document, undo_stack, redo_stack
    
    undo_stack.append((document, timestamp()))
    if len(undo_stack) > MAX_HISTORY:
        undo_stack.pop(0)
    
    redo_stack.clear()
    document = new_text
    print(f"Changed document at {timestamp()}.")

def undo():
    global document, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append((document, timestamp()))
        if len(redo_stack) > MAX_HISTORY:
            redo_stack.pop(0)
        document, ts = undo_stack.pop()
        print(f"Undo: reverted to state from {ts}")
    else:
        print("Nothing to undo.")

def redo():
    global document, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append((document, timestamp()))
        if len(undo_stack) > MAX_HISTORY:
            undo_stack.pop(0)
        document, ts = redo_stack.pop()
        print(f"Redo: moved forward to state from {ts}")
    else:
        print("Nothing to redo.")

def save():
    global original_document, document
    original_document = document
    print("Document saved.")

def revert_to_original():
    global document, undo_stack, redo_stack, original_document
    undo_stack.append((document, timestamp()))
    if len(undo_stack) > MAX_HISTORY:
        undo_stack.pop(0)
    document = original_document
    redo_stack.clear()
    print("Reverted to original document.")

def show_undo_history():
    print("Undo History (oldest to latest):")
    for i, (state, ts) in enumerate(undo_stack):
        print(f"{i+1}: [{ts}] {repr(state)}")

def show_redo_history():
    print("Redo History (oldest to latest):")
    for i, (state, ts) in enumerate(redo_stack):
        print(f"{i+1}: [{ts}] {repr(state)}")

def show_document():
    print(f"\nCurrent Document: {repr(document)}\n")

def main_loop():
    print("Simple Text Editor with Undo/Redo")
    print("Commands: update, undo, redo, save, revert, show, history, quit\n")
    
    while True:
        cmd = input("Enter command: ").strip().lower()
        
        if cmd == "update":
            new_text = input("Enter new document text: ")
            make_change(new_text)
        
        elif cmd == "undo":
            undo()
        
        elif cmd == "redo":
            redo()
        
        elif cmd == "save":
            save()
        
        elif cmd == "revert":
            revert_to_original()
        
        elif cmd == "show":
            show_document()
        
        elif cmd == "history":
            print("--- Undo History ---")
            show_undo_history()
            print("--- Redo History ---")
            show_redo_history()
        
        elif cmd == "quit":
            print("Exiting editor.")
            break
        
        else:
            print("Unknown command. Try: update, undo, redo, save, revert, show, history, quit.")

if __name__ == "__main__":
    main_loop()
