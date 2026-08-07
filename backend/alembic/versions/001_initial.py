from alembic import op
import sqlalchemy as sa

revision = "001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("password_hash", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("height", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("goal_weight", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)

    op.create_table(
        "nutrition",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("calories", sa.Integer(), nullable=True),
        sa.Column("proteins", sa.Integer(), nullable=True),
        sa.Column("hydration", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index(op.f("ix_nutrition_id"), "nutrition", ["id"], unique=False)

    op.create_table(
        "training",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("session_type", sa.String(), nullable=True),
        sa.Column("notes", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index(op.f("ix_training_id"), "training", ["id"], unique=False)

    op.create_table(
        "progress",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("muscle_mass", sa.String(), nullable=True),
        sa.Column("comment", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index(op.f("ix_progress_id"), "progress", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_progress_id"), table_name="progress")
    op.drop_table("progress")
    op.drop_index(op.f("ix_training_id"), table_name="training")
    op.drop_table("training")
    op.drop_index(op.f("ix_nutrition_id"), table_name="nutrition")
    op.drop_table("nutrition")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
