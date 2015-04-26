# -*- coding: utf-8 -*-
import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def main(global_config, **local_config):
    """This function returns a Pyramid application.
    """
    settings = dict(global_config)
    settings.update(local_config)
    config = Configurator(settings=settings)
    for plugin in settings.get('plugins', '').split():
        config.include(plugin)

    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    config.scan()
    return config.make_wsgi_app()

if __name__ == '__main__':
    PORT = int(os.getenv('VCAP_APP_PORT', 8000))
    app = main()
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
