# Memory Agent

An AI memory agent built using **Agno**, **Groq**, and **SQLite**.

This project demonstrates how an AI agent can store and retrieve user-specific information using persistent memory. The agent can remember information provided by a user and use that information in future interactions.

## Features

- Persistent user memory
- User-specific memory using unique user IDs
- Conversation history support
- SQLite-based database
- AI-powered responses using Groq
- Built using Agno
- Retrieves stored user memories

## Architecture

```text
                    User Query
                        |
                        v
                +---------------+
                |  Memory Agent |
                +-------+-------+
                        |
              +---------+---------+
              |                   |
              v                   v
       Conversation         User Memories
          History                |
              |                   |
              +---------+---------+
                        |
                        v
                  SQLite Database
                        |
                        v
                 AI Response
```

## Technologies Used

- Python
- Agno
- Groq
- SQLite
- python-dotenv
- SQLAlchemy
- Rich

## Project Structure

```text
Memory-Agent/
|
├── memory.py
├── requirements.txt
├── .gitignore
└── .env
```

> `.env` contains the API key and is excluded from GitHub using `.gitignore`.
>
> `agno.db` is the local SQLite database created by the application and is also excluded from GitHub.

## Installation

Clone the repository:

```bash
git clone https://github.com/arishak10/memory-agent.git
cd memory-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_groq_api_key

**Never upload your `.env` file or expose your API key publicly.**
```

## Run the Project

Run the following command:

```bash
python memory.py
```

The agent stores user-specific information and retrieves it when the same user interacts with the agent again.

## Example

### First Interaction

```text
User: I am Rahul and I am a Data Analyst.
```

The agent stores the user's information in memory.

### Second Interaction

```text
User: Who am I?
```

The agent can retrieve the stored information and respond based on the user's previous interaction.

## Purpose

This project demonstrates how AI agents can use persistent memory to remember user-specific information and provide more personalized responses across interactions.

## Author

**Arisha Khan**

Computer Science Student | AI/ML Enthusiast
