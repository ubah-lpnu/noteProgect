"""'v.4.1'

Revision ID: 1c2b616ab50d
Revises: 6d5d7ed0e43a
Create Date: 2022-11-07 01:44:01.441476

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1c2b616ab50d'
down_revision = '6d5d7ed0e43a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'dateOfEditing',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('users', 'numOfNotes',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'numOfEditingNotes',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('users', 'dateOfCreating',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'dateOfCreating',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('users', 'numOfEditingNotes',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('users', 'numOfNotes',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('notes', 'dateOfEditing',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###