import logging.config
import shutil
from pathlib import Path

import pkg_resources
import yaml
from zveronics import serve_zveronics


def load_cfg():
    cfg_dir = Path.home() / '.config' / 'zveronics'
    cfg_dir.mkdir(parents=True, exist_ok=True)

    logging_cfg_file = 'logging.yaml'
    logging_cfg_path = cfg_dir / logging_cfg_file
    stream = pkg_resources.resource_stream('zveronics', 'etc/logging.yaml')
    if not logging_cfg_path.is_file():
        with stream as src, open(logging_cfg_path, 'wb') as dst:
            shutil.copyfileobj(src, dst)

    with open(logging_cfg_path, 'r') as f:
        return yaml.safe_load(f)


def main():
    logging.config.dictConfig(load_cfg())
    serve_zveronics('0.0.0.0', 50000)


if __name__ == '__main__':
    main()
