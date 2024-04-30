"""add content column to posts table

Revision ID: d14c63684342
Revises: bc1aab469c45
Create Date: 2024-04-28 03:57:33.282166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd14c63684342'
down_revision: Union[str, None] = 'bc1aab469c45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
