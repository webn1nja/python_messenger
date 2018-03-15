# программа клиента, запрашивающего текущее время

from socket import *
import sys
import utils


# создание клиентского парсера аргументов командной строки
parser = utils.create_client_arg_parser()
namespace = parser.parse_args(sys.argv[1:])
# print(namespace)

def connect_to_server(ip, port_num):
    s = socket(AF_INET, SOCK_STREAM)  # создали сокет TCP
    print('Подключение...\n Создан сокет TCP')
    try:
        s.connect((ip, port_num))  # соединиться с сервером по адресу и порту
        print('Соединяемся с сервером по адресу: {} и порту: {}'.format(ip, port_num))
        # отправляем на сервер presence сообщение в формате json
        pr_msg = utils.pack_msg(utils.make_pr_msg())
        print('Посылаем на сервер presence сообщение...\n')
        print(pr_msg)
        s.send(pr_msg)
        # принимаем ответ от сервера
        recieved_data = s.recv(1024) # принимаем не более 1024 байт данных
        parsed_json_recieved_data = utils.load_msg(recieved_data)
        if parsed_json_recieved_data['response'] == 200:
            print('Получен status 200. Соединение установлено!')

        return 1
        # s.close()     # адо закрывать или нет?
        pass
    except ConnectionRefusedError:
        print('Подключение не установлено, т.к конечный компьютер отверг запрос на подключение')


if not (namespace.r or namespace.w):
    print("Укажите режим работы клиента с помощью флагов -w или -r")
    print("Завершение клиента...")
    sys.exit()

else:
    print("Клиент начинает работу...")
    connect_status = connect_to_server(namespace.a, namespace.p)
    print(connect_to_server(namespace.a, namespace.p))
    if connect_status:
        #  enter message func
        utils.write_message()

