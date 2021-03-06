"""Added user about me and last seen columns

Revision ID: 739076e31d9b
Revises: 9726daf19d1b
Create Date: 2019-07-11 15:37:31.966024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '739076e31d9b'
down_revision = '9726daf19d1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
