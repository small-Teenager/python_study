import time
import urllib.request
import schedule

response = urllib.request.urlopen('https://baidu.com')


# print(response.read().decode('utf-8'))


def job():
    print("I'm working... in job1  start")


time.sleep(10)
print("I'm working... in job1  end")


def job2():
    print("I'm working... in job2")


time.sleep(1)
