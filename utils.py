import json
import time
import datetime
import argparse


# получение unix timestamp

def get_timestamp():
    dt = datetime.datetime.now()
    unix_time_stamp = time.mktime(dt.timetuple())
    # print(unix_time_stamp)
    return unix_time_stamp

# упаковка сообщения


def pack_msg(msg):
    packed_msg = json.dumps(msg).encode('utf-8')
    return packed_msg

# распаковка сообщения


def load_msg(msg):
    unpacked_msg = json.loads(msg)
    return unpacked_msg

# написание сообщения

def write_message():
    user_message = input('Введите сообщение:  \n\n-->')
    return user_message

# отправка сообщения


def send_message():
    pass

# создание presence message для клиента


def make_pr_msg():
    presence_message = {
        'action': 'presence',
        'time': get_timestamp(),
        'type': 'status',
        'user': {
                'account_name': 'C0deMaver1ck',
                'status': 'Yep, I am here!'
                }
    }
    return presence_message


# Парсер аргументов командной строки для клиента
def create_client_arg_parser():
    parser = argparse.ArgumentParser(
                                    description='Клиент для работы по TCP',
                                    epilog='''Made with deadly ninja skills 
                                    Fork me on github: https://github.com/webn1nja''',
                                    add_help=False
                                    )
    param_group = parser.add_argument_group(title='Параметры')

    param_group.add_argument(
                            '-a',
                            default='127.0.0.1',
                            help='IP - адрес для прослушивания. По умолчанию прослушиваются все адреса',
                            metavar='< addr >'
                            )

    param_group.add_argument(
                            '-p',
                            type=int,
                            default='7777',
                            help='TCP порт. По умолчанию использует порт 7777',
                            metavar='< port >'

                             )

    param_group.add_argument(
                            '-r',
                            action='store_const',
                            const='True',
                            help='Для того, чтобы клиент работал в режиме чтения, поставьте ключ -r',
                            metavar='< read chat >'

                            )

    param_group.add_argument(
                            '-w',
                            action='store_const',
                            const='True',
                            help='Для того, чтобы клиент работал в режиме написания, поставьте ключ -w',
                            metavar='< write to chat >'

                           )

    param_group.add_argument(
                            '-h',
                            action='help',
                            help='Справка',
                            )

    return parser

# Парсер аргументов командной строки для сервера

def create_server_arg_parser():
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
                            help='Справка',
                            )

    return parser


# JIM statuses
status_ok = {
            'response': 200,
            'alert': 'Status is OK'
            }
# -------------