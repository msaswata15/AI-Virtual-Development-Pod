import sqlite3
from typing import Optional, List, Tuple

def init_db():
    """Initialize the database with tickets table"""
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  status TEXT DEFAULT 'Backlog',
                  design TEXT DEFAULT '',
                  code TEXT DEFAULT '',
                  test_results TEXT DEFAULT '')''')
    conn.commit()
    conn.close()

def create_ticket(title: str, description: str = "") -> int:
    """Create a new ticket and return its ID"""
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute("INSERT INTO tickets (title, description) VALUES (?, ?)",
              (title, description))
    ticket_id = c.lastrowid
    conn.commit()
    conn.close()
    return ticket_id

def get_tickets() -> List[Tuple]:
    """Get all tickets"""
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tickets ORDER BY id DESC")
    tickets = c.fetchall()
    conn.close()
    return tickets

def delete_ticket(ticket_id: int):
    """Delete a ticket by ID"""
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute("DELETE FROM tickets WHERE id=?", (ticket_id,))
    conn.commit()
    conn.close()

def update_ticket(ticket_id: int, **kwargs):
    """
    Update ticket fields
    Example: update_ticket(1, status="In Progress", design="<xml>...")
    """
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    
    valid_fields = ['title', 'description', 'status', 'design', 'code', 'test_results']
    updates = {k: v for k, v in kwargs.items() if k in valid_fields}
    
    if updates:
        set_clause = ", ".join(f"{field}=?" for field in updates.keys())
        query = f"UPDATE tickets SET {set_clause} WHERE id=?"
        params = tuple(updates.values()) + (ticket_id,)
        c.execute(query, params)
    
    conn.commit()
    conn.close()