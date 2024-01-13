from datetime import datetime, timedelta
import time
from Modules.Configfile.Config import Configfile


class CalculateDelta:
    def __init__(self):
        # This class calculates out the delta between the current time and the end of the lesson or break

        # Defining variables
        self.config = None
        self.time_left = 0
        self.class_number = 0
        self.is_lesson_over = False
        self.time_delta = 0
        self.progress = 0

    def check_end_time(self, config, current_time):
        # This function find which lesson is happening currently
        # If there is no lesson it will set is_lesson_over to True

        self.config = config
        # Get current time
        # current_time = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")

        self.class_number = self.get_class_number(current_time)

        current_end_time = datetime.strptime(self.config.break_pattern[self.class_number][1], "%H:%M:%S")
        current_start_time = datetime.strptime(self.config.break_pattern[self.class_number][0], "%H:%M:%S")
        if current_time > current_end_time and self.class_number == self.config.number_of_lessons_today - 1:
            # The last lessons are over
            self.is_lesson_over = True
        elif current_time < current_start_time:
            # If the day hasn't begun yet
            self.is_lesson_over = True
        elif current_time > current_end_time:
            # The lesson is over and it is currently break time
            next_class_start_time = datetime.strptime(self.config.break_pattern[self.class_number + 1][0], "%H:%M:%S")
            self.is_lesson_over = True
            self.time_delta = next_class_start_time - current_time
            self.time_left = self.format_time_minutes_and_seconds(self.time_delta)
            time_difference = next_class_start_time - current_end_time
            self.progress = ((time_difference.seconds - self.time_delta.seconds) / time_difference.seconds) * 100
        else:
            # If the lesson is still going
            self.is_lesson_over = False
            self.time_delta = current_end_time - current_time
            self.time_left = self.format_time_minutes_and_seconds(self.time_delta)
            time_difference = current_end_time - current_start_time
            self.progress = ((time_difference.seconds - self.time_delta.seconds) / time_difference.seconds) * 100

    def get_class_number(self, current_time):
        class_number = 0
        for i in range(self.config.number_of_lessons_today):
            if datetime.strptime(self.config.break_pattern[i][0], "%H:%M:%S") <= current_time:
                # Get the class number
                class_number = i
        return class_number

    @staticmethod
    def format_time_minutes_and_seconds(delta):
        return str(delta)[:0] + str(delta)[2:]
