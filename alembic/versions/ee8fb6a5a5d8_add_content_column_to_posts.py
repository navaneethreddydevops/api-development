"""add content column to posts

Revision ID: ee8fb6a5a5d8
Revises: 953ccfb7217c
Create Date: 2024-03-27 01:38:40.017939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee8fb6a5a5d8'
down_revision: Union[str, None] = '953ccfb7217c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
