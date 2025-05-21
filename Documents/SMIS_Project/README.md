# SMIS - Student Management Information System

A C++/CLI Windows Forms application for managing student information, featuring a modern tabbed interface and MySQL database connectivity.

---

## 📋 Project Description

**SMIS** is a Student Management Information System built using C++/CLI and Windows Forms. It provides a graphical interface to perform CRUD (Create, Read, Update, Delete) operations on student records stored in a MySQL database. The application is designed for ease of use, with separate tabs for data entry and database viewing.

---

## ✨ Features

- Add, update, delete, and view student records
- Connects to a MySQL database (`visualcppdb`)
- Tabbed interface:
  - **College System**: Enter and manage student details
  - **Student Database**: View all student records in a table
- DataGridView for displaying records
- User-friendly design with labeled fields and action buttons

---

## 🖼️ Screenshots

### College System Tab
![College System Tab](./screenshot1.png)

### Student Database Tab
![Student Database Tab](./screenshot2.png)

---

## 🛠️ Requirements

- Visual Studio 2019/2022 (with C++/CLI and Windows Forms support)
- MySQL Server (e.g., via XAMPP)
- MySQL Connector for C++/CLI
- .NET Framework 4.7.2 or later

---

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramcharan0308/MYSQL_Project.git
   ```
2. **Open the solution:**
   - Open `studentsql.sln` in Visual Studio.
3. **Restore NuGet packages** (if required).
4. **Configure MySQL:**
   - Ensure MySQL is running (default: `localhost`, user: `root`, password: empty).
   - Create a database named `visualcppdb` and a table `userinfotbl` with columns:
     - `rollno` (int, primary key)
     - `name` (varchar)
     - `college` (varchar)
     - `phone` (varchar)
     - `email` (varchar)
5. **Build and run the project** in Visual Studio.

---

## 📝 Usage

- **College System Tab:**
  - Enter student details and use the `INSERT`, `UPDATE`, `DELETE`, `SELECT`, and `RESET` buttons to manage records.
- **Student Database Tab:**
  - View all student records in a table format.

---

## ⚠️ Notes

- The MySQL connection string is set to `Server=127.0.0.1;Uid=root;Pwd=;Database=visualcppdb` by default. Update it in the code if your setup is different.
- Make sure MySQL is running before launching the application.

---

## 🙏 Acknowledgments

- Developed using Visual Studio and Windows Forms
- MySQL for database management
- [XAMPP](https://www.apachefriends.org/) for local MySQL server

---

## 📄 License

This project is for educational purposes.

---

**Feel free to contribute or raise issues!** 