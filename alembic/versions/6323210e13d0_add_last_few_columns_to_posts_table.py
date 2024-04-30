"""add last few columns to posts table

Revision ID: 6323210e13d0
Revises: 45a49ed659d5
Create Date: 2024-04-28 04:27:49.713282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6323210e13d0'
down_revision: Union[str, None] = '45a49ed659d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"
    ))
    op.add_column("posts", 
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column('posts', "published")
    op.drop_column("posts", "created_at")
    pass
