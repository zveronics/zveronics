import json
import logging
import socketserver
import struct

import msgpack

log = logging.getLogger(__name__)


def unpack(data):
    return msgpack.unpackb(data, raw=False)


def pack(data):
    return msgpack.packb(data, use_bin_type=True)


class MsgSize(struct.Struct):
    def __init__(self):
        super().__init__('<I')


class UserRequestHandler(socketserver.BaseRequestHandler):
    """The request handler class for zveronics server."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self):
        s = MsgSize()
        size = int(s.size)
        log.debug('Waiting message size (%s bytes)', str(size))
        msg_size = s.unpack(self.request.recv(size))[0]
        log.debug('Reading message of size %s', msg_size)
        msg = unpack(self.request.recv(msg_size))
        log.debug('Got message: %s', json.dumps(msg))


def serve_zveronics(host, port):
    log.info(f'Starting zveronics server on {host}:{port}')
    with socketserver.TCPServer((host, port),
                                UserRequestHandler) as server:
        server.serve_forever()
