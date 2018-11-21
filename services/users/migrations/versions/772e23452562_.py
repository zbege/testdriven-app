"""empty message

Revision ID: 772e23452562
Revises: b8e4f6affebb
Create Date: 2018-11-21 17:24:02.177819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '772e23452562'
down_revision = 'b8e4f6affebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255)))
    op.execute('UPDATE users SET password=email')
    op.alter_column('users', 'password', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###