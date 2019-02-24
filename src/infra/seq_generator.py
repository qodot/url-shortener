from sqlalchemy.schema import Sequence

from src.domain.seq_generator import SeqGenerator, UrlSeq
from src.infra.sqlalchemy import tx


class PGSeqGenerator(SeqGenerator):
    def get_next(self) -> UrlSeq:
        with tx() as session:
            next_seq = session.execute(Sequence('url_seq'))

        return UrlSeq(str(next_seq))
