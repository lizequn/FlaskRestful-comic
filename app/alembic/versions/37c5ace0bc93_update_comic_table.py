"""update comic table

Revision ID: 37c5ace0bc93
Revises: a6739b656741
Create Date: 2022-10-03 15:08:51.487740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c5ace0bc93'
down_revision = 'a6739b656741'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comic', sa.Column('recomm_result', sa.String(length=255), nullable=True))
    op.add_column('comic', sa.Column('version', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comic', 'version')
    op.drop_column('comic', 'recomm_result')
    # ### end Alembic commands ###
