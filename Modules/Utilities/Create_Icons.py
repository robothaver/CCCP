from tkinter import messagebox
from PIL import Image
import PIL


class CreateIcon:
    def __init__(self, image_location, index):
        # This class gets called by the ChangeSettingsForButton class
        try:
            # If the image is found open and resize
            image = Image.open(image_location)
            image.thumbnail(size=(100, 100))
            # Save to Icon folder with the name of the button
            image.save(f"Icons/button{index}_icon.png")
        except FileNotFoundError:
            # If the image is not found
            messagebox.showerror(title="Error", message="Image not found!")
            image = Image.open("Assets/Images/Default_Icon.png")
            # Save and set the default image for button
            image.save(f"Icons/button{index}_icon.png")
        except PIL.UnidentifiedImageError:
            # If the file is not an image
            messagebox.showerror(title="Error", message="Invalid img file selected!")
            image = Image.open("Assets/Images/Default_Icon.png")
            # Save and set the default image for button
            image.save(f"Icons/button{index}_icon.png")
