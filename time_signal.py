from send2slack import send_msg
import datetime


def time_signal(today, flag, ziho_time, tmp, hum, url):
    today = list([today])
    dt = datetime.datetime.today()
    date = dt.date()
    time = dt.time()
    if date not in today:
        today = set([date])
        flag = True
    dt -= datetime.timedelta(hours=ziho_time)
    
    if time >= dt.time() and flag:
        flag = False
        message = f"Good morning!:power: \ntemperature: {tmp} C, humid: {hum} %"
        send_msg(url, message)
    
    return *today, flag

if __name__ == '__main__':
    today = 1
    flag = True
    today, flag = time_signal(today, flag, 8, 21, 10)
    print(today, flag)
    today, flag = time_signal(today, flag, 8, 22, 12)
    