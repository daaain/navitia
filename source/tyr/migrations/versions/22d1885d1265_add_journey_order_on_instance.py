"""add journey_order column on instance table

Revision ID: 22d1885d1265
Revises: 45d7fa0ad882
Create Date: 2014-10-13 07:48:18.842239

"""

# revision identifiers, used by Alembic.
revision = '22d1885d1265'
down_revision = '45d7fa0ad882'

from alembic import op
import sqlalchemy as sa

journey_order = sa.Enum('arrival_time', 'departure_time', name='journey_order')

def upgrade():
    journey_order.create(op.get_bind())
    op.add_column('instance', sa.Column('journey_order', journey_order, nullable=False, server_default='arrival_time'))


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('instance', 'journey_order')
    journey_order.drop(op.get_bind())
    ### end Alembic commands ###
