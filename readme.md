# IRC

A simple IRC bot. 


## Freenode example:

```bash
# vim ~/.bashrc
export IRC_NETWORK='irc.freenode.net'
export IRC_PORT='6667'
export IRC_USERNAME='wat'
export IRC_PASSWORD='okay'  # SASL is handled.
export IRC_CHANNELS='#css,#javascript,#python'
```


## Twitch example:

Get a password here: https://twitchapps.com/tmi/

```bash
# vim ~/.bashrc
export IRC_NETWORK='irc.chat.twitch.tv'
export IRC_PORT='6667'
export IRC_USERNAME='wat'
export IRC_PASSWORD='oauth:okaaaaaaaaaaaaaaaaaaaaaaaaaaay'
export IRC_CHANNELS='#twitchpresents,#bobross,#food,#kitboga'
```


## Build and run:

```bash
source ~/.bashrc
git clone git@github.com:dancrew32/irc.git irc
cd irc
make venv deps run
```