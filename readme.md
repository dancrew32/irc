# IRC

A simple IRC bot. It follows channels, writes messages to Postgres.


## Docker setup:

Get Docker for your system: https://docs.docker.com
You'll want `docker-compose`: https://docs.docker.com/compose/install/



## Freenode example:

```bash
# vim ~/.bashrc
export IRC_NETWORK='irc.freenode.net'
export IRC_PORT='6667'
export IRC_USERNAME='wat'
export IRC_PASSWORD='okay'  # SASL is handled.
export IRC_CHANNELS='#css,#javascript,#python'
export IRC_DB_USER='wat'
export IRC_DB_PASSWORD='okay'
export IRC_DB_NAME='irc'
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
export IRC_DB_USER='wat'
export IRC_DB_PASSWORD='okay'
export IRC_DB_NAME='irc'
```


## Build and run:

```bash
source ~/.bashrc
git clone git@github.com:dancrew32/irc.git irc
cd irc
make build run
```


## Read database:

### Open `psql` prompt:

```bash
make psql
```

### Top channels:

```bash
make top_channels
```

### Top users:

```bash
make top_who
```