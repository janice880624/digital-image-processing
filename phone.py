from time import sleep
import os

def test_call(numb1):
    call = os.popen('adb shell am start -a android.intent.action.CALL -d tel:{}'.format(number1))
    sleep(20)

    Hangup = os.popen('adb shell input keyevent 26')
    sleep(2)


number1 = 10010

test_call(num1)


