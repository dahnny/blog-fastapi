"""add phone number to posts

Revision ID: 13f6bb8bfb15
Revises: 9079491544c1
Create Date: 2025-06-14 18:46:27.778652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13f6bb8bfb15'
down_revision: Union[str, None] = '9079491544c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users',
        sa.Column('phone_number', sa.String(), nullable=True, default=None)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')  # drop the column
    pass
