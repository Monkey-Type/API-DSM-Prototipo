"""empty message

Revision ID: 7cb8c21d6884
Revises: 8119cea91c8f
Create Date: 2021-10-21 14:01:40.182303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cb8c21d6884'
down_revision = '8119cea91c8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user', 'area', ['area_id'], ['id'])
    op.drop_column('user', 'cargo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cargo', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    # ### end Alembic commands ###
