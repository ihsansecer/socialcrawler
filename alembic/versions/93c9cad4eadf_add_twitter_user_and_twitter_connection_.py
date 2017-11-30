"""
Add twitter user and twitter connection tables

Revision ID: 93c9cad4eadf
Revises: 
Create Date: 2017-11-30 15:00:54.885649
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93c9cad4eadf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twitter_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('screen_name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=160), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('twitter_connection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=True),
    sa.Column('to_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['from_user_id'], ['twitter_user.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], ['twitter_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('twitter_connection')
    op.drop_table('twitter_user')
    # ### end Alembic commands ###