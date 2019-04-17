# Raspberry Kit support
Welcome to Raspberry Kit support page. Here you can download all files necessary for our Kit completion.   
Also the source code for every chapter is provided.   

![Image](/docs/images/title.png)   

## Setup
If you've got no spare monitor or keyboard you may connect Raspberry Pi via SSH, VNC and FTP protocols.
Full instruction is provided starting on page 56 of the book. Here are all third party programms you need for that.

## # For Windows
- [Angry IP Scanner](http://github.com)
- [Putty](http://github.com)
- [VNC-Viewer](http://github.com)
- [FileZilla](http://github.com)
## # For MacOS
- [Angry IP Scanner](http://github.com)
- [VNC-Viewer](http://github.com)
- [FileZilla](http://github.com)

## Wi-Fi

Connect to Raspberry Pi via SSH.

Open the Wi-Fi configuration file using the built in text editor "Nano"   
In order to do this, enter the following line:   
```python
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
And hit Enter.

The file will open. Add your network parameters as follows:
```python
network={
    ssid="your wi-fi name"
    psk="your wi-fi password"
}
```

Close the file using keyboard shortcut ctrl+X (cmd+X for Mac OS). Nano will ask if you want to save the changes.    
Press Y (Yes), then Enter.    
Reboot the system via command `sudo reboot`

```python
sudo reboot
```

After the reboot, disconnect the Ethernet cable and now you can control your Raspberry Pi via Wi-Fi.

## 3. BLINK

When Thonny Python IDE is opened for the first time the main menu is usually hidden.    
In order to make it visible, press the link in the right corner: 

![Image](/docs/images/p25-1.png)   

Confirm changes:

![Image](/docs/images/p25-2.png)   

Then Thonny reboots and you get the full interface:

![Image](/docs/images/p25-3.png) 

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

i = 0
while (i < 5):
    i = i + 1
    time.sleep(0.5)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17, GPIO.LOW)

GPIO.cleanup()
```

## 4. BUTTON

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

while (True):
    time.sleep(0.5)
    button = GPIO.input(2)
    print(button)
```

Transfer the `button` variable to the `output` function to control the LED.

```python
while (True):
	button = GPIO.input(2)
	GPIO.output(24, button)
```

Don't forget to add the pin initialization code for the output:

```python
GPIO.setup(24, GPIO.OUT)
```

## 5. CONDITIONAL EXPRESSIONS

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

while (True):
    button = GPIO.input(8)
    if (button == False):
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
    else:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)
```

## 6. CONTROLLING THE LEDS

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
dutyCycle = 50
pwm.start(dutyCycle)

while (True):
    time.sleep(0.01)
    dutyCycle = dutyCycle + 1
    if (dutyCycle > 100):
        dutyCycle = 0
        pwm.ChangeDutyCycle(dutyCycle)
```

## 7. LIGHT CONTROL PANELS

```python
import RPi.GPIO as GPIO

def isPressed(btn, led):
    if (GPIO.input(btn) == False):
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)

button1 = 3
button2 = 4
led1 = 14
led2 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

while (True):
    isPressed(button1, led1)
    isPressed(button2, led2)
```

## 8. MASSIVE OPTIMIZATION
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [12, 13, 14, 18]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)

time.sleep(3)

for led in leds:
    GPIO.output(led, GPIO.LOW)

GPIO.cleanup()
```

```python
import RPi.GPIO as GPIO

def isPressed(btn, led):
    state = 1-GPIO.input(btn)
    GPIO.output(led, state)
    
leds = [12, 13, 14, 18]
buttons = [2, 3, 4, 8]

GPIO.setmode(GPIO.BCM)
for i in range(4):
    print(i, leds[i], buttons[i])
    GPIO.setup(leds[i], GPIO.OUT)
    GPIO.output(buttons[i], GPIO.IN)
    
while (True):
    for i in range(4):
        isPressed(buttons[i], leds[i])
```
## 9. MAKING A SERVER
```python simpleServer.py>
from flask import Flask
app = Flask('simpleServer')

@app.route('/')
def index():
    return 'Hello Amperka'

app.run(debug=True, port=3000, host='0.0.0.0')
```
## 10. LANDING PAGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Web-server archive link bellow: 
```
http://amperka.github.io/raspberry_support/docs/web-server.zip
```

```python
from flask import Flask, send_file

app = Flask('landingPage')

@app.route('/')
def index():
	return send_file('landing.html')

@app.route('/images/<filename>')
def get_image(filename):
	return send_file('images/'+filename)

app.run(debug=True, port=3000, host='0.0.0.0')
```
По умолчанию Thonny Python IDE настроено на открытие только Python файлов
{{ :malina:4.png?nolink |}}
Чтобы увидеть все файлы в директории нужно выбрать пункт ''all files''в выпадающем списке
{{ :malina:5.png?nolink |}}
Теперь можно выбрать необходимые файлы
{{ :malina:6.png?nolink |}}
Если при перезапуске сервера консоль ответит сообщением «socket.error: [Errno 48] Address already in use», набери команду
```
ps -fA | grep python
```
В консоль выведется список запущенных процессов. Найди строку с файлом landing.py. Во второй колонке будет указан номер процесса. Отключи его командой
```
kill -9 xxx
```
Где xxx — номер процесса. Команда kill «убивает» процесс, иногда это называют «убить девяткой».

Запусти сервер заново.
## 11. Интернет свет 
```python light.py>
from flask import Flask, send_file
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led = 18
GPIO.setup(led, GPIO.OUT)

app = Flask('lightControl')

@app.route('/')
def index():
    return send_file('light.html')

@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/'+filename)

@app.route('/turnOn')
def turnOn():
    GPIO.output(led, GPIO.HIGH)
    return 'turnedOn'

@app.route('/turnOff')
def turnOff():
    GPIO.output(led, GPIO.LOW)
    return 'turnedOff'

app.run(debug=True, port=3000, host='0.0.0.0')
```
## 12. Обратная связь 
```
sudo pip3 install flask-socketio eventlet
```
```python feedback.py>
from flask import Flask, send_file
from flask_socketio import SocketIO
import RPi.GPIO as GPIO

app = Flask('feedback')
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)
btn = 2
GPIO.setup(btn, GPIO.IN)

@app.route('/')
def index():
	return send_file('feedback.html')

@app.route('/images/<filename>')
def get_image(filename):
	return send_file('images/'+filename)

@socketio.on('isPressed')
def checkButton(receivedData):
	if (GPIO.input(btn) == False):
		socketio.emit('button', 'pressed')
	else:
		socketio.emit('button', 'released')

socketio.run(app, port=3000, host='0.0.0.0', debug=True)
```
Запусти сервер командой
```
python3 feedback.py
```
## 13. Погодный фиджет 

```python fydget.py>
import requests, json
from pprint import pprint
 
url = 'http://api.openweathermap.org/data/2.5/forecast'
 
payload = {
	'lat': 'широта_твоего_города',
	'lon': 'долгота_твоего_города',
	'units': 'metric',
	'appid': 'твой_ключ'
}
 
res = requests.get(url, params=payload)
data = json.loads(res.text)
weather = data['list'][0]

def pars_weather(weatherType, timeRange, measurementUnits):
    if (weatherType in weather) and (timeRange in weather[a].keys()):
        print weatherType, ': ', weather[weatherType][timeRange], c
    else:
        print weatherType, ': ', 'none'

pars_weather('clouds', 'all', '%')
pars_weather('rain', '3h', 'mm')
pars_weather('snow', '3h', 'mm')

print 'temp:', weather['main']['temp'], 'C'
```

Наш вариант погодного фиджета:
```
amperka.github.io/malina_support/weather.py
```
## 14. Бот ВКонтакте 

```python vk.py>
# -*- coding: utf-8 -*-
import time
import vk_api

from socket import gethostbyname
 
vk = vk_api.VkApi(token = 'твой токен')
 
param = {
    'count' : 1,
    'time_offset' : 5,
    'filter' : 'unread'
}

def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id':random,
    })
while True:
    response = vk.method('messages.getConversations', param)
    if response['items']:
        item = response['items'][0]
        last_mess = item['last_message']
        random = last_mess['random_id']
        my_id = last_mess['peer_id']
        text = last_mess['text']
        write_msg(my_id, text, random)    
    time.sleep(1)
```


## 17. Кинотеатр 
```
amperka.github.io/malina_support/omx-web.zip
```
## 18. Поставь торрент заранее 

```python deluge_vk.py>
# -*- coding: utf-8 -*-
import time
import vk_api

from deluge_client import DelugeRPCClient
from pprint import pprint
 
vk = vk_api.VkApi(token = 'твой токен')


values = {
    'count' : 1,
    'offset' : 0,
    'filter' : 'unread'
}
 
client = DelugeRPCClient(
    '127.0.0.1',
    58846,
    'pi',
    'raspberry'
)
 
client.connect()
 
def write_msg(user_id, msg , random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id':random,
    })
 
while True:
    response = vk.method('messages.getConversations', values)
    if response['items']:
        item = response['items'][0]
        last_mess = item['last_message']
        random = last_mess['random_id']
        my_id = last_mess['peer_id']
        text = last_mess['text'] 
        client.call('core.add_torrent_url', text, {'move_completed_path' : '/home/pi/Torrents'})
        write_msg(my_id, u'Download is begin!', random)
    time.sleep(1)
```
## Включить все светодиоды на Облаке 
```python
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
leds = [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]
 
for led in leds:
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, GPIO.HIGH)
 
time.sleep(3)
 
for led in leds:
	GPIO.output(led, GPIO.LOW)
 
GPIO.cleanup()
```
