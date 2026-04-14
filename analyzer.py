import google.generativeai as genai

# configure API
genai.configure(api_key="your_real_key")

model = genai.GenerativeModel("models/gemini-2.5-flash")

def get_ai_response(prompt):
    response = model.generate_content(prompt)
    return response.text


def analyze_answer(topic, explanation):
    with open("prompt.txt", "r") as f:
        base_prompt = f.read()

    full_prompt = f"""
Topic: {topic}

Candidate Explanation:
{explanation}

{base_prompt}
"""

    return get_ai_response(full_prompt)

def check_keywords(topic, explanation):
    topic_keywords={
        "rag":["retrieval", "embedding", "vector", "database", "llm"],
        "oops":["class", "object", "inheritance", "polymorphism"],
    }

    words=explanation.lower()

    missing=[]

    if topic.lower() in topic_keywords:
        for keyword in topic_keywords[topic.lower()]:
            if keyword not in words:
                missing.append(keyword)
        
    return missing
