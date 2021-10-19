"""empty message

Revision ID: 25aac75e8625
Revises: cd08f7dab0bd
Create Date: 2021-10-19 17:50:22.149645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25aac75e8625'
down_revision = 'cd08f7dab0bd'
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
