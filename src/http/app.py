from flask import Flask, request, render_template, abort, redirect

from src.service.url import UrlService
from src.domain.error import (
    NotExistShortUrlError, AlreadyExistOriginUrl, InvalidUrl,
)
from src.domain.url import OriginUrl, ShortenHash
from src.infra.url_repository import SAUrlRepository


def create_app():
    app = Flask(__name__)

    return app


app = create_app()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/generate', methods=['POST'])
def generate():
    origin = request.form.get('origin')
    if not origin:
        abort(400, 'origin URL is required')

    service = UrlService(SAUrlRepository())

    try:
        origin_url = OriginUrl(origin)
    except InvalidUrl as e:
        abort(400, str(e))

    try:
        shorten_hash = service.shortify(origin_url)
    except AlreadyExistOriginUrl:
        shorten_hash = service.get_shorten(origin_url)

    url_root = request.url_root.replace('http://', 'https://')
    shorten_url = f'{url_root}{shorten_hash.hash}'

    return render_template('generated.html', shorten_url=shorten_url)


@app.route('/<string:hash_>')
def go(hash_):
    service = UrlService(SAUrlRepository())

    try:
        origin = service.get_origin(ShortenHash(hash_))
    except NotExistShortUrlError as e:
        abort(404, str(e))

    return redirect(origin.url)
