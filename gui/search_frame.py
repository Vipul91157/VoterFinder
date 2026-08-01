import customtkinter as ctk


class SearchFrame(ctk.CTkFrame):

    def __init__(self, master, search_callback):

        super().__init__(master)

        self.pack(fill="x", padx=20, pady=20)

        # Search Type
        self.search_type = ctk.StringVar(value="Name")

        title = ctk.CTkLabel(
            self,
            text="Search By",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(anchor="w", pady=(10, 5))

        radio_frame = ctk.CTkFrame(self, fg_color="transparent")
        radio_frame.pack(anchor="w")

        ctk.CTkRadioButton(
            radio_frame,
            text="Name",
            variable=self.search_type,
            value="Name"
        ).pack(side="left", padx=10)

        ctk.CTkRadioButton(
            radio_frame,
            text="EPIC Number",
            variable=self.search_type,
            value="EPIC"
        ).pack(side="left", padx=10)

        ctk.CTkLabel(
            self,
            text="Search Value"
        ).pack(anchor="w", pady=(20, 5))

        self.entry = ctk.CTkEntry(
            self,
            width=500,
            height=40
        )

        self.entry.pack(anchor="w")

        self.search_button = ctk.CTkButton(
    self,
    text="🔍 Search",
    width=150,
    height=40,
    command=search_callback
)

        self.search_button.pack(pady=20)