# Программа клиента, запрашивающего текущее время
from socket import *
import sys
import time
import datetime
import json


# получение таймстемпа

dt = datetime.datetime.now()

unix_time_stamp = time.mktime(dt.timetuple())
print(unix_time_stamp)

# json
def presence_msg():
    presence_message = {
        "action": "presence",
        "time": unix_time_stamp,
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
        }
    }
    return json.dumps(presence_message)


presence_msg()


try:
    ip_addr = sys.argv[1]
except IndexError:
    ip_addr = None

try:
    port = sys.argv[2]
except IndexError:
    port = 7777  # порт по умолчанию для подключения к серверу

if ip_addr:
    server_ip_address = ip_addr
else:
    print('\n\nНе задан ip-адрес для подключения к серверу!\nЗавершение работы скрипта')
    sys.exit()

if port:
    server_port_number = port
else:
    print('Не задан порт для подключения к серверу!\n'
          'Подключение к серверу произойдет на порт 7777 (порт по умолчанию)\n'
          'Введите значение порта для подключения через другой')


def connect_to_server(ip, port_num):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    print('Подключение...\nСоздан сокет TCP')
    try:
        s.connect((ip, int(port_num)))  # Соединиться с сервером по адресу и порту
        print('Соединяемся с сервером по адресу:{} и порту:{}'.format(ip, port))
        # отправляем на сервер json data
        pr_msg = presence_msg().encode('ascii')
        print('Посылаем на сервер presence сообщение...\n')
        s.send(pr_msg)
        recieved_data = s.recv(1024)  # Принять не более 1024 байтов данных
        parsed__json_recieved_data = json.loads(recieved_data)
        if parsed__json_recieved_data['response'] == 200:
            print('Получен status 200. Соединение установлено!')
        s.close()

    except ConnectionRefusedError:
        print('Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение')


connect_to_server(server_ip_address, server_port_number)





