import customtkinter as ctk
from tkinter import ttk


class ResultTable(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True, padx=20, pady=10)

        columns = (
            "Name",
            "Relation",
            "Gender",
            "Age",
            "Booth",
            "EPIC"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:

            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        self.tree.pack(fill="both", expand=True)

    def clear(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    def insert_voters(self, voters):

        self.clear()

        for voter in voters:

            self.tree.insert(
                "",
                "end",
                values=(
                    voter["name"],
                    voter["relation_name"],
                    voter["gender"],
                    voter["age"],
                    voter["part_no"],
                    voter["epic_no"]
                )
            )