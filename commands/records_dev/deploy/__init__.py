import click
from records_dev.aws_service import AwsInit
from . import function, web

@click.group()
@click.pass_context
def deploy(ctx):
    ctx.obj = AwsInit()
    pass

deploy.add_command(function.function)
deploy.add_command(web.web)