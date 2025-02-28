import os
import requests
import psycopg2
from psycopg2.extras import execute_values

GITHUB_API_URL = "https://api.github.com/repos/pytorch/pytorch/issues"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#GITHUB_API_URL_COMMENTS = "https://api.github.com/repos/pytorch/pytorch/issues/{issue_number}/comments"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

DB_CONFIG = {
    "host": "localhost",
    "database": "Ativ1",
    "user": "postgres",
    "password": f"{DB_PASSWORD}",
    "port": 5432
}

def fetch_issues(page, per_page):
    params = {"page": page, "per_page": per_page, "state": "closed"}
    response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def create_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS github_issues (
        id SERIAL PRIMARY KEY,
        issue_id VARCHAR(20) NOT NULL UNIQUE,
        github_id VARCHAR(20) NOT NULL UNIQUE,
        number INTEGER NOT NULL,
        title TEXT NOT NULL,
        body TEXT,
        state VARCHAR(20),
        classificacao VARCHAR(20),
        labels TEXT[],
        comments_count INTEGER,
        created_at TIMESTAMP,
        updated_at TIMESTAMP,
        closed_at TIMESTAMP,
        user_login TEXT,
        assignee TEXT,
        milestone TEXT,
        html_url TEXT
    );

    """)

    conn.commit()
    cursor.close()
    conn.close()
    return None

def save_issues_to_db(issues):

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO github_issues (
        issue_id, github_id, number, title, body, state, classificacao, labels, comments_count, created_at, updated_at, closed_at,
        user_login, assignee, milestone, html_url
    )
    VALUES %s
    ON CONFLICT (github_id) DO NOTHING
    """
    
    values = [
        (
            issue["id"],  # issue_id
            issue["id"],  # github_id (mesmo ID, já que a API do GitHub usa isso)
            issue["number"],
            issue["title"],
            issue.get("body", ""),
            issue["state"],
            issue["Resultado"],
            [label["name"] for label in issue.get("labels", [])],  # Lista de labels
            issue["comments"],
            issue["created_at"],
            issue["updated_at"],
            issue.get("closed_at"),  # Algumas issues podem não estar fechadas
            issue["user"]["login"] if "user" in issue else None,  # Pode não ter um usuário associado
            issue.get("assignee", {}).get("login") if issue.get("assignee") else None,  # Pode não ter assign
            issue.get("milestone", {}).get("title") if issue.get("milestone") else None,  # Pode não ter milestone
            issue["html_url"]
        )
        for issue in issues
    ]

    execute_values(cursor, insert_query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return None