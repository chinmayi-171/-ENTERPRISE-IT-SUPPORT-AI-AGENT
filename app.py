import streamlit as st

from auth.login import login_page
from auth.signup import signup_page

from agents.orchestrator_agent import process_query

from agents.memory_agent import (
    save_chat,
    update_chat,
    get_user_history,
    delete_chat
)

from agents.ticket_agent import (
    get_user_tickets,
    update_ticket_status
)


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Helpdesk",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# SESSION STATES
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "attempt" not in st.session_state:
    st.session_state.attempt = 0

if "current_query" not in st.session_state:
    st.session_state.current_query = ""

if "current_solution" not in st.session_state:
    st.session_state.current_solution = ""

if "classification" not in st.session_state:
    st.session_state.classification = {}

if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None

if "all_solutions" not in st.session_state:
    st.session_state.all_solutions = []


# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #0b0b0f;
    color: white;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

section[data-testid="stSidebar"] {
    resize: horizontal;
    overflow: auto;
    min-width: 280px;
    max-width: 600px;
    background-color: #111827;
}

.nav-container {
    background-color: #111827;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 70px;
    font-weight: bold;
    color: white;
}

.highlight {
    color: #ff6b35;
}

.hero-subtitle {
    font-size: 24px;
    color: #9ca3af;
    margin-top: 15px;
}

.hero-text {
    font-size: 20px;
    line-height: 1.8;
    color: #d1d5db;
    margin-top: 30px;
}

.stButton > button {
    width: 100%;
    background-color: transparent;
    border: 1px solid #ff6b35;
    color: white;
    border-radius: 10px;
    padding: 12px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #ff6b35;
    color: white;
}

.feature-card {
    background-color: #15151d;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
}

.attempt-card {
    background:#1f2937;
    padding:20px;
    border-radius:15px;
    margin-top:20px;
}

