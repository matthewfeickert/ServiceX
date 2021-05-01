"""v1.0-rc4-a2

Revision ID: 04b9fb8ffee1
Revises: a6cbb6201d3d
Create Date: 2021-05-01 16:58:29.532726

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '04b9fb8ffee1'
down_revision = 'a6cbb6201d3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('requests_request_id_key', 'requests', type_='unique')
    op.create_index(op.f('ix_requests_request_id'), 'requests', ['request_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_requests_request_id'), table_name='requests')
    op.create_unique_constraint('requests_request_id_key', 'requests', ['request_id'])
    # ### end Alembic commands ###
