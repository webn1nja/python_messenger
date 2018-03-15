from socket import *
import sys
import utils
import select

# создание серверного парсера аргументов командной строки
parser = utils.create_server_arg_parser()
namespace = parser.parse_args(sys.argv[1:])


def read_requests(clients):
    '''
    Чтение запросов из списка клиентов
    '''
    requests = {} # Словарь ответов сервера вида {сокет: запрос}
    for sock in clients:
        print(sock)
        try:
            data = sock.recv(1024)
            parsed_data = utils.load_msg(data)
            requests[sock] = parsed_data

        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))  # ???????
            clients.remove(sock)
        print("REQUESTS IN READ FUNC:",requests)
        print(type(requests))
        return requests


def write_responses(requests, clients):

    '''
    Эхо-ответы сервера клиентам, от которых были запросы
    '''
    print("Clients:",clients)
    print(type(clients))
    print("requests:  ",requests)
    print(type(requests))  #### ПОЧЕМУ-то  Nonetype!!!!
    r = requests
    print(r)
    for sock in clients:
        if sock in r:

            try:
                # подготовить и отправить ответ сервера
                resp = utils.pack_msg(requests[sock])
                test_len = sock.send(resp.upper())
            except:  # окет недоступен - клиент отключился
                print('Клиент {} отключился'.format(sock.getpeername()))
                sock.close()
                clients.remove(sock)


def mainloop():
    '''

    основной цикл обработки запросов клиентов

    '''
    clients = []

    s = socket(AF_INET, SOCK_STREAM)  # создали сокет TCP
    s.bind(('', namespace.p))  # присваивает порт по умолчанию или тот, что установлен
    print('Слушаю порт %s ... \n' % namespace.p)
    s.listen(5)
    s.settimeout(0.2) # таймаут для операций с сокетом
    print('\nСервер запущен...\n')
    while True:
        try:
            client, addr = s.accept()  # принять запрос на соединение
        except OSError as e:
            pass
        else:
            print('Получен запрос на соединение от %s' % str(addr))
            clients.append(client) # объявляем новое подключение в список clients
        finally:
            # Проверяем наличие событий ввода-вывода с помощью  select
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass   # ничего не делать, если клиент отключился
        # print('r',r)
        # print('w', w)
        req = read_requests(r)  # сохраняем запросы клиентов
        # print("REQUESTS IN THE BOTTOM:", req)
        # print(type(req))
        write_responses(req, w)  # выполним отправку ответов клиентам

                    # print("FINAL REQ", requests)
                    # try:
                    #     _ =(z for z in requests)
                    #     print('ITER!!!!!!!!')
                    # except:
                    #
                    #     print('NOT ITER')
#




mainloop()








#
# print('\nСервер запущен...\n')
#
# s = socket(AF_INET, SOCK_STREAM)      # создали сокет TCP
# s.bind(('', namespace.p))         # присваивает порт по умолчанию или тот, что установлен
# print('Слушаю порт %s ... \n' % namespace.p)
# s.listen(5)
#
#
# while True:
#     client, addr = s.accept()  # принять запрос на соединение
#     print('Получен запрорс на соединение от %s' % str(addr))
#     data = client.recv(1024)
#
#     parsed_json_data = json.loads(data)
#
#     #  если принятое сообщение содержит precense, то отправляем статус 200 на клиент
#
#     if parsed_json_data['action'] == 'presence':
#         print('Получено presence сообщение...\n')
#         client.send(json.dumps(utils.status_ok).encode('utf-8'))
#
#     client.close()
#
#
