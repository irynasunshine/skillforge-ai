# SkillForge AI — Personalized CLI Learning Assistant

SkillForge AI is a Python CLI application that helps you learn new skills through
AI-generated personalized learning plans. It generates customized roadmaps, tracks
your progress, and provides an AI mentor you can chat with at any time.

---

## Features

- Personalized learning roadmap generation (powered by Groq)
- Weekly task breakdown
- Progress tracking with visual status
- Interactive AI mentor for on-demand Q&A
- Lightweight local SQLite storage — no server required

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository>
cd skillforge-ai
```

### 2. Create and activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy `.env.example` to `.env` and add your Groq API key:

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_api_key_here
```

---

## Usage

### Create a new learning plan

```bash
python main.py create-plan
```

You will be prompted for the skill, your current level, hours per week, and target
duration. A weekly plan is generated and saved to the local database.

### View your progress

```bash
python main.py progress
```

### Mark a task as complete

```bash
python main.py complete 3
```

### Ask the AI mentor

```bash
python main.py ask "Explain REST APIs"
```

---

## Architecture

```
skillforge_ai/
├── app/
│   ├── ai/           # OpenAI integration (planner, mentor, prompts)
│   ├── cli/          # Typer commands and Rich menu
│   ├── core/         # Domain models, scheduler, progress tracker
│   ├── database/     # SQLAlchemy engine, session, repository
│   └── utils/        # Shared helpers
├── data/             # Reserved for exported data
├── tests/            # Unit tests
├── main.py
├── requirements.txt
└── .env.example
```

**Layers:**

| Layer    | Responsibility                                 |
|----------|------------------------------------------------|
| CLI      | User interaction via Typer + Rich              |
| AI       | Prompt construction and OpenAI API calls       |
| Core     | Business logic — scheduling and tracking       |
| Database | SQLite persistence via SQLAlchemy ORM          |

---

## AI Integration

Two AI functions power the application:

- `generate_learning_plan` — sends a structured prompt to `llama-3.3-70b-versatile` and parses
  the response into weekly tasks.
- `ask_mentor` — passes the user's question to the model and returns a plain-text
  answer.

Prompts live in `app/ai/prompts.py` and are kept separate from business logic for
easy tuning.

---

## Database

SQLite is used for zero-setup local persistence. The schema contains a single
`tasks` table:

| Column    | Type    |
|-----------|---------|
| id        | Integer |
| title     | String  |
| week      | Integer |
| completed | Boolean |

The database file `skillforge.db` is created automatically on first run.

---

## Running Tests

```bash
pytest tests/
```

---

## Limitations

- Requires an active internet connection and a valid Groq API key.
- Learning plans are not automatically adapted based on performance (v1).
- No user authentication — single-user local application.

---

## Future Improvements

- Adaptive scheduling based on completion rate
- Daily task breakdown and streak system
- Quiz and flashcard generation
- Markdown / PDF export of learning plans
- Offline mode via local models (Ollama)
- Web or mobile interface
