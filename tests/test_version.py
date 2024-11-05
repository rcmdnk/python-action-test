from pathlib import Path
from python_action_test import __version__


def test_version():
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    with open(Path(__file__).parents[1] / "pyproject.toml", "rb") as f:
        yml = tomllib.load(f)
        if "project" in yml:
            version = yml["project"]["version"]
        else:
            version = yml["tool"]["poetry"]["version"]
    assert version == __version__
