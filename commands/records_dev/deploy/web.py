import click

@click.command()
@click.pass_context
def web(ctx):
    """
    upload webui to s3 buket

    """
    