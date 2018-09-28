import pkg_resources


def test_logging_config():
    assert pkg_resources.resource_exists('zveronics', 'etc/logging.yaml')
    assert not pkg_resources.resource_isdir('zveronics', 'etc/logging.yaml')

