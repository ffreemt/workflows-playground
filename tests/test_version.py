from src import __version__


def test_version():
    assert __version__.startswith("0.1")
