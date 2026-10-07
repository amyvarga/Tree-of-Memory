"""Add the second photo batch delivered 2026-10-07 (unlabelled photos dropped into
pendant_photos/, since renamed by rename_new_photos.py to the SKU convention).
"""
from db_helpers import get_conn, add_material, add_gemstone, add_parent, add_pendant, log_action, DB_PATH

GRT_SYMBOLISM = (
    "Garnet is traditionally associated with strength, passion and protection, and its deep red "
    "sparkle makes this pendant a bold, timeless gift. It is also the birthstone for those born "
    "in January."
)
MAL_SYMBOLISM = (
    "Malachite is known for its striking bands of green, and is traditionally associated with "
    "transformation, protection and balance. It makes a bold, eye-catching gift for anyone who "
    "loves statement crystal jewellery."
)

TRIBAL_INTRO = (
    "Wear a bold statement piece with this tribal medallion pendant. Its {shape} is finely "
    "engraved with sun and moon motifs, in a warm, oxidised antique finish that gives it real "
    "character.\n\n"
    "Inspired by traditional tribal and Rajasthani jewellery, this piece makes a striking "
    "statement necklace, whether worn alone or layered with finer chains. It's a meaningful gift "
    "for anyone who loves bold, ethnic-inspired style."
)
TRIBAL_TAGS = ("tribal medallion necklace, boho statement necklace, engraved pendant, ethnic "
               "jewellery, oxidised brass, bold necklace, Rajasthani jewellery, {shape_tag}, "
               "statement necklace, gift for her")

ZODIAC_SIGNS = {
    # code: (full name, date range, traits)
    "ARI": ("Aries", "21 March - 19 April", "bold, energetic and a natural leader"),
    "TAU": ("Taurus", "20 April - 20 May", "grounded, reliable and a lover of comfort"),
    "GMN": ("Gemini", "21 May - 20 June", "curious, adaptable and quick to communicate"),
    "CAN": ("Cancer", "21 June - 22 July", "intuitive, nurturing and deeply loyal"),
    "LEO": ("Leo", "23 July - 22 August", "confident, warm and generous"),
    "VIR": ("Virgo", "23 August - 22 September", "analytical, practical and kind-hearted"),
    "LIB": ("Libra", "23 September - 22 October", "balanced, diplomatic and a lover of harmony"),
    "SCO": ("Scorpio", "23 October - 21 November", "passionate, intense and resourceful"),
    "SAG": ("Sagittarius", "22 November - 21 December", "adventurous, optimistic and free-spirited"),
    "CAP": ("Capricorn", "22 December - 19 January", "ambitious, disciplined and practical"),
    "AQU": ("Aquarius", "20 January - 18 February", "independent, original and forward-thinking"),
    "PIS": ("Pisces", "19 February - 20 March", "intuitive, compassionate and dreamy"),
}


