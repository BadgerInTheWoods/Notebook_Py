import os
from datetime import datetime


class Notebook:
    FileName = "notes.txt"

    def __init__(self, file_name=FileName):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r+") as file:
                return file.readlines()
        else:
            return []

    def save_notes(self):
        with open(self.file_name, "w") as file:
            for note in self.notes:
                file.write(note)
            file.close()

    def add_note(self):
        self.notes.append(input("Введите заголовок заметки: ") + ":" + " " +
                          input("Введите текст заметки: ") + " " +
                          datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        self.save_notes()
        print("Note added successfully!")

    def delete_note(self):
        try:
            note_index = int(input("Enter the index of the note to delete: ")) - 1
            del self.notes[note_index]
            self.save_notes()
            print("Note deleted successfully!")
        except ValueError:
            print("Invalid note index!")

    def edit_note(self):
        try:
            note_index = int(input("Enter the index of the note to edit: ")) - 1
            self.notes[note_index] = (input("Введите новый заголовок заметки: ") + ":" + " " +
                                      input("Введите новый текст заметки: ") + " " +
                                      datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            self.save_notes()
            print("redacted successfully")
        except ValueError:
            print("Invalid note index!")

    def display_notes(self):
        if self.notes:
            print("Your Notes:")
            for i, note in enumerate(self.notes):
                print(f"{i + 1}. {note}")
        else:
            print("No notes available.")
