"""empty message

Revision ID: 24bbbf34b67b
Revises: 57d04cb51cf0
Create Date: 2019-08-06 08:51:52.257486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24bbbf34b67b'
down_revision = '57d04cb51cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adms')
    # ### end Alembic commands ###
