"""add study template

Revision ID: 4f53ec506661
Revises: 4302608638bc
Create Date: 2018-05-23 15:44:01.450488

"""

# revision identifiers, used by Alembic.
revision = '4f53ec506661'
down_revision = '4302608638bc'
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
    op.add_column('twitter_user_recruitment_tweet_attempt', sa.Column('study_template', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade_development():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_user_recruitment_tweet_attempt', 'study_template')
    # ### end Alembic commands ###


def upgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_user_recruitment_tweet_attempt', sa.Column('study_template', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade_test():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_user_recruitment_tweet_attempt', 'study_template')
    # ### end Alembic commands ###


def upgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('twitter_user_recruitment_tweet_attempt', sa.Column('study_template', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade_production():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('twitter_user_recruitment_tweet_attempt', 'study_template')
    # ### end Alembic commands ###

