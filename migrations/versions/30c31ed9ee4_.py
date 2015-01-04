"""empty message

Revision ID: 30c31ed9ee4
Revises: 13f4fd1f458
Create Date: 2015-01-04 17:41:06.103150

"""

# revision identifiers, used by Alembic.
revision = '30c31ed9ee4'
down_revision = '13f4fd1f458'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('season', sa.Integer(), nullable=False),
    sa.Column('episode', sa.Integer(), nullable=False),
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['show_id'], ['show.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episode')
    ### end Alembic commands ###
