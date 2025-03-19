# Phase 3 Code Challenge: Theater Work

## Overview
This project is a command-line interface (CLI) application that manages auditions for a theater company using SQLAlchemy and SQLite. The application allows users to:

- Add roles for a theater play.
- Add auditions for actors.
- View roles and auditions.
- Call back actors (mark them as hired).
- Manage role assignments (lead and understudy).

## Project Structure
```
project-directory/
│-- database.py
│-- models.py
│-- cli.py
│-- README.md
│-- Pipfile
│-- Pipfile.lock
│-- theater.db (auto-generated SQLite database)
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone <repository-url>
cd project-directory
```

### 2. Set Up a Virtual Environment
```sh
pipenv install
pipenv shell
```

### 3. Run Database Migrations
```sh
python cli.py
```

## Usage
Run the application using:
```sh
python cli.py
```
You will be presented with a menu where you can interact with the system.

## Features

### 1. Add a Role
Allows adding a new theater role.

### 2. Add an Audition
Actors audition for a specific role.

### 3. View Roles
Lists all available roles.

### 4. View Auditions
Lists all actors who auditioned.

### 5. Call Back an Actor
Marks an actor as hired.

### 6. Exit
Closes the application.

## Models

### Role
- `id`: Primary key.
- `character_name`: Name of the role.
- Relationship: One `Role` can have many `Auditions`.

### Audition
- `id`: Primary key.
- `actor`: Name of the actor.
- `location`: Audition location.
- `phone`: Contact number.
- `hired`: Boolean indicating if the actor was hired.
- `role_id`: Foreign key linking to a `Role`.

## SQLAlchemy Relationships
- **One-to-Many**: A `Role` can have multiple `Auditions`, but an `Audition` belongs to only one `Role`.

## License
This project is licensed under the MIT License.