def main():
    conn = get_conn()

    # --- new gemstones ---------------------------------------------------
    add_gemstone(conn, "GRT", "Garnet", "deep red Garnet", ", January Birthstone Gift", GRT_SYMBOLISM)
    add_gemstone(conn, "MAL", "Malachite", "banded green Malachite", ", Gemstone Gift", MAL_SYMBOLISM)

    # --- LOT-001: two new brass gemstone variants of the existing lotus ----
    add_pendant(conn, "LOT-001-BR-TE", "LOT-001", "BR", "TE",
                ["LOT-001-BR-TE-1.JPG", "LOT-001-BR-TE-2.JPG"],
                tags="lotus necklace, tiger's eye pendant, tiger eye necklace, gemstone pendant, crystal jewellery, boho necklace, protection stone, brass pendant, mystical jewellery, yoga jewellery")
    add_pendant(conn, "LOT-001-BR-ON", "LOT-001", "BR", "ON",
                ["LOT-001-BR-ON-1.JPG"],
                tags="lotus necklace, onyx pendant, onyx necklace, gemstone pendant, crystal jewellery, boho necklace, protection stone, brass pendant, yoga jewellery, statement pendant")

    # --- BEE-001: honeycomb + bee pendant (fixed 46cm chain) ----------------
    add_parent(
        conn, "BEE-001",
        "{MATERIAL} Honeycomb Bee Pendant Necklace, Nature Inspired Jewellery",
        "Carry a little buzz of nature with you with this honeycomb and bee pendant. Two rows of "
        "honeycomb cells frame a finely detailed bee, caught mid-flight, for a charming "
        "nature-inspired design.\n\n"
        "Bees are often seen as a symbol of hard work, community and new beginnings, making this "
        "a thoughtful gift for a gardener, nature lover or anyone who loves bees. It's a sweet, "
        "wearable way to bring a little of the outdoors with you every day.",
        "4 x 2 cm (H x W)",
        chain_length_override="46 cm / 18 inch",
    )
    add_pendant(conn, "BEE-001-BR", "BEE-001", "BR", None,
                ["BEE-001-BR-1.JPG", "BEE-001-BR-2.JPG"],
                tags="bee necklace, honeycomb pendant, nature jewellery, bee pendant, garden lover gift, insect jewellery, boho necklace, brass pendant, nature-inspired, gift for her")

    # --- LEAF-001: leaf lariat necklace (fixed 64cm chain) -------------------
    add_parent(
        conn, "LEAF-001",
        "{MATERIAL} Leaf Lariat Necklace, Layered Botanical Pendant Jewellery",
        "Wear a modern, layered look with this leaf lariat necklace. A single etched leaf sits at "
        "the collarbone, with the chain continuing down into a second matching leaf that drapes "
        "elegantly below.\n\n"
        "The leaf motif brings an easy, nature-inspired feel to any outfit, and the lariat drop "
        "gives it a little extra movement and interest. It makes a lovely gift for a nature "
        "lover, or a treat for yourself if you love layered, boho-style necklaces.",
        "5 x 2 cm (H x W)",
        chain_length_override="64 cm / 25 inch",
    )
    add_pendant(conn, "LEAF-001-BR", "LEAF-001", "BR", None,
                ["LEAF-001-BR-1.JPG", "LEAF-001-BR-2.JPG"],
                tags="leaf necklace, lariat necklace, layered necklace, botanical jewellery, nature lover gift, boho necklace, Y necklace, brass pendant, minimalist jewellery, gift for her")

    # --- LOT-002: lotus petal collar necklace (fixed 52cm chain) -------------
    add_parent(
        conn, "LOT-002",
        "{MATERIAL} Lotus Petal Collar Necklace, Fanned Lotus Pendant Jewellery",
        "Add a delicate, boho touch to your neckline with this lotus petal collar necklace. A fan "
        "of open lotus petals sits along the chain itself, for a light, elegant piece that sits "
        "beautifully at the collarbone.\n\n"
        "The lotus is a symbol of purity, rebirth and spiritual awakening in many traditions, "
        "making this a meaningful gift for anyone drawn to yoga, meditation or boho style, or a "
        "treat for yourself.",
        "2 x 5 cm (H x W)",
        chain_length_override="52 cm / 20.5 inch",
    )
    add_pendant(conn, "LOT-002-BR", "LOT-002", "BR", None,
                ["LOT-002-BR-1.JPG", "LOT-002-BR-2.JPG"],
                tags="lotus necklace, collar necklace, petal necklace, boho necklace, yoga jewellery, minimalist pendant, nature-inspired, brass necklace, delicate necklace, gift for her")

    # --- TMED family: tribal engraved medallions, 4 shapes -------------------
    add_parent(
        conn, "TMED-001",
        "{MATERIAL} Tribal Medallion Cross Pendant Necklace, Engraved Boho Jewellery",
        TRIBAL_INTRO.format(shape="quatrefoil cross shape"),
        "7 x 5.5 cm (H x W)",
    )
    add_pendant(conn, "TMED-001-BR", "TMED-001", "BR", None,
                ["TMED-001-BR-1.JPG", "TMED-001-BR-2.JPG"],
                tags=TRIBAL_TAGS.format(shape_tag="cross pendant"))

    add_parent(
        conn, "TMED-002",
        "{MATERIAL} Tribal Medallion Oval Pendant Necklace, Engraved Boho Jewellery",
        TRIBAL_INTRO.format(shape="elongated oval shape"),
        "7 x 4.5 cm (H x W)",
    )
    add_pendant(conn, "TMED-002-BR", "TMED-002", "BR", None,
                ["TMED-002-BR-1.JPG", "TMED-002-BR-2.JPG"],
                tags=TRIBAL_TAGS.format(shape_tag="oval pendant"))

    add_parent(
        conn, "TMED-003",
        "{MATERIAL} Tribal Medallion Flower Pendant Necklace, Engraved Boho Jewellery",
        TRIBAL_INTRO.format(shape="six-petal flower shape"),
        "6 x 5.5 cm (H x W)",
    )
    add_pendant(conn, "TMED-003-BR", "TMED-003", "BR", None,
                ["TMED-003-BR-1.JPG", "TMED-003-BR-2.JPG"],
                tags=TRIBAL_TAGS.format(shape_tag="flower pendant"))

    add_parent(
        conn, "TMED-004",
        "{MATERIAL} Tribal Medallion Rounded Oval Pendant Necklace, Engraved Boho Jewellery",
        TRIBAL_INTRO.format(shape="rounded oval shape"),
        "5.5 x 6 cm (H x W)",
    )
    add_pendant(conn, "TMED-004-BR", "TMED-004", "BR", None,
                ["TMED-004-BR-1.JPG", "TMED-004-BR-2.JPG"],
                tags=TRIBAL_TAGS.format(shape_tag="rounded oval pendant"))

    # --- SPIR-001: spiral triskele disc pendant -------------------------------
    add_parent(
        conn, "SPIR-001",
        "{MATERIAL} Spiral Disc Pendant Necklace, Triple Spiral Celtic Jewellery",
        "Wear a striking take on an ancient symbol with this spiral disc pendant. A ridged, "
        "sun-like disc is topped with three small spirals and a half-moon bail, for a bold, "
        "textured piece with real presence.\n\n"
        "Spirals are one of the oldest symbols in human history, often linked to growth, energy "
        "and the cycles of life. It makes a meaningful gift for anyone drawn to Celtic, tribal or "
        "sun-symbol jewellery, or a treat for yourself if you love bold, textured statement "
        "pieces.",
        "6 x 5 cm (H x W)",
    )
    add_pendant(conn, "SPIR-001-BR", "SPIR-001", "BR", None,
                ["SPIR-001-BR-1.JPG", "SPIR-001-BR-2.JPG"],
                tags="spiral pendant, sun disc necklace, Celtic jewellery, triple spiral, statement necklace, boho pendant, textured jewellery, brass pendant, symbolic jewellery, bold necklace")

    # --- HAM-001: hamsa hand pendant --------------------------------------------
    add_parent(
        conn, "HAM-001",
        "{MATERIAL} Hamsa Hand Pendant Necklace, Filigree Hand of Fatima Jewellery",
        "Wear a symbol of protection with this hamsa hand pendant. Delicate filigree swirls fill "
        "the hand-shaped silhouette, for a light, detailed piece that's easy to wear every day.\n\n"
        "The hamsa, also known as the Hand of Fatima or Hand of Miriam, is a symbol of "
        "protection, blessings and good fortune found across many cultures and faiths. It makes "
        "a meaningful gift for anyone who loves spiritual or protective jewellery, or a treat for "
        "yourself.",
        "5 x 3 cm (H x W)",
    )
    add_pendant(conn, "HAM-001-BR", "HAM-001", "BR", None,
                ["HAM-001-BR-1.JPG", "HAM-001-BR-2.JPG"],
                tags="hamsa necklace, hand of Fatima, hamsa pendant, protection jewellery, filigree necklace, spiritual necklace, boho pendant, brass pendant, symbolic jewellery, gift for her")

    # --- SEED-003: plain beaded-border seed of life (no gemstone) --------------
    add_parent(
        conn, "SEED-003",
        "{MATERIAL} Seed of Life Pendant Necklace, Beaded Border Sacred Geometry",
        "At the centre of this seed of life pendant is a beaded border and radiating petal "
        "design, giving it a detailed, bohemian look. It's a light, eye-catching piece that works "
        "as a statement necklace or layered with other chains.\n\n"
        "The seed of life is considered the blueprint of creation in sacred geometry, often "
        "linked to growth, balance and the interconnection of all things. It makes a meaningful "
        "gift for anyone interested in spirituality, meditation or sacred geometry, or a treat "
        "for yourself if you love boho, symbolic jewellery.",
        "4 x 4 cm (H x W)",
    )
    add_pendant(conn, "SEED-003-BR", "SEED-003", "BR", None,
                ["SEED-003-BR-1.JPG", "SEED-003-BR-2.JPG"],
                tags="seed of life pendant, sacred geometry jewellery, beaded pendant, spiritual necklace, meditation gift, minimalist pendant, boho necklace, brass pendant, gift for her, symbolic jewellery")

    # --- SEED-004: same beaded-border casting, gemstone variants ---------------
    add_parent(
        conn, "SEED-004",
        "{MATERIAL} {GEM} Seed of Life Pendant Necklace, Beaded Border Sacred Geometry{SUFFIX}",
        "A smooth {GEM_DESC} gemstone sits at the centre of this seed of life pendant, framed by "
        "a beaded border and radiating petal design. It's a detailed, bohemian piece that works "
        "as a statement necklace or layered with other chains.\n\n{SYMBOLISM}",
        "4 x 4 cm (H x W)",
    )
    add_pendant(conn, "SEED-004-BR-AM", "SEED-004", "BR", "AM",
                ["SEED-004-BR-AM-1.JPG", "SEED-004-BR-AM-2.JPG"],
                tags="seed of life pendant, amethyst pendant, amethyst necklace, February birthstone, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, meditation gift, gemstone necklace")
    add_pendant(conn, "SEED-004-BR-GRT", "SEED-004", "BR", "GRT",
                ["SEED-004-BR-GRT-1.JPG", "SEED-004-BR-GRT-2.JPG"],
                tags="seed of life pendant, garnet pendant, garnet necklace, January birthstone, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, statement pendant, gemstone necklace")
    add_pendant(conn, "SEED-004-BR-MAL", "SEED-004", "BR", "MAL",
                ["SEED-004-BR-MAL-1.JPG", "SEED-004-BR-MAL-2.JPG"],
                tags="seed of life pendant, malachite pendant, malachite necklace, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, statement pendant, gemstone necklace")
    add_pendant(conn, "SEED-004-BR-MOON", "SEED-004", "BR", "MOON",
                ["SEED-004-BR-MOON-1.JPG", "SEED-004-BR-MOON-2.JPG"],
                tags="seed of life pendant, moonstone pendant, moonstone necklace, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, lunar jewellery, gemstone necklace")
    add_pendant(conn, "SEED-004-BR-ON", "SEED-004", "BR", "ON",
                ["SEED-004-BR-ON-1.JPG"],
                tags="seed of life pendant, onyx pendant, onyx necklace, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, protection stone, gemstone necklace")
    add_pendant(conn, "SEED-004-BR-TE", "SEED-004", "BR", "TE",
                ["SEED-004-BR-TE-1.JPG"],
                tags="seed of life pendant, tiger's eye pendant, tiger eye necklace, sacred geometry jewellery, crystal jewellery, boho necklace, brass pendant, protection stone, gemstone necklace")

    # --- ZDC-001: zodiac symbol charms, 12 signs x 2 materials -----------------
    add_parent(
        conn, "ZDC-001",
        "{MATERIAL} Zodiac Symbol Charm Necklace, Astrology Pendant Jewellery",
        "Wear your star sign with this delicate zodiac charm necklace. The symbol sits on a fine "
        "chain, for a simple, personal piece that's easy to wear every day.\n\n"
        "A thoughtful birthday gift, or a lovely everyday piece for anyone who loves astrology "
        "and personal, symbolic jewellery.",
        "approx. 2 x 2 cm (H x W)",
    )
    for code, (sign, dates, traits) in ZODIAC_SIGNS.items():
        for material_code, material_name in [("BR", "Brass"), ("SL", "Silver-plated")]:
            sku = f"ZDC-001-{material_code}-{code}"
            add_pendant(
                conn, sku, "ZDC-001", material_code, None,
                [f"ZDC-001-{material_code}-{code}-1.JPG"],
                tags=f"{sign.lower()} necklace, zodiac charm, astrology jewellery, star sign necklace, birthday gift, personal jewellery, minimalist charm, {material_name.lower()} pendant, horoscope jewellery, celestial jewellery",
                name_override=f"{material_name} {sign} Zodiac Symbol Charm Necklace, Astrology Pendant Jewellery",
                description_override=(
                    f"Wear your star sign with this delicate {sign} charm necklace. The {sign} "
                    f"symbol sits on a fine chain, for a simple, personal piece that's easy to "
                    f"wear every day.\n\n"
                    f"{sign} ({dates}) is known for being {traits}. It makes a thoughtful "
                    f"birthday gift, or a lovely everyday piece for anyone who loves astrology "
                    f"and personal, symbolic jewellery."
                ),
            )

    log_action(conn, "Added 2026-10-07 photo batch",
               "Unlabelled photos dropped into pendant_photos/ - identified by viewing each "
               "photo and renamed to the SKU convention (with several corrections from the "
               "user along the way re: which photos belong to the same product, and a later "
               "addition of 4 more zodiac signs completing the full set of 12). Added 10 new "
               "parent designs (BEE-001, LEAF-001, LOT-002, TMED-001/002/003/004, SPIR-001, "
               "HAM-001, SEED-003, SEED-004) and one new multi-SKU collection (ZDC-001, 12 "
               "zodiac signs x 2 materials = 24 SKUs), plus 2 new gemstone variants of the "
               "existing LOT-001 (Tiger's Eye, Onyx). New gemstones added: Garnet, Malachite. "
               "SEED-003 (plain) and SEED-004 (gemstone variants) are the same beaded-border "
               "casting split into two parents, same reasoning as LOT-001/LOT-001-GEM. "
               "BEE-001, LEAF-001 and LOT-002 have fixed chain lengths (46cm, 64cm, 52cm "
               "respectively) instead of the usual 43/53cm choice, via the new "
               "chain_length_override column. 5 duplicate photos were deleted (user confirmed "
               "backup exists).")
    conn.commit()
    conn.close()
    print(f"Updated {DB_PATH}")


if __name__ == "__main__":
    main()
