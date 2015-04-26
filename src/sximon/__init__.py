# -*- coding: utf-8 -*-
from pyramid.config import Configurator


def main(global_config, **local_config):
    """This function returns a Pyramid application.
    """
    settings = dict(global_config)
    settings.update(local_config)
    config = Configurator(settings=settings)
    for plugin in settings.get('plugins', '').split():
        config.include(plugin)

    config.add_route('ping', '/ping')
    config.add_route('slack.outcomming', '/slack/outcomming')

    config.scan()

    return config.make_wsgi_app()
