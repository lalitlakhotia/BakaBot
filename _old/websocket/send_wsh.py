# -*- coding: utf-8 -*-
from mod_pywebsocket import msgutil
import redis

def web_socket_do_extra_handshake(request):
    pass  # Always accept.

def web_socket_transfer_data(request):
    r = redis.Redis()
    while True:
        message = msgutil.receive_message(request)
        nick = message.split(':',1)[0]
        present_nicks = r.lrange('regs',0,-1)
    
        try:
            present_nicks.index(nick)
            r.push ('msgs',message,tail=True)
        except ValueError:
            # nick not present in chatroom
            return