"""empty message

Revision ID: 43b708fdda8
Revises: 234acea6f69
Create Date: 2015-05-01 12:33:31.509285

"""

# revision identifiers, used by Alembic.
revision = '43b708fdda8'
down_revision = '234acea6f69'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_skills', sa.Column('proficiency', sa.Integer(), nullable=True))
    op.drop_column('user_skills', 'competence')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_skills', sa.Column('competence', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('user_skills', 'proficiency')
    ### end Alembic commands ###