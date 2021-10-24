"""empty message

Revision ID: 357df65ba34a
Revises: 5e1ef3ec3df1
Create Date: 2021-10-21 20:18:11.171308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '357df65ba34a'
down_revision = '5e1ef3ec3df1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(' postagem ',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('texto', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(' servico ',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('area', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('area')
    )
    op.create_table(' usuario ',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=True),
    sa.Column('cpf', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    op.drop_table('user')
    op.drop_table('area')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('assunto', sa.VARCHAR(), nullable=False),
    sa.Column('remetente', sa.VARCHAR(), nullable=False),
    sa.Column('recebido', sa.VARCHAR(), nullable=False),
    sa.Column('texto', sa.VARCHAR(), nullable=False),
    sa.Column('data', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('area',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('area', sa.VARCHAR(length=100), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('cpf', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.Column('senha', sa.VARCHAR(length=100), nullable=False),
    sa.Column('ra', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('envia', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table(' usuario ')
    op.drop_table(' servico ')
    op.drop_table(' postagem ')
    # ### end Alembic commands ###
