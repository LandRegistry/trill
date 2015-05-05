"""empty message

Revision ID: 234acea6f69
Revises: 59cfda6ff6f
Create Date: 2015-04-30 15:28:37.158641

"""

# revision identifiers, used by Alembic.
revision = '234acea6f69'
down_revision = '59cfda6ff6f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pwhash', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pwhash')
    ### end Alembic commands ###
