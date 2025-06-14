"""add foreign key to posts table

Revision ID: 9079491544c1
Revises: 575e48ff025f
Create Date: 2025-06-11 20:04:04.253546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9079491544c1'
down_revision: Union[str, None] = '575e48ff025f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'fk_posts_users',  # name of the foreign key constraint
        'posts',           # source table
        'users',           # referent table
        ['owner_id'],      # source column(s)
        ['id'],            # referent column(s)
        ondelete='CASCADE' # action on delete
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        'fk_posts_users',  # name of the foreign key constraint
        'posts',           # source table
        type_='foreignkey' # type of the constraint
    )
    op.drop_column('posts', 'owner_id')  # drop the column
    pass
