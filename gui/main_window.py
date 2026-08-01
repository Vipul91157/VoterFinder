import customtkinter as ctk

from gui.theme import *
from gui.result_table import ResultTable
from gui.search_frame import SearchFrame
from search.search import search_by_name, search_by_epic
from exporter.excel_export import export_voters
from tkinter import messagebox
class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("VoterFinder")

        self.geometry("1200x700")

        self.configure(fg_color=BACKGROUND)

        title = ctk.CTkLabel(
            self,
            text="VoterFinder",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="ECI Voter Search System",
            font=("Segoe UI", 16)
        )

        subtitle.pack()

        self.search = SearchFrame(self, self.search_voters)
        self.results = ResultTable(self)
        

        self.export_button = ctk.CTkButton(
         self,
         text="📄 Export to Excel",
          command=self.export_results
          )

        self.export_button.pack(pady=10)
        
    def export_results(self):
    
      if not hasattr(self, "current_results") or not self.current_results:
        messagebox.showwarning(
            "No Data",
            "Please search for voters before exporting."
        )
        return

      export_voters(self.current_results)

      messagebox.showinfo(
        "Export Successful",
        "Search_Result.xlsx has been saved successfully."
        )
    def search_voters(self):
    
      value = self.search.entry.get().strip()

      print("=" * 40)
      print("Search Type :", self.search.search_type.get())
      print("Search Value:", value)

      if not value:
        print("No value entered.")
        return

      if self.search.search_type.get() == "Name":
        print("Calling search_by_name()")
        self.current_results = search_by_name(value)
      else:
        print("Calling search_by_epic()")
        self.current_results = search_by_epic(value)

      print("Results Found:", len(self.current_results))

      self.results.insert_voters(self.current_results)

if __name__ == "__main__":

    app = MainWindow()

    app.mainloop()