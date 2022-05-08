"""Adding likes and dislikes model

Revision ID: 49ca69b522a4
Revises: cd21d7ecdce5
Create Date: 2022-05-08 23:45:32.460063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ca69b522a4'
down_revision = 'cd21d7ecdce5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('like', sa.Column('author', sa.Integer(), nullable=False))
    op.drop_constraint('like_user_id_fkey', 'like', type_='foreignkey')
    op.create_foreign_key(None, 'like', 'user', ['author'], ['id'])
    op.drop_column('like', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('like', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'like', type_='foreignkey')
    op.create_foreign_key('like_user_id_fkey', 'like', 'user', ['user_id'], ['id'])
    op.drop_column('like', 'author')
    # ### end Alembic commands ###