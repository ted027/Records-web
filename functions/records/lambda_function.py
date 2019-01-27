"""
lambda handler
"""
import os
import sys

import requests
import bs4
import json

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def lambda_handler(event, context):
    logger.debug('router start')
    # router
    logger.debug('router end')
