"""empty message

Revision ID: ae920ab6621d
Revises: 615508a26e32
Create Date: 2021-10-19 17:35:40.688079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae920ab6621d'
down_revision = '615508a26e32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Car', 'price_avg',
                existing_type=sa.INTEGER(),
                nullable=False,
                existing_server_default=sa.text("'1'"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Car', 'price_avg',
                existing_type=sa.INTEGER(),
                nullable=True,
                existing_server_default=sa.text("'1'"))
    # ### end Alembic commands ###
