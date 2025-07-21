# app/cli.py

import click
from app.controller import handle_pow, handle_factorial, handle_fibonacci

@click.group()
def cli():
    """CLI pentru operații matematice."""
    pass


@cli.command()
@click.option('--x', type=float, required=True, help="Baza.")
@click.option('--y', type=float, required=True, help="Exponentul.")
def pow(x, y):
    """Calculează x la puterea y."""
    result = handle_pow(x, y)
    click.echo(f"Rezultatul: {result}")


@cli.command()
@click.option('--n', type=int, required=True, help="Numărul pentru factorial.")
def factorial(n):
    """Calculează factorialul unui număr."""
    result = handle_factorial(n)
    click.echo(f"Rezultatul: {result}")


@cli.command()
@click.option('--n', type=int, required=True, help="Indexul din seria Fibonacci.")
def fibonacci(n):
    """Calculează al n-lea număr Fibonacci."""
    result = handle_fibonacci(n)
    click.echo(f"Rezultatul: {result}")



@cli.command()
def list_log():
    """Afișează ultimele 10 operații din log."""
    from app.databases import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT operation, input_1, input_2, result, timestamp FROM operations_log ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
