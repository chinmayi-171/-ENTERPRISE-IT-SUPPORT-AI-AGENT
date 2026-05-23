from groq import Groq

# GROQ CLIENT
client = Groq(

    api_key="GROQ_API_KEY"
)


def regenerate_solution(issue, previous_solution):

    # PROMPT
    prompt = f"""
The previous troubleshooting attempt failed.

User Issue:
{issue}

Previous Failed Solution:
{previous_solution}

Generate a COMPLETELY DIFFERENT troubleshooting approach.

Generate ONLY:

1. Alternative Solution Steps
2. Expected Result

STRICT RULES:
- Do NOT repeat previous steps
- Use numbered troubleshooting steps
- Keep response under 100 words
- No paragraphs
- No repeated content
- Be concise and technical

EXAMPLE FORMAT:

1. Alternative Solution Steps
1. Clear saved WiFi credentials
2. Flush DNS cache
3. Restart network adapter
4. Reconnect to office WiFi

2. Expected Result
- Stable network connection established
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

        temperature=0.5
    )

    return response.choices[0].message.content