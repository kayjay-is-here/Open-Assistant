"""add collective flag to task

Revision ID: 464ec4667aae
Revises: ef0b52902560
Create Date: 2022-12-29 21:03:06.841962

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "464ec4667aae"
down_revision = "ef0b52902560"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "work_package", sa.Column("collective", sa.Boolean(), server_default=sa.text("false"), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("work_package", "collective")
    # ### end Alembic commands ###