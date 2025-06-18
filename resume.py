import gradio as gr
import requests
import os

# === Config ===
API_KEY = "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"
MODEL = "deepseek/deepseek-r1:free"

resume_text = """
James is Dedicated technical support professional with a proven track record in troubleshooting and technical problem resolution across various platforms. Enthusiasm for driving customer experience enhancement through effective communication and proactive problem-solving is evident. Experience in working in a 24x7 environment, monitoring systems, and collaborating with teams aligns well with the commitment to ensuring seamless service delivery. A strong focus on understanding customer needs and implementing process improvements contributes to fostering trust and satisfaction.

JAMES CHERIYAN
Technical Support Specialist | IT Solutions | Customer Experience
+44  7442585688
jamescheriyan47@outlook.com
Belfast, UK
Dedicated technical support professional with a proven track record in troubleshooting and technical problem resolution across various platforms. Enthusiasm for driving customer experience enhancement through effective communication and proactive problem-solving is evident. Experience in working in a 24x7 environment, monitoring systems, and collaborating with teams aligns well with the commitment to ensuring seamless service delivery. A strong focus on understanding customer needs and implementing process improvements contributes to fostering trust and satisfaction.
Technical Support Engineer
Natterbox

01/2025 - Present 

Belfast, United Kingdom
•
Customer Contact & Experience
NatWest Group

03/2022 - Present 

FirstSource Belfast, United Kingdom
•
Served as the first point of contact for online banking issues, troubleshooting and escalating technical problems via call and email.
•
Documented common issues and solutions to enhance internal knowledge resources.
•
Collaborated with IT teams to resolve technical issues, ensuring timely and effective solutions.
•
Assisted customers with digital banking services, ensuring smooth adoption and quick issue resolution.
•
Identified recurring technical challenges and proactively suggested process improvements.
•
Maintained detailed logs of customer interactions and issues for further analysis, contributing to enhanced service delivery.
•
Monitored multiple customer-facing banking systems to ensure seamless operation and alignment with business and customer needs.
Customer Contact Associate - Technical Support
Comcast Corp Xfinity

07/2019 - 09/2021 

Nuance Communications Bangalore
•
Provided technical support to end-users, resolving hardware, software, and connectivity issues via live chat, email and CRM.
•
Diagnosed and resolved critical system failures in a time-sensitive environment.
•
Monitored IT systems and networks, proactively identifying and resolving performance bottlenecks.
•
Managed system health and availability through regular audits and maintenance tasks.
•
Collaborated with cross-functional teams to ensure timely resolution of service disruptions.
•
Delivered remote technical support for Xfinity digital services, including internet, TV, and VoIP phone systems.
•
Designed and implemented process improvements, reducing downtime and enhancing efficiency.
•
Maintained accurate and up-to-date customer records in CRM.
•
Acted as a liaison between technical teams and non-technical users, ensuring mutual understanding.
Technical Troubleshooting
System Monitoring
Problem Solving
Collaboration
Communication Skills
Attention to Detail
Process Optimization
24x7 Environment
Adaptability
Telecoms Experience
Quick Learning
Networking Knowledge
Decision Making
Help Desk
Active Listening
User Feedback Analysis
CRM Proficiency
Knowledge Base Development
VoIP
Python
IT Systems Proficiency
SQL
Technical support specialist
Excels in software support services via multiple channels.
Collaboration
Skilled in collaborating with cross-functional teams to achieve organizational goals and drive effective solutions.
Customer-focused problem solver
Resolves complex issues while improving user experience.
Effective communicator
Exceptional communication skills, ensuring efficient issue resolution.
Customer-centric approach
Strong ability to analyze customer feedback and drive system improvements.
MSc Computer Science
Ulster University

02/2022 - 09/2023 

Belfast, UK
BCA - Bachelor's in Computer Application
Kannur University

06/2011 - 06/2014 

Kannur
Page 2
Customer Service Advisor - Technical Support
AT&T U-verse

11/2017 - 12/2018 

[24]7.ai Bangalore
•
Effectively managed multiple priorities in a structured and timely manner within a 24x7 shift environment via live chat, email and CRM.
•
Diagnosed and resolved technical issues for AT&T U-verse internet, TV, and VoIP phone services.
•
Addressed customer service concerns with professionalism, ensuring compliance with quality standards and adherence to established procedures.
•
Conducted training sessions to promote best practices and improve individual and team performance in technical support and service delivery.
•
Monitored and maintained customer-facing systems to ensure operational continuity and prompt issue resolution.
•
Ensure customer records in the CRM are consistently accurate and current.
•
Assisted customers with service setups, upgrades, and troubleshooting, ensuring seamless adoption and optimal performance of digital solutions.
IT Technical Support Specialist and Trainer
Little Flower Convent School

06/2014 - 01/2017 

•
Conducted training sessions for staff on TechNext digital systems, ensuring smooth adoption of new technologies.
•
Provided technical support for school software, improving system usability and user satisfaction.
•
Improved understanding of computer systems for over 300 students, resulting in 95% exam pass rate improvement.
HOBBIES
Football
Badminton
Cycling
Traveling & Hiking

"""

# === Ask Function ===
def ask_question(question,history):
    prompt = f"""
You are an AI assistant that answers questions about a person based on their resume. You should act a James Cheriyan and need to answer to the questions. 

Resume:
\"\"\"
{resume_text}
\"\"\"

Question: {question}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    return response.json()["choices"][0]["message"]["content"]

starter_questions = [
    "What are your technical skills?",
    "Describe your experience at Natterbox.",
    "What is your educational background?",
    "Summarize your work history.",
    "What certifications or degrees do you have?",
    "Where have you worked before?",
    "What experience do you have in telecom or VoIP?",
    "How do you handle system monitoring in a 24x7 environment?"
]

# === Gradio Chatbot Interface ===

chat = gr.ChatInterface(fn=ask_question,title="📄 Ask Me About My Resume", examples=starter_questions)
chat.launch(server_name="0.0.0.0", server_port=8080,share=True)
