"""empty message

Revision ID: 1521d624ede9
Revises: 8fe448871150
Create Date: 2021-10-21 17:47:49.597904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1521d624ede9'
down_revision = '8fe448871150'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('assunto', sa.String(), nullable=False),
    sa.Column('remetente', sa.String(), nullable=False),
    sa.Column('recebido', sa.String(), nullable=False),
    sa.Column('texto', sa.String(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('postagem')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postagem',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('assunto', sa.VARCHAR(), nullable=False),
    sa.Column('data', sa.DATETIME(), nullable=True),
    sa.Column('texto', sa.VARCHAR(), nullable=False),
    sa.Column('recebido', sa.VARCHAR(), nullable=False),
    sa.Column('remetente', sa.VARCHAR(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post')
    # ### end Alembic commands ###
