"""empty message

Revision ID: bd203d01de64
Revises: a33cce49df39
Create Date: 2021-10-21 19:43:35.520978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd203d01de64'
down_revision = 'a33cce49df39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'area', type_='foreignkey')
    op.drop_column('area', 'user_id')
    op.add_column('post', sa.Column('area_id', sa.Integer(), nullable=False))
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'post', 'area', ['area_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.alter_column('post', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('post', 'area_id')
    op.add_column('area', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'area', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
