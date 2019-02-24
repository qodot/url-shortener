from flask import Flask, request, render_template, abort, redirect

from src.service.url import UrlShortenerService
from src.domain.url import OriginUrl, ShortenHash
from src.domain.error import NotExistShortUrlError, AlreadyExistOriginUrl
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
    origin_url = request.form.get('origin')
    if not origin_url:
        abort(400, 'origin URL is required')

    service = UrlShortenerService(SAUrlRepository())

    try:
        shorten_hash: ShortenHash = service.shortify(OriginUrl(origin_url))
    except AlreadyExistOriginUrl as e:
        abort(400, e.message)

    return render_template(
            'generated.html', host=f'{request.url_root}',
            shorten=shorten_hash.hash)


@app.route('/<string:hash_>')
def go(hash_):
    service = UrlShortenerService(SAUrlRepository())

    try:
        origin: OriginUrl = service.get_origin(ShortenHash(hash_))
    except NotExistShortUrlError as e:
        abort(404, e.message)

    return redirect(origin.url)
