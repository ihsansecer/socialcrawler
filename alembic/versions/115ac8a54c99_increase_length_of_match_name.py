"""
Increase length of match name

Revision ID: 115ac8a54c99
Revises: 1f72e7b6c260
Create Date: 2018-04-22 10:33:35.387590
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115ac8a54c99'
down_revision = '1f72e7b6c260'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('twitter_user', 'match_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=150),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('twitter_user', 'match_name',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    # ### end Alembic commands ###