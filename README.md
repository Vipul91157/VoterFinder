# 🗳️ VoterFinder

A Python-based offline Windows desktop application for searching voter records quickly and efficiently.

VoterFinder allows users to search voter records stored in a local SQLite database by **Name (Hindi)** or **EPIC Number**, display detailed voter information, and export search results to Microsoft Excel.

> **Note:** The database is not included in this repository because it contains electoral roll data imported from official PDF sources.

---

## ✨ Features

- 🔍 Search voter records by Name (Hindi)
- 🆔 Search voter records by EPIC Number
- ⚡ Fast offline search using SQLite
- 📄 Export search results to Excel (.xlsx)
- 🖥️ Modern desktop interface built with CustomTkinter
- 📦 Standalone Windows executable support
- 💻 Windows installer support

---

## 🛠 Tech Stack

- Python
- CustomTkinter
- SQLite
- SQL
- OpenPyXL
- PyInstaller
- Inno Setup

---

## 📂 Project Structure

```
VoterFinder
│
├── api/
├── database/
├── downloader/
├── exporter/
├── extractor/
├── gui/
├── search/
├── services/
├── data/
│   └── README.md
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/VoterFinder.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---



## 📌 Current Limitations

- Supports searching by **Hindi Name** and **EPIC Number**
- Uses electoral roll data imported from approximately **250 PDFs**
- Current implementation is based on the **Maharajganj Assembly Constituency, Siwan District, Bihar**
- Database is intentionally excluded from this repository

---

## 📚 What I Learned

This project helped me gain practical experience with:

- Desktop application development
- Database integration
- SQL queries
- GUI development
- Data export to Excel
- Debugging
- Packaging Python applications
- Windows software deployment

---

## 📄 License

This project is shared for educational and portfolio purposes.
