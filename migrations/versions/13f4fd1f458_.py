"""empty message

Revision ID: 13f4fd1f458
Revises: None
Create Date: 2015-01-04 17:33:37.776644

"""

# revision identifiers, used by Alembic.
revision = '13f4fd1f458'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_show_slug'), 'show', ['slug'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_show_slug'), table_name='show')
    op.drop_table('show')
    ### end Alembic commands ###