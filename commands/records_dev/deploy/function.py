import click

@click.command()
@click.pass_context
def function(ctx):
    """
    upload lambda function to s3 buket

    """
    