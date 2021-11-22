# Todo List Flask App

## Overview

This is an example of a Flask-based todo list application. It performs full CRUD functionality and models a database with a single `tasks` table using SQLAlchemy.

## Running the Application

These instructions assume you are running your app on an Ubuntu machine.

1.  Install the necessary `apt` requirements:

    ```bash
    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    ```

2.  Create a Python virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the required Python packages with `pip` using the [`requirements.txt`](/requirements.txt) file:

    ```bash
    pip3 install -r requirements.txt
    ```

4.  Define the connection string for your database as an environment variable named `DATABASE_URI`:

    ```bash
    export DATABASE_URI=<your_database_uri_here>
    ```

    If you are connecting to an external database, your connection string will be in the format:

    ```bash
    export DATABASE_URI=mysql+pymysql://<username>:<password>@<db_hostname>:3306/<database>
    ```

    Alternatively, you can use SQLite to store your database data as a file:

    ```bash
    export DATABASE_URI=sqlite:///data.db
    ```

    This will create a file called `data.db` in your [`application/`](/application) directory.

5.  Set the `CREATE_SCHEMA` environment variable.

    ```bash
    export CREATE_SCHEMA=<true_or_false>
    ```

    When this variable is set to `true`, it will generate the table schema in the database you are connecting to (as defined by the `DATABASE_URI` variable).
    
    Any other value will not generate the schema at app start-up.

    >NOTE: if `CREATE_SCHEMA` is not set, it will cause the application to crash at start-up. I will likely add some code at a later point so this does not happen.

6.  Run the application:

    ```bash
    python3 app.py
    ```