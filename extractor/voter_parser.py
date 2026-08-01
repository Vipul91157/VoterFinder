import re


def clean_text(text):
    """
    Clean extracted PDF text.
    """

    if text is None:
        return ""

    text = str(text)

    # Remove PDF encoding artifacts
    text = re.sub(r"\(cid:\d+\)", "", text)

    # Replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def parse_row(row):
    """
    Convert one extracted table row into a voter dictionary.
    """

    if not row:
        return None

    row = [clean_text(cell) for cell in row]

    # Skip header rows
    if len(row) == 0:
        return None

    if row[0] == "AC_NO":
        return None

    # Some pages have incomplete rows
    while len(row) < 14:
        row.append("")

    voter = {

        "ac_no": row[0],

        "part_no": row[1],

        "serial_no": row[2],

        "house_no": row[3],

        "section_no": row[4],

        "name": (row[5] + " " + row[6]).strip(),

        "relation_type": row[7],

        "relation_name": (row[8] + " " + row[9]).strip(),

        "epic_no": row[10],

        "part_link_no": row[11],

        "gender": row[12],

        "age": row[13]

    }

    return voter