"""Add the new pendant photos delivered 2026-10-05 (folder: Ebay/05.10.26/Pendant photos).

Existing SKUs found in that folder are skipped (already in the database from the
original PDF import); only genuinely new SKUs are added here.
"""
from db_helpers import get_conn, add_material, add_gemstone, add_parent, add_pendant, log_action, DB_PATH

LAB_SYMBOLISM = (
    "Labradorite is known for its flashes of blue and green light within a grey stone, and is "
    "often linked to intuition, transformation and protection. It makes a meaningful gift for "
    "anyone drawn to mystical or spiritual jewellery."
)
MOON_SYMBOLISM = (
    "Moonstone has long been associated with intuition, new beginnings and feminine energy, and "
    "its soft glow makes it a popular choice for those who love dreamy, ethereal jewellery."
)
LAP_SYMBOLISM = (
    "Lapis lazuli has been prized since ancient times for wisdom, truth and inner power, and its "
    "deep blue colour makes this pendant a striking, timeless piece."
)
TURQ_SYMBOLISM = (
    "Turquoise is traditionally associated with protection, good fortune and calm, and its bright "
    "blue-green colour makes this pendant a bold, eye-catching piece for boho and festival style."
)


def main():
    conn = get_conn()

    # --- new gemstones ---------------------------------------------------
    add_gemstone(conn, "LAB", "Labradorite", "labradorite", ", Mystical Gemstone Gift", LAB_SYMBOLISM)
    add_gemstone(conn, "MOON", "Moonstone", "moonstone", ", Lunar Gemstone Gift", MOON_SYMBOLISM)
    add_gemstone(conn, "LAP", "Lapis Lazuli", "lapis lazuli", ", Gemstone Gift", LAP_SYMBOLISM)
    add_gemstone(conn, "TURQ", "Turquoise", "turquoise", ", Protection Stone Gift", TURQ_SYMBOLISM)

    # --- CHAK-001: Seven Chakra lariat -----------------------------------
    add_parent(
        conn, "CHAK-001",
        "{MATERIAL} Seven Chakra Pendant Necklace, Lariat Style Yoga Jewellery",
        "Wear all seven chakras in one meaningful piece with this lariat-style necklace. Seven "
        "delicate chakra symbols, from the root to the crown, hang in a line down the chain, "
        "finishing in a small rose charm.\n\n"
        "Each chakra represents a different centre of energy in the body, and wearing them "
        "together is a popular way to symbolise balance, alignment and spiritual wellbeing. It "
        "makes a thoughtful gift for yoga teachers, meditation lovers or anyone building a "
        "mindfulness practice, or a treat for yourself if you love boho and spiritual jewellery.",
        "9 cm drop length",
    )
    add_pendant(conn, "CHAK-001-BR", "CHAK-001", "BR", None,
                ["CHAK-001-BR-1.JPG", "CHAK-001-BR-2.JPG"],
                tags="chakra necklace, seven chakra pendant, lariat necklace, yoga jewellery, meditation gift, spiritual jewellery, energy healing, boho pendant, mindfulness gift, brass pendant")
    add_pendant(conn, "CHAK-001-SL", "CHAK-001", "SL", None,
                ["CHAK-001-SL-1.JPG", "CHAK-001-SL-2.JPG"],
                tags="chakra necklace, seven chakra pendant, lariat necklace, yoga jewellery, meditation gift, spiritual jewellery, energy healing, boho pendant, mindfulness gift, silver pendant")

    # --- LOT-001: Lotus flower (plain brass + 3 silver gemstone variants) ---
    add_parent(
        conn, "LOT-001",
        "{MATERIAL} Lotus Flower Pendant Necklace, Yoga Meditation Jewellery{SUFFIX}",
        "An open lotus flower sits at the heart of this pendant, its petals rendered in a delicate "
        "linework silhouette, with a smooth {GEM_DESC} gemstone set at the centre.\n\n"
        "The lotus is a symbol of purity, rebirth and spiritual awakening in many traditions, "
        "rising clean and beautiful from the mud. {SYMBOLISM}",
        "5 x 4 cm (H x W)",
    )
    add_pendant(conn, "LOT-001-BR", "LOT-001", "BR", None,
                ["LOT-001-BR-1.JPG", "LOT-001-BR-2.JPG"],
                tags="lotus necklace, lotus pendant, yoga jewellery, meditation gift, spiritual jewellery, boho pendant, minimalist pendant, nature-inspired, gift for her, brass pendant",
                name_override="Brass Lotus Flower Pendant Necklace, Yoga Meditation Jewellery",
                description_override=(
                    "An open lotus flower sits at the heart of this pendant, its petals rendered "
                    "in a delicate linework silhouette that catches the light beautifully.\n\n"
                    "The lotus is a symbol of purity, rebirth and spiritual awakening in many "
                    "traditions, rising clean and beautiful from the mud. It makes a meaningful "
                    "gift for yoga practitioners, meditation lovers or anyone on a spiritual "
                    "journey, or a treat for yourself if you love boho and symbolic jewellery."
                ))
    add_pendant(conn, "LOT-001-SL-AM", "LOT-001", "SL", "AM",
                ["LOT-001-SL-AM-1.JPG", "LOT-001-SL-AM-2.JPG"],
                tags="lotus necklace, amethyst pendant, amethyst necklace, February birthstone, birthstone gift, yoga jewellery, meditation gift, crystal jewellery, boho necklace, silver pendant")
    add_pendant(conn, "LOT-001-SL-LAB", "LOT-001", "SL", "LAB",
                ["LOT-001-SL-LAB-1.JPG", "LOT-001-SL-LAB-2.JPG"],
                tags="lotus necklace, labradorite pendant, labradorite necklace, gemstone pendant, crystal jewellery, yoga jewellery, meditation gift, boho necklace, silver pendant, mystical jewellery")
    add_pendant(conn, "LOT-001-SL-LAP", "LOT-001", "SL", "LAP",
                ["LOT-001-SL-LAP-1.JPG", "LOT-001-SL-LAP-2.JPG"],
                tags="lotus necklace, lapis lazuli pendant, lapis lazuli necklace, gemstone pendant, crystal jewellery, yoga jewellery, meditation gift, boho necklace, silver pendant")

    # --- SEED-001: Seed of Life -------------------------------------------
    add_parent(
        conn, "SEED-001",
        "{MATERIAL} Seed of Life Pendant Necklace, Sacred Geometry Jewellery",
        "Carry a piece of sacred geometry with this seed of life pendant. Seven overlapping "
        "circles form a perfectly balanced flower-like pattern, in a light, open-cut design "
        "that's easy to layer or wear alone.\n\n"
        "The seed of life is considered the blueprint of creation in sacred geometry, often "
        "linked to growth, balance and the interconnection of all things. It makes a meaningful "
        "gift for anyone interested in spirituality, meditation or sacred geometry, or a treat "
        "for yourself if you love minimalist, symbolic jewellery.",
        "4 x 3 cm (H x W)",
    )
    add_pendant(conn, "SEED-001-BR", "SEED-001", "BR", None,
                ["SEED-001-BR-1.JPG", "SEED-001-BR-2.JPG"], price_gbp=12,
                tags="seed of life pendant, sacred geometry jewellery, spiritual necklace, meditation gift, minimalist pendant, boho necklace, symbolic jewellery, geometric necklace, brass pendant, gift for her")

    # --- SIX-001: Six-pointed star / interwoven hexagram --------------------
    add_parent(
        conn, "SIX-001",
        "{MATERIAL} Six-Pointed Star Pendant Necklace, Interwoven Hexagram Jewellery",
        "Wear a bold piece of sacred geometry with this six-pointed star pendant. Interlocking "
        "bands weave over and under each other to form the hexagram, giving it a woven, "
        "three-dimensional look within a clean circular edge.\n\n"
        "The six-pointed star appears across many cultures and spiritual traditions, often linked "
        "to balance, harmony and the union of opposites. It makes a meaningful gift for anyone "
        "drawn to sacred geometry, spiritual symbolism or bold, graphic jewellery.",
        "4.5 x 3 cm (H x W)",
    )
    add_pendant(conn, "SIX-001-BR", "SIX-001", "BR", None,
                ["SIX-001-BR-1.JPG", "SIX-001-BR-2.JPG"], price_gbp=12,
                tags="six pointed star necklace, hexagram pendant, sacred geometry jewellery, star necklace, spiritual jewellery, geometric pendant, boho necklace, statement pendant, symbolic jewellery, brass pendant")

    # --- TREE-002: Tree of Life (rounded branches design) --------------------
    add_parent(
        conn, "TREE-002",
        "{MATERIAL} Tree of Life Pendant Necklace, Rounded Branches Design",
        "Carry a symbol of growth and connection with this tree of life pendant. A simple, "
        "rounded tree sits within a plain circular frame, with a soft, solid silhouette that "
        "gives it a clean, modern take on a classic design.\n\n"
        "The tree of life is a symbol found in many cultures, often linked to strength, family, "
        "growth and the connection between earth and sky. This makes it a meaningful gift for a "
        "birthday, a new beginning or a family occasion, or a treat for yourself if you love "
        "nature-inspired and minimalist jewellery.",
        "4 x 3.2 cm (H x W)",
    )
    add_pendant(conn, "TREE-002-BR", "TREE-002", "BR", None,
                ["TREE-002-BR-1.JPG", "TREE-002-BR-2.JPG"], price_gbp=12,
                tags="tree of life necklace, tree of life pendant, family tree necklace, nature jewellery, minimalist pendant, spiritual gift, boho pendant, brass pendant, gift for her, nature lover gift")

    # --- TRIS-002: Triskele (wave spiral design) ------------------------------
    add_parent(
        conn, "TRIS-002",
        "{MATERIAL} Triskele Pendant Necklace, Wave Spiral Celtic Jewellery",
        "Wear another take on an ancient Celtic symbol with this triskele pendant. Three gently "
        "curling, wave-like spirals meet at the centre within a plain round frame, giving it a "
        "softer, more rounded look than a traditional triskele.\n\n"
        "The triskele, or triple spiral, is one of the oldest symbols in Celtic art, often linked "
        "to movement, growth and the connection between past, present and future. It makes a "
        "meaningful gift for anyone drawn to Irish, Celtic or pagan traditions, or simply someone "
        "who loves spiral designs.",
        "4 x 3 cm (H x W)",
    )
    add_pendant(conn, "TRIS-002-BR", "TRIS-002", "BR", None,
                ["TRIS-002-BR-1.JPG", "TRIS-002-BR-2.JPG"], price_gbp=12,
                tags="triskele necklace, triskelion pendant, Celtic jewellery, triple spiral, Irish jewellery, pagan necklace, spiritual gift, boho pendant, symbolic jewellery, brass pendant")

    # --- FOL-002: Flower of Life sun mandala --------------------------------
    add_parent(
        conn, "FOL-002",
        "{MATERIAL} Flower of Life Sun Mandala Pendant Necklace, Sacred Geometry Jewellery",
        "Add a touch of sacred geometry to your look with this sun mandala pendant. At its heart "
        "is the Flower of Life, framed by an ornate sunburst edge that catches the light "
        "beautifully, for a bold, statement-making piece.\n\n"
        "The Flower of Life is an ancient symbol often linked to unity, creation and the "
        "connection of all living things. It makes a meaningful gift for yoga and meditation "
        "lovers, anyone interested in spirituality, or a treat for yourself if you love boho and "
        "bohemian jewellery.",
        "6 x 5.5 cm (H x W)",
    )
    add_pendant(conn, "FOL-002-BR", "FOL-002", "BR", None,
                ["FOL-002-BR-1.JPG", "FOL-002-BR-2.JPG"],
                tags="flower of life pendant, sacred geometry jewellery, sun mandala necklace, statement pendant, yoga jewellery, spiritual gift, boho pendant, meditation gift, brass pendant, sunburst necklace")

    # --- MOON-001: Crescent moon + turquoise --------------------------------
    add_parent(
        conn, "MOON-001",
        "{MATERIAL} Crescent Moon Turquoise Pendant Necklace, Boho Celestial Jewellery{SUFFIX}",
        "A pair of smooth {GEM_DESC} cabochons sit within a crescent moon design, framed by a "
        "beaded border in warm antique brass. It's a bold, eye-catching piece with a boho, "
        "celestial feel.\n\n{SYMBOLISM}",
        "5 x 2.5 cm (H x W)",
    )
    # CRES-001-BR-TURQ-1.JPG and MOON-001-BR-TURQ-2.JPG were two photos of the
    # same pendant filed under two different parent codes - merged per instruction.
    add_pendant(conn, "MOON-001-BR-TURQ", "MOON-001", "BR", "TURQ",
                ["CRES-001-BR-TURQ-1.JPG", "MOON-001-BR-TURQ-2.JPG"],
                tags="crescent moon necklace, turquoise pendant, turquoise necklace, boho necklace, celestial jewellery, protection stone, festival jewellery, brass pendant, statement pendant, gemstone necklace")

    # --- GEM-002: scrollwork-border gemstone pendants (brass) ----------------
    add_parent(
        conn, "GEM-002",
        "{MATERIAL} {GEM} Gemstone Pendant Necklace, Boho Scrollwork Jewellery{SUFFIX}",
        "A smooth {GEM_DESC} gemstone sits at the centre of this pendant, framed by an ornate "
        "scrollwork border in warm antique brass. It's a detailed, bohemian piece that works as a "
        "statement necklace or layered with other chains.\n\n{SYMBOLISM}",
        "4.5 x 2 cm (H x W)",
    )
    add_pendant(conn, "GEM-002-BR-LAB", "GEM-002", "BR", "LAB",
                ["GEM-001-BR-LAB-1.JPG", "GEM-001-BR-LAB-2.JPG"],
                tags="labradorite pendant, labradorite necklace, gemstone pendant, crystal jewellery, boho necklace, scrollwork jewellery, brass pendant, mystical jewellery, statement pendant")
    add_pendant(conn, "GEM-002-BR-MOON", "GEM-002", "BR", "MOON",
                ["GEM-001-BR-MOON-1.JPG", "GEM-001-BR-MOON-2.JPG"],
                tags="moonstone pendant, moonstone necklace, gemstone pendant, crystal jewellery, boho necklace, scrollwork jewellery, brass pendant, lunar jewellery, statement pendant")

    log_action(conn, "Added 2026-10-05 photo batch",
               "Source folder: 'Ebay/05.10.26/Pendant photos'. Added 8 new parent designs "
               "(CHAK-001, LOT-001, SEED-001, SIX-001, TREE-002, TRIS-002, FOL-002, MOON-001) "
               "and a new parent GEM-002 split out from GEM-001-BR-LAB/MOON (different physical "
               "design: scrollwork border vs rope-and-bead border), 12 new SKUs total. "
               "CRES-001-BR-TURQ-1.JPG and MOON-001-BR-TURQ-2.JPG merged into one SKU "
               "(MOON-001-BR-TURQ) per instruction - same pendant, two photos filed under "
               "different codes. Existing SKUs already in the folder (ANK-001-*, FOL-001-BR, "
               "GEM-001-SL-*, GL-001-BR, OM-001-SL, TB-001-BR, TREE-001-BR, TRIS-001-*, ZOD-001-*) "
               "were left untouched as they were already in the database. Prices: TREE-002, "
               "TRIS-002, SEED-001, SIX-001 = £12 (user-specified); all others default £15.")
    conn.commit()
    conn.close()
    print(f"Updated {DB_PATH}")


if __name__ == "__main__":
    main()
