"""empty message

Revision ID: 3709a9e6a77d
Revises: 796319e66add
Create Date: 2021-10-19 15:57:14.980676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3709a9e6a77d'
down_revision = '796319e66add'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'postagem', type_='foreignkey')
    op.create_foreign_key(None, 'postagem', 'user', ['user_id'], ['nome'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'postagem', type_='foreignkey')
    op.create_foreign_key(None, 'postagem', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
