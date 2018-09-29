# zveronics
Python server for zveronics game

## Development
Create a virtualenv and activate it:
```bash
make venv
source venv/bin/activate
```
Install the project in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#install-editable) with all the test dependencies:
```bash
pip install -e .[test]
```
Run all checks:
```bash
make check-all
```
Spin up a server:
```bash
python -m zveronics
```
Send a request to the server:
```bash
echo -e "\x01\x00\x00\x00\xc2" | nc localhost 50000
```
