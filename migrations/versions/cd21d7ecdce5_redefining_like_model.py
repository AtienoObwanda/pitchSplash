"""Redefining like model

Revision ID: cd21d7ecdce5
Revises: fa50123b079e
Create Date: 2022-05-08 23:28:20.574154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd21d7ecdce5'
down_revision = 'fa50123b079e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('likes')
    op.drop_table('dislikes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dislikes',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], name='dislikes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='dislikes_user_id_fkey')
    )
    op.create_table('likes',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], name='likes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='likes_user_id_fkey')
    )
    op.drop_table('like')
    # ### end Alembic commands ###
