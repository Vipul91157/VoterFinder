# Data Folder

This folder is intentionally left empty.

The original SQLite database (`voters.db`) is **not included** in this repository because it contains electoral roll data imported from official PDF sources.

To run the application, place a compatible `voters.db` file inside this directory:

```
data/
└── voters.db
```

The database schema is created automatically by the application, or you can generate a compatible database by importing electoral roll PDFs using the provided import utilities.

> **Note:** This repository is intended to showcase the application's architecture and implementation. The electoral roll data itself is not distributed with this project.