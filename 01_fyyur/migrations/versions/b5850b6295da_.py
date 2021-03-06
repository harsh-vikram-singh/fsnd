"""empty message

Revision ID: b5850b6295da
Revises: 8dd7814f4478
Create Date: 2020-02-22 00:35:23.437728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5850b6295da'
down_revision = '8dd7814f4478'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
    # ### end Alembic commands ###
