import tomli

from python_action_test import __version__


def test_version():
    with open("pyproject.toml", "rb") as f:
        version = tomli.load(f)["tool"]["poetry"]["version"]
    assert version == __version__
