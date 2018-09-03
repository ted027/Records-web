import click
from . import records

@click.group()
@click.pass_context
def update(ctx):
    pass

update.add_command(records.records)