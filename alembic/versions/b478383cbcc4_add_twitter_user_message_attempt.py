"""Add twitter user message attempt

Revision ID: b478383cbcc4
Revises: 7b8a9e7f8c9f
Create Date: 2017-12-04 01:00:21.854323

"""

# revision identifiers, used by Alembic.
revision = 'b478383cbcc4'
down_revision = '7b8a9e7f8c9f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_development():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twitter_user_message_attempt',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('message_id', sa.String(length=64), nullable=True),
    sa.Column('account_found', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_development():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('twitter_user_message_attempt')
    # ### end Alembic commands ###


def upgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twitter_user_message_attempt',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('message_id', sa.String(length=64), nullable=True),
    sa.Column('account_found', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('twitter_user_message_attempt')
    # ### end Alembic commands ###


def upgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twitter_user_message_attempt',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('message_id', sa.String(length=64), nullable=True),
    sa.Column('account_found', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('twitter_user_message_attempt')
    # ### end Alembic commands ###

