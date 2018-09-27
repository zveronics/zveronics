# zveronics
Python server for zveronics game

## Development
Create virtualenv and activate it:
```bash
python3.6 -m virtualenv venv/
source venv/bin/activate
```
Install the project in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#install-editable):
```bash
pip install -e .
```
Spin up the server:
```bash
python -m zveronics
```
Send a request to the server
```bash
echo -e "\x01\x00\x00\x00\xc2" | nc localhost 50000
```
