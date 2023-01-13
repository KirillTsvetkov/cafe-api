"""init

Revision ID: ec498eaf27dc
Revises: 
Create Date: 2023-01-13 14:38:59.366811

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'ec498eaf27dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_category_title'), 'category', ['title'], unique=False)
    op.create_table('customer',
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    op.create_index(op.f('ix_customer_phone'), 'customer', ['phone'], unique=False)
    op.create_table('order',
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_code'), 'order', ['code'], unique=False)
    op.create_index(op.f('ix_order_date'), 'order', ['date'], unique=False)
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_index(op.f('ix_order_status'), 'order', ['status'], unique=False)
    op.create_index(op.f('ix_order_total'), 'order', ['total'], unique=False)
    op.create_table('cart',
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_customer_id'), 'cart', ['customer_id'], unique=False)
    op.create_index(op.f('ix_cart_id'), 'cart', ['id'], unique=False)
    op.create_table('food',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_food_category_id'), 'food', ['category_id'], unique=False)
    op.create_index(op.f('ix_food_description'), 'food', ['description'], unique=False)
    op.create_index(op.f('ix_food_id'), 'food', ['id'], unique=False)
    op.create_index(op.f('ix_food_title'), 'food', ['title'], unique=False)
    op.create_table('cartitem',
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('food_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cartitem_cart_id'), 'cartitem', ['cart_id'], unique=False)
    op.create_index(op.f('ix_cartitem_food_id'), 'cartitem', ['food_id'], unique=False)
    op.create_index(op.f('ix_cartitem_id'), 'cartitem', ['id'], unique=False)
    op.create_index(op.f('ix_cartitem_quantity'), 'cartitem', ['quantity'], unique=False)
    op.create_index(op.f('ix_cartitem_subtotal'), 'cartitem', ['subtotal'], unique=False)
    op.create_table('orderitem',
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('food_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orderitem_food_id'), 'orderitem', ['food_id'], unique=False)
    op.create_index(op.f('ix_orderitem_id'), 'orderitem', ['id'], unique=False)
    op.create_index(op.f('ix_orderitem_order_id'), 'orderitem', ['order_id'], unique=False)
    op.create_index(op.f('ix_orderitem_quantity'), 'orderitem', ['quantity'], unique=False)
    op.create_index(op.f('ix_orderitem_subtotal'), 'orderitem', ['subtotal'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orderitem_subtotal'), table_name='orderitem')
    op.drop_index(op.f('ix_orderitem_quantity'), table_name='orderitem')
    op.drop_index(op.f('ix_orderitem_order_id'), table_name='orderitem')
    op.drop_index(op.f('ix_orderitem_id'), table_name='orderitem')
    op.drop_index(op.f('ix_orderitem_food_id'), table_name='orderitem')
    op.drop_table('orderitem')
    op.drop_index(op.f('ix_cartitem_subtotal'), table_name='cartitem')
    op.drop_index(op.f('ix_cartitem_quantity'), table_name='cartitem')
    op.drop_index(op.f('ix_cartitem_id'), table_name='cartitem')
    op.drop_index(op.f('ix_cartitem_food_id'), table_name='cartitem')
    op.drop_index(op.f('ix_cartitem_cart_id'), table_name='cartitem')
    op.drop_table('cartitem')
    op.drop_index(op.f('ix_food_title'), table_name='food')
    op.drop_index(op.f('ix_food_id'), table_name='food')
    op.drop_index(op.f('ix_food_description'), table_name='food')
    op.drop_index(op.f('ix_food_category_id'), table_name='food')
    op.drop_table('food')
    op.drop_index(op.f('ix_cart_id'), table_name='cart')
    op.drop_index(op.f('ix_cart_customer_id'), table_name='cart')
    op.drop_table('cart')
    op.drop_index(op.f('ix_order_total'), table_name='order')
    op.drop_index(op.f('ix_order_status'), table_name='order')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_index(op.f('ix_order_date'), table_name='order')
    op.drop_index(op.f('ix_order_code'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_customer_phone'), table_name='customer')
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_category_title'), table_name='category')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
