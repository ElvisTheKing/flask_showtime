"""empty message

Revision ID: 20fc435e292
Revises: 4996818bda6
Create Date: 2015-01-16 01:39:41.363397

"""

# revision identifiers, used by Alembic.
revision = '20fc435e292'
down_revision = '4996818bda6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('updated_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'updated_at')
    ### end Alembic commands ###
