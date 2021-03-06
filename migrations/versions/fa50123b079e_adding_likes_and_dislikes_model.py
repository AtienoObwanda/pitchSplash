"""Adding likes and dislikes model

Revision ID: fa50123b079e
Revises: f2b5b79705d4
Create Date: 2022-05-08 22:38:58.869783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa50123b079e'
down_revision = 'f2b5b79705d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dislikes',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('like')
    op.drop_table('dislike')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dislike',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], name='dislike_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='dislike_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='dislike_pkey')
    )
    op.create_table('like',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], name='like_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='like_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='like_pkey')
    )
    op.drop_table('likes')
    op.drop_table('dislikes')
    # ### end Alembic commands ###
