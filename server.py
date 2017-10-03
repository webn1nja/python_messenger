from socket import *
import sys
import argparse
import json

# SERVER
# command line arguments parser below


def createParser():
    parser = argparse.ArgumentParser(
                                     description='Сервер для работы по TCP',
                                     epilog='''Made with deadly ninja skills 
                                      Fork me on github: https://github.com/webn1nja''',
                                     add_help=False
                                     )
    param_group = parser.add_argument_group(title='Параметры')
    param_group.add_argument(
                             '-p',
                             type=int,
                             default='7777',
                             help='TCP порт. По умолчанию использует порт 7777',
                             metavar='< port >'
                            )
    param_group.add_argument(
                             '-a',
                             default='',
                             help='IP - адрес для прослушивания. По умолчанию прослушиваются все адреса',
                             metavar='< addr >'
                            )
    param_group.add_argument(
                             '-h',
                             action='help',
                             help='Справка'
                            )

    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])



print('\nСервер запущен...\n')
s = socket(AF_INET, SOCK_STREAM)  # создает сокет TCP
s.bind(('', namespace.p))  # присваивает порт по умолчанию или тот, что установлен
print('Слушаю порт %s ...\n' % namespace.p)
s.listen(5)

status_ok = {
            "response": 200,
            "alert": "Status is OK"
        }


while True:
    client, addr = s.accept()  # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(addr))
    data = client.recv(1024)

    parsed_json_data = json.loads(data)

    # если принятое сообщение содержит precense - отправляем статус 200 на клиент
    if parsed_json_data['action'] == 'presence':
        print('Получено presence сообщение...\n')
        client.send(json.dumps(status_ok).encode('ascii'))

    client.close()


