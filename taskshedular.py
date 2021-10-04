import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(

            title='************* DRINKING WATER*****************',
            message='As you know that a human body make 80 % with water so please drink water',
            timeout=2

        )
        time.sleep(6)