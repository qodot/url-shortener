"""add url sequence

Revision ID: 0e09985d5f24
Revises: d74bc26fe1a8
Create Date: 2019-02-23 19:59:20.196090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, CreateSequence


# revision identifiers, used by Alembic.
revision = '0e09985d5f24'
down_revision = 'd74bc26fe1a8'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(CreateSequence(Sequence('url_seq')))


def downgrade():
    op.execute('DROP SEQUENCE url_seq')
