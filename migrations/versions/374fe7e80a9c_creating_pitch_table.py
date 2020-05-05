"""creating pitch table

Revision ID: 374fe7e80a9c
Revises: 07bb05d6b73c
Create Date: 2020-05-04 22:24:37.484241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '374fe7e80a9c'
down_revision = '07bb05d6b73c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(length=255), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    # ### end Alembic commands ###