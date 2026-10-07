"""Rename the unlabelled UUID photos added 2026-10-07 into the shop's SKU
filename convention, and discard the identified duplicate shots."""
import shutil
from pathlib import Path

LOCAL_DIR = Path("/Users/amyvarga/Tree of Memory/pendant_photos")
SOURCE_DIR = Path("/Users/amyvarga/Documents/Beam Beam Digital /Clients/Tree of Memory/Ebay/05.10.26/Pendant photos")

# uuid -> new filename (without extension's case changes; keep .JPG)
RENAMES = {
    # BEE-001: honeycomb + bee pendant
    "c991a009-b9e1-41c5-8628-6431ca7edc80": "BEE-001-BR-1",
    "68ab6c6f-49ee-440f-8ec5-fa9263556607": "BEE-001-BR-2",
    # LEAF-001: leaf lariat necklace
    "f5c15b2c-2373-4934-8a21-a11dc1096bdb": "LEAF-001-BR-1",
    "71e1b9c8-094a-4349-b6e9-7f4eef582197": "LEAF-001-BR-2",
    # LOT-002: lotus petal fan/collar necklace
    "612c0757-08d0-43e7-93d4-a11221f5f10d": "LOT-002-BR-1",
    "7f30cb00-0778-4b69-b358-44826dc11c25": "LOT-002-BR-2",
    # TMED-001: tribal medallion, cross shape
    "023a03f8-0a8e-4464-87f0-0752547c5ebb": "TMED-001-BR-1",
    "39c02f23-c84f-42af-b936-da9c13389428": "TMED-001-BR-2",
    "d46b44e1-5f9d-40bb-bc00-dff7063d7aef": "TMED-001-BR-3",
    # TMED-002: tribal medallion, oval shape
    "ae56184d-2726-4df2-8694-0fccc94baa5d": "TMED-002-BR-1",
    "fe38c35a-4d11-488d-8363-b0594e061f40": "TMED-002-BR-2",
    "bf354030-ca3e-4a4d-845d-0fbe1a62662c": "TMED-002-BR-3",
    # TMED-003: tribal medallion, flower shape
    "809e12ef-a423-4a25-b8b6-630527d6f674": "TMED-003-BR-1",
    "f0f34124-3ac5-4178-875c-1b8872a81a03": "TMED-003-BR-2",
    # SPIR-001: spiral triskele disc pendant
    "053c5bd6-0f39-4edf-945e-0e0fa22ed1cf": "SPIR-001-BR-1",
    "abbbaef9-e04c-4d79-bb1f-b719c538d1e7": "SPIR-001-BR-2",
    # HAM-001: hamsa hand pendant
    "d96c7cf4-c909-408c-ba25-d8c5bed55668": "HAM-001-BR-1",
    "e2535d6d-d45d-4beb-be59-1ad1cc5668d6": "HAM-001-BR-2",
    # LOT-001 new gemstone variants (existing parent)
    "0785253f-6e96-4cda-82c2-d6e1424fdac4": "LOT-001-BR-TE-1",
    "1c4cc329-2858-4d83-b8cc-3a18a0e75f80": "LOT-001-BR-TE-2",
    "3c4166cf-a0ab-4cb8-a84b-c89f4a0719a5": "LOT-001-BR-ON-1",
    # SEED-002: beaded-border seed of life (plain + gemstone variants)
    "041013bd-93a3-46dc-9149-aac37bbd90ae": "SEED-002-BR-1",
    "0528a676-323e-4c11-9d7b-b104a57146dc": "SEED-002-BR-2",
    "3f21551e-e189-42ab-931b-a1f2760b1d4a": "SEED-002-BR-GRT-1",
    "52de6c69-9939-4c2c-921d-0885d6cf9944": "SEED-002-BR-GRT-2",
    "5924dfa8-47da-41af-958e-4477f7c3bc4b": "SEED-002-BR-TE-1",
    "3ddb3bbb-5a0e-4ca0-97f4-c7ff9845297f": "SEED-002-BR-ON-1",
    "d687b709-935b-4b04-aa00-9cd8d74246d4": "SEED-002-BR-MOON-1",
    "2618967a-8b17-4d56-96c3-b6d16b6fc816": "SEED-002-BR-MOON-2",
    "8425706c-b645-47e4-9a6f-d2c4e1d7eea4": "SEED-002-BR-MAL-1",
    "ec1d1792-997e-4e72-9d31-67e7cc8ae57f": "SEED-002-BR-MAL-2",
    "2e3cae6a-d54f-4632-a82d-9dcb6472b107": "SEED-002-BR-AM-1",
    "8457820e-ec9d-4ec5-b992-6cd158f9fe75": "SEED-002-BR-AM-2",
    # ZDC-001: zodiac symbol charms (1 photo per sign/material)
    "6d9440b0-44e4-48f1-aa0f-724639f54182": "ZDC-001-BR-PIS-1",
    "5d30e5c1-d0da-4342-9532-99ec9ec7030a": "ZDC-001-SL-PIS-1",
    "b506ed34-be3c-4886-8600-7ad4b9ecb377": "ZDC-001-BR-GMN-1",
    "8efe674c-bf3c-4d67-9fd6-b708e7aaadae": "ZDC-001-SL-GMN-1",
    "ce14ece6-f4c1-414f-a09c-4167ba4878a7": "ZDC-001-BR-CAP-1",
    "69f0f90e-9843-4a4b-93fc-f12e5129e5ed": "ZDC-001-SL-CAP-1",
    "343adebc-4ccb-4a7c-a6c6-da8a5c824652": "ZDC-001-BR-SCO-1",
    "337d131b-3c32-4fb2-94bc-287f5a4846f8": "ZDC-001-SL-SCO-1",
    "ab669c65-e049-4203-8bf0-05845b35b652": "ZDC-001-BR-SAG-1",
    "c9ec5d4a-3422-4ef0-b0de-724c76cdd1d1": "ZDC-001-SL-SAG-1",
    "6e8ae1cc-3dce-4de4-b1b7-de59f1f1000b": "ZDC-001-BR-VIR-1",
    "304b0d3c-fe6d-4517-b8d8-0bb5e6206ac4": "ZDC-001-SL-VIR-1",
    "b0440cdb-53fd-47d5-83ce-9b4e47ec0b5b": "ZDC-001-BR-TAU-1",
    "67242f40-d812-43a3-980c-9e2256485e9c": "ZDC-001-SL-TAU-1",
    "e54ee951-d291-4f04-8ecc-3df24d1e5fa8": "ZDC-001-BR-LEO-1",
    "57687e8e-e41c-4740-8091-867c0c7fca88": "ZDC-001-SL-LEO-1",
}

