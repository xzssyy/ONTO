"""empty message

Revision ID: c1416d126ebb
Revises: 232eae95851a
Create Date: 2022-11-07 09:56:07.264376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1416d126ebb'
down_revision = '232eae95851a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ontologyTags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ontology_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ontologyTags')
    # ### end Alembic commands ###
