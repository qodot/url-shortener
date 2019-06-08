from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
)

from src.service.url import UrlService
from src.domain.error import (
    NotExistShortUrlError,
    AlreadyExistOriginUrl,
)
from src.infra.url_repository import SAUrlRepository
from src.infra.seq_generator import PGSeqGenerator


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

    service = UrlService(SAUrlRepository(), PGSeqGenerator())

    try:
        shorten_hash = service.shortify(origin)
    except AlreadyExistOriginUrl:
        shorten_hash = service.get_shorten_by_origin(origin)

    url_root = request.url_root.replace('http://', 'https://')
    shorten_url = f'{url_root}{shorten_hash}'

    return render_template('generated.html', shorten_url=shorten_url)


@app.route('/<string:hash_>')
def go(hash_):
    service = UrlService(SAUrlRepository(), PGSeqGenerator())

    try:
        origin = service.get_origin_by_shorten(hash_)
    except NotExistShortUrlError as e:
        abort(404, str(e))

    return redirect(origin)
