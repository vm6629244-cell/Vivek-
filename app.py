"""
AI Vivek Consultant Bot - Enhanced Version
WhatsApp + OpenAI Integration
"""

from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import requests
import json
import os
from datetime import datetime
import threading
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration from environment
TOKEN = os.getenv("WHATSAPP_TOKEN", "")
PHONE_ID = os.getenv("PHONE_NUMBER_ID", "")
VERIFY = os.getenv("VERIFY_TOKEN", "ai_vivek_365")
OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
UPI_ID = os.getenv("UPI_ID", "misharvivek0201@axl")

# Validate required environment variables
required_vars = ["WHATSAPP_TOKEN", "PHONE_NUMBER_ID", "VERIFY_TOKEN"]
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    logger.error(f"Missing environment variables: {', '.join(missing_vars)}")
    logger.error("Copy .env.example to .env and fill in your values")
    if os.getenv("FLASK_ENV") != "development":
        exit(1)

# File paths
USERS_FILE = "users.json"
ENQ_FILE = "enquiries.json"
LOGS_FILE = "bot_logs.json"

# Initialize files
for f in [USERS_FILE, ENQ_FILE, LOGS_FILE]:
    if not os.path.exists(f):
        with open(f, "w") as jf:
            json.dump({} if f != LOGS_FILE else [], jf)

def load(p):
    """Load JSON file safely"""
    try:
        with open(p) as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading {p}: {e}")
        return {} if "enq" in p or "user" in p else []

def save(p, data):
    """Save JSON file safely"""
    try:
        with open(p, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Error saving {p}: {e}")

def log_event(event_type, phone, message, response=""):
    """Log bot events for analytics"""
    try:
        logs = load(LOGS_FILE)
        logs.append({
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "phone": phone,
            "message": message[:100],  # Truncate long messages
            "response": response[:100]
        })
        save(LOGS_FILE, logs[-100:])  # Keep last 100 logs
    except Exception as e:
        logger.error(f"Error logging event: {e}")

def send(to, txt):
    """Send message via WhatsApp API"""
    if not TOKEN or not PHONE_ID:
        logger.warning("WhatsApp credentials not configured")
        return False
    
    url = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"
    h = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": txt[:3800]}
    }
    
    try:
        response = requests.post(url, headers=h, json=payload, timeout=10)
        if response.status_code == 200:
            logger.info(f"Message sent to {to}")
            return True
        else:
            logger.error(f"Failed to send message: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        return False

# Expert AI Prompt
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
    
    # Try OpenAI first if key is configured
    if OPENAI_KEY and OPENAI_KEY.startswith("sk-"):
        try:
            import openai
            openai.api_key = OPENAI_KEY
            prompt = EXPERT_PROMPT.format(upi=UPI_ID, problem=problem)
            
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
                temperature=0.7,
                timeout=10
            )
            
            result = response.choices[0].message.content.strip()
            logger.info(f"OpenAI response generated")
            return result
            
        except Exception as e:
            logger.warning(f"OpenAI error: {e}, using fallback template")
    
    # Fallback templates based on keywords
    low = problem.lower()
    
    if any(w in low for w in ["career", "job", "naukri", "business", "promotion", "salary"]):
        return f"""Career Pattern: '{problem}'

1. **Soch**: Tum safety aur growth me confuse ho.
2. **Aadat**: Roz 2 ghante ek hi skill par bina phone ke.
3. **Nazariya**: Naukri tumhe paisa deti hai, skill tumhe choice deti hai. Agle 7 din ek skill chuno.

Detail me samjhau? **HUMAN likho**. 
Note: Ye margdarshan hai, antim nirnay aapka vivek."""
    
    elif any(w in low for w in ["love", "rishta", "shaadi", "relationship", "breakup", "proposal"]):
        return f"""Relationship Pattern: '{problem}'

1. **Sunna**: 2 min bina advise ke suno.
2. **Samjhana**: 'Tumhe aisa lag raha hai' bolo.
3. **Suljhana**: Solution se pehle feeling ko accept karo.

Is pattern ko todne ka daily task du? **HUMAN likho**."""
    
    elif any(w in low for w in ["paise", "money", "investment", "business", "earn", "rich"]):
        return f"""Money Mindset: '{problem}'

1. **Samjho**: Paisa earn se zyada important save karna hai.
2. **Action**: Aaj se 1 jar, 100 rupay roz dalo.
3. **Result**: 1 saal me 36,000. 5 saal me 2 lakhs+.

Aur seekhna hai? **HUMAN likho**."""
    
    elif any(w in low for w in ["overthink", "anxiety", "tension", "stress", "worry", "fear"]):
        return f"""Mind Hack: '{problem}'

Overthinking ka ilaaj sochna nahi, action hai.
1 kaam chuno, 2 min me shuru karo.
Kal ka wait khatam, aaj se start.

Aur guidance chahiye? **HUMAN likho**."""
    
    else:
        return f"""Life Hack: '{problem}'

Ek kagaz nikalo. Likho: 'Aaj ka 1 kaam jisse raat ko sukoon milega'.
Bas wahi kar. 2 min me shuru kar.
Roz ye karo, life change hoga.

Personal session chahiye? **HUMAN likho**."""

# Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "🎯 AI Vivek Consultant Bot v2 - LIVE 🚀",
        "version": "2.0.0",
        "endpoints": {
            "webhook": "/webhook (POST)",
            "enquiries": "/api/enquiries (GET)",
            "reply": "/api/reply (POST)",
            "dashboard": "/consultant (GET)",
            "logs": "/api/logs (GET)"
        }
    }), 200

@app.route("/webhook", methods=["GET"])
def verify():
    """Webhook verification for WhatsApp"""
    if request.args.get("hub.verify_token") == VERIFY:
        logger.info("Webhook verified successfully")
        return request.args.get("hub.challenge"), 200
    logger.warning("Webhook verification failed")
    return "fail", 403

@app.route("/webhook", methods=["POST"])
def hook():
    """Handle incoming WhatsApp messages"""
    try:
        data = request.get_json()
        entry = data.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})
        
        if "messages" not in value:
            return "ok", 200
        
        message = value["messages"][0]
        phone = message["from"]
        text = message.get("text", {}).get("body", "").strip()
        
        if not text:
            return "ok", 200
        
        logger.info(f"Message from {phone}: {text[:50]}")
        
        # Save enquiry
        enq = load(ENQ_FILE)
        enq[phone] = {
            "problem": text,
            "time": datetime.now().strftime("%d/%m %H:%M"),
            "status": "pending"
        }
        save(ENQ_FILE, enq)
        
        low = text.lower()
        
        # Handle commands
        if low in ["hi", "hello", "start", "start 365"]:
            greeting = f"""Namaste 🙏 Main AI Vivek - 40 saal ke adhyayan se bana Consultant

Problem ek line me likho, main pattern + solution dunga.

📱 UPI: {UPI_ID}
📍 Follow: @vivekmishravoidhissa0007 | @vivekmishra77771"""
            send(phone, greeting)
            log_event("greeting", phone, text)
            
        elif low == "human":
            send(phone, "✅ Human consultant ko request bhej di. 2 ghante me reply ayega. Tab tak DOB + sawal bhej do. Priority ke liye 199 pay karke PAID likho.")
            log_event("human_request", phone, text)
            
        elif low == "paid":
            send(phone, "✅ Premium ON! Ab tum priority me ho. Problem dubara likho.")
            log_event("premium_activated", phone, text)
            
        else:
            # Generate AI reply asynchronously
            def send_ai_reply():
                try:
                    reply = get_ai_reply(text)
                    send(phone, reply)
                    log_event("ai_response", phone, text, reply)
                except Exception as e:
                    logger.error(f"Error generating AI response: {e}")
                    send(phone, "Kuch error hua. Dobara try kar.")
            
            threading.Thread(target=send_ai_reply, daemon=True).start()
    
    except Exception as e:
        logger.error(f"Webhook error: {e}")
    
    return "ok", 200

@app.route("/api/enquiries", methods=["GET"])
def get_enquiries():
    """Get all enquiries"""
    try:
        enq = load(ENQ_FILE)
        return jsonify(enq), 200
    except Exception as e:
        logger.error(f"Error fetching enquiries: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/reply", methods=["POST"])
def reply_enquiry():
    """Send reply via WhatsApp"""
    try:
        data = request.get_json()
        phone = data.get("phone")
        reply_text = data.get("reply")
        
        if not phone or not reply_text:
            return jsonify({"error": "Phone and reply required"}), 400
        
        # Send message
        if send(phone, reply_text):
            # Update enquiry
            enq = load(ENQ_FILE)
            if phone in enq:
                enq[phone]["status"] = "replied"
                enq[phone]["reply"] = reply_text
                enq[phone]["reply_time"] = datetime.now().strftime("%d/%m %H:%M")
                save(ENQ_FILE, enq)
            
            log_event("reply_sent", phone, reply_text[:100])
            return jsonify({"success": True}), 200
        else:
            return jsonify({"error": "Failed to send message"}), 500
    
    except Exception as e:
        logger.error(f"Error sending reply: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/api/logs", methods=["GET"])
def get_logs():
    """Get bot activity logs"""
    try:
        logs = load(LOGS_FILE)
        return jsonify(logs[-50:]), 200  # Return last 50 logs
    except Exception as e:
        logger.error(f"Error fetching logs: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/consultant")
def dashboard():
    """Serve consultant dashboard"""
    try:
        return send_from_directory(".", "consultant_dashboard.html")
    except Exception as e:
        logger.error(f"Dashboard error: {e}")
        return f"Dashboard error: {e}", 404

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {error}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    
    logger.info(f"🚀 Starting AI Vivek Bot on port {port}")
    logger.info(f"📱 WhatsApp Phone ID: {PHONE_ID if PHONE_ID else 'NOT CONFIGURED'}")
    logger.info(f"🤖 OpenAI: {'CONFIGURED' if OPENAI_KEY else 'NOT CONFIGURED'}")
    
    app.run(host="0.0.0.0", port=port, debug=debug)