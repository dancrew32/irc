import collections
import socket
import base64
import re

RE_MESSAGE = re.compile(
    '^(?:@([^\r\n ]*) +|())(?::([^\r\n ]+) +|())([^\r\n ]+)(?: +([^:\r\n ]+[^\r\n ]*(?: +[^:\r\n ]+[^\r\n ]*)*)|())?(?: +:([^\r\n]*)| +())?[\r\n]*$')
Message = collections.namedtuple(
    'Message', ['who', 'command', 'channel', 'text'])


class IRC(object):

    def __init__(self, network, port, username, password):
        self.network = network
        self.port = int(port)
        self.username = username
        self.password = password
        self.irc = None

    def connect(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.connect((self.network, self.port))
        self.twitch()
        self.sasl()
        self.send(f'NICK {self.username}')
        self.send(
            f'USER {self.username} {self.username} {self.username} :{self.username}')

    def twitch(self):
        if 'twitch' not in self.network:
            return False
        self.send(f'PASS {self.password}')
        return True

    def sasl(self):
        if 'freenode' not in self.network:
            return False
        self.send('CAP LS')
        self.send('CAP REQ :sasl')
        self.send('AUTHENTICATE PLAIN')
        sasl = f'{self.username}\0{self.username}\0{self.password}'
        auth = base64.encodebytes(sasl.encode('utf8')).decode('utf8')
        self.send(f'AUTHENTICATE {auth}')
        self.send('CAP END')
        return True

    def pong(self, text):
        if text[0:4] != 'PING':
            return False
        server = text.split()[1]
        self.send(f'PONG {server}')
        return True

    def send(self, msg):
        out = f'{msg}\r\n'.encode('utf8')
        print(out)
        self.irc.send(out)

    def join(self, channel):
        self.send(f'JOIN {channel}')

    def message(self, at, text):
        self.send(f'PRIVMSG {at} :{text}')

    def part(self, channel):
        self.send(f'PART {channel}')

    def quit(self):
        self.send('QUIT')

    def read(self):
        text = self.irc.recv(4096).decode('utf8')
        return text.strip(), self.get_groups(text)

    def get_groups(self, text):
        match = RE_MESSAGE.match(text)
        if not match:
            return None
        groups = match.groups()
        if len(groups) != 9:
            return None
        try:
            who = groups[2].split('!')[0]
        except Exception as e:
            return None
        return Message(who=who, command=groups[4], channel=groups[5], text=groups[7])
