from sqlalchemy.schema import Sequence

from src.domain.seq import SeqGenerator
from .sqlalchemy import tx


class PGSeqGenerator(SeqGenerator):
    def get_next(self) -> int:
        with tx() as session:
            next_seq = session.execute(Sequence('url_seq'))

        return next_seq
