from sqlalchemy.schema import Sequence

from src.domain.seq_generator import SeqGenerator
from src.infra.sqlalchemy import Session


class PGSeqGenerator(SeqGenerator):
    def get_next(self) -> int:
        with Session.begin() as session:
            next_seq = session.execute(Sequence('url_seq'))

        return next_seq
