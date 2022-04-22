"""add language to posts

Revision ID: 1ef5b2310b0b
Revises: b47cf3f9ace4
Create Date: 2022-04-22 15:26:27.270114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ef5b2310b0b'
down_revision = 'b47cf3f9ace4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
