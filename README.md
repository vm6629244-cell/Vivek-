# AI Vivek - 365 Days Mindset Challenge Platform

Complete AI-powered consultation platform with WhatsApp integration, OpenAI responses, live dashboards, and automated content generation.

## 🎯 Features

### 🤖 WhatsApp Consultant Bot
- Real-time message handling
- AI-powered responses (OpenAI GPT-4o-mini)
- Smart fallback templates (Hinglish + practical advice)
- Command handling (hi, human, paid)
- Async message processing
- Activity logging & analytics

### 📊 Live Enquiry Dashboard
- Real-time pending enquiries
- Quick-reply templates
- Batch response management
- Statistics (pending, replied, conversion rate)
- Auto-refresh every 5 seconds
- Professional UI (Gradient design)

### 📱 Content Generators
- **Daily Posts**: 365 days pre-written social media posts
- **Reels Scripts**: 15-second Instagram Reels / YouTube Shorts scripts
- **Theme Rotation**: Mindset, Career, Relationship, Money, Focus, Overthinking
- **Auto-Generation**: Works for any day (1-365)

### 🔗 Integrations
- WhatsApp Cloud API
- OpenAI GPT-4o-mini
- GitHub Actions (Render webhooks)
- JSON-based data storage
- Flask REST API

### 🚀 Deployment Ready
- Environment configuration (.env)
- Production logging
- Error handling & validation
- Gunicorn WSGI support
- Render / Heroku compatible

---

## 📋 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/vm6629244-cell/Vivek-.git
cd Vivek-
cp .env.example .env
# Fill in your WhatsApp & OpenAI tokens
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
python app.py
# Visit: http://localhost:5000/consultant
```

### 4. Send WhatsApp Message
- Text your WhatsApp number
- Type: `hi` or ask a question
- Get AI response instantly

---

## 📁 Project Structure

```
Vivek-/
├── app.py                          # Main Flask bot
├── app.ts                          # Render webhook (TypeScript)
├── requirements.txt                # Python dependencies
├── package.json                    # Node.js dependencies
│
├── consultant_dashboard.html       # Live enquiry panel UI
├── day_post_generator.py           # 365 days post generator
├── reels_script_generator.py       # 15-sec video script generator
│
├── .env.example                    # Configuration template
├── .github/workflows/example.yaml  # GitHub Actions workflow
├── render.yaml                     # Render deployment config
│
├── SETUP_GUIDE.md                  # Complete setup instructions
├── README.md                       # This file
└── LICENSE                         # MIT License

# Generated at runtime:
├── enquiries.json                  # Pending/replied messages
├── users.json                      # User data
├── bot_logs.json                   # Activity logs
└── app.log                         # Application logs
```

---

## 🔐 Environment Variables

See `.env.example` for complete list. Key ones:

```env
WHATSAPP_TOKEN=your_token
PHONE_NUMBER_ID=your_phone_id
OPENAI_API_KEY=sk-your-key
VERIFY_TOKEN=ai_vivek_365
UPI_ID=misharvivek0201@axl
```

---

## 🌐 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|----------|
| GET | `/` | Health check + info |
| GET | `/webhook` | WhatsApp verification |
| POST | `/webhook` | Receive WhatsApp messages |
| GET | `/api/enquiries` | List all enquiries |
| POST | `/api/reply` | Send reply via WhatsApp |
| GET | `/api/logs` | Bot activity logs |
| GET | `/consultant` | Live dashboard UI |

---

## 🚀 Deployment

### Render
```bash
# Connect GitHub repo to Render
# Build: pip install -r requirements.txt
# Start: python app.py
# Add env vars from .env
```

### Heroku
```bash
heroku create your-app
git push heroku main
heroku config:set WHATSAPP_TOKEN=xxx
```

### Docker
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

## 📊 Usage Examples

### Generate Daily Post (Day 5)
```python
from day_post_generator import generate_post
post = generate_post(5)
print(post)
```

### Generate Reels Script (Day 10)
```python
from reels_script_generator import generate_reels_script, format_script_for_video
script = generate_reels_script(10)
print(format_script_for_video(script))
```

### Use AI Response Directly
```python
from app import get_ai_reply
response = get_ai_reply("Mera career stuck hai")
print(response)
```

---

## 💡 Features Breakdown

### WhatsApp Bot Commands
- `hi` / `hello` / `start` - Get greeting
- `human` - Request human consultant
- `paid` - Activate premium mode
- Any text - Get AI consultation response

### Dashboard Features
- 📊 Real-time statistics
- 🔄 Auto-refresh every 5 seconds
- 💬 Quick-reply templates
- ✅ Pending/replied tracking
- 📈 Conversion rate display

### AI Response Features
- 🎯 Personalized advice
- 🔄 3-point structure (Soch, Aadat, Nazariya)
- 🌍 Hinglish language
- 📱 WhatsApp-friendly format
- 🤖 Fallback templates when API fails

---

## 🔧 Customization

### Change AI Persona
Edit `EXPERT_PROMPT` in `app.py`

### Add More Day Posts
Edit `reels_scripts` dict in `reels_script_generator.py`

### Modify Dashboard UI
Edit `consultant_dashboard.html`

### Add Database
Replace JSON files with MongoDB/PostgreSQL

---

## 📈 Analytics

Bot logs all interactions in `bot_logs.json`:
```json
{
  "timestamp": "2026-07-12T10:30:00",
  "type": "ai_response",
  "phone": "918000000000",
  "message": "Mera career stuck hai",
  "response": "Career Pattern: ..."
}
```

Access via `/api/logs` endpoint.

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file

---

## 📞 Support

- 📱 UPI: misharvivek0201@axl
- 📧 Instagram: @vivekmishravoidhissa0007
- 🐛 Issues: [GitHub Issues](https://github.com/vm6629244-cell/Vivek-/issues)

---

## 🙏 Credits

**AI Vivek** - 40 years combined study in:
- AI & Machine Learning
- Career Astrology Patterns
- Human Behaviour & Psychology
- Mindset Coaching

Built with ❤️ for Young India

---

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Database integration (MongoDB)
- [ ] Email notifications
- [ ] SMS integration
- [ ] Payment gateway (Razorpay)
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] Video consultation feature

---

## 📊 Tech Stack

**Backend**: Flask, Python 3.11, OpenAI API
**Frontend**: HTML5, CSS3, JavaScript (vanilla)
**Messaging**: WhatsApp Cloud API, Meta Platform
**Deployment**: Render, Heroku, Docker, AWS
**Storage**: JSON (local), MongoDB/PostgreSQL (optional)
**Monitoring**: Python logging, JSON logs

---

**Last Updated**: 2026-07-12
**Version**: 2.0.0
**Status**: Production Ready ✅