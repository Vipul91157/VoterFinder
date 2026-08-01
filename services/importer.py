import os
from tqdm import tqdm

from extractor.pdf_extractor import extract_tables
from extractor.voter_parser import parse_row
from database.insert import get_connection, insert_voters


def import_folder(folder="downloads"):

    pdf_files = [
        os.path.join(folder, file)
        for file in os.listdir(folder)
        if file.lower().endswith(".pdf")
    ]

    pdf_files.sort()

    print(f"\nFound {len(pdf_files)} PDF files\n")

    conn = get_connection()

    total_voters = 0

    try:

        for pdf in tqdm(pdf_files):

            rows = extract_tables(pdf)

            voters = []

            for row in rows:

                voter = parse_row(row)

                if voter:
                    voters.append(voter)

            insert_voters(conn, voters)

            total_voters += len(voters)

    finally:

       conn.commit()
       conn.close()

    print("\n============================")
    print("Import Completed")
    print("============================")
    print(f"Total Voters Imported : {total_voters}")