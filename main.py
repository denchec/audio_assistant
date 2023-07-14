from assistant_functions.alarm_clock import AlarmClock
from get_command import recognize_voice_message


def main():
    message = recognize_voice_message().split(' ')
    command = message[0]

    if command == 'будильник':
        """
        Голосовое сообщение должно быть следующего формата:
        "Будильник на 7 часов/час 27 минут/минута/минуты"
        """
        print(message)
        AlarmClock(message).execute()

    print(message)


if __name__ == '__main__':
    main()
