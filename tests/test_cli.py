from example_package import cli

def test_main_returns_true():
    result = cli.main()
    assert(result is True)
