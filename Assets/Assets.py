break_pattern_45_10 = [
    ("07:30:00", "08:15:00"),
    ("08:25:00", "09:10:00"),
    ("09:20:00", "10:05:00"),
    ("10:20:00", "11:05:00"),
    ("11:15:00", "12:00:00"),
    ("12:10:00", "12:55:00"),
    ("13:05:00", "13:50:00"),
    ("14:00:00", "14:45:00"),
    ("14:55:00", "15:40:00"),
    ("15:50:00", "16:35:00")
]

break_pattern_40_10 = [
    ("07:30:00", "08:10:00"),
    ("08:20:00", "09:00:00"),
    ("09:10:00", "09:50:00"),
    ("10:05:00", "10:45:00"),
    ("10:55:00", "11:35:00"),
    ("11:45:00", "12:25:00"),
    ("12:30:00", "13:10:00"),
    ("13:15:00", "13:55:00"),
    ("14:00:00", "14:40:00"),
    ("14:45:00", "15:25:00")
]

break_pattern_35_10 = [
    ("07:30:00", "08:05:00"),
    ("08:15:00", "08:50:00"),
    ("09:00:00", "09:35:00"),
    ("09:45:00", "10:20:00"),
    ("10:30:00", "11:05:00"),
    ("11:15:00", "11:50:00"),
    ("12:00:00", "12:35:00"),
    ("12:45:00", "13:20:00"),
    ("13:30:00", "14:05:00"),
    ("14:15:00", "14:50:00")
]

break_pattern_35_05 = [
    ('07:30:00', '08:05:00'),
    ('08:10:00', '08:45:00'),
    ('08:50:00', '09:25:00'),
    ('09:30:00', '10:05:00'),
    ('10:10:00', '10:45:00'),
    ('10:50:00', '11:25:00'),
    ('11:30:00', '12:05:00'),
    ('12:10:00', '12:45:00'),
    ('12:50:00', '13:25:00'),
    ('13:30:00', '14:05:00')
]

default_image_locations = "Assets/Images/Default_Icon.png"

default_number_of_lessons = [8, 8, 8, 8, 8]

reminder_activations = ["1 minute", "3 minutes", "5 minutes", "10 minutes", "15 minutes"]

selected_navbar_icons = ["Assets/Images/Home_Icon_Selected.png",
                         "Assets/Images/Backup_Icon_Selected.png",
                         "Assets/Images/File_Generator_Icon_Selected.png",
                         "Assets/Images/Application_Dashboard_Selected.png",
                         "Assets/Images/Settings_Icon_Selected.png"]

deselected_navbar_icons = ["Assets/Images/Home_Icon_Deselected.png",
                           "Assets/Images/Backup_Icon_Deselected.png",
                           "Assets/Images/File_Generator_Icon_Deselected.png",
                           "Assets/Images/Application_Dashboard_Deselected.png",
                           "Assets/Images/Settings_Icon_Deselected.png"]

html_boilerplate = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="CSS/styles.css" />
  </head>
  <body>
    

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
"""

github_link = "https://github.com/robothaver/CCCP"

classroom_link = "https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fclassroom.google.com&passive=true"

ttkbootstrap_link = "https://github.com/israel-dryer/ttkbootstrap"

page_names = ["Home", "Backup Page", "File Generator", "Application Dashboard", "Settings", "Last Used Page"]

browsers = ["chrome", "firefox", "brave", "system default"]

program_description = """
CCCP is a compact program designed for your pendrive, 
packed with powerful features. Launch applications, create backups, 
generate files, set reminders, and much more, all from your portable drive. 
Experience convenience and productivity on the go with CCCP. 
"""

ttkbootstrap_description = """
This program was created with the amazing ttkbootstrap.
Ttkbootstrap is powerful framework which offers a wide array of themes, styles, and components to enhance the 
visual appeal of your tkinter programs.
"""
