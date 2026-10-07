"""Build the eBay bulk-listing CSV for everything still unposted as of 2026-10-07:
the whole second photo batch (BEE-001, LEAF-001, LOT-002, TMED-001/002/003/004,
SPIR-001, HAM-001, SEED-003, SEED-004, ZDC-001) plus the two new brass gemstone
variants of LOT-001 (which need their own listing since the live LOT-001 listing
is fixed to "no stone" and LOT-001-GEM is fixed to Silver Plated).

Already-live listings (2026-10-05 batch: CHAK-001, LOT-001, LOT-001-GEM, SEED-001,
SIX-001, TREE-002, TRIS-002, FOL-002, MOON-001, GEM-002) are NOT included here -
confirmed live with ItemIDs in eBay/Results/.

Fix applied vs the first batch: a variation's PicURL is only set on its first
Necklace Length row (43cm), left blank on the 53cm row, to avoid the "Duplicate
Variation specific value ... in variation specific picture set" warning eBay
raised on LOT-001-GEM and GEM-002 last time.
"""
import csv
from pathlib import Path

GITHUB_RAW = "https://raw.githubusercontent.com/amyvarga/Tree-of-Memory/main/pendant_photos/"
OUT_PATH = Path(__file__).parent / "eBay" / "eBay_listings_upload_TreeOfMemory - Pendants - 2026-10-07.csv"
TEMPLATE_PATH = Path(__file__).parent / "eBay" / "eBay-category-listing-template-Oct-5-2026-17-14-46.csv"

HEADER = [
    "*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)", "CustomLabel", "*Category",
    "StoreCategory", "*Title", "Subtitle", "Relationship", "RelationshipDetails", "ScheduleTime",
    "*ConditionID", "VAT%", "*C:Brand", "*C:Style", "*C:Type", "C:Main Stone", "C:Metal",
    "C:Main Stone Colour", "C:Colour", "C:Setting Style", "C:Material", "C:Materials sourced from",
    "C:Main Stone Shape", "C:Main Stone Creation", "C:Department", "C:Metal Purity",
    "C:Diamond Colour Grade", "C:Coloured Diamond Intensity", "C:Diamond Clarity Grade",
    "C:Necklace Length", "C:Main Stone Treatment", "C:Total Carat Weight", "C:Secondary Stone",
    "C:Base Metal", "C:Pendant/Locket Type", "C:Pendant Shape", "C:Number of Diamonds",
    "C:Number of Gemstones", "C:Theme", "C:Country of Origin", "C:Chain Type", "C:Closure",
    "C:Personalise", "C:Seller Warranty", "C:Signed", "C:Vintage", "C:Features",
    "C:Gemstone Clarity Grade", "C:Era", "C:MPN", "C:Unit Quantity", "C:Unit Type",
    "C:Personalisation Instructions", "PicURL", "GalleryType", "VideoID", "*Description", "*Format",
    "*Duration", "*StartPrice", "BuyItNowPrice", "BestOfferEnabled", "BestOfferAutoAcceptPrice",
    "MinimumBestOfferPrice", "*Quantity", "ImmediatePayRequired", "*Location", "ShippingType",
    "ShippingService-1:Option", "ShippingService-1:Cost", "ShippingService-2:Option",
    "ShippingService-2:Cost", "*DispatchTimeMax", "PromotionalShippingDiscount",
    "ShippingDiscountProfileID", "DomesticRateTable", "*ReturnsAcceptedOption",
    "ReturnsWithinOption", "RefundOption", "ShippingCostPaidByOption", "AdditionalDetails",
    "Product Safety Pictograms", "Product Safety Statements", "Product Safety Component",
    "Regulatory Document Ids", "Manufacturer Name", "Manufacturer AddressLine1",
    "Manufacturer AddressLine2", "Manufacturer City", "Manufacturer Country",
    "Manufacturer PostalCode", "Manufacturer StateOrProvince", "Manufacturer Phone",
    "Manufacturer Email", "Manufacturer ContactURL", "Responsible Person 1",
    "Responsible Person 1 Type", "Responsible Person 1 AddressLine1",
    "Responsible Person 1 AddressLine2", "Responsible Person 1 City",
    "Responsible Person 1 Country", "Responsible Person 1 PostalCode",
    "Responsible Person 1 StateOrProvince", "Responsible Person 1 Phone",
    "Responsible Person 1 Email", "Responsible Person 1 ContactURL", "ShippingProfileName",
    "ReturnProfileName", "PaymentProfileName",
]
COL = {name: i for i, name in enumerate(HEADER)}


