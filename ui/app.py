import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add project root to path

# Now import utils
import streamlit as st
import time
from utils.db import init_db, get_tickets, create_ticket, delete_ticket
from main import DevPod  # Import at top level for better performance

# Initialize database
init_db()

st.title("AI Dev Pod - Ticket Management")

# Create new ticket
with st.form("new_ticket"):
    title = st.text_input("Ticket Title")
    description = st.text_area("Description")
    submit_button = st.form_submit_button("Create Ticket")

    if submit_button:
        with st.status("Processing...", expanded=True) as status:
            # Step 1: Create ticket
            st.write("📝 Creating ticket in database...")
            create_ticket(title, description)
            time.sleep(0.5)
            
            # Step 2: Initialize agents
            st.write("🤖 Activating AI agents...")
            pod = DevPod()
            time.sleep(0.5)
            
            # Step 3: Run workflow
            st.write("⚙️ Executing development workflow...")
            result = pod.run_project(description)
            time.sleep(0.5)
            
            status.update(label="✅ Workflow Complete!", state="complete")
        
        st.success("Ticket created and processed!")
        st.rerun()

# Display all tickets
st.header("Current Tickets")
tickets = get_tickets()

if not tickets:
    st.info("No tickets found")
else:
    for ticket in tickets:
        with st.expander(f"#{ticket[0]} - {ticket[1]}"):
            st.write(f"**Status:** {ticket[3]}")
            st.write(ticket[2])
            if st.button("Delete", key=f"del_{ticket[0]}"):
                delete_ticket(ticket[0])
                st.rerun()