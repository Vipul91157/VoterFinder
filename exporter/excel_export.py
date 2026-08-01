from openpyxl import Workbook


def export_voters(voters, filename="Search_Result.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Voters"

    headers = [
        "Name",
        "Relation",
        "Gender",
        "Age",
        "EPIC",
        "House No",
        "Section",
        "Part No",
        "Serial No"
    ]

    ws.append(headers)

    for voter in voters:
        ws.append([
            voter["name"],
            voter["relation_name"],
            voter["gender"],
            voter["age"],
            voter["epic_no"],
            voter["house_no"],
            voter["section_no"],
            voter["part_no"],
            voter["serial_no"]
        ])

    wb.save(filename)