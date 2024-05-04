"""empty message

Revision ID: 0fc8964d760a
Revises: 3b73aca7a14c
Create Date: 2024-04-21 22:31:18.953136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fc8964d760a'
down_revision = '3b73aca7a14c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages_table', schema=None) as batch_op:
        batch_op.alter_column('registration_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages_table', schema=None) as batch_op:
        batch_op.alter_column('registration_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###