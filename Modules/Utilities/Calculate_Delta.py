from datetime import datetime
from Modules.Configfile.Config import Configfile


class CalculateDelta:
    def __init__(self):
        self.day_of_week = 0
        self.time_left = 0
        self.lesson_index = None
        self.is_lesson_over = False
        self.time_delta = 0
        self.progress = 0
        self.current_time = None

    def check_end_time(self, current_time):
        self.current_time = current_time
        self.day_of_week = datetime.today().weekday()

        if self.lesson_index is None:
            self.lesson_index = self.get_current_lesson()

        current_end_time = datetime.strptime(Configfile.current_break_pattern[self.lesson_index][1], "%H:%M:%S")
        current_start_time = datetime.strptime(Configfile.current_break_pattern[self.lesson_index][0], "%H:%M:%S")

        if self.day_of_week > 4 or Configfile.number_of_lessons_today == 0:
            # If it is the weekend
            self.set_as_break_and_try_get_lesson()
        elif current_time > current_end_time and self.lesson_index == Configfile.number_of_lessons_today - 1:
            # The last lesson is over
            self.set_as_break_and_try_get_lesson()
        elif current_time < current_start_time:
            # If the day hasn't begun yet
            self.set_as_break_and_try_get_lesson()
        elif current_time > current_end_time:
            # The lesson is over and it is currently break time
            next_class_start_time = datetime.strptime(Configfile.current_break_pattern[self.lesson_index + 1][0], "%H:%M:%S")
            self.is_lesson_over = True
            self.time_delta = next_class_start_time - current_time
            self.time_left = self.format_time_minutes_and_seconds(self.time_delta)
            time_difference = next_class_start_time - current_end_time
            self.progress = ((time_difference.seconds - self.time_delta.seconds) / time_difference.seconds) * 100
            self.try_get_next_lesson()
        else:
            # If the lesson is still going
            self.is_lesson_over = False
            self.time_delta = current_end_time - current_time
            self.time_left = self.format_time_minutes_and_seconds(self.time_delta)
            time_difference = current_end_time - current_start_time
            self.progress = ((time_difference.seconds - self.time_delta.seconds) / time_difference.seconds) * 100
            self.try_get_next_lesson()

    def set_as_break_and_try_get_lesson(self):
        self.is_lesson_over = True
        self.time_delta = 0
        self.lesson_index = self.get_current_lesson()

    def try_get_next_lesson(self):
        if self.time_delta.seconds == 0:
            self.lesson_index = self.get_current_lesson()

    def update_state(self, current_time):
        self.current_time = current_time
        self.lesson_index = self.get_current_lesson()

    def get_current_lesson(self):
        lesson_index = 0
        for i in range(Configfile.number_of_lessons_today):
            lesson_start = datetime.strptime(Configfile.current_break_pattern[i][0], "%H:%M:%S")
            if lesson_start <= self.current_time:
                lesson_index = i
        return lesson_index

    @staticmethod
    def format_time_minutes_and_seconds(delta):
        return str(delta)[:0] + str(delta)[2:]
