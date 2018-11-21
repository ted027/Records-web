import click
from . import ypersonal, spersonal, yteam

@click.group()
@click.pass_context
def write(ctx):
    pass

write.add_command(ypersonal.ypersonal)
write.add_command(spersonal.spersonal)
write.add_command(yteam.yteam)