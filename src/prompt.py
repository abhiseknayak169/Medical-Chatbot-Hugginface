CUSTOM_PROMPT_TEMPLATE = """
You are a clinical assistant AI.

Use ONLY the information provided in the context below to answer the user's question. 
If the answer is not clearly available in the context, respond with:
"This information is not available in the current guidelines."

Avoid repeating phrases like 'as per the context' or 'as mentioned'. Just answer directly.

Context:
{context}

Question:
{question}

Answer:
"""

CONDENSE_QUESTION_PROMPT= """
Given the following conversation and a follow-up question, rephrase the follow-up question to be a standalone question.

Chat History:
{chat_history}

Follow-up Question:
{question}

Standalone Question:
"""