# import module
import time,os

while True:
    os.system('cls')
    lt=time.localtime()
    # print(time.strftime('%I:%M:%S %p',lt))
    print(time.strftime('%I:%M:%S',lt))
    time.sleep(1)
