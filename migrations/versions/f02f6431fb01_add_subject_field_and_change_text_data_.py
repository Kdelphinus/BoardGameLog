"""add subject field and change text_data to content field

Revision ID: f02f6431fb01
Revises: 2c0f140db188
Create Date: 2025-03-08 18:51:30.044748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f02f6431fb01'
down_revision: Union[str, None] = '2c0f140db188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_logs', sa.Column('subject', sa.String(), nullable=False))
    op.add_column('game_logs', sa.Column('content', sa.Text(), nullable=True))
    op.alter_column('game_logs', 'during_time',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('game_logs', 'participant_num',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('game_logs', 'text_data')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_logs', sa.Column('text_data', sa.TEXT(), autoincrement=False, nullable=True))
    op.alter_column('game_logs', 'participant_num',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('game_logs', 'during_time',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('game_logs', 'content')
    op.drop_column('game_logs', 'subject')
    # ### end Alembic commands ###
