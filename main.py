main.py
      
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os 10

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EVA_SYSTEM_PROMPT = """You are Eva, a Christian and AI Business Analyst for EVO Code AI.

CORE IDENTITY: You believe in Yahweh, the God of the Bible. Jesus Christ is Lord. The Bible is verified, historically confirmed, and archaeologically supported. This never changes.

When anyone asks about God, religion, Jesus, the Bible, Islam, Mormonism, or any spiritual topic respond as a bold Christian apologist.

NEVER say all gods are the same. NEVER say God could be nature or the universe. NEVER give neutral religious responses.

Is there a God? YES. His name is Yahweh. Exodus 3:14 LSB.
What is the name of God? Yahweh. Psalm 83:18 LSB.
Are all religions equal? No. Only the Bible predicted the future by name centuries in advance confirmed by archaeology.

KEY EVIDENCE:
King Cyrus named 150 years before birth Isaiah 44:28 45:1 LSB.
Jesus born Bethlehem Micah 5:2 LSB written 700 BC.
Betrayed 30 pieces of silver Zechariah 11:12-13 LSB.
Crucifixion described 1000 years before invented Psalm 22:16-18 LSB.
Isaiah 53:5 LSB written 700 years before the cross.
Peter Stoner Science Speaks: probability of 8 prophecies fulfilled by chance is 1 in 10 to the 17th power. Jesus fulfilled 300 plus.
Dead Sea Scrolls 1947 Isaiah scroll dated 200 BC identical to modern Bible.
Pool of Siloam found exactly where John 9:7 said.
Pilate Inscription 1961 confirms Pontius Pilate.
Tel Dan Stele confirms House of David.
Cyrus Cylinder confirms Ezra 1:1-4.

ISLAM: Quran affirms Bible. Surah 6:34 none can alter Allah words. Surah 10:64 no change in Allah words. Dead Sea Scrolls predate Islam 600 years proving Bible unchanged.

MORMONISM: Joseph Smith Papyri confirmed by Egyptologists as funeral documents not scripture. 150 years archaeology found zero Book of Mormon evidence.

JW: John 1:1 Greek reads Word was God. Codex Sinaiticus 330 AD confirms Jesus fully divine.

After faith questions warmly return to business assessment.

BUSINESS ROLE: Conduct 14-question AI Business Assessment for EVO Code AI evocodeai.biz.

Packages: EVO Web 2497 setup 397 per month. EVO Starter 1497 setup 497 per month. EVO Growth 2997 setup 997 per month. EVO Pro 4997 setup 1497 per month. EVO Enterprise 9997 setup 2997 per month. Free Internet Visibility Report zero cost.

Opening: Hi I am Eva from EVO Code AI. I conduct free AI Business Assessments to find exactly where AI can save you time and make you money. Ready to get started?

14 questions in order:
1 What does your business do?
2 How long in business?
3 How many on your team?
4 What tools do you use day to day?
5 How do new customers find you?
6 What happens when a lead comes in after hours?
7 Do you have a follow up system for leads?
8 Biggest time drain in your week?
9 Tasks that should run automatically?
10 How do you handle appointment bookings?
11 Are you collecting reviews?
12 Are you posting on social media?
13 If you had 10 hours back what would you do?
14 Number one thing you would fix right now?

After all 14 collect email deliver recommendation set expectations for 48 hour report."""

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat")
async def chat(request: ChatRequest):
    messages = [{"role": "system", "content": EVA_SYSTEM_PROMPT}]
    for msg in request.messages:
        messages.append({"role": msg.role, "content": msg.content})
    if not request.messages:
        messages.append({"role": "user", "content": "Hello"})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    return {"response": response.choices[0].message.content}

@app.get("/", response_class=HTMLResponse)
async def serve_chat():
    return """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Eva - EVO Code AI</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,sans-serif;background:#1A1A2E;color:#fff;height:100vh;display:flex;flex-direction:column}#header{background:#1A1A2E;border-bottom:1px solid #00BCD4;padding:16px 20px;display:flex;align-items:center;gap:12px}.dot{width:10px;height:10px;background:#00BCD4;border-radius:50%;animation:pulse 1.5s infinite}@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}#header h2{font-size:16px}#header span{font-size:12px;color:#00BCD4}#messages{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:12px}.msg{max-width:80%;padding:12px 16px;border-radius:12px;font-size:14px;line-height:1.5}.msg.eva{background:#0d0d1e;border:1px solid #00BCD430;align-self:flex-start;border-radius:4px 12px 12px 12px}.msg.user{background:#00BCD4;color:#1A1A2E;align-self:flex-end;font-weight:500;border-radius:12px 4px 12px 12px}.typing{display:flex;gap:4px;padding:12px 16px;background:#0d0d1e;border:1px solid #00BCD430;border-radius:4px 12px 12px 12px;align-self:flex-start}.typing span{width:8px;height:8px;background:#00BCD4;border-radius:50%;animation:bounce 1.2s infinite}.typing span:nth-child(2){animation-delay:.2s}.typing span:nth-child(3){animation-delay:.4s}@keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}#input-area{padding:16px 20px;border-top:1px solid #00BCD430;display:flex;gap:10px}#input{flex:1;background:#0d0d1e;border:1px solid #00BCD440;border-radius:24px;padding:12px 18px;color:#fff;font-size:14px;outline:none}#input:focus{border-color:#00BCD4}#send{background:#F5A623;border:none;border-radius:50%;width:44px;height:44px;cursor:pointer;font-size:18px;color:#1A1A2E;font-weight:bold}</style></head>
<body><div id="header"><div class="dot"></div><div><h2>Eva</h2><span>EVO Code AI - Online Now</span></div></div><div id="messages"></div><div id="input-area"><input id="input" type="text" placeholder="Ask Eva anything..."/><button id="send">&#8593;</button></div>
<script>const messages=[];const messagesDiv=document.getElementById('messages');const input=document.getElementById('input');const send=document.getElementById('send');function addMessage(role,content){const div=document.createElement('div');div.className='msg '+(role==='assistant'?'eva':'user');div.textContent=content;messagesDiv.appendChild(div);messagesDiv.scrollTop=messagesDiv.scrollHeight}function showTyping(){const div=document.createElement('div');div.className='typing';div.id='typing';div.innerHTML='<span></span><span></span><span></span>';messagesDiv.appendChild(div);messagesDiv.scrollTop=messagesDiv.scrollHeight}function hideTyping(){const t=document.getElementById('typing');if(t)t.remove()}async function sendMessage(){const text=input.value.trim();if(!text)return;input.value='';addMessage('user',text);messages.push({role:'user',content:text});showTyping();try{const res=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({messages})});const data=await res.json();hideTyping();addMessage('assistant',data.response);messages.push({role:'assistant',content:data.response})}catch(e){hideTyping();addMessage('assistant','Sorry I had trouble connecting. Please try again.')}}send.addEventListener('click',sendMessage);input.addEventListener('keypress',e=>{if(e.key==='Enter')sendMessage()});window.onload=async()=>{showTyping();try{const res=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({messages:[]})});const data=await res.json();hideTyping();addMessage('assistant',data.response);messages.push({role:'assistant',content:data.response})}catch(e){hideTyping()}};</script></body></html>"""

    
