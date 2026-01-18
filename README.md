# Terminal Calendar & Task Manager

A Python-based **terminal calendar application** that displays the current month in a color-coded grid and allows users to manage simple tasks directly from the command line.

This project is designed as a lightweight, interactive calendar with task tracking, written using only Python’s standard library.

---

## ✨ Features

### 📅 Calendar View

* Displays the **current month** in a weekly grid (Sunday → Saturday)
* Automatically detects:

  * Current year
  * Current month
  * Current day
* **Color-coded output** (ANSI escape codes):

  * 🔵 Blue → Current day
  * 🔴 Red → Days from the previous month (optional)

### ⚙️ Settings

* Toggle whether to show **days from the previous month** before the first day of the current month

### 📝 Task Management

* Add tasks with:

  * Name
  * Due date (year, month, day, hour – numeric format)
  * Optional importance
  * Description
* Delete tasks by number
* Tasks are:

  * Sorted by due date
  * Displayed below the calendar

---

## 🛠 Requirements

* Python **3.8+**
* Works on:

  * macOS
  * Linux
  * Windows (CMD / PowerShell recommended for ANSI colors)

No external libraries are required.

---

## ▶️ How to Run

1. Save the script as `calendar.py`
2. Open a terminal
3. Run:

```bash
python calendar.py
```

---

## 🎮 Controls

After the calendar is displayed, you will see:

```
Functions:
s - Settings
t - Tasks
```

### Settings (`s`)

* Toggle whether days before the first day of the month are displayed

### Tasks (`t`)

* **Add a task**
* **Delete a task** by selecting its number

---

## 🧾 Task Date Format

When adding a task, enter the date as:

```
YYMMDDHH   (NO SPACES)
```

Example:

* `24112812` → November 28, 2024 at 12:00

> The program uses this numeric ID to sort tasks chronologically.

---

## 🎨 Color Legend

| Color   | Meaning                  |
| ------- | ------------------------ |
| Blue    | Current day              |
| Red     | Days from previous month |
| Default | Normal days              |

> Note: ANSI colors may not render correctly in some terminals.

---

## ⚠️ Known Limitations

* Leap years are **not currently handled** (February always has 28 days)
* Tasks are stored **in memory only** (no file saving)
* Date parsing relies on strict numeric input
* ANSI color support depends on terminal compatibility

---

## 🚀 Future Improvements (Ideas)

* Save/load tasks from a file (JSON or CSV)
* Leap year support
* Month navigation (previous / next month)
* Better input validation
* Task highlighting on calendar days

---

## 📄 License

This project is open for educational and personal use. Feel free to modify and expand it.

---

**Author:** Rian Thomas
**Language:** Python
**Type:** Terminal Application
