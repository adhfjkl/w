import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time is up!')

def focus_timer():
    print("欢迎使用专注时钟！")
    print("请输入专注时长（以分钟为单位）：")
    try:
        time_input = int(input())
        countdown(time_input * 60)
    except ValueError:
        print("输入无效，请输入一个整数。")

focus_timer()
