"""Reusable helpers for building and maintaining pendants.db.

Usage pattern for adding new stock:
    import sqlite3
    from db_helpers import get_conn, add_pendant, log_action

    conn = get_conn()
    add_pendant(conn, sku="MOON-001-BR", parent_id="MOON-001",
                material_code="BR", gemstone_code=None,
                photos=["MOON-001-BR-1.JPG", "MOON-001-BR-2.JPG"],
                price_gbp=15, tags="moon phase pendant, ...")
    log_action(conn, "Added variant", "MOON-001-BR (new material of existing design)")
    conn.commit()
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "pendants.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_conn(db_path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_PATH.read_text())


def add_material(conn, code, name, material_label, chain_material, cleaning_blurb, gemstone_cleaning_blurb):
    conn.execute(
        """INSERT OR REPLACE INTO materials
           (code, name, material_label, chain_material, cleaning_blurb, gemstone_cleaning_blurb)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (code, name, material_label, chain_material, cleaning_blurb, gemstone_cleaning_blurb),
    )


def add_gemstone(conn, code, name, desc_phrase, title_suffix, symbolism_paragraph):
    conn.execute(
        """INSERT OR REPLACE INTO gemstones
           (code, name, desc_phrase, title_suffix, symbolism_paragraph)
           VALUES (?, ?, ?, ?, ?)""",
        (code, name, desc_phrase, title_suffix, symbolism_paragraph),
    )


def add_parent(conn, parent_id, name_template, description, size, sourcing="India"):
    conn.execute(
        """INSERT OR REPLACE INTO parent_products
           (parent_id, name_template, description, size, sourcing)
           VALUES (?, ?, ?, ?, ?)""",
        (parent_id, name_template, description, size, sourcing),
    )


def add_pendant(conn, sku, parent_id, material_code, gemstone_code, photos,
                 price_gbp=15, tags="", name_override=None, description_override=None):
    conn.execute(
        """INSERT OR REPLACE INTO pendants
           (sku, parent_id, material_code, gemstone_code, price_gbp, tags, name_override, description_override)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (sku, parent_id, material_code, gemstone_code, price_gbp, tags, name_override, description_override),
    )
    conn.execute("DELETE FROM photos WHERE sku = ?", (sku,))
    for i, filename in enumerate(photos, start=1):
        conn.execute(
            "INSERT INTO photos (sku, filename, sort_order) VALUES (?, ?, ?)",
            (sku, filename, i),
        )


def log_action(conn, action, details=""):
    conn.execute(
        "INSERT INTO change_log (action, details) VALUES (?, ?)",
        (action, details),
    )
