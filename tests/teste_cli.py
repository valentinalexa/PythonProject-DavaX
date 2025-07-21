from click.testing import CliRunner
from app.cli import cli
 
runner = CliRunner()
 
def test_pow_cli():
    result = runner.invoke(cli, ['pow', '--x', '2', '--y', '3'])
    assert '8' in result.output
 
def test_factorial_cli():
    result = runner.invoke(cli, ['factorial', '--n', '5'])
    assert '120' in result.output
 
def test_fibonacci_cli():
    result = runner.invoke(cli, ['fibonacci', '--n', '6'])
    assert '8' in result.output