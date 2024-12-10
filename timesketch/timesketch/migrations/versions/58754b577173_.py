"""Add AggregationGroup model

Revision ID: 58754b577173
Revises: 64c00337b9d1
Create Date: 2020-04-20 09:52:16.715947

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '58754b577173'
down_revision = '64c00337b9d1'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'aggregation',
        sa.Column('aggregationgroup_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, 'aggregation', 'aggregationgroup',
        ['aggregationgroup_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'aggregation', type_='foreignkey')
    op.drop_column('aggregation', 'aggregationgroup_id')
    # ### end Alembic commands ###