"""create DBES table

Revision ID: 0280a592952e
Revises: 
Create Date: 2023-09-08 05:53:12.099392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0280a592952e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "DBES",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("project_name", sa.String(100), nullable=False),
        sa.Column("project_type", sa.String(2), nullable=False),
        sa.Column("facts", sa.String(500), nullable=False),
        sa.Column("rules", sa.String(500), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("DBES")
