from datetime import datetime
import time
from Modules.Configfile.Config import Configfile


class CalculateDelta:
    def __init__(self):
        # This class calculates out the delta between the current time and the end of the lesson or break

        # Defining variables
        self.config = Configfile()
        self.is_lesson_over = False
        self.class_number = 0
        self.break_time_delta = ""
        self.end_time = 0
        self.current_time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")

    def check_end_time(self):
        # This function find which lesson is happening currently
        # If there is no lesson it will set is_lesson_over to True
        # Get current time
        self.current_time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")

        # Find the current lesson
        for x, start_time in enumerate(self.config.break_pattern):
            if datetime.strptime(start_time[0], "%H:%M:%S") <= self.current_time <= \
                    datetime.strptime(start_time[1], "%H:%M:%S"):
                # If class is now
                self.is_lesson_over = False
                self.end_time = datetime.strptime(start_time[1], "%H:%M:%S")
            if datetime.strptime(start_time[0], "%H:%M:%S") <= self.current_time:
                # Get the class number
                self.class_number = x + 1
        try:
            if self.end_time < self.current_time:
                # If the lesson is over
                self.is_lesson_over = True
        except TypeError:
            self.is_lesson_over = True
        return self.end_time

    def time_difference(self):
        self.end_time = self.check_end_time()
        if not self.is_lesson_over:
            # If the lesson is not over, calculate the delta
            delta = self.end_time - self.current_time
            # Time difference in seconds (in string from for the end of lesson timer label)
            delta_string = str(delta)[:0] + str(delta)[2:]
            return delta, delta_string

    def break_time_difference(self):
        # This function calculates out how much time is left of the break
        if not self.class_number == 8 or 0:
            # If the class is not 0 or 8
            break_time_difference_var = \
                datetime.strptime(self.config.break_pattern[self.class_number - 1][1], "%H:%M:%S") - self.current_time
            self.break_time_delta = str(break_time_difference_var)[:0] + str(break_time_difference_var)[2:]

    def check_if_lesson_is_over(self):
        self.check_end_time()
        self.break_time_difference()
        return self.is_lesson_over, self.class_number, self.break_time_delta
