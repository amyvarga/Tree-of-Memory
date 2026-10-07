"""One-time build + seed of pendants.db from the existing PDF catalogue."""
from db_helpers import get_conn, init_schema, add_material, add_gemstone, add_parent, add_pendant, log_action, DB_PATH

BRASS_CLEANING = (
    "Brass naturally darkens over time and develops an antique patina. Polish gently with "
    "Brasso and a soft cloth for a bright shine, or leave it to age for a vintage look. "
    "Keep it dry and away from perfume and water to slow tarnishing."
)
SILVER_CLEANING = (
    "Gently clean with a silver polishing cloth or silver plated cleaner to restore its shine. "
    "Avoid harsh abrasives, as they can wear the plating."
)
SILVER_GEMSTONE_CLEANING = (
    "Silver tarnishes naturally over time. Gently clean with a silver polishing cloth, avoiding "
    "the stone, and don't use harsh abrasives. Keep away from water, perfume and chlorine. The "
    "oxidised finish is meant to look darker in the recesses, so polish lightly to keep the contrast."
)
BRASS_GEMSTONE_CLEANING = (
    "Brass naturally darkens over time and develops an antique patina. Polish gently with Brasso "
    "and a soft cloth, avoiding the stone, for a bright shine, or leave it to age for a vintage "
    "look. Keep it dry and away from perfume and water to slow tarnishing."
)


