from services.importer import import_folder
from search.search import search_by_name, search_by_epic


def menu():

    while True:

        print("\n==============================")
        print("ECI Voter Search System")
        print("==============================")
        print("1. Import All Downloaded PDFs")
        print("2. Search by Name")
        print("3. Search by EPIC Number")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            import_folder()

        elif choice == "2":

            name = input("\nEnter voter name: ")

            voters = search_by_name(name)

            print(f"\nFound {len(voters)} voter(s)\n")

            for voter in voters:

                print("--------------------------------")

                print("Name :", voter["name"])
                print("Relation :", voter["relation_name"])
                print("Gender :", voter["gender"])
                print("Age :", voter["age"])
                print("Booth :", voter["part_no"])
                print("Serial :", voter["serial_no"])
                print("EPIC :", voter["epic_no"])

        
        elif choice == "3":
    
           epic = input("\nEnter EPIC Number: ").strip().upper()

           voters = search_by_epic(epic)

           print(f"\nFound {len(voters)} voter(s)\n")

           for voter in voters:

             print("--------------------------------")

             print("Name :", voter["name"])
             print("Relation :", voter["relation_name"])
             print("Gender :", voter["gender"])
             print("Age :", voter["age"])
             print("Booth :", voter["part_no"])
             print("Serial :", voter["serial_no"])
         
         
             print("EPIC :", voter["epic_no"])
        elif choice == "4":
             break
        else:

            print("Invalid Choice")


if __name__ == "__main__":
    menu()