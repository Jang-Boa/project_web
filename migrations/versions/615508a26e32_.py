"""empty message

Revision ID: 615508a26e32
Revises: e38154464eed
Create Date: 2021-10-19 17:35:12.515407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '615508a26e32'
down_revision = 'e38154464eed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Car', sa.Column('price_avg', sa.Integer(), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Car', 'price_avg')
    # ### end Alembic commands ###
