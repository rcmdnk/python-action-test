def hello():
    return "Hello World"


def test_loop(benchmark):
    ret = benchmark.pedantic(hello, rounds=100, iterations=10)
    assert ret == "Hello World"
