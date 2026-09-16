# Car Inventory Management System

A simple **Car Inventory Management System** built using Python and Oracle Database.

## Features

* Select and view car brand details
* Update the total number of models
* Delete brand details
* Add new brand details
* View the entire car inventory

## Technologies Used

* Python
* Oracle Database
* `oracledb`
* `python-dotenv`

## Project Structure

```text
Cars_information/
│
├── main.py
├── source/
│   └── car_brand_inventory.py
├── .gitignore
└── README.md
```

## Database

The project uses an Oracle Database table named `Car_Inventory`.

The table stores:

* Car ID
* Brand
* Company Website
* Established Year
* CEO
* Total Models
* Headquarters
* Country

## Setup

### 1. Clone the repository

Clone this repository to your computer using Git.

### 2. Install required packages

Open the project folder in VS Code and run:

```bash
pip install oracledb python-dotenv
```

### 3. Configure Oracle Database

Create a local `.env` file in the project folder with your Oracle database details:

```text
ORACLE_USER=your_oracle_username
ORACLE_PASSWORD=your_oracle_password
ORACLE_DSN=your_oracle_dsn
```

**Do not upload `.env` to GitHub.**

The `.gitignore` file is configured to prevent `.env` from being uploaded.

### 4. Run the project

```bash
python main.py
```

## Important

This project is created for learning and practice with **Python, Oracle Database, and CRUD operations**.
