# Task Tracker Web App (Flask + Flask-SQLAlchemy)

A structured backend foundation for a task management or progress-tracking platform built with **Flask** and **Flask-SQLAlchemy (SQLite)**, featuring dynamic user-to-table-to-task relationships and cookie handling.

## Good Points & Features
* **Robust Relational Models:** Implements a well-designed ORM schema with `User`, `Table`, and `Task` models, complete with foreign keys, back-populates, and many-to-many relationship structures.
* **Dynamic Theming System:** Randomly selects and applies a UI theme (`neon`, `monohrom`, `beer`, `xeon`, `etti`, `sea`, `deep_ocean`, `christmas`) from a predefined array on every homepage hit.
* **Cookie Management:** Demonstrates basic cookie inspection and assignment (`make_response` and `resp.set_cookie`) on the root route.

## Technologies Used
* **Python & Flask** (micro-framework)
* **Flask-SQLAlchemy** (ORM for SQLite database modeling)
* **Jinja2** (template rendering with theme injection)

---
> **Project Status:** Abandoned (Backend architecture prototype).
---
