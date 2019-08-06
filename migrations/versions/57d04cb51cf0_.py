"""empty message

Revision ID: 57d04cb51cf0
Revises: 
Create Date: 2019-08-05 21:06:55.552634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d04cb51cf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sprints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('relatorio', sa.String(), nullable=True),
    sa.Column('objetivo', sa.String(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('horario_inicio', sa.String(), nullable=True),
    sa.Column('horario_termino', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('matricula', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricula'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('sprints')
    # ### end Alembic commands ###
