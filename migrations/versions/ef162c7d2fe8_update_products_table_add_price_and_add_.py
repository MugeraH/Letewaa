"""update products table add price and add product cost and price to cart table

Revision ID: ef162c7d2fe8
Revises: 9903134358c6
Create Date: 2021-05-06 11:00:25.596676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef162c7d2fe8'
down_revision = '9903134358c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_price', sa.Integer(), nullable=True))
    op.add_column('cart', sa.Column('product_cost', sa.Integer(), nullable=True))
    op.add_column('products', sa.Column('product_price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'product_price')
    op.drop_column('cart', 'product_cost')
    op.drop_column('cart', 'product_price')
    # ### end Alembic commands ###