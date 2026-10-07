PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS materials (
    code                    TEXT PRIMARY KEY,      -- e.g. 'BR', 'SL'
    name                    TEXT NOT NULL,         -- word used in Name column, e.g. 'Brass', 'Silver-plated' (never bare 'Silver')
    material_label          TEXT NOT NULL,         -- base "Material" column text, e.g. 'Solid brass', 'Silver plated'
    chain_material          TEXT NOT NULL,         -- e.g. 'Brass', 'Silver plated'
    cleaning_blurb          TEXT NOT NULL,         -- used when the pendant has no gemstone
    gemstone_cleaning_blurb TEXT NOT NULL          -- used when the pendant has a gemstone (care differs: avoid the stone, etc.)
);

CREATE TABLE IF NOT EXISTS gemstones (
    code                TEXT PRIMARY KEY,  -- e.g. 'TE', 'AM', 'ON'
    name                TEXT NOT NULL,     -- e.g. "Tiger's Eye"
    desc_phrase         TEXT NOT NULL,     -- e.g. "golden-brown Tiger's Eye"
    title_suffix        TEXT NOT NULL DEFAULT '',  -- e.g. ", Protection Stone Gift" (include leading comma/space, or '')
    symbolism_paragraph TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS parent_products (
    parent_id             TEXT PRIMARY KEY,      -- e.g. 'ZOD-001'
    name_template         TEXT NOT NULL,         -- contains {MATERIAL}/{GEM}/{SUFFIX} placeholders
    description           TEXT NOT NULL,         -- contains {GEM_DESC}/{SYMBOLISM} placeholders where relevant
    size                  TEXT NOT NULL,         -- e.g. '4.5 x 4.5 cm (H x W)'
    sourcing              TEXT NOT NULL DEFAULT 'India',
    chain_length_override TEXT                   -- overrides the standard '43 cm / 17 inch' choice for designs with one fixed chain length (e.g. a lariat)
);

CREATE TABLE IF NOT EXISTS pendants (
    sku                 TEXT PRIMARY KEY,      -- e.g. 'ZOD-001-BR', 'GEM-001-SL-TE'
    parent_id           TEXT NOT NULL REFERENCES parent_products(parent_id),
    material_code       TEXT NOT NULL REFERENCES materials(code),
    gemstone_code       TEXT REFERENCES gemstones(code),
    price_gbp           REAL NOT NULL DEFAULT 15,
    tags                TEXT NOT NULL DEFAULT '',
    name_override        TEXT,              -- bypasses parent name_template when a SKU's copy can't be templated (e.g. a plain variant sharing a parent with gemstone variants)
    description_override TEXT,
    created_at          TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Multiple photos per pendant are normal; each gets its own row here and
-- pendants_flat below joins them back into one comma-separated "Photo" cell.
CREATE TABLE IF NOT EXISTS photos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    sku             TEXT NOT NULL REFERENCES pendants(sku),
    filename        TEXT NOT NULL,
    sort_order      INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS change_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    logged_at       TEXT NOT NULL DEFAULT (datetime('now')),
    action          TEXT NOT NULL,
    details         TEXT NOT NULL DEFAULT ''
);

DROP VIEW IF EXISTS pendants_flat;
CREATE VIEW pendants_flat AS
SELECT
    p.parent_id                                                        AS "Parent ID",
    p.sku                                                              AS "SKU",
    (SELECT GROUP_CONCAT(ph.filename, ', ')
       FROM (SELECT filename FROM photos
              WHERE sku = p.sku ORDER BY sort_order) ph)                AS "Photo",
    COALESCE(p.name_override, REPLACE(REPLACE(REPLACE(
        pp.name_template,
        '{MATERIAL}', m.name),
        '{GEM}', COALESCE(g.name, '')),
        '{SUFFIX}', COALESCE(g.title_suffix, '')))                     AS "Name",
    COALESCE(p.description_override, REPLACE(REPLACE(
        pp.description,
        '{GEM_DESC}', COALESCE(g.desc_phrase, '')),
        '{SYMBOLISM}', COALESCE(g.symbolism_paragraph, '')))            AS "Description",
    p.price_gbp                                                        AS "Price GBP",
    m.material_label ||
        CASE WHEN EXISTS (
            SELECT 1 FROM pendants p2
             WHERE p2.parent_id = p.parent_id AND p2.material_code <> p.material_code
        ) THEN ', also available in ' ||
               (SELECT LOWER(m2.name) FROM pendants p2
                  JOIN materials m2 ON m2.code = p2.material_code
                 WHERE p2.parent_id = p.parent_id AND p2.material_code <> p.material_code
                 LIMIT 1)
        ELSE '' END                                                     AS "Material",
    COALESCE(g.name, '')                                                AS "Gemstone",
    CASE WHEN g.code IS NOT NULL THEN m.gemstone_cleaning_blurb ELSE m.cleaning_blurb END AS "Cleaning",
    pp.size                                                             AS "Size",
    pp.sourcing                                                         AS "Sourcing",
    'Yes'                                                                AS "Chain included",
    'Snake chain'                                                       AS "Chain type",
    m.chain_material                                                    AS "Chain material",
    COALESCE(pp.chain_length_override, '43 cm / 17 inch')               AS "Chain length",
    'Hook clasp'                                                        AS "Clasp",
    p.tags                                                              AS "Tags"
FROM pendants p
JOIN parent_products pp ON pp.parent_id = p.parent_id
JOIN materials m        ON m.code = p.material_code
LEFT JOIN gemstones g    ON g.code = p.gemstone_code
ORDER BY p.parent_id, p.sku;
