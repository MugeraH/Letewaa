"""add amount and size to cart table

Revision ID: cb36061ebf77
Revises: 9bbc78174c08
Create Date: 2021-05-06 14:28:20.639874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb36061ebf77'
down_revision = '9bbc78174c08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('amount', sa.Integer(), nullable=True))
    op.add_column('cart', sa.Column('size', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'size')
    op.drop_column('cart', 'amount')
    # ### end Alembic commands ###