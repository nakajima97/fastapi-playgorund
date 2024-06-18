"""Add index to created_at column in memos table

Revision ID: 37376cefa3eb
Revises: 6bf8d449e119
Create Date: 2024-06-18 00:14:59.067745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37376cefa3eb'
down_revision: Union[str, None] = '6bf8d449e119'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_memos_created_at'), 'memos', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_memos_created_at'), table_name='memos')
    # ### end Alembic commands ###