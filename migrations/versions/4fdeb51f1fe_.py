"""empty message

Revision ID: 4fdeb51f1fe
Revises: None
Create Date: 2015-06-10 07:52:20.347331

"""

# revision identifiers, used by Alembic.
revision = '4fdeb51f1fe'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skill_role_stage',
    sa.Column('trill_role_group', sa.String(length=80), nullable=True),
    sa.Column('skillgroup', sa.String(length=80), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('surname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('managerfirstname', sa.String(length=80), nullable=True),
    sa.Column('managersurname', sa.String(length=80), nullable=True),
    sa.Column('pwhash', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('people_role_stage',
    sa.Column('firstname', sa.String(length=80), nullable=True),
    sa.Column('surname', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('trill_role_group', sa.String(length=80), nullable=True),
    sa.Column('managerfirstname', sa.String(length=80), nullable=True),
    sa.Column('managersurname', sa.String(length=80), nullable=True),
    sa.Column('job_title', sa.String(length=80), nullable=True),
    sa.Column('encrypted_passwd', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('skill_mapping_stage',
    sa.Column('skilltype', sa.String(length=10), nullable=True),
    sa.Column('skillgroup', sa.String(length=80), nullable=True),
    sa.Column('skilltitlename', sa.String(length=240), nullable=True),
    sa.Column('skilldescription', sa.String(), nullable=True),
    sa.Column('skillcode', sa.String(length=80), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trill_role_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('groupname', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skill_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skillgroupname', sa.String(length=80), nullable=True),
    sa.Column('skilltype', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skillgroupname')
    )
    op.create_table('job_titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('trill_role_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trill_role_group_id'], ['trill_role_groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('skill_titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skilltitlename', sa.String(length=240), nullable=True),
    sa.Column('skill_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_group_id'], ['skill_groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skilltitlename')
    )
    op.create_table('trill_role_skill_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trill_role_group_id', sa.Integer(), nullable=True),
    sa.Column('skill_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_group_id'], ['skill_groups.id'], ),
    sa.ForeignKeyConstraint(['trill_role_group_id'], ['trill_role_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_title_id', sa.Integer(), nullable=True),
    sa.Column('startdate', sa.Date(), nullable=True),
    sa.Column('enddate', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skillcode', sa.String(length=80), nullable=True),
    sa.Column('skilldescription', sa.String(), nullable=True),
    sa.Column('skill_title_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_title_id'], ['skill_titles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('skillcode')
    )
    op.create_table('user_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('proficiency', sa.Integer(), nullable=True),
    sa.Column('confidence', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('user_skill_id_index', 'user_skills', ['skill_id', 'user_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_skills')
    op.drop_table('skills')
    op.drop_table('user_jobs')
    op.drop_table('trill_role_skill_groups')
    op.drop_table('skill_titles')
    op.drop_table('job_titles')
    op.drop_table('skill_groups')
    op.drop_table('trill_role_groups')
    op.drop_table('skill_mapping_stage')
    op.drop_table('people_role_stage')
    op.drop_table('users')
    op.drop_table('skill_role_stage')
    ### end Alembic commands ###