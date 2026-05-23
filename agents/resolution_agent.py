from groq import Groq

# GROQ CLIENT
client = Groq(

    api_key="GROQ_API_KEY"
)


def generate_solution(user_query, retrieved_results):

    # RETRIEVED INCIDENTS
    docs = retrieved_results["documents"][0]

    metadata = retrieved_results["metadatas"][0]

    # BUILD CONTEXT
    context = ""

    for i in range(len(docs)):

        context += f"""

Issue:
{docs[i]}

Solution:
{metadata[i]['solution']}
"""

    # PROMPT
    prompt = f"""
You are an enterprise IT Helpdesk AI Assistant.

User Issue:
{user_query}

Previous Similar Incidents:
{context}

Generate ONLY the following sections:

1. Root Cause
2. Solution Steps
3. Expected Outcome

STRICT RULES:
- Keep response under 120 words
- Use point-wise format
- Use numbered troubleshooting steps
- No paragraphs
- No repeated text
- Keep concise and technical

EXAMPLE FORMAT:

1. Root Cause
- WiFi adapter driver corrupted after update

2. Solution Steps
1. Restart WiFi adapter
2. Update network drivers
3. Forget and reconnect office WiFi

3. Expected Outcome
- WiFi connectivity restored
"""

    # GROQ RESPONSE
    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content