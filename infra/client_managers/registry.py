import logging
from collections import OrderedDict

from infra.client_managers import (
    base
)
from infra.config import Config


registered_clients = OrderedDict([
    ('base', base.ClientManager),
])


def get():
    client_manager_type = "base"
    if hasattr(Config().server, "client_manager"):
        client_manager_type = Config().server.client_manager.type

    if client_manager_type in registered_clients:
        logging.info("Client manager: %s", client_manager_type)
        registered_client_manager = registered_clients[client_manager_type]()
    else:
        raise ValueError('No such client managers: {}'.format(client_manager_type))

    return registered_client_manager
