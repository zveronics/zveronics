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


class UserRequestHandler(socketserver.BaseRequestHandler):
    """The request handler class for zveronics server."""

    def handle(self):
        int_format = struct.Struct('<I')
        size = int(int_format.size)
        log.debug('Waiting message size (%s bytes)', str(size))
        msg_size = int_format.unpack(self.request.recv(size))[0]
        log.debug('Reading message of size %s', msg_size)
        msg = unpack(self.request.recv(msg_size))
        log.debug('Got message: %s', json.dumps(msg))


def serve_zveronics(host, port):
    log.info('Starting zveronics server on %s:%s', host, port)
    with socketserver.TCPServer((host, port),
                                UserRequestHandler) as server:
        server.serve_forever()