.section-title {
    font-size: 45px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

.section-text {
    color: #d1d5db;
    font-size: 20px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# NAVBAR
# =====================================================

st.markdown(
    '<div class="nav-container">',
    unsafe_allow_html=True
)

# =====================================================
# AFTER LOGIN
# =====================================================

if st.session_state.logged_in:

    nav1, nav2, nav3, nav4 = st.columns(4)

    with nav1:

        if st.button("🏠 Home"):

            st.session_state.page = "Dashboard"

            st.rerun()

    with nav2:

        if st.button("ℹ️ About"):

            st.session_state.page = "About"

            st.rerun()

    with nav3:

        if st.button("📞 Contact"):

            st.session_state.page = "Contact"

            st.rerun()

    with nav4:

        if st.button("🎫 Tickets"):

            st.session_state.page = "Tickets"

            st.rerun()

# =====================================================
# BEFORE LOGIN
# =====================================================

else:

    nav1, nav2, nav3, nav4, nav5 = st.columns(5)

    with nav1:

        if st.button("🏠 Home"):

            st.session_state.page = "Home"

            st.rerun()

    with nav2:

        if st.button("ℹ️ About"):

            st.session_state.page = "About"

            st.rerun()

    with nav3:

        if st.button("📞 Contact"):

            st.session_state.page = "Contact"

            st.rerun()

    with nav4:

        if st.button("🔐 Login"):

            st.session_state.page = "Login"

            st.rerun()

    with nav5:

        if st.button("📝 Signup"):

            st.session_state.page = "Signup"

            st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# HOME PAGE
# =====================================================

if st.session_state.page == "Home":

    left, right = st.columns([2, 1])

    with left:

        st.markdown("""
        <div class="hero-title">
        Multi-Agent <br>
        <span class="highlight">
        AI Helpdesk
        </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-subtitle">
        AI-powered intelligent IT support platform
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="hero-text">

        Resolve technical issues instantly using AI-generated troubleshooting,
        smart ticket escalation,
        WhatsApp technician notifications,
        and persistent support history.

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.image(
            "https://thunderonthegulf.com/wp-content/uploads/2025/10/RMA-47.jpg",
            width=1000
        )

    st.write("")
    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="feature-card">
        <h3>AI Troubleshooting</h3>
        <p>
        Generate intelligent troubleshooting solutions instantly.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="feature-card">
        <h3>Smart Escalation</h3>
        <p>
        Automatically escalate unresolved tickets to technicians.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="feature-card">
        <h3>Persistent History</h3>
        <p>
        Store and manage previous support conversations.
        </p>
        </div>
        """, unsafe_allow_html=True)


# =====================================================
# ABOUT PAGE
# =====================================================

elif st.session_state.page == "About":

    left, right = st.columns([2, 1])

    with left:

        st.markdown("""
        <div class="section-title">
        About Platform
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            font-size:24px;
            color:#d1d5db;
            line-height:2;
        ">

        ✅ AI-powered intelligent IT support system<br>

        ⚙️ Automated troubleshooting using Multi-Agent AI architecture<br>

        📂 Smart issue classification based on category and priority<br>

        🚨 Automatic ticket escalation for unresolved incidents<br>

        📲 Real-time WhatsApp technician notifications using Twilio<br>

        🧠 Persistent chat history and incident tracking system<br>

        ⚡ Faster incident resolution with AI-generated solutions<br>

        🔐 Secure authentication and user management system<br>

        🌐 Users can submit issues related to network connectivity, VPN access, WiFi failures, software crashes, authentication problems, email access issues, system performance errors, printer connectivity, and other IT support incidents.

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.image(
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200",
            width=1000
        )


# =====================================================
# CONTACT PAGE
# =====================================================

elif st.session_state.page == "Contact":

    st.markdown("""
    <div class="section-title">
    Contact
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-text">

    📧 support@aihelpdesk.com

    🏫 Siddaganga Institute of Technology

    💻 Multi-Agent Autonomous AI Helpdesk

    </div>
    """, unsafe_allow_html=True)


# =====================================================
# TICKET TRACKING PAGE
# =====================================================

elif (
    st.session_state.page == "Tickets"
    and st.session_state.logged_in
):

    import pandas as pd
    import plotly.express as px

    col_back1, col_back2 = st.columns([1, 5])

    with col_back1:

        if st.button("⬅ Back to Chatbot"):

            st.session_state.page = "Dashboard"

            st.rerun()

    st.markdown("""
    <div class="section-title">
    Ticket Tracking Dashboard
    </div>
    """, unsafe_allow_html=True)

    tickets = get_user_tickets(
        st.session_state.username
    )

    # =====================================================
    # NO TICKETS
    # =====================================================

    if len(tickets) == 0:

        st.info(
            "No tickets generated yet."
        )

    # =====================================================
    # ANALYTICS SECTION
    # =====================================================

    else:

        df = pd.DataFrame(tickets)

        # =====================================================
        # METRICS
        # =====================================================

        total_tickets = len(df)

        solved_tickets = len(
            df[df["status"] == "RESOLVED"]
        )

        pending_tickets = len(
            df[df["status"] != "RESOLVED"]
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🎫 Total Tickets",
                total_tickets
            )

        with col2:

            st.metric(
                "✅ Solved",
                solved_tickets
            )

        with col3:

            st.metric(
                "🚨 Pending",
                pending_tickets
            )

        st.write("")
        st.write("")

        # =====================================================
        # CATEGORY GRAPH
        # =====================================================

        category_chart = px.pie(

            df,

            names="category",

            title="Issue Category Distribution"
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )

        # =====================================================
        # PRIORITY GRAPH
        # =====================================================

        priority_chart = px.bar(

            df["priority"].value_counts(),

            title="Priority Distribution"
        )

        st.plotly_chart(
            priority_chart,
            use_container_width=True
        )

        st.write("")
        st.write("")

        # =====================================================
        # TICKET CARDS
        # =====================================================

        for ticket in reversed(tickets):

            st.markdown(
                f"""
<div class="feature-card">

<h3>
🎫 {ticket['ticket_id']}
</h3>

<p>
<b>Issue:</b>
{ticket['issue']}
</p>

<p>
<b>Assigned Team:</b>
{ticket['team']}
</p>

<p>
<b>Priority:</b>
{ticket['priority']}
</p>

<p>
<b>Category:</b>
{ticket['category']}
</p>

<p>
<b>Status:</b>
{ticket['status']}
</p>

</div>
""",
                unsafe_allow_html=True
            )

            # =====================================================
            # BUTTONS ONLY FOR OPEN TICKETS
            # =====================================================

            if ticket["status"] != "RESOLVED":

                col1, col2 = st.columns(2)

                # =====================================================
                # RESOLVE BUTTON
                # =====================================================

                with col1:

                    if st.button(

                        f"✅ Resolve {ticket['ticket_id']}"
                    ):

                        update_ticket_status(

                            ticket["ticket_id"],

                            "RESOLVED"
                        )

                        st.success(
                            "Ticket closed successfully."
                        )

                        st.rerun()

                # =====================================================
                # REMINDER BUTTON
                # =====================================================

                with col2:

                    if st.button(

                        f"🔔 Reminder {ticket['ticket_id']}"
                    ):

                        from agents.twilio_agent import send_whatsapp_notification

                        reminder_message = f"""

🚨 Reminder Notification

🎫 Ticket ID:
{ticket['ticket_id']}

Issue still unresolved.

Please contact the user again immediately.

"""

                        send_whatsapp_notification(
                            reminder_message
                        )

                        st.success(
                            "Reminder sent to technician."
                        )

# =====================================================
# LOGIN PAGE
# =====================================================

elif st.session_state.page == "Login":

    login_page()


# =====================================================
# SIGNUP PAGE
# =====================================================

elif st.session_state.page == "Signup":

    signup_page()


# =====================================================
# DASHBOARD PAGE
# =====================================================

elif (
    st.session_state.page == "Dashboard"
    and st.session_state.logged_in
):

    st.sidebar.success(
        f"Welcome {st.session_state.name}"
    )

    st.sidebar.markdown("## 💬 Chat History")

    history = get_user_history(
        st.session_state.username
    )

    if len(history) == 0:

        st.sidebar.info(
            "No previous chats"
        )

    else:

        reversed_history = list(
            reversed(history)
        )

        for i, chat in enumerate(reversed_history):

            title = chat.get(
                "issue",
                "Untitled Chat"
            )[:35]

            col1, col2 = st.sidebar.columns([4, 1])

            with col1:

                if st.button(
                    f"💬 {title}",
                    key=f"history_{i}"
                ):

                    st.session_state.selected_chat = chat

                    st.session_state.current_solution = ""

            with col2:

                if st.button(
                    "🗑️",
                    key=f"delete_{i}"
                ):

                    delete_chat(
                        st.session_state.username,
                        chat["issue"]
                    )

                    st.session_state.selected_chat = None

                    st.rerun()

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.session_state.page = "Home"

        st.rerun()

    st.markdown("""
    <div class="section-title">
    AI Incident Resolution Dashboard
    </div>
    """, unsafe_allow_html=True)

    if st.button("➕ New Chat"):

        st.session_state.current_query = ""

        st.session_state.current_solution = ""

        st.session_state.classification = {}

        st.session_state.attempt = 0

        st.session_state.all_solutions = []

        st.session_state.selected_chat = None

        st.rerun()

    if st.session_state.selected_chat:

        selected_chat = st.session_state.selected_chat

        st.subheader("📝 Previous Conversation")

        st.markdown(
            f"""
### Issue
{selected_chat.get('issue', 'N/A')}

### 📂 Category
{selected_chat.get('classification', {}).get('category', 'N/A')}

### ⚡ Priority
{selected_chat.get('classification', {}).get('priority', 'N/A')}

### 📌 Status
{selected_chat.get('status', 'N/A')}
"""
        )

        solutions = selected_chat.get(
            "solutions",
            []
        )

        for idx, sol in enumerate(solutions):

            st.markdown(
                f"""
<div class="attempt-card">

<h3>
Attempt {idx + 1}
</h3>

<div style="
font-size:18px;
line-height:2;
color:#d1d5db;
">

{sol.replace(chr(10), '<br>')}

</div>

</div>
""",
                unsafe_allow_html=True
            )

    query = st.text_area(
        "Describe Your IT Issue",
        value=st.session_state.current_query,
        height=150
    )

    if st.button("Analyze Issue"):

        if query.strip() == "":

            st.warning(
                "Please enter your issue."
            )

        else:

            processing = st.empty()

            processing.info(
                "🔄 AI agents are analyzing your issue..."
            )

            with st.spinner("Processing..."):

                result = process_query(query)

            processing.success(
                "✅ Analysis completed successfully"
            )

            st.session_state.current_query = query

            st.session_state.current_solution = result["solution"]

            st.session_state.classification = result["classification"]

            st.session_state.attempt = 1

            st.session_state.all_solutions = [
                result["solution"]
            ]

            save_chat(

                st.session_state.username,

                query,

                st.session_state.all_solutions,

                1,

                "AI_RESPONSE",

                result["classification"]
            )

            st.rerun()

    if st.session_state.current_solution != "":

        classification = st.session_state.classification

        st.markdown(
            f"""
<div class="feature-card">

<h3>
AI Resolution Attempts
</h3>

<p>
📂 <b>Category:</b>
{classification.get('category', 'N/A')}
</p>

<p>
⚡ <b>Priority:</b>
{classification.get('priority', 'N/A')}
</p>

<p>
👨‍💻 <b>Assigned Team:</b>
{classification.get('team', 'N/A')}
</p>

</div>
""",
            unsafe_allow_html=True
        )

        for idx, sol in enumerate(
            st.session_state.all_solutions
        ):

            st.markdown(
                f"""
<div class="attempt-card">

<h3>
Attempt {idx + 1}
</h3>

<div style="
font-size:18px;
line-height:2;
color:#d1d5db;
">

{sol.replace(chr(10), '<br>')}

</div>

</div>
""",
                unsafe_allow_html=True
            )

        st.subheader(
            "Was your issue resolved?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✅ Yes, Issue Solved"):

                update_chat(

                    st.session_state.username,

                    st.session_state.current_query,

                    st.session_state.all_solutions,

                    st.session_state.attempt,

                    "RESOLVED",

                    st.session_state.classification
                )

                st.success(
                    "Glad your issue was resolved successfully."
                )

                st.balloons()

        with col2:

            if st.button("❌ No, Issue Not Solved"):

                if st.session_state.attempt == 1:

                    from agents.feedback_agent import regenerate_solution

                    processing = st.empty()

                    processing.warning(
                        "🔄 Generating another AI troubleshooting solution..."
                    )

                    with st.spinner(
                        "Generating second attempt..."
                    ):

                        new_solution = regenerate_solution(

                            st.session_state.current_query,

                            st.session_state.current_solution
                        )

                    processing.success(
                        "✅ Alternative solution generated"
                    )

                    st.session_state.current_solution = new_solution

                    st.session_state.attempt = 2

                    st.session_state.all_solutions.append(
                        new_solution
                    )

                    update_chat(

                        st.session_state.username,

                        st.session_state.current_query,

                        st.session_state.all_solutions,

                        2,

                        "SECOND_ATTEMPT",

                        st.session_state.classification
                    )

                    st.rerun()

                elif st.session_state.attempt == 2:

                    from agents.escalation_agent import escalate_issue

                    escalation = escalate_issue(

                        st.session_state.username,

                        st.session_state.name,

                        st.session_state.phone,

                        st.session_state.current_query,

                        st.session_state.current_solution,

                        st.session_state.classification
                    )

                    update_chat(

                        st.session_state.username,

                        st.session_state.current_query,

                        st.session_state.all_solutions,

                        st.session_state.attempt,

                        "ESCALATED",

                        st.session_state.classification
                    )

                    st.error(
                        "Issue unresolved after 2 AI attempts."
                    )

                    st.success(
                        f"""
🎫 Ticket Generated Successfully

Ticket ID:
{str(escalation.get("ticket_id", "N/A"))}
"""
                    )

                    st.info(
                        f"""
📲 WhatsApp notification sent successfully.

Twilio SID:
{str(escalation.get("sid", "N/A"))}
"""
                    )

                    st.balloons()