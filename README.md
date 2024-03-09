![Alt Text](https://i.imgur.com/ogbfW3k.png)

# AirBnB Clone Project

This project aims to create an AirBnB clone application with a command-line interface (CLI) for managing AirBnB objects. The CLI allows users to perform various operations such as creating new objects, retrieving objects, updating attributes, and more.

## Curriculum

**AirBnB Clone Project:**

- **Objective:** Deploy a simple copy of the AirBnB website on your server.
- **Duration:** From now until the end of the first year.
- **Components:**
  - Command interpreter for data manipulation (Shell-like interface).
  - Website (front-end) showcasing static and dynamic content.
  - Database or file storage for object persistence.
  - API for communication between front-end and data.
- **Key Concepts to Learn:**
  - Unittest for collaborative test case development.
  - Python packages concept.
  - Serialization/Deserialization.
  - *args, **kwargs usage.
  - Handling datetime in Python.
- **Steps:**
  1. Develop the command interpreter:
      - Create data model.
      - Manage objects via a console.
      - Store and persist objects to a JSON file.
  2. Implement web static:
      - Learn HTML/CSS.
      - Create HTML templates for application.
  3. Integrate MySQL storage:
      - Replace file storage with database.
      - Map models to database tables using ORM.
  4. Develop web framework and templating:
      - Set up Python web server.
      - Render dynamic content using stored data.
  5. Build RESTful API:
      - Expose objects via JSON web interface.
      - Enable CRUD operations via API.
  6. Enhance web dynamic functionality:
      - Learn JQuery for client-side manipulation.
      - Load objects using custom RESTful API.
- **File Structure:**
  - **models:** Contains all classes for the project.
  - **tests:** Contains unit tests.
  - **console.py:** Entry point for the command interpreter.
  - **models/base_model.py:** Base class for all models.
  - **models/engine:** Contains storage classes (e.g., file_storage.py).
- **Storage Management:**
  - Utilize file and database storage for object persistency.
  - Separate storage management from model logic for modularity.
  - Convert instances to JSON for serialization and deserialization.
- **Miscellaneous:**
  - Understand *args and **kwargs for flexible function arguments.
  - Manipulate datetime objects for date and time operations.

## Command Interpreter

The command interpreter provides a Shell-like interface for interacting with the AirBnB objects. It allows users to perform various actions such as creating new objects, retrieving objects, updating attributes, and more.

### How to Start

To start the command interpreter, run the `console.py` script:

```bash
$ ./console.py
```

### How to Use

Once inside the command interpreter, you can use various commands to interact with the AirBnB objects. Use the `help` command to view the list of available commands and their descriptions.

```bash
(hbnb) help
```

### Examples

Here are some examples of how to use the command interpreter:

Creating a new User object:
```bash
(hbnb) create User
```

Retrieving all objects of a certain type:
```bash
(hbnb) all User
```

Updating attributes of an object:
```bash
(hbnb) update User <user_id> name "John Doe"
```

Deleting an object:
```bash
(hbnb) destroy User <user_id>
```

Feel free to explore other commands and functionalities of the command interpreter!

