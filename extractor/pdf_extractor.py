import pdfplumber


def extract_tables(pdf_path):
    """
    Extract all table rows from every page.
    """

    rows = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:

                if table:

                    rows.extend(table)

    return rows