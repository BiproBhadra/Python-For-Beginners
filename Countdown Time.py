import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)  #The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(10)
