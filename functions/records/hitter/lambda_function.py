"""
lambda handler
"""
import os
import sys

import requests
import bs4
from records.1_external_interface.api.router import Router

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def lambda_handler(event, context):
    try:
        logger.debug('router start')
        result = Router.route(event, self_=router)
        logger.debug('router end')
    except BaseException:
        logger.warning('Exception was raised on Router.')
        raise
    return result
