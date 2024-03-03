from NoteBook.Notebook import Notebook


def run():
    notebook = Notebook()

    while True:
        print("\nNotebook Menu:")
        print("print 'add' - to add note")
        print("print 'delete' - to delete a note")
        print("print 'edit' - to edit a note")
        print("print 'view' - to view all notes")
        print("print 'exit' - to exit")

        choice = input("Enter your choice: ")
        print()

        if choice == "add":
            notebook.add_note()
        elif choice == "delete":
            notebook.delete_note()
        elif choice == "edit":
            notebook.edit_note()
        elif choice == "view":
            notebook.display_notes()
        elif choice == "exit":
            print("Exiting...")
            notebook.save_notes()
            return
        else:
            print("Invalid choice! Please try again.")
