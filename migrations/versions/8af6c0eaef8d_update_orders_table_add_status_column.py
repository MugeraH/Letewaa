"""update orders table add status column

Revision ID: 8af6c0eaef8d
Revises: d688fb8b3505
Create Date: 2021-05-06 03:09:13.711558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8af6c0eaef8d'
down_revision = 'd688fb8b3505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###
