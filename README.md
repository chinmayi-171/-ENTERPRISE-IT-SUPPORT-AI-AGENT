Enterprise IT Support AI Agent

Overview
An AI-powered enterprise IT support and incident management system that uses Retrieval-Augmented Generation (RAG), ChromaDB, and multi-agent architecture to analyze incidents, retrieve similar past issues, and generate intelligent troubleshooting solutions.


Features
- Intelligent incident classification
- RAG-based incident retrieval
- AI-generated troubleshooting solutions
- Ticket escalation support
- WhatsApp notifications using Twilio
- Multi-agent architecture
- ChromaDB vector database integration

Technologies Used
- Python
- Streamlit
- ChromaDB
- Groq LLM
- Sentence Transformers
- Twilio API
- LangChain

Project Structure

```bash
project/
│
├── agents/
├── vectordb/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
```

Installation

```bash
pip install -r requirements.txt
```

Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=your_number
TECHNICIAN_WHATSAPP=your_number
```

Run the Application

```bash
streamlit run app.py
```

Future Enhancements
- Dashboard analytics
- Voice-enabled support
- Automated ticket prioritization
- Cloud deployment
