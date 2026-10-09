# 📚 Library Inventory Management System

### Full Stack Development — Course 117
**Developed by Shea Melissa**

---

## 📖 Project Overview

The Library Inventory Management System is a web application
developed using Python and Django.

This project was created as part of the Course 117 Django
extra-credit activities to demonstrate the development of
a Django project from scratch.

The application allows users to explore a library's book
collection, view book information, and check inventory
availability.

Administrators can manage book records through Django's
built-in administration panel.

The project also incorporates responsive web design,
custom CSS styling, and database integration.

---

## 🎯 Project Objectives

The primary objectives of this project were to:

- Create and configure a Django project.
- Develop multiple Django applications.
- Configure templates and static files.
- Implement function-based views.
- Establish URL routing between applications.
- Create a database model for managing books.
- Register and manage book records through Django admin.
- Retrieve and display database records dynamically.
- Apply custom CSS styling.
- Develop an organized and user-friendly interface.

---

## 🛠️ Technologies Used

### Backend
- Python
- Django
- SQLite

### Frontend
- HTML5
- CSS3
- Django Template Language

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
117-LibraryInventoryManagement/
│
├── library/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── pages/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── inventory/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── inventory.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── 117Library.png
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🏗️ Activity 1 — Django Project Setup

The first activity focused on creating and configuring
the Django project.

### Completed Tasks

1. Created the Django project named `library`.
2. Created two Django applications:
   - `pages`
   - `inventory`
3. Registered both applications in `INSTALLED_APPS`.
4. Configured the project's template directory.
5. Created reusable HTML templates.
6. Implemented function-based views.
7. Configured URL routing.
8. Created directories for CSS and images.
9. Developed custom CSS styling.
10. Successfully launched the Django development server.

### Homepage

The homepage introduces the Library Inventory
Management System and provides navigation to
the inventory collection.

Features include:

- Responsive navigation bar.
- Library-themed homepage image.
- Project introduction.
- Inventory navigation button.
- Custom navy-blue and gold design.
- Footer with developer attribution.

---

## 📚 Activity 2 — Book Model and Inventory

The second activity focused on creating a database
model and displaying book records dynamically.

### Book Model

A `Book` model was created in the `inventory`
application.

The model includes the following attributes:

| Field | Description |
|-------|-------------|
| Title | Name of the book |
| Author | Author of the book |
| ISBN | Unique book identification number |
| Publication Year | Year the book was published |
| Quantity | Number of available copies |

### Database Configuration

The project uses SQLite as its database.

Django migrations were created and applied to
establish the database structure.

### Django Administration

The Book model was registered in Django's
administration panel.

Administrators can:

- Add new books.
- Edit existing book records.
- Delete books.
- Search books by title, author, or ISBN.
- Filter books by publication year.
- Manage inventory quantities.

---

## 📖 Initial Book Collection

Five books were added through the Django
administration panel.

| Title | Author | Publication Year |
|-------|--------|------------------|
| Pride and Prejudice | Jane Austen | 1813 |
| The Great Gatsby | F. Scott Fitzgerald | 1925 |
| The Hobbit | J.R.R. Tolkien | 1937 |
| 1984 | George Orwell | 1949 |
| To Kill a Mockingbird | Harper Lee | 1960 |

These records are stored in the database and
retrieved dynamically for display on the
inventory page.

---

## 💻 Inventory Page Features

The inventory page displays the library's
book collection in an organized table.

Information displayed includes:

- Book title
- Author
- ISBN
- Publication year
- Quantity
- Availability status

### Dynamic Inventory

Book information is retrieved directly from
the database using Django's ORM.

Changes made through the administration panel
are reflected in the inventory display.

### Availability Indicators

The inventory page uses visual indicators
to communicate book availability.

- Green badges indicate available books.
- Red badges indicate unavailable books.

Availability is determined by the quantity
recorded for each book.

### Inventory Count

The page also displays the total number
of book titles currently registered
in the database.

---

## 🎨 User Interface Design

In addition to the required functionality,
custom styling was implemented to improve
the overall user experience.

### Design Features

- Navy-blue and gold color palette.
- Cream-colored page backgrounds.
- Responsive page layouts.
- Styled inventory tables.
- Alternating table row colors.
- Hover effects.
- Rounded containers.
- Availability badges.
- Consistent navigation and footer.
- Mobile-responsive styling.

The design emphasizes readability,
organization, and ease of navigation.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL of
your GitHub repository.

### 2. Navigate to the Project Directory

```bash
cd 117-LibraryInventoryManagement
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 5. Install Django

```bash
python -m pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your
administrator credentials.

### 8. Start the Development Server

```bash
python manage.py runserver
```

### 9. Access the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

### Inventory Page

```text
http://127.0.0.1:8000/inventory/
```

### Django Administration

```text
http://127.0.0.1:8000/admin/
```

---

## 🧪 Testing and Verification

The application was manually tested to verify
the following functionality:

- Django development server starts successfully.
- Homepage loads correctly.
- Navigation between pages works.
- Django administration is accessible.
- Book records can be added through Django admin.
- Database records display on the inventory page.
- Inventory quantities display correctly.
- Availability indicators display.
- Total book count displays correctly.
- Custom CSS loads successfully.

---

## 🌟 Additional Features

Beyond the basic assignment requirements,
the project includes:

- Custom library-themed homepage.
- Professional navigation and page layouts.
- Responsive CSS styling.
- Dynamic inventory table.
- Visual availability indicators.
- Inventory record count.
- Django admin search functionality.
- Django admin filtering.
- Consistent branding throughout the application.

These enhancements were added to create
a more complete and user-friendly application.

---

## 📌 Future Improvements

Potential improvements include:

- Public book search functionality.
- Book category filtering.
- Book detail pages.
- User authentication.
- Book checkout and return functionality.
- Inventory quantity updates.
- Book cover images.
- Additional inventory reporting.

These features are potential future
enhancements and are not currently implemented.

---

## 🎓 Course Information

**Program:** Full Stack Development

**Course:** 117 — Django Portfolio Development

**Assignment:** Library Inventory Management
Extra-Credit Activities

**Instructor:** Dr. Fernanda Murillo

### Assignment Activities

**Activity 1:** Create and Set Up the Project

**Activity 2:** Create and Display the Book Model

Both activities demonstrate the integration
of Django project configuration, database
management, frontend development, and
dynamic content rendering.

---

## 👩‍💻 Developer

**Shea Melissa**

Full Stack Development Student

Interested in software development,
web applications, database management,
and creating practical technology solutions.

---

## 📄 Project Status

**Status: Completed**

The Library Inventory Management System
successfully demonstrates the requirements
outlined in both Course 117 extra-credit
activities.

Developed by Shea Melissa.