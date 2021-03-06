"""empty message

Revision ID: a32c72dbce78
Revises: None
Create Date: 2016-06-29 09:45:58.235845

"""

# revision identifiers, used by Alembic.
revision = 'a32c72dbce78'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('fishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Text(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fishes')
    op.drop_table('users')
    ### end Alembic commands ###
