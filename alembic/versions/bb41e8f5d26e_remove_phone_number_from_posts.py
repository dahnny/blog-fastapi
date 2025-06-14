"""remove phone number from posts

Revision ID: bb41e8f5d26e
Revises: 6dfd0d552a9b
Create Date: 2025-06-14 19:20:28.066190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb41e8f5d26e'
down_revision: Union[str, None] = '6dfd0d552a9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('posts', 'phone_number')  # drop the column from posts table
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        'posts',
        sa.Column('phone_number', sa.String(), nullable=True, default=None)
    )  # re-add the column to posts table
    pass
