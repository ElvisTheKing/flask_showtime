"""empty message

Revision ID: 4996818bda6
Revises: 2dace2d8387
Create Date: 2015-01-06 19:22:35.739002

"""

# revision identifiers, used by Alembic.
revision = '4996818bda6'
down_revision = '2dace2d8387'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('can_view_links', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'can_view_links')
    ### end Alembic commands ###
