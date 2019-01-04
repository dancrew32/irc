import os
import sys
import time
import bot


irc = bot.IRC(
    network=os.environ['IRC_NETWORK'],
    port=os.environ['IRC_PORT'],
    username=os.environ['IRC_USERNAME'],
    password=os.environ['IRC_PASSWORD']
)

irc.connect()

for channel in os.environ['IRC_CHANNELS'].split(','):
    irc.join(channel)


def loop():
    text, message = irc.read()

    if irc.pong(text):
        return

    if message:
        print(message)


def try_loop():
    try:
        loop()
        time.sleep(.1)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    while 1:
        try_loop()
