"""empty message

Revision ID: d850e6a84680
Revises: 
Create Date: 2018-10-22 00:25:13.590944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd850e6a84680'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=False),
    sa.Column('isStandalone', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('restaurant_id', 'id', name='menu_item__pk')
    )
    op.create_table('modifier',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('main_item_id', sa.Integer(), nullable=False),
    sa.Column('modifier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id', 'main_item_id'], ['menu_item.restaurant_id', 'menu_item.id'], name='main_item__menu_item__fk', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['restaurant_id', 'modifier_id'], ['menu_item.restaurant_id', 'menu_item.id'], name='modifier__menu_item__fk', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('restaurant_id', 'main_item_id', 'modifier_id', name='modifier__pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modifier')
    op.drop_table('menu_item')
    # ### end Alembic commands ###