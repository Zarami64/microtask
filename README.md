# Micro Task Point

Micro Task Point is a comprehensive micro-task management platform that enables users to complete and manage small tasks in exchange for rewards. The platform includes features for user registration, task management, video watching, and more, with a focus on an intuitive and beautiful user interface.

## Features

- **User Registration**: Users can sign up with their name, email, phone number, or Google authentication.
- **User Dashboard**: Provides an overview of earnings, points, completed and pending tasks, and notifications. Users can edit their profile and upload a profile picture.
- **Video Watching**: Users can watch YouTube videos set by the admin. The platform tracks and displays the watch count for each user.
- **Task Management**: Users can view and manage tasks, including job requirements and submissions.
- **Admin Dashboard**: Admins can post jobs, manage categories, handle point payments, and oversee user activities.

## Folder Structure


## Setup

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:Zarami64/microtask.git
   cd microtask
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

```
pip install -r requirements.txt
```

```
python run.py db upgrade
```

```
python run.py
```

By default, the application will run on http://127.0.0.1:5000.

Usage
User Registration: Access the registration page to create a new account.
Dashboard: Log in to view your dashboard, manage tasks, and track your earnings.
Video Watching: Watch videos assigned by the admin and track your watch count.
Admin Management: Admins can log in to manage tasks, user accounts, and other platform settings.
Contributing
Contributions are welcome! Please submit issues and pull requests via the GitHub repository. Make sure to follow the coding guidelines and include relevant tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.





