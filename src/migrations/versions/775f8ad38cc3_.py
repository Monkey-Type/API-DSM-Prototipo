"""empty message

Revision ID: 775f8ad38cc3
Revises: d02b9701192f
Create Date: 2021-10-21 19:53:23.761674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '775f8ad38cc3'
down_revision = 'd02b9701192f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'area', type_='foreignkey')
    op.drop_column('area', 'user_id')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    op.add_column('user', sa.Column('post_id', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('area_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'user', 'area', ['area_id'], ['id'])
    op.create_foreign_key(None, 'user', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'area_id')
    op.drop_column('user', 'post_id')
    op.add_column('post', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    op.add_column('area', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'area', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
