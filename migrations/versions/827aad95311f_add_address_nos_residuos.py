"""add address nos residuos

Revision ID: 827aad95311f
Revises: 72ddd240548a
Create Date: 2022-04-29 20:30:07.041068
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '827aad95311f'
down_revision = '72ddd240548a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'residues',
        sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_foreign_key(None, 'residues', 'address', ['address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'residues', type_='foreignkey')
    op.drop_column('residues', 'address_id')
    # ### end Alembic commands ###
