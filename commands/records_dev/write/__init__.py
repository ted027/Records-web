import click
from . import yrecords, yteam, yprofile, yyearly

@click.group()
@click.pass_context
def write(ctx):
    pass

write.add_command(yrecords.yrecords)
write.add_command(yprofile.yprofile)
write.add_command(yyearly.yyearly)
# write.add_command(spersonal.spersonal)
write.add_command(yteam.yteam)