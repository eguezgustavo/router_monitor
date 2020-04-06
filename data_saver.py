from subprocess import Popen, PIPE
import requests
import datetime
import time

router = 'http://192.168.10.1/cgi-bin/monitor/monitor'

while True:
    p = Popen(['fast-speedtest', 'YXNkZmFzZGxmbnNkYWZoYXNkZmhrYWxm'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    output = str(output)

    if 'Speed' in output:
        speed = output.split(' ')[1]
        resp = requests.get(url=router)
        data = resp.json()
        loss = data['loss']
        time_of_ping = data['time']
        day_of_week = datetime.datetime.today().weekday()
    
        print(f'speed: {speed}, loss: {loss}, time: {time_of_ping}, day: {day_of_week}')

        f=open("/Users/eguezgustavo/internet.csv", "a+")
        f.write(f'{speed},{loss},{time_of_ping},{day_of_week}\n')
        f.close()

        time.sleep(5)
