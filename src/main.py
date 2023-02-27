# demo script for GitHub Actions
import logging

logger = logging.getLogger(__name__)


def hello_world(name: str):
    logger.debug('Input name: %s', name)
    print(f'Hello {name}')
