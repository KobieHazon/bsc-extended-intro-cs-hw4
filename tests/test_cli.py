from extended_intro_hw4.cli import cli


def test_rod_profit_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw4", "rod-profit", "4", "1,5,8,9"])

    cli()

    assert capsys.readouterr().out == "10\n"


def test_winning_position_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["extended-intro-hw4", "winning-position", "20", "1,2,3,4"])

    cli()

    assert capsys.readouterr().out == "False\n"
