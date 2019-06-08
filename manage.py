import click
from gevent.pywsgi import WSGIServer
from werkzeug.serving import run_with_reloader

from src.http.app import app


@click.group()
def manage():
    pass


@manage.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000)
def run(host, port):
    @run_with_reloader
    def serve_forever():
        click.echo("Run gevent wsgi server")
        server = WSGIServer((host, port), app)
        server.serve_forever()

    app.debug = True
    serve_forever()


if __name__ == "__main__":
    manage()
