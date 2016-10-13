"""add post's title

Revision ID: 34313cc5ca5f
Revises: dfebf1556f0a
Create Date: 2016-10-13 13:49:05.276164

"""

# revision identifiers, used by Alembic.
revision = '34313cc5ca5f'
down_revision = 'dfebf1556f0a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    ### end Alembic commands ###