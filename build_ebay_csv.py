"""Build the eBay bulk-listing CSV for the 9 new parent designs (2026-10-05 batch),
matching the column structure and conventions of the already-uploaded
'eBay_listings_upload_TreeOfMemory - Pendants.csv'.

Images are referenced via the GitHub raw URLs (pendant_photos pushed to
github.com/amyvarga/Tree-of-Memory) as a stand-in until proper eBay API image
hosting is set up.
"""
import csv
from pathlib import Path

GITHUB_RAW = "https://raw.githubusercontent.com/amyvarga/Tree-of-Memory/main/pendant_photos/"
OUT_PATH = Path(__file__).parent / "eBay" / "eBay_listings_upload_TreeOfMemory - Pendants - NEW.csv"
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


def chain_line(matching_metal):
    suffix = ", in matching metal" if matching_metal else ""
    return (f"Chain: choose a 43 cm (17 inch) or 53 cm (21 inch) snake chain with hook clasp, "
            f"included{suffix}. Photos show the 43 cm chain")


BRASS_CARE = ("Brass naturally darkens over time and develops an antique patina. Polish gently "
              "with Brasso and a soft cloth for a bright shine, or leave it to age for a vintage "
              "look. Keep it dry and away from perfume and water to slow tarnishing.")
SILVER_CARE = ("Gently clean with a silver polishing cloth or silver plated cleaner to restore "
               "its shine. Avoid harsh abrasives, as they can wear the plating.")
SILVER_GEM_CARE = ("Silver tarnishes naturally over time. Gently clean with a silver polishing "
                    "cloth, avoiding the stone, and don't use harsh abrasives. Keep away from "
                    "water, perfume and chlorine. The oxidised finish is meant to look darker in "
                    "the recesses, so polish lightly to keep the contrast.")
BRASS_GEM_CARE = ("Brass naturally darkens over time and develops an antique patina. Polish "
                   "gently with Brasso and a soft cloth, avoiding the stone, for a bright shine, "
                   "or leave it to age for a vintage look. Keep it dry and away from perfume and "
                   "water to slow tarnishing.")


