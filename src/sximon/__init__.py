# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response



def main(global_config, **local_config):
    """This function returns a Pyramid application.
    """
    settings = dict(global_config)
    settings.update(local_config)
    config = Configurator(settings=settings)
    for plugin in settings.get('plugins', '').split():
        config.include(plugin)

    config.add_route('slack.outcomming', '/outcomming')
    return config.make_wsgi_app()
