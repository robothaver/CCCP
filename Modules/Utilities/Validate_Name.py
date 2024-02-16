from tkinter import messagebox


class ValidateName:
    def __init__(self, string):
        self.string = string
        self.is_valid = self.validate_name()

    def contains_special_char(self):
        exceptions = [" ", "_", "-"]
        for char in self.string:
            if not char.isalnum() and char not in exceptions:
                return True
        return False

    def validate_name(self):
        is_valid = False
        if self.string != "":
            if not self.contains_special_char():
                if len(self.string) < 25:
                    is_valid = True
                else:
                    messagebox.showwarning(title="Warning", message="Name too long! 25 letters max")
            else:
                is_valid = False
                messagebox.showwarning(title="Warning", message="Name can't contain special characters!")
        else:
            messagebox.showwarning(title="Warning", message="You must input a name!")
        return is_valid
