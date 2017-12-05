"""empty message

Revision ID: 38a8cfc1451
Revises: None
Create Date: 2017-11-30 11:03:27.870698

"""

# revision identifiers, used by Alembic.
revision = '38a8cfc1451'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('nickname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('notify_phone', sa.String(length=20), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('sex', sa.Integer(), server_default='0', nullable=True),
    sa.Column('platform', sa.String(length=20), nullable=True),
    sa.Column('device_id', sa.String(length=40), nullable=True),
    sa.Column('register_ip', sa.String(length=20), nullable=True),
    sa.Column('intro', sa.String(length=300), nullable=True),
    sa.Column('aphorism', sa.String(length=200), nullable=True),
    sa.Column('oauth_from', sa.String(length=20), server_default='', nullable=True),
    sa.Column('oauth_openid', sa.String(length=128), nullable=True),
    sa.Column('oauth_userinfo', sa.Text(), nullable=True),
    sa.Column('oauth_time', sa.DateTime(), nullable=True),
    sa.Column('oauth_nickname', sa.String(length=50), nullable=True),
    sa.Column('oauth_avatar', sa.String(length=200), nullable=True),
    sa.Column('modified', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('created', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_user_device_id'), 'user', ['device_id'], unique=True)

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_device_id'), table_name='user')
    op.drop_table('user')
    ### end Alembic commands ###