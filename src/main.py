# demo script for GitHub Actions
import json
import logging

logger = logging.getLogger(__name__)


def hello_world(name: str):
    """Trigger GHA change"""
    logger.debug('Input name: %s', name)
    print(f'Hello {name}')


def read_json(file_name: str):
    with open(file_name) as f:
        data = json.load(f)

    print(data)


def foo_bar():
    logger.error('You have been foo bar')
