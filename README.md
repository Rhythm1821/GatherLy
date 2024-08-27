# GatherLy

## Description

This is a real-time chat application built using Django and Django Channels. Users can create accounts, establish chat rooms, and communicate with other users in real-time. The application utilizes WebSocket functionality for seamless and instantaneous messaging.

## Features

- **User Authentication**: Users can create accounts and authenticate to access chat rooms.
- **Chat Rooms**: Users can create new chat rooms and join existing ones using unique room identifiers (UUIDs).
- **Real-time Messaging**: Messages are sent and received instantly using WebSocket technology.
- **Admin Controls**: Admins have the authority to delete chat rooms and remove users from chats.
- **Responsive Design**: The application is designed to be responsive and works well on both desktop and mobile devices.

## Technologies Used

- **Django**: Backend web framework for building the application's structure and handling user authentication.
- **Django Channels**: Handles WebSocket connections for real-time messaging.
- **HTML/CSS/JavaScript**: Frontend technologies for building the user interface and interactivity.
- **SQLite** (For local development): Database management system for storing user data and chat information.
- **Supabase** (For deployment): Cloud-based database management system for storing user data and chat information.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Rhythm1821/GatherLy.git
    ```

2. Navigate to the project directory:
   ```
   cd GatherLy
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Make migrations to set up the database:
    ```
    python3 manage.py makemigrations
    ```

4. Run migrations to set up the database:
    ```
    python3 manage.py migrate
    ```

5. Start the development server:
    ```
    python3 manage.py runserver
    ```

6. Access the application in your web browser at http://127.0.0.1:8000.

## Usage
1. Create a new account or log in with existing credentials.
2. Navigate to the Search section to view available chat rooms or create a new one.
3. Join a chat room using the provided UUID.
4. Start sending and receiving messages in real-time.
5. Admins can manage chat rooms and users as needed.