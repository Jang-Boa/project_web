"""empty message

Revision ID: cd08f7dab0bd
Revises: 58cff94d68be
Create Date: 2021-10-19 17:45:48.167782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd08f7dab0bd'
down_revision = '58cff94d68be'
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
