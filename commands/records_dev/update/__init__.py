import click
from . import records, scores

@click.group()
@click.pass_context
def update(ctx):
    pass

update.add_command(records.records)
update.add_command(scores.scores)