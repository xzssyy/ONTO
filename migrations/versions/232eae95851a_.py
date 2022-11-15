"""empty message

Revision ID: 232eae95851a
Revises: 
Create Date: 2022-11-07 09:53:14.321949

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '232eae95851a'
down_revision = None
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
    op.drop_table('ontologytags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ontologytags',
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ontology_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', 'ontology_id', 'tag_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('ontologyTags')
    # ### end Alembic commands ###