from pathlib import Path
from python_action_test import __version__


def test_version():
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    with open(Path(__file__).parents[1] / "pyproject.toml", "rb") as f:
        version = tomllib.load(f)["tool"]["poetry"]["version"]
    assert version == __version__
