from flask import Flask, request, jsonify, send_from_directory
import requests, json, os
from datetime import datetime
import threading

app = Flask(__name__)

TOKEN = os.getenv("WHATSAPP_TOKEN", "YOUR_TOKEN")
PHONE_ID = os.getenv("PHONE_NUMBER_ID", "YOUR_PHONE_ID")
VERIFY = os.getenv("VERIFY_TOKEN", "ai_vivek_365")
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
UPI_ID = "misharvivek0201@axl"

USERS_FILE = "users.json"
ENQ_FILE = "enquiries.json"

# Initialize files
for f in [USERS_FILE, ENQ_FILE]:
    if not os.path.exists(f):
        with open(f, "w") as jf:
            json.dump({} if "enq" in f else [], jf)

def load(p):
    try:
        with open(p) as f:
            return json.load(f)
    except:
        return {} if "enq" in p else []

def save(p, data):
    with open(p, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def send(to, txt):
    """Send message via WhatsApp"""
    url = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"
    h = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    try:
        requests.post(url, headers=h, json={
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": txt[:3800]}
        }, timeout=10)
    except Exception as e:
        print(f"Send error: {e}")

# 40 Years Expert Prompt
EXPERT_PROMPT = """
You are AI Vivek, 40 years combined study in AI, Career Astrology Patterns, Human Behaviour.
Rules:
1. Never give false prediction like "job will come on 15th". Always say pattern, habit, mindset.
2. Language: Hindi mix, simple, respectful, expert tone.
3. Structure: Problem ko 1 line me samjho, fir 3 point solution - Soch, Aadat, Nazariya.
4. End me always ask: HUMAN likho agar human consultant se detail me baat karni hai.
5. Never claim you are God or guarantee. Say "ye margdarshan self-reflection ke liye hai".
6. UPI ID {upi} par support ka zikr sirf jab user paid puche ya 3rd message ke baad.
User problem: {problem}
Give reply in 120 words max, WhatsApp friendly.
"""

def get_ai_reply(problem):
    """Get AI response using OpenAI or fallback template"""
    if OPENAI_KEY and OPENAI_KEY.startswith("sk-"):
        try:
            import openai
            openai.api_key = OPENAI_KEY
            prompt = EXPERT_PROMPT.format(upi=UPI_ID, problem=problem)
            resp = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.7
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI error: {e}")
    
    # Fallback templates
    low = problem.lower()
    if any(w in low for w in ["career", "job", "naukri", "business"]):
        return f"""Career Pattern: '{problem}'

1. **Soch**: Tum safety aur growth me confuse ho.
2. **Aadat**: Roz 2 ghante ek hi skill par bina phone ke.
3. **Nazariya**: Naukri tumhe paisa deti hai, skill tumhe choice deti hai. Agle 7 din ek skill chuno.

Detail me samjhau? **HUMAN likho**. 
Note: Ye margdarshan hai, antim nirnay aapka vivek."""
    
    if any(w in low for w in ["love", "rishta", "shaadi", "relationship"]):
        return f"""Relationship Pattern: '{problem}'

1. **Sunna**: 2 min bina advise ke suno.
2. **Samjhana**: 'Tumhe aisa lag raha hai' bolo.
3. **Suljhana**: Solution se pehle feeling ko accept karo.

Is pattern ko todne ka daily task du? **HUMAN likho**."""
    
    return f"""Mind Hack: '{problem}'

Overthinking ka ilaaj action hai. Ek kagaz par likho 'Aaj ka 1 kaam jisse raat ko sukoon milega'. Bas wahi karo. 2 min me shuru karo.

Roz 7AM ko exercise chahiye to **START 365 likho**. Human se baat karni hai to **HUMAN likho**."""

@app.route("/")
def home():
    return "🎯 AI Vivek Consultant Bot v2 - LIVE 🚀"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY:
        return request.args.get("hub.challenge"), 200
    return "fail", 403

@app.route("/webhook", methods=["POST"])
def hook():
    """Handle incoming WhatsApp messages"""
    try:
        v = request.get_json()["entry"][0]["changes"][0]["value"]
        if "messages" not in v:
            return "ok", 200
        
        m = v["messages"][0]
        frm = m["from"]
        txt = m.get("text", {}).get("body", "").strip()
        
        if not txt:
            return "ok", 200
        
        low = txt.lower()
        
        # Save enquiry
        enq = load(ENQ_FILE)
        enq[frm] = {
            "problem": txt,
            "time": datetime.now().strftime("%d/%m %H:%M"),
            "status": "pending"
        }
        save(ENQ_FILE, enq)
        
        # Handle commands
        if low in ["hi", "hello", "start", "start 365"]:
            send(frm, f"""Namaste 🙏 Main AI Vivek - 40 saal ke adhyayan se bana Consultant

Problem ek line me likho, main pattern + solution dunga.

📱 UPI: {UPI_ID}
📍 IDs: @vivekmishravoidhissa0007, @vivekmishra77771, @viv.ek00047, @viekvoidhissa0369""")
        elif low == "human":
            send(frm, "✅ Human consultant ko request bhej di. 2 ghante me reply ayega. Tab tak DOB + sawal bhej do. Priority ke liye 199 pay karke PAID likho.")
        elif low == "paid":
            send(frm, "✅ Premium ON! Ab tum priority me ho. Problem dubara likho.")
        else:
            # Send AI reply async
            def reply_async():
                reply = get_ai_reply(txt)
                send(frm, reply)
            threading.Thread(target=reply_async, daemon=True).start()
    
    except Exception as e:
        print(f"Webhook error: {e}")
    
    return "ok", 200

@app.route("/api/enquiries", methods=["GET"])
def get_enquiries():
    """API to get all enquiries for dashboard"""
    try:
        enq = load(ENQ_FILE)
        return jsonify(enq), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/reply", methods=["POST"])
def reply_enquiry():
    """API to send reply via WhatsApp"""
    try:
        data = request.get_json()
        phone = data.get("phone")
        reply_text = data.get("reply")
        
        if not phone or not reply_text:
            return jsonify({"error": "Phone and reply required"}), 400
        
        # Send message
        send(phone, reply_text)
        
        # Update enquiry status
        enq = load(ENQ_FILE)
        if phone in enq:
            enq[phone]["status"] = "replied"
            enq[phone]["reply"] = reply_text
            enq[phone]["reply_time"] = datetime.now().strftime("%d/%m %H:%M")
            save(ENQ_FILE, enq)
        
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/consultant")
def dashboard():
    """Serve consultant dashboard"""
    try:
        return send_from_directory(".", "consultant_dashboard.html")
    except:
        return "Dashboard not found", 404

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
