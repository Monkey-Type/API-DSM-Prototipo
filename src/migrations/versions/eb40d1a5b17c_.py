"""empty message

Revision ID: eb40d1a5b17c
Revises: 357df65ba34a
Create Date: 2021-10-21 20:24:18.481532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb40d1a5b17c'
down_revision = '357df65ba34a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('colors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('color_association',
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['cards.id'], ),
    sa.ForeignKeyConstraint(['color_id'], ['colors.id'], ),
    sa.PrimaryKeyConstraint('card_id', 'color_id')
    )
    op.drop_table(' usuario ')
    op.drop_table(' postagem ')
    op.drop_table(' servico ')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(' servico ',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('area', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('area')
    )
    op.create_table(' postagem ',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('texto', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(' usuario ',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=150), nullable=True),
    sa.Column('cpf', sa.VARCHAR(length=12), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    op.drop_table('color_association')
    op.drop_table('colors')
    op.drop_table('cards')
    # ### end Alembic commands ###
