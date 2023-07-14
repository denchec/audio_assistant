import re
from threading import Thread
from time import sleep

import playsound
import schedule as schedule


class AlarmClock:
    def __init__(self, message: list):
        self.message = message

    def execute(self):
        # alarm_time = '00:25'
        alarm_time = self.get_alarm_time()
        schedule.every().day.at(alarm_time).do(self.time_to_get_up)
        Thread(target=schedule_checker).start()

    @staticmethod
    def time_to_get_up():
        playsound.playsound('mp3/mojj_rok_n_roll.mp3')

    def get_alarm_time(self):
        alarm_time = self.message[-1]

        if len(alarm_time) == 5:
            return alarm_time

        return '0' + alarm_time

    # def get_alarm_time(self):
    #     hours = re.search(r"(\S+)\s+(?:часов|час|часа)\b", self.message).group(1)
    #     minutes = re.search(r"(\S+)\s+(?:минут|минута|минуты)\b", self.message).group(1)
    #
    #     alarm_time = f'{hours}:{minutes}'
    #
    #     if len(alarm_time) == 5:
    #         return alarm_time
    #
    #     return '0' + alarm_time


def schedule_checker():
    """Check schedule every second"""
    while True:
        schedule.run_pending()
        sleep(1)
