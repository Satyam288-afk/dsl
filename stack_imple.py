
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


make_change(document+"vicky bruh")
show_document()
undo()
show_document()
redo()
show_document()
