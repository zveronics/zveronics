import pytest
from zveronics.server import pack, unpack


@pytest.mark.parametrize('data', [
    None,
    True,
    False,
    [],
    {},
    ['hey', b'guys'],
    {'i': 'am', 'a': ['complex', b'data', 'structure']},
])
def test_pack_unpack(data):
    packed = pack(data)
    assert isinstance(packed, bytes)
    assert data == unpack(packed)


@pytest.mark.parametrize('data', [
    set(),
])
def test_pack_failure(data):
    with pytest.raises(TypeError):
        pack(data)
