import pytest


@pytest.mark.add
def test_add():
    result = 1 + 3
    assert result == 4

@pytest.mark.skip
def test_multiple():
    result = 2 * 4
    assert result == 5

@pytest.mark.xfail
def test_divide():
    result = 9 / 3
    assert result == 2