def main():
    conn = get_conn()
    init_schema(conn)

    # --- materials -----------------------------------------------------
    add_material(conn, "BR", "Brass", "Solid brass", "Brass", BRASS_CLEANING, BRASS_GEMSTONE_CLEANING)
    add_material(conn, "SL", "Silver-plated", "Silver plated", "Silver plated", SILVER_CLEANING, SILVER_GEMSTONE_CLEANING)

    # --- gemstones -------------------------------------------------------
    add_gemstone(
        conn, "TE", "Tiger's Eye", "golden-brown Tiger's Eye", ", Protection Stone Gift",
        "Tiger's eye is often linked to courage, confidence and protection, which makes this a "
        "popular gift for anyone drawn to crystals and gemstone jewellery. Wear it alone as a "
        "statement piece or layer it with other necklaces for a boho style.",
    )
    add_gemstone(
        conn, "AM", "Amethyst", "amethyst", ", Birthstone Gift",
        "Amethyst is traditionally associated with calm, clarity and balance, and its deep purple "
        "shade makes this pendant a lovely gift for anyone who enjoys meditation and crystal "
        "jewellery. It is also the birthstone for those born in February.",
    )
    add_gemstone(
        conn, "ON", "Onyx", "onyx", "",
        "Onyx is traditionally associated with strength, grounding and protection, and its deep "
        "black shine makes this pendant a bold, versatile gift that goes with almost any outfit.",
    )

    # --- ZOD-001: Tree of Life Zodiac -----------------------------------
    add_parent(
        conn, "ZOD-001",
        "{MATERIAL} Tree of Life Zodiac Pendant Necklace, Celtic Knot Astrology Jewellery",
        "Celebrate your star sign with this Tree of Life zodiac pendant. At its heart is an "
        "intricate Celtic knot tree, its branches reaching up and its roots spreading below, "
        "framed by a ring of astrology symbols. It's a meaningful piece for anyone drawn to "
        "nature, spirituality and the stars.\n\n"
        "The Tree of Life stands for growth, strength and connection, and the twelve zodiac signs "
        "around the edge give it a personal, celestial touch. It makes a thoughtful birthday gift "
        "for her, or a treat for yourself if you love boho, witchy or pagan-inspired jewellery.",
        "4.5 x 4.5 cm (H x W)",
    )
    add_pendant(conn, "ZOD-001-BR", "ZOD-001", "BR", None,
                ["ZOD-001-BR-1.JPG", "ZOD-001-BR-2.JPG", "ZOD-001-BR-3.JPG"],
                tags="Tree of life, zodiac, Celtic knot, brass pendant, gift, boho, witchy, pagan, Yggdrasil, astrology")
    add_pendant(conn, "ZOD-001-SL", "ZOD-001", "SL", None,
                ["ZOD-001-SL-1.JPG", "ZOD-001-SL-2.JPG", "ZOD-001-SL-3.JPG"],
                tags="Tree of life, zodiac, Celtic knot, pendant, gift, boho, witchy, pagan, Yggdrasil, astrology, silver pendant")

    # --- GL-001: Ginkgo Leaf ---------------------------------------------
    add_parent(
        conn, "GL-001",
        "{MATERIAL} Ginkgo Leaf Pendant Necklace, Boho Nature Jewellery",
        "Bring a little nature with you with this brass ginkgo leaf pendant. Its delicate fan "
        "shape and finely etched veins capture the beauty of one of the world's oldest tree "
        "species.\n\n"
        "In many traditions the ginkgo is a symbol of resilience, longevity and hope, which makes "
        "this a meaningful gift for a nature lover or a treat for yourself. Wear it simply for an "
        "everyday boho look, or layer it with other necklaces.",
        "4 x 3.5 cm (H x W)",
    )
    add_pendant(conn, "GL-001-BR", "GL-001", "BR", None,
                ["GL-001-BR-1.JPG", "GL-001-BR-2.JPG"],
                tags="ginkgo leaf, ginkgo biloba, botanical, nature-inspired, leaf necklace, boho, woodland, minimalist, gift for her, nature lover gift, brass pendant")

    # --- TB-001: Tree Branch ----------------------------------------------
    add_parent(
        conn, "TB-001",
        "{MATERIAL} Tree Branch Necklace, Nature Inspired Twig Pendant Jewellery",
        "Carry a little of the woodland with you with this brass branch pendant. Delicate stems "
        "fan out from the top, each ending in a small leaf bud, in an organic design that looks "
        "like a twig, an olive branch or a tree in miniature. The soft matte finish gives it a "
        "warm, earthy glow that suits everyday wear.",
        "4 x 4.5 cm (H x W)",
    )
    add_pendant(conn, "TB-001-BR", "TB-001", "BR", None,
                ["TB-001-BR-1.JPG", "TB-001-BR-2.JPG"],
                tags="branch necklace, olive branch, twig pendant, leaf necklace, botanical jewellery, nature lover gift, boho necklace, woodland, minimalist, brass pendant")

    # --- TRIS-001: Triskele -------------------------------------------------
    add_parent(
        conn, "TRIS-001",
        "{MATERIAL} Triskele Pendant Necklace, Celtic Triple Spiral Jewellery, {MATERIAL} Triskelion Charm",
        "Wear an ancient Celtic symbol with this triskele pendant. Three flowing spirals meet at "
        "the centre inside an open circle, in a clean, simple design that works with everyday "
        "outfits and boho looks alike.\n\n"
        "The triskele, or triple spiral, is one of the oldest symbols in Celtic art. It's often "
        "linked to movement, growth and the connection between past, present and future. Many "
        "people also read it as a symbol of earth, sea and sky, or mind, body and spirit, or "
        "maiden, mother and crone. It makes a meaningful gift for anyone drawn to Irish, Celtic or "
        "pagan traditions, or simply someone who loves spiral designs.",
        "3.5 x 3.5 cm (H x W)",
    )
    add_pendant(conn, "TRIS-001-BR", "TRIS-001", "BR", None,
                ["TRIS-001-BR-1.JPG", "TRIS-001-BR-2.JPG"],
                tags="triskele necklace, triskelion pendant, Celtic jewellery, triple spiral, Irish jewellery, pagan necklace, spiritual gift, boho pendant, symbolic jewellery, brass pendant")
    add_pendant(conn, "TRIS-001-SL", "TRIS-001", "SL", None,
                ["TRIS-001-SL-1.JPG", "TRIS-001-SL-2.JPG"],
                tags="triskele necklace, triskelion pendant, Celtic jewellery, triple spiral, Irish jewellery, pagan necklace, spiritual gift, boho pendant, symbolic jewellery, silver pendant")

    # --- FOL-001: Flower of Life --------------------------------------------
    add_parent(
        conn, "FOL-001",
        "{MATERIAL} Flower of Life Mandala Necklace, Lotus Brass Pendant, Flower of Life Sacred Geometry Jewellery",
        "Add a touch of sacred geometry to your look with this brass mandala pendant. At its heart "
        "is the Flower of Life, set within layers of delicate openwork and an outer ring of "
        "lotus-style petals. It's an intricate, eye-catching piece that works as a statement "
        "necklace or layered with other chains.\n\n"
        "The Flower of Life is an ancient symbol often linked to unity, creation and the "
        "connection of all living things, while the mandala and lotus are associated with "
        "balance, harmony and spiritual growth. It makes a meaningful gift for yoga and "
        "meditation lovers, anyone interested in spirituality, or a treat for yourself if you "
        "love boho and bohemian jewellery.",
        "4.5 x 4.5 cm (H x W)",
    )
    add_pendant(conn, "FOL-001-BR", "FOL-001", "BR", None,
                ["FOL-001-BR-1.JPG", "FOL-001-BR-2.JPG"],
                tags="flower of life pendant, sacred geometry jewellery, lotus necklace, yoga jewellery, spiritual gift, boho pendant, meditation gift, statement pendant, brass pendant")

    # --- ANK-001: Ankh -----------------------------------------------------
    add_parent(
        conn, "ANK-001",
        "{MATERIAL} Ankh Pendant Necklace, Egyptian Symbol of Life Jewellery, Minimalist Ankh Cross",
        "Wear one of the most recognisable symbols of ancient Egypt with this ankh pendant. Its "
        "smooth, simple lines make it easy to wear every day, either on its own or layered with "
        "other necklaces.\n\n"
        "The ankh, also known as the key of life, was used in ancient Egypt to represent life, "
        "vitality and immortality. Today it's worn as a symbol of protection, balance and "
        "spiritual connection. It makes a meaningful gift for anyone who loves Egyptian history, "
        "spiritual jewellery or minimalist style, and its clean design suits both men and women.",
        "4 x 2 cm (H x W)",
    )
    add_pendant(conn, "ANK-001-BR", "ANK-001", "BR", None,
                ["ANK-001-BR-1.JPG", "ANK-001-BR-2.JPG"],
                tags="ankh necklace, ankh pendant, Egyptian jewellery, key of life, ankh cross, spiritual necklace, unisex pendant, minimalist jewellery, symbolic jewellery, brass pendant")
    add_pendant(conn, "ANK-001-SL", "ANK-001", "SL", None,
                ["ANK-001-SL-1.JPG", "ANK-001-SL-2.JPG"],
                tags="ankh necklace, ankh pendant, Egyptian jewellery, key of life, ankh cross, spiritual necklace, unisex pendant, minimalist jewellery, symbolic jewellery, silver pendant")

    # --- OM-001: Om Mandala --------------------------------------------------
    add_parent(
        conn, "OM-001",
        "{MATERIAL} Om Mandala Pendant Necklace, Lotus Yoga Meditation Jewellery, Spiritual Gift",
        "Carry a symbol of peace and mindfulness with this silver Om mandala pendant. The Om sits "
        "at the heart of the design, surrounded by finely detailed patterns and a ring of "
        "lotus-style petals. It's an intricate, eye-catching piece that works as a statement "
        "necklace or layered with other chains.\n\n"
        "Om is a sacred sound and symbol in Hindu, Buddhist and yogic traditions, often linked to "
        "the universe, inner peace and spiritual connection. The mandala and lotus add ideas of "
        "balance, harmony and growth. It makes a meaningful gift for yoga teachers, meditation "
        "lovers and anyone drawn to spirituality, or a treat for yourself if you love boho "
        "jewellery.",
        "4 x 4 cm (H x W)",
    )
    add_pendant(conn, "OM-001-SL", "OM-001", "SL", None,
                ["OM-001-SL-1.JPG", "OM-001-SL-2.JPG"],
                tags="Om necklace, mandala pendant, lotus necklace, yoga jewellery, meditation gift, spiritual jewellery, Om symbol, boho pendant, statement pendant, silver pendant")

    # --- GEM-001: gemstone family --------------------------------------------
    add_parent(
        conn, "GEM-001",
        "{MATERIAL} {GEM} Gemstone Pendant Necklace, Boho Crystal Jewellery{SUFFIX}",
        "A smooth {GEM_DESC} gemstone sits at the centre, framed by a twisted rope border and "
        "rings of tiny granulated beads. The oxidised finish deepens the detail and gives the "
        "stone an antique, bohemian look.\n\n{SYMBOLISM}",
        "2.5 x 2.5 cm (H x W)",
    )
    add_pendant(conn, "GEM-001-SL-TE", "GEM-001", "SL", "TE",
                ["GEM-001-SL-TE-1.JPG", "GEM-001-SL-TE-2.JPG", "GEM-001-SL-TE-3.JPG"],
                tags="tiger's eye pendant, tiger eye necklace, gemstone pendant, crystal jewellery, boho necklace, protection stone, silver pendant, oxidised silver, healing crystal gift")
    add_pendant(conn, "GEM-001-SL-AM", "GEM-001", "SL", "AM",
                ["GEM-001-SL-AM-1.JPG", "GEM-001-SL-AM-2.JPG", "GEM-001-SL-AM-3.JPG"],
                tags="amethyst pendant, amethyst necklace, purple gemstone necklace, February birthstone, birthstone gift, meditation gift, crystal jewellery, boho necklace, silver pendant, oxidised silver")
    add_pendant(conn, "GEM-001-SL-ON", "GEM-001", "SL", "ON",
                ["GEM-001-SL-ON-1.JPG", "GEM-001-SL-ON-2.JPG", "GEM-001-SL-ON-3.JPG"],
                tags="onyx pendant, onyx necklace, black gemstone necklace, grounding stone, protection stone, crystal jewellery, boho necklace, silver pendant, oxidised silver")

    # --- TREE-001: Tree of Life ----------------------------------------------
    add_parent(
        conn, "TREE-001",
        "{MATERIAL} Tree of Life Pendant Necklace, Yggdrasil Family Tree Jewellery, Roots and Branches Design",
        "Carry a symbol of growth and connection with this tree of life pendant. Delicate "
        "branches stretch upwards and deep roots spread below, all held within a clean circular "
        "frame. The open-cut design is light and detailed, so it's easy to wear every day or "
        "layer with other necklaces.\n\n"
        "The tree of life is a symbol found in many cultures, and it's often linked to strength, "
        "family, growth and the connection between earth and sky. This makes it a meaningful gift "
        "for a birthday, a new beginning, Mother's Day or a family occasion, or a treat for "
        "yourself if you love nature-inspired and boho jewellery.",
        "4 x 4 cm (H x W)",
    )
    add_pendant(conn, "TREE-001-BR", "TREE-001", "BR", None,
                ["TREE-001-BR-1.JPG", "TREE-001-BR-2.JPG"],
                tags="tree of life necklace, tree of life pendant, Yggdrasil, family tree necklace, nature jewellery, spiritual gift, boho pendant, roots and branches, Mother's Day gift, brass pendant")

    log_action(conn, "Database created and seeded",
               "Imported existing catalogue from 'Tree of Memory stock - Pendants.pdf': "
               "10 parent designs, 15 SKUs. Standardised all silver wording to 'Silver-plated' "
               "/ 'silver-plated' per house rule (never bare 'Silver'). Note: GEM-001-SL-ON tags "
               "were corrected to onyx-specific keywords (the source PDF had amethyst tags "
               "copy-pasted into the onyx row by mistake).")
    conn.commit()
    conn.close()
    print(f"Built and seeded {DB_PATH}")


if __name__ == "__main__":
    main()