def write_rows(writer):
    # ---- CHAK-001: Metal variation (BR/SL) x Necklace Length -----------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "CHAK-001"
    parent[COL["*Title"]] = "Seven Chakra Pendant Necklace, Lariat Style Yoga Jewellery"
    parent[COL["RelationshipDetails"]] = "Metal=Brass;Silver Plated|Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("CHAK-001-BR-1.JPG, CHAK-001-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Wear all seven chakras in one meaningful piece with this lariat-style necklace. "
        "Seven delicate chakra symbols, from the root to the crown, hang in a line down the "
        "chain, finishing in a small rose charm.</p>"
        "<p>Each chakra represents a different centre of energy in the body, and wearing them "
        "together is a popular way to symbolise balance, alignment and spiritual wellbeing. It "
        "makes a thoughtful gift for yoga teachers, meditation lovers or anyone building a "
        "mindfulness practice, or a treat for yourself if you love boho and spiritual jewellery."
        "</p><p><b>Details</b></p>"
        + details_li("Choose your finish: solid brass or silver plated", "Drop length: 9 cm",
                      chain_line(True), "Country of origin: India")
        + "<p><b>Care</b></p>"
        + f"<p><b>Brass:</b> {BRASS_CARE}</p><p><b>Silver plated:</b> {SILVER_CARE}</p>"
    )
    writer.writerow(parent)
    for metal_code, metal_label, sku in [("Brass", "Brass", "CHAK-001-BR"), ("Silver Plated", "Silver-plated", "CHAK-001-SL")]:
        for length in ["43", "53"]:
            v = blank_row()
            v[COL["CustomLabel"]] = f"{sku}-{length}"
            v[COL["Relationship"]] = "Variation"
            v[COL["RelationshipDetails"]] = f"Metal={metal_code}|Necklace Length={length} cm"
            v[COL["PicURL"]] = f"{metal_code}=" + urls(f"{sku}-1.JPG, {sku}-2.JPG")
            v[COL["*StartPrice"]] = "15.00"
            v[COL["*Quantity"]] = "2"
            writer.writerow(v)

    # ---- LOT-001: plain brass, Necklace Length only ---------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "LOT-001"
    parent[COL["*Title"]] = "Brass Lotus Flower Pendant Necklace, Yoga Meditation Jewellery"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Pendant Shape"]] = "Flower"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("LOT-001-BR-1.JPG, LOT-001-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>An open lotus flower sits at the heart of this pendant, its petals rendered in a "
        "delicate linework silhouette that catches the light beautifully.</p>"
        "<p>The lotus is a symbol of purity, rebirth and spiritual awakening in many traditions, "
        "rising clean and beautiful from the mud. It makes a meaningful gift for yoga "
        "practitioners, meditation lovers or anyone on a spiritual journey, or a treat for "
        "yourself if you love boho and symbolic jewellery.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 5 x 4 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"LOT-001-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "15.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- LOT-001-GEM: silver, Colour(gemstone) x Necklace Length ----------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "LOT-001-GEM"
    parent[COL["*Title"]] = "Gemstone Lotus Flower Pendant Necklace, Yoga Jewellery, Silver Plated Cabochon"
    parent[COL["RelationshipDetails"]] = "Colour=Amethyst;Labradorite;Lapis Lazuli|Necklace Length=43 cm;53 cm"
    parent[COL["C:Metal"]] = "Silver Plated"
    parent[COL["C:Material"]] = "Gemstone"
    parent[COL["C:Main Stone Shape"]] = "Cabochon"
    parent[COL["C:Pendant Shape"]] = "Flower"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("LOT-001-SL-AM-1.JPG, LOT-001-SL-AM-2.JPG")
    parent[COL["*Description"]] = (
        "<p>An open lotus flower sits at the heart of this pendant, its petals rendered in a "
        "delicate linework silhouette, with a smooth gemstone cabochon set at the centre.</p>"
        "<p>The lotus is a symbol of purity, rebirth and spiritual awakening in many traditions, "
        "rising clean and beautiful from the mud.</p>"
        "<p><b>Choose your stone:</b></p>"
        "<p><b>Amethyst</b> is traditionally associated with calm, clarity and balance, and its "
        "deep purple shade makes this pendant a lovely gift for anyone who enjoys meditation and "
        "crystal jewellery. It is also the birthstone for those born in February.</p>"
        "<p><b>Labradorite</b> is known for its flashes of blue and green light within a grey "
        "stone, and is often linked to intuition, transformation and protection.</p>"
        "<p><b>Lapis Lazuli</b> has been prized since ancient times for wisdom, truth and inner "
        "power, and its deep blue colour makes this pendant a striking, timeless piece.</p>"
        "<p>Stones vary slightly in colour and pattern.</p><p><b>Details</b></p>"
        + details_li("Material: silver plated", "Stone: choose amethyst, labradorite or lapis lazuli",
                      "Size: 5 x 4 cm (H x W)", chain_line(False), "Country of origin: India")
        + f"<p><b>Care</b></p><p>{SILVER_GEM_CARE}</p>"
    )
    writer.writerow(parent)
    for gem_name, sku in [("Amethyst", "LOT-001-SL-AM"), ("Labradorite", "LOT-001-SL-LAB"), ("Lapis Lazuli", "LOT-001-SL-LAP")]:
        for length in ["43", "53"]:
            v = blank_row()
            v[COL["CustomLabel"]] = f"{sku}-{length}"
            v[COL["Relationship"]] = "Variation"
            v[COL["RelationshipDetails"]] = f"Colour={gem_name}|Necklace Length={length} cm"
            v[COL["PicURL"]] = f"{gem_name}=" + urls(f"{sku}-1.JPG, {sku}-2.JPG")
            v[COL["*StartPrice"]] = "15.00"
            v[COL["*Quantity"]] = "2"
            writer.writerow(v)

    # ---- SEED-001: single material, Necklace Length only ------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "SEED-001"
    parent[COL["*Title"]] = "Brass Seed of Life Pendant Necklace, Sacred Geometry Jewellery"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Pendant Shape"]] = "Round"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("SEED-001-BR-1.JPG, SEED-001-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Carry a piece of sacred geometry with this seed of life pendant. Seven overlapping "
        "circles form a perfectly balanced flower-like pattern, in a light, open-cut design "
        "that's easy to layer or wear alone.</p>"
        "<p>The seed of life is considered the blueprint of creation in sacred geometry, often "
        "linked to growth, balance and the interconnection of all things. It makes a meaningful "
        "gift for anyone interested in spirituality, meditation or sacred geometry, or a treat "
        "for yourself if you love minimalist, symbolic jewellery.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 4 x 3 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"SEED-001-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "12.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- SIX-001: single material, Necklace Length only --------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "SIX-001"
    parent[COL["*Title"]] = "Brass Six-Pointed Star Pendant Necklace, Interwoven Hexagram Jewellery"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("SIX-001-BR-1.JPG, SIX-001-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Wear a bold piece of sacred geometry with this six-pointed star pendant. "
        "Interlocking bands weave over and under each other to form the hexagram, giving it a "
        "woven, three-dimensional look within a clean circular edge.</p>"
        "<p>The six-pointed star appears across many cultures and spiritual traditions, often "
        "linked to balance, harmony and the union of opposites. It makes a meaningful gift for "
        "anyone drawn to sacred geometry, spiritual symbolism or bold, graphic jewellery.</p>"
        "<p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 4.5 x 3 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"SIX-001-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "12.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- TREE-002: single material, Necklace Length only --------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "TREE-002"
    parent[COL["*Title"]] = "Brass Tree of Life Pendant Necklace, Rounded Branches Design"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Pendant Shape"]] = "Round"
    parent[COL["C:Theme"]] = "Nature"
    parent[COL["PicURL"]] = urls("TREE-002-BR-1.JPG, TREE-002-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Carry a symbol of growth and connection with this tree of life pendant. A simple, "
        "rounded tree sits within a plain circular frame, with a soft, solid silhouette that "
        "gives it a clean, modern take on a classic design.</p>"
        "<p>The tree of life is a symbol found in many cultures, often linked to strength, "
        "family, growth and the connection between earth and sky. This makes it a meaningful "
        "gift for a birthday, a new beginning or a family occasion, or a treat for yourself if "
        "you love nature-inspired and minimalist jewellery.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 4 x 3.2 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"TREE-002-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "12.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- TRIS-002: single material, Necklace Length only --------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "TRIS-002"
    parent[COL["*Title"]] = "Brass Triskele Pendant Necklace, Wave Spiral Celtic Jewellery"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Pendant Shape"]] = "Round"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("TRIS-002-BR-1.JPG, TRIS-002-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Wear another take on an ancient Celtic symbol with this triskele pendant. Three "
        "gently curling, wave-like spirals meet at the centre within a plain round frame, "
        "giving it a softer, more rounded look than a traditional triskele.</p>"
        "<p>The triskele, or triple spiral, is one of the oldest symbols in Celtic art, often "
        "linked to movement, growth and the connection between past, present and future. It "
        "makes a meaningful gift for anyone drawn to Irish, Celtic or pagan traditions, or "
        "simply someone who loves spiral designs.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 4 x 3 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"TRIS-002-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "12.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- FOL-002: single material, Necklace Length only ---------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "FOL-002"
    parent[COL["*Title"]] = "Brass Flower of Life Sun Mandala Pendant Necklace, Sacred Geometry"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Main Stone"]] = "No Stone"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Colour"]] = "Gold"
    parent[COL["C:Pendant Shape"]] = "Round"
    parent[COL["C:Theme"]] = "Signs & Symbols"
    parent[COL["PicURL"]] = urls("FOL-002-BR-1.JPG, FOL-002-BR-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Add a touch of sacred geometry to your look with this sun mandala pendant. At its "
        "heart is the Flower of Life, framed by an ornate sunburst edge that catches the light "
        "beautifully, for a bold, statement-making piece.</p>"
        "<p>The Flower of Life is an ancient symbol often linked to unity, creation and the "
        "connection of all living things. It makes a meaningful gift for yoga and meditation "
        "lovers, anyone interested in spirituality, or a treat for yourself if you love boho and "
        "bohemian jewellery.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Size: 6 x 5.5 cm (H x W)", chain_line(False),
                      "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"FOL-002-BR-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "15.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- MOON-001-BR-TURQ: single material+stone, Necklace Length only ------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "MOON-001"
    parent[COL["*Title"]] = "Brass Crescent Moon Turquoise Pendant Necklace, Boho Celestial Jewellery"
    parent[COL["RelationshipDetails"]] = "Necklace Length=43 cm;53 cm"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Material"]] = "Gemstone"
    parent[COL["C:Main Stone Shape"]] = "Cabochon"
    parent[COL["C:Theme"]] = "Celestial & Horoscope"
    parent[COL["PicURL"]] = urls("CRES-001-BR-TURQ-1.JPG, MOON-001-BR-TURQ-2.JPG")
    parent[COL["*Description"]] = (
        "<p>A pair of smooth turquoise cabochons sit within a crescent moon design, framed by a "
        "beaded border in warm antique brass. It's a bold, eye-catching piece with a boho, "
        "celestial feel.</p>"
        "<p>Turquoise is traditionally associated with protection, good fortune and calm, and "
        "its bright blue-green colour makes this pendant a bold, eye-catching piece for boho "
        "and festival style.</p><p><b>Details</b></p>"
        + details_li("Material: brass with turquoise cabochons", "Size: 5 x 2.5 cm (H x W)",
                      chain_line(False), "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_GEM_CARE}</p>"
    )
    writer.writerow(parent)
    for length in ["43", "53"]:
        v = blank_row()
        v[COL["CustomLabel"]] = f"MOON-001-BR-TURQ-{length}"
        v[COL["Relationship"]] = "Variation"
        v[COL["RelationshipDetails"]] = f"Necklace Length={length} cm"
        v[COL["*StartPrice"]] = "15.00"
        v[COL["*Quantity"]] = "2"
        writer.writerow(v)

    # ---- GEM-002: brass, Colour(gemstone) x Necklace Length -------------------
    parent = common_fields(blank_row())
    parent[COL["*Action(SiteID=UK|Country=GB|Currency=GBP|Version=1193|CC=UTF-8)"]] = "Add"
    parent[COL["CustomLabel"]] = "GEM-002"
    parent[COL["*Title"]] = "Gemstone Pendant Necklace, Boho Scrollwork Jewellery, Brass Cabochon"
    parent[COL["RelationshipDetails"]] = "Colour=Labradorite;Moonstone|Necklace Length=43 cm;53 cm"
    parent[COL["C:Metal"]] = "Brass"
    parent[COL["C:Material"]] = "Gemstone"
    parent[COL["C:Main Stone Shape"]] = "Cabochon"
    parent[COL["C:Pendant Shape"]] = "Round"
    parent[COL["C:Theme"]] = "Bohemian"
    parent[COL["PicURL"]] = urls("GEM-001-BR-LAB-1.JPG, GEM-001-BR-LAB-2.JPG")
    parent[COL["*Description"]] = (
        "<p>Add some colour to your look with this ornate brass gemstone pendant. A smooth "
        "cabochon sits at the centre, framed by an ornate scrollwork border in warm antique "
        "brass. It's a detailed, bohemian piece that works as a statement necklace or layered "
        "with other chains.</p>"
        "<p><b>Choose your stone:</b></p>"
        "<p><b>Labradorite</b> is known for its flashes of blue and green light within a grey "
        "stone, and is often linked to intuition, transformation and protection.</p>"
        "<p><b>Moonstone</b> has long been associated with intuition, new beginnings and "
        "feminine energy, and its soft glow makes it a popular choice for those who love dreamy, "
        "ethereal jewellery.</p>"
        "<p>Stones vary slightly in colour and pattern.</p><p><b>Details</b></p>"
        + details_li("Material: solid brass", "Stone: choose labradorite or moonstone",
                      "Size: 4.5 x 2 cm (H x W)", chain_line(False), "Country of origin: India")
        + f"<p><b>Care</b></p><p>{BRASS_GEM_CARE}</p>"
    )
    writer.writerow(parent)
    for gem_name, sku, files in [
        ("Labradorite", "GEM-002-BR-LAB", "GEM-001-BR-LAB-1.JPG, GEM-001-BR-LAB-2.JPG"),
        ("Moonstone", "GEM-002-BR-MOON", "GEM-001-BR-MOON-1.JPG, GEM-001-BR-MOON-2.JPG"),
    ]:
        for length in ["43", "53"]:
            v = blank_row()
            v[COL["CustomLabel"]] = f"{sku}-{length}"
            v[COL["Relationship"]] = "Variation"
            v[COL["RelationshipDetails"]] = f"Colour={gem_name}|Necklace Length={length} cm"
            v[COL["PicURL"]] = f"{gem_name}=" + urls(files)
            v[COL["*StartPrice"]] = "15.00"
            v[COL["*Quantity"]] = "2"
            writer.writerow(v)


def main():
    with open(TEMPLATE_PATH, newline="", encoding="utf-8-sig") as f:
        template_rows = list(csv.reader(f))
    info_rows = template_rows[:1]  # the "Info Version=..." line

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for r in info_rows:
            writer.writerow(r)
        writer.writerow(HEADER)
        write_rows(writer)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
