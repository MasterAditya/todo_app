# Todo App

This is a simple Todo application built with FastAPI and SQLite. The app allows users to manage their tasks efficiently with features like adding, completing, deleting, and filtering tasks.

## Features

- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Filter tasks by status (All, Active, Completed)
- Display task creation timestamps
- Responsive and user-friendly UI

## Technologies Used

- **Backend**: FastAPI
- **Database**: SQLite
- **Frontend**: Jinja2 templates with TailwindCSS for styling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MasterAditya/todo_app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd todo_app
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   uvicorn todo_app.app.main:app --reload
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Project Structure

```
.
├── todo_app/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── templates/
│   │   │   └── index.html
│   └── README.md
├── requirements.txt
└── setup-project.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project by submitting issues or pull requests!
