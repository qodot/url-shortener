import click
from gevent.pywsgi import WSGIServer

from src.http.app import app


@click.group()
def manage():
    pass


@manage.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000)
def run(host, port):
    app.debug = True

    click.echo("Run gevent wsgi server")
    server = WSGIServer((host, port), app)
    server.serve_forever()


if __name__ == "__main__":
    manage()
