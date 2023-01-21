import sys

import pytest

from test_python_action_test import main


@pytest.mark.parametrize(
    "argv, out",
    [
        (["python_template"], "Hello World!\n"),
        (["python_template", "Alice"], "Hello Alice!\n"),
        (
            ["python_template", "Alice", "Bob", "Carol"],
            "Hello Alice, Bob, Carol!\n",
        ),
    ],
)
def test_main(argv, out, capsys):
    sys.argv = argv
    main()
    captured = capsys.readouterr()
    assert captured.out == out
