import logging
from zveronics import serve_zveronics


def main():
    logging.basicConfig(level=logging.DEBUG)
    serve_zveronics('0.0.0.0', 50000)


if __name__ == '__main__':
    main()