def blank_row():
    return [""] * len(HEADER)


def common_fields(row):
    row[COL["*Category"]] = "110655"
    row[COL["*ConditionID"]] = "1000"
    row[COL["*C:Brand"]] = "Unbranded"
    row[COL["*C:Style"]] = "Pendant"
    row[COL["*C:Type"]] = "Necklace"
    row[COL["C:Materials sourced from"]] = "India"
    row[COL["C:Country of Origin"]] = "India"
    row[COL["C:Chain Type"]] = "Snake"
    row[COL["C:Closure"]] = "Hook"
    row[COL["C:MPN"]] = "Does not apply"
    row[COL["*Format"]] = "FixedPrice"
    row[COL["*Duration"]] = "GTC"
    row[COL["*Location"]] = "Totnes"
    row[COL["ShippingProfileName"]] = "UK Tracked 2 Day Dispatch"
    row[COL["ReturnProfileName"]] = "No Returns"
    row[COL["PaymentProfileName"]] = "Standard Payment"
    return row


def urls(filenames):
    return "|".join(GITHUB_RAW + f for f in filenames.split(", "))


def details_li(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def chain_line_variable(matching_metal=False):
    suffix = ", in matching metal" if matching_metal else ""
    return (f"Chain: choose a 43 cm (17 inch) or 53 cm (21 inch) snake chain with hook clasp, "
            f"included{suffix}. Photos show the 43 cm chain")


def chain_line_fixed(length_cm, length_inch):
    return f"Chain: {length_cm} cm ({length_inch} inch) snake chain with hook clasp, included"


BRASS_CARE = ("Brass naturally darkens over time and develops an antique patina. Polish gently "
              "with Brasso and a soft cloth for a bright shine, or leave it to age for a vintage "
              "look. Keep it dry and away from perfume and water to slow tarnishing.")
SILVER_CARE = ("Gently clean with a silver polishing cloth or silver plated cleaner to restore "
               "its shine. Avoid harsh abrasives, as they can wear the plating.")
BRASS_GEM_CARE = ("Brass naturally darkens over time and develops an antique patina. Polish "
                   "gently with Brasso and a soft cloth, avoiding the stone, for a bright shine, "
                   "or leave it to age for a vintage look. Keep it dry and away from perfume and "
                   "water to slow tarnishing.")

TRIBAL_INTRO = (
    "Wear a bold statement piece with this tribal medallion pendant. Its {shape} is finely "
    "engraved with sun and moon motifs, in a warm, oxidised antique finish that gives it real "
    "character.\n\n"
    "Inspired by traditional tribal and Rajasthani jewellery, this piece makes a striking "
    "statement necklace, whether worn alone or layered with finer chains. It's a meaningful gift "
    "for anyone who loves bold, ethnic-inspired style."
)

ZODIAC_ORDER = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
                 "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
ZODIAC_CODES = {"Aries": "ARI", "Taurus": "TAU", "Gemini": "GMN", "Cancer": "CAN", "Leo": "LEO",
                 "Virgo": "VIR", "Libra": "LIB", "Scorpio": "SCO", "Sagittarius": "SAG",
                 "Capricorn": "CAP", "Aquarius": "AQU", "Pisces": "PIS"}


def variation_listing_single_material(writer, custom_label, title, description, size_line,
                                       theme, price, photos_filename_str, sku_suffix,
                                       shape_specifics=None):
    """Single-material parent with just a 43/53cm Necklace Length variation."""
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = custom_label
    parent[COL["*Title"]] = title
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Theme"]] = theme
    if shape_specifics:
        for k, v in shape_specifics.items():
            parent[COL[k]] = v
    parent[COL["PicURL"]] = urls(photos_filename_str)
    parent[COL["*Description"]] = (
        f"{description}<p><b>Details</b></p>"
        + details_li("Material: solid brass", size_line, chain_line_variable(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"{sku_suffix}-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = f"{price:.2f}"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)


def main():
    with open(TEMPLATE_PATH, newline="", encoding="utf-8-sig") as f:
        info_row = next(csv.reader(f))

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(info_row)
        writer.writerow(HEADER)

        # --- BEE-001, LEAF-001 & LOT-002: simple listings, fixed chain lengths ---
        for custom_label, title, desc, size_line, length_cm, length_inch, price, photos, theme in [
            ("BEE-001-BR", "Brass Honeycomb Bee Pendant Necklace, Nature Inspired Jewellery",
             "<p>Carry a little buzz of nature with you with this honeycomb and bee pendant. "
             "Two rows of honeycomb cells frame a finely detailed bee, caught mid-flight, for a "
             "charming nature-inspired design.</p>"
             "<p>Bees are often seen as a symbol of hard work, community and new beginnings, "
             "making this a thoughtful gift for a gardener, nature lover or anyone who loves "
             "bees. It's a sweet, wearable way to bring a little of the outdoors with you every "
             "day.</p>",
             "Size: 4 x 2 cm (H x W)", "46", "18", 15.0, "BEE-001-BR-1.JPG, BEE-001-BR-2.JPG", "Nature"),
            ("LEAF-001-BR", "Brass Leaf Lariat Necklace, Layered Botanical Pendant Jewellery",
             "<p>Wear a modern, layered look with this leaf lariat necklace. A single etched "
             "leaf sits at the collarbone, with the chain continuing down into a second "
             "matching leaf that drapes elegantly below.</p>"
             "<p>The leaf motif brings an easy, nature-inspired feel to any outfit, and the "
             "lariat drop gives it a little extra movement and interest. It makes a lovely gift "
             "for a nature lover, or a treat for yourself if you love layered, boho-style "
             "necklaces.</p>",
             "Size: 5 x 2 cm (H x W)", "64", "25", 15.0, "LEAF-001-BR-1.JPG, LEAF-001-BR-2.JPG", "Nature"),
            ("LOT-002-BR", "Brass Lotus Petal Collar Necklace, Fanned Lotus Pendant Jewellery",
             "<p>Add a delicate, boho touch to your neckline with this lotus petal collar "
             "necklace. A fan of open lotus petals sits along the chain itself, for a light, "
             "elegant piece that sits beautifully at the collarbone.</p>"
             "<p>The lotus is a symbol of purity, rebirth and spiritual awakening in many "
             "traditions, making this a meaningful gift for anyone drawn to yoga, meditation or "
             "boho style, or a treat for yourself.</p>",
             "Size: 2 x 5 cm (H x W)", "52", "20.5", 15.0, "LOT-002-BR-1.JPG, LOT-002-BR-2.JPG", "Signs & Symbols"),
        ]:
            row = common_fields(blank_row())
            row[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
            row[COL["CustomLabel"]] = custom_label
            row[COL["*Title"]] = title
            row[COL["C:Main Stone"]] = "No Stone"
            row[COL["C:Metal"]] = "Brass"
            row[COL["C:Colour"]] = "Gold"
            row[COL["C:Theme"]] = theme
            row[COL["PicURL"]] = urls(photos)
            row[COL["*Description"]] = (
                f"{desc}<p><b>Details</b></p>"
                + details_li("Material: solid brass", size_line,
                              chain_line_fixed(length_cm, length_inch), "Country of origin: India")
                + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
            )
            row[COL["*StartPrice"]] = f"{price:.2f}"
            row[COL["*Quantity"]] = "2"
            writer.writerow(row)

        # --- TMED family: tribal medallions, 4 shapes, standard variation -------
        for parent_id, shape_name, shape_desc, size_line, photos in [
            ("TMED-001", "Cross", "quatrefoil cross shape", "Size: 7 x 5.5 cm (H x W)", "TMED-001-BR-1.JPG, TMED-001-BR-2.JPG"),
            ("TMED-002", "Oval", "elongated oval shape", "Size: 7 x 4.5 cm (H x W)", "TMED-002-BR-1.JPG, TMED-002-BR-2.JPG"),
            ("TMED-003", "Flower", "six-petal flower shape", "Size: 6 x 5.5 cm (H x W)", "TMED-003-BR-1.JPG, TMED-003-BR-2.JPG"),
            ("TMED-004", "Rounded Oval", "rounded oval shape", "Size: 5.5 x 6 cm (H x W)", "TMED-004-BR-1.JPG, TMED-004-BR-2.JPG"),
        ]:
            variation_listing_single_material(
                writer, parent_id,
                f"Brass Tribal Medallion {shape_name} Pendant Necklace, Engraved Boho Jewellery",
                f"<p>{TRIBAL_INTRO.format(shape=shape_desc)}</p>".replace("\n\n", "</p><p>"),
                size_line, "Bohemian", 15.0, photos, f"{parent_id}-BR",
            )

        # --- SPIR-001: spiral disc pendant --------------------------------------
        variation_listing_single_material(
            writer, "SPIR-001",
            "Brass Spiral Disc Pendant Necklace, Triple Spiral Celtic Jewellery",
            "<p>Wear a striking take on an ancient symbol with this spiral disc pendant. A "
            "ridged, sun-like disc is topped with three small spirals and a half-moon bail, for "
            "a bold, textured piece with real presence.</p>"
            "<p>Spirals are one of the oldest symbols in human history, often linked to growth, "
            "energy and the cycles of life. It makes a meaningful gift for anyone drawn to "
            "Celtic, tribal or sun-symbol jewellery, or a treat for yourself if you love bold, "
            "textured statement pieces.</p>",
            "Size: 6 x 5 cm (H x W)", "Signs & Symbols", 15.0,
            "SPIR-001-BR-1.JPG, SPIR-001-BR-2.JPG", "SPIR-001-BR",
        )

        # --- HAM-001: hamsa hand pendant ----------------------------------------
        variation_listing_single_material(
            writer, "HAM-001",
            "Brass Hamsa Hand Pendant Necklace, Filigree Hand of Fatima Jewellery",
            "<p>Wear a symbol of protection with this hamsa hand pendant. Delicate filigree "
            "swirls fill the hand-shaped silhouette, for a light, detailed piece that's easy to "
            "wear every day.</p>"
            "<p>The hamsa, also known as the Hand of Fatima or Hand of Miriam, is a symbol of "
            "protection, blessings and good fortune found across many cultures and faiths. It "
            "makes a meaningful gift for anyone who loves spiritual or protective jewellery, or "
            "a treat for yourself.</p>",
            "Size: 5 x 3 cm (H x W)", "Signs & Symbols", 15.0,
            "HAM-001-BR-1.JPG, HAM-001-BR-2.JPG", "HAM-001-BR",
        )

        # --- SEED-003: plain beaded-border seed of life -------------------------
        variation_listing_single_material(
            writer, "SEED-003",
            "Brass Seed of Life Pendant Necklace, Beaded Border Sacred Geometry",
            "<p>At the centre of this seed of life pendant is a beaded border and radiating "
            "petal design, giving it a detailed, bohemian look. It's a light, eye-catching piece "
            "that works as a statement necklace or layered with other chains.</p>"
            "<p>The seed of life is considered the blueprint of creation in sacred geometry, "
            "often linked to growth, balance and the interconnection of all things. It makes a "
            "meaningful gift for anyone interested in spirituality, meditation or sacred "
            "geometry, or a treat for yourself if you love boho, symbolic jewellery.</p>",
            "Size: 4 x 4 cm (H x W)", "Signs & Symbols", 15.0,
            "SEED-003-BR-1.JPG, SEED-003-BR-2.JPG", "SEED-003-BR",
        )

        # --- SEED-004: beaded-border seed of life, 6 gemstone variants ----------
        parent = common_fields(blank_row())
        parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
        parent[COL["CustomLabel"]] = "SEED-004"
        parent[COL["*Title"]] = "Gemstone Seed of Life Pendant Necklace, Boho Sacred Geometry, Brass Cabochon"
        parent[COL["RelationshipDetails"]] = "Colour=Amethyst;Garnet;Malachite;Moonstone;Onyx;Tiger's Eye|Necklace Length=43 cm;53 cm"
        parent[COL["C:Metal"]] = "Brass"
        parent[COL["C:Material"]] = "Gemstone"
        parent[COL["C:Main Stone Shape"]] = "Cabochon"
        parent[COL["C:Theme"]] = "Bohemian"
        parent[COL["PicURL"]] = urls("SEED-004-BR-AM-1.JPG, SEED-004-BR-AM-2.JPG")
        parent[COL["*Description"]] = (
            "<p>A smooth gemstone cabochon sits at the centre of this seed of life pendant, "
            "framed by a beaded border and radiating petal design. It's a detailed, bohemian "
            "piece that works as a statement necklace or layered with other chains.</p>"
            "<p><b>Choose your stone:</b></p>"
            "<p><b>Amethyst</b> is traditionally associated with calm, clarity and balance, and "
            "its deep purple shade makes this pendant a lovely gift for anyone who enjoys "
            "meditation and crystal jewellery. It is also the birthstone for those born in "
            "February.</p>"
            "<p><b>Garnet</b> is traditionally associated with strength, passion and "
            "protection, and its deep red sparkle makes this pendant a bold, timeless gift. It "
            "is also the birthstone for those born in January.</p>"
            "<p><b>Malachite</b> is known for its striking bands of green, and is traditionally "
            "associated with transformation, protection and balance.</p>"
            "<p><b>Moonstone</b> has long been associated with intuition, new beginnings and "
            "feminine energy, and its soft glow makes it a popular choice for those who love "
            "dreamy, ethereal jewellery.</p>"
            "<p><b>Onyx</b> is traditionally associated with strength, grounding and "
            "protection, and its deep black shine makes this pendant a bold, versatile gift.</p>"
            "<p><b>Tiger's Eye</b> is often linked to courage, confidence and protection, which "
            "makes this a popular gift for anyone drawn to crystals and gemstone jewellery.</p>"
            "<p>Stones vary slightly in colour and pattern.</p><p><b>Details</b></p>"
            + details_li("Material: solid brass",
                          "Stone: choose amethyst, garnet, malachite, moonstone, onyx or tiger's eye",
                          "Size: 4 x 4 cm (H x W)", chain_line_variable(False),
                          "Country of origin: India")
            + f"<p><b>Care</b></p><p>{BRASS_GEM_CARE}</p>"
        )
        writer.writerow(parent)
        for gem_name, sku, files in [
            ("Amethyst", "SEED-004-BR-AM", "SEED-004-BR-AM-1.JPG, SEED-004-BR-AM-2.JPG"),
            ("Garnet", "SEED-004-BR-GRT", "SEED-004-BR-GRT-1.JPG, SEED-004-BR-GRT-2.JPG"),
            ("Malachite", "SEED-004-BR-MAL", "SEED-004-BR-MAL-1.JPG, SEED-004-BR-MAL-2.JPG"),
            ("Moonstone", "SEED-004-BR-MOON", "SEED-004-BR-MOON-1.JPG, SEED-004-BR-MOON-2.JPG"),
            ("Onyx", "SEED-004-BR-ON", "SEED-004-BR-ON-1.JPG"),
            ("Tiger's Eye", "SEED-004-BR-TE", "SEED-004-BR-TE-1.JPG"),
        ]:
            for i, length in enumerate(["43", "53"]):
                v = blank_row()
                v[COL["CustomLabel"]] = f"{sku}-{length}"
                v[COL["Relationship"]] = "Variation"
                v[COL["RelationshipDetails"]] = f"Colour={gem_name}|Necklace Length={length} cm"
                if i == 0:  # only set PicURL once per gemstone, on the 43cm row
                    v[COL["PicURL"]] = f"{gem_name}=" + urls(files)
                v[COL["*StartPrice"]] = "15.00"
                v[COL["*Quantity"]] = "2"
                writer.writerow(v)

        # --- LOT-001-GEM-BR: new brass gemstone variants of the lotus -----------
        # (separate listing: the live LOT-001 is fixed "no stone", LOT-001-GEM is
        # fixed Silver Plated - neither fits a brass+gemstone combo)
        parent = common_fields(blank_row())
        parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
        parent[COL["CustomLabel"]] = "LOT-001-GEM-BR"
        parent[COL["*Title"]] = "Gemstone Lotus Flower Pendant Necklace, Yoga Jewellery, Brass Cabochon"
        parent[COL["RelationshipDetails"]] = "Colour=Tiger's Eye;Onyx|Necklace Length=43 cm;53 cm"
        parent[COL["C:Metal"]] = "Brass"
        parent[COL["C:Material"]] = "Gemstone"
        parent[COL["C:Main Stone Shape"]] = "Cabochon"
        parent[COL["C:Pendant Shape"]] = "Flower"
        parent[COL["C:Theme"]] = "Signs & Symbols"
        parent[COL["PicURL"]] = urls("LOT-001-BR-TE-1.JPG, LOT-001-BR-TE-2.JPG")
        parent[COL["*Description"]] = (
            "<p>An open lotus flower sits at the heart of this pendant, its petals rendered in "
            "a delicate linework silhouette, with a smooth gemstone cabochon set at the centre."
            "</p>"
            "<p>The lotus is a symbol of purity, rebirth and spiritual awakening in many "
            "traditions, rising clean and beautiful from the mud.</p>"
            "<p><b>Choose your stone:</b></p>"
            "<p><b>Tiger's Eye</b> is often linked to courage, confidence and protection, which "
            "makes this a popular gift for anyone drawn to crystals and gemstone jewellery.</p>"
            "<p><b>Onyx</b> is traditionally associated with strength, grounding and "
            "protection, and its deep black shine makes this pendant a bold, versatile gift.</p>"
            "<p>Stones vary slightly in colour and pattern.</p><p><b>Details</b></p>"
            + details_li("Material: solid brass", "Stone: choose tiger's eye or onyx",
                          "Size: 5 x 4 cm (H x W)", chain_line_variable(False),
                          "Country of origin: India")
            + f"<p><b>Care</b></p><p>{BRASS_GEM_CARE}</p>"
        )
        writer.writerow(parent)
        for gem_name, sku, files in [
            ("Tiger's Eye", "LOT-001-BR-TE", "LOT-001-BR-TE-1.JPG, LOT-001-BR-TE-2.JPG"),
            ("Onyx", "LOT-001-BR-ON", "LOT-001-BR-ON-1.JPG"),
        ]:
            for i, length in enumerate(["43", "53"]):
                v = blank_row()
                v[COL["CustomLabel"]] = f"{sku}-{length}"
                v[COL["Relationship"]] = "Variation"
                v[COL["RelationshipDetails"]] = f"Colour={gem_name}|Necklace Length={length} cm"
                if i == 0:
                    v[COL["PicURL"]] = f"{gem_name}=" + urls(files)
                v[COL["*StartPrice"]] = "15.00"
                v[COL["*Quantity"]] = "2"
                writer.writerow(v)

        # --- ZDC-001: zodiac charms, split by material to avoid a 3-way variation -
        # (split per material since images vary by BOTH metal and sign, and eBay's
        # variation picture mechanism only keys off one aspect cleanly - Colour)
        for material_code, material_name, custom_label in [("BR", "Brass", "ZDC-001-BR"), ("SL", "Silver Plated", "ZDC-001-SL")]:
            parent = common_fields(blank_row())
            parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
            parent[COL["CustomLabel"]] = custom_label
            parent[COL["*Title"]] = f"{material_name} Zodiac Symbol Charm Necklace, Astrology Pendant Jewellery"
            parent[COL["RelationshipDetails"]] = f"Colour={';'.join(ZODIAC_ORDER)}|Necklace Length=43 cm;53 cm"
            parent[COL["C:Metal"]] = material_name
            parent[COL["C:Main Stone"]] = "No Stone"
            parent[COL["C:Theme"]] = "Celestial & Horoscope"
            parent[COL["PicURL"]] = urls(f"ZDC-001-{material_code}-ARI-1.JPG")
            parent[COL["*Description"]] = (
                "<p>Wear your star sign with this delicate zodiac charm necklace. The symbol "
                "sits on a fine chain, for a simple, personal piece that's easy to wear every "
                "day.</p>"
                "<p>A thoughtful birthday gift, or a lovely everyday piece for anyone who loves "
                "astrology and personal, symbolic jewellery.</p><p><b>Details</b></p>"
                + details_li(f"Material: {'solid brass' if material_code == 'BR' else 'silver plated'}",
                              "Sign: choose from all 12 zodiac signs - "
                              + ", ".join(ZODIAC_ORDER),
                              "Size: approx. 2 x 2 cm (H x W)", chain_line_variable(False),
                              "Country of origin: India")
                + f"<p><b>Care</b></p><p>{BRASS_CARE if material_code == 'BR' else SILVER_CARE}</p>"
            )
            writer.writerow(parent)
            for sign in ZODIAC_ORDER:
                code = ZODIAC_CODES[sign]
                sku = f"ZDC-001-{material_code}-{code}"
                for i, length in enumerate(["43", "53"]):
                    v = blank_row()
                    v[COL["CustomLabel"]] = f"{sku}-{length}"
                    v[COL["Relationship"]] = "Variation"
                    v[COL["RelationshipDetails"]] = f"Colour={sign}|Necklace Length={length} cm"
                    if i == 0:
                        v[COL["PicURL"]] = f"{sign}=" + urls(f"{sku}-1.JPG")
                    v[COL["*StartPrice"]] = "15.00"
                    v[COL["*Quantity"]] = "2"
                    writer.writerow(v)

    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