# Duplicate shots to delete (user confirmed a backup exists).
DUPLICATES = {
    "126b19a5-c3d2-40a2-a774-5455f164ab07",  # SEED-002-BR-GRT dupe
    "2bd7feb1-3b2a-4ee0-a5eb-73b10842890f",  # SEED-002-BR-GRT dupe
    "6fe5c2da-5b45-4437-973d-6439c7a4243d",  # SEED-002-BR-MOON dupe
    "763038f0-a733-44ad-9eb9-6425b758093a",  # SEED-002-BR-MAL dupe
    "fb5d62fd-543e-4076-9a76-a5b6554dbfca",  # SEED-002-BR-MAL dupe
}


def main():
    renamed = 0
    for uuid_stem, new_stem in RENAMES.items():
        src = LOCAL_DIR / f"{uuid_stem}.JPG"
        dst = LOCAL_DIR / f"{new_stem}.JPG"
        if not src.exists():
            print(f"MISSING: {src.name}")
            continue
        src.rename(dst)
        shutil.copy2(dst, SOURCE_DIR / dst.name)
        renamed += 1
    print(f"Renamed {renamed}/{len(RENAMES)} files (and copied to source folder)")

    removed = 0
    for uuid_stem in DUPLICATES:
        f = LOCAL_DIR / f"{uuid_stem}.JPG"
        if f.exists():
            f.unlink()
            removed += 1
    print(f"Removed {removed}/{len(DUPLICATES)} duplicate files from local repo folder")


if __name__ == "__main__":
    main()
