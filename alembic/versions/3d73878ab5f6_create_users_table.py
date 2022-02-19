"""create users table

Revision ID: 3d73878ab5f6
Revises: 
Create Date: 2021-12-28 03:18:45.344611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d73878ab5f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(
                    ), primary_key=True, nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(),
                              unique=True, nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('phone', sa.Integer(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('postal_code', sa.Integer(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(),
                              server_default="False", nullable=False),
                    sa.Column('is_super', sa.Boolean(),
                              server_default="False", nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('NOW()'), nullable=False),
                    sa.Column('updated_at', sa.TIMESTAMP(
                        timezone=True), server_default=sa.text('NOW()'), onupdate=sa.text('NOW()'), nullable=True)
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
