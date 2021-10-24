"""empty message

Revision ID: d2d7c1c5d3da
Revises: 3c02a98bdbc9
Create Date: 2021-10-23 23:55:56.255768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2d7c1c5d3da'
down_revision = '3c02a98bdbc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postagem',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('assunto', sa.String(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('texto', sa.String(), nullable=False),
    sa.Column('recebido', sa.String(), nullable=False),
    sa.Column('remetente', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=True),
    sa.Column('grade', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=True),
    sa.Column('office', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('user')
    op.drop_table('teacher')
    op.drop_table('student')
    op.drop_table('postagem')
    # ### end Alembic commands ###
