"""Initial Migration

Revision ID: 0f023fad2678
Revises: 
Create Date: 2022-05-20 11:56:49.080194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f023fad2678'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('password_secure', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('pitch_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('pitchcontent', sa.Text(), nullable=False),
    sa.Column('Additiontime', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitch_types_category'), 'pitch_types', ['category'], unique=False)
    op.create_table('user_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_Message', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_downvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_upvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_upvotes')
    op.drop_table('user_downvotes')
    op.drop_table('user_comments')
    op.drop_index(op.f('ix_pitch_types_category'), table_name='pitch_types')
    op.drop_table('pitch_types')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
