# 🚀 AI Vivek - Complete Setup Guide

## 📋 Prerequisites

- Python 3.8+
- Node.js 18+ (for TypeScript/Render webhook)
- WhatsApp Business Account
- Meta Developer Account
- OpenAI API Key
- Render Account (optional, for deployments)

---

## 🔐 Step 1: Get WhatsApp API Tokens

### 1.1 Create Meta Business Account
1. Go to [facebook.com/business](https://facebook.com/business)
2. Sign in or create account
3. Go to Meta Business Platform

### 1.2 Create WhatsApp App
1. Navigate to [developers.facebook.com](https://developers.facebook.com)
2. Go to **My Apps** → **Create App**
3. App Name: `AI Vivek Consultant`
4. App Purpose: **Business**
5. Select **WhatsApp** product

### 1.3 Get Phone Number ID
1. In your app, go to **WhatsApp** → **Phone Numbers**
2. Add a phone number (or use test number)
3. Copy the **Phone Number ID** (looks like: `102340567890123`)
4. Save to `.env` as `PHONE_NUMBER_ID`

### 1.4 Get WhatsApp API Token
1. Go to **Settings** → **API Credentials**
2. Copy **Temporary Access Token** or generate **Permanent Token**
3. Save to `.env` as `WHATSAPP_TOKEN`

---

## 📱 Step 2: Configure WhatsApp Webhook

### 2.1 Generate Webhook URL
Your webhook runs at: `https://your-domain.com/webhook`

### 2.2 Set Webhook in Meta Platform
1. Go to **App Settings** → **Webhooks**
2. Click **Manage webhooks for WhatsApp**
3. Set **Callback URL**: `https://your-domain.com/webhook`
4. Set **Verify Token**: `ai_vivek_365` (or custom value from `.env`)
5. Subscribe to: `messages`, `message_status`
6. Save and verify

### 2.3 Test Webhook
```bash
curl -X GET "http://localhost:5000/webhook?hub.mode=subscribe&hub.challenge=test_challenge&hub.verify_token=ai_vivek_365"
# Should return: test_challenge
```

---

## 🤖 Step 3: OpenAI Setup

### 3.1 Create API Key
1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Click **Create New Secret Key**
3. Copy key (starts with `sk-`)
4. Save to `.env` as `OPENAI_API_KEY`

### 3.2 Add Billing
1. Go to **Billing** → **Overview**
2. Add payment method
3. Set usage limits

---

## 🔧 Step 4: Environment Setup

### 4.1 Clone Repository
```bash
git clone https://github.com/vm6629244-cell/Vivek-.git
cd Vivek-
```

### 4.2 Create .env File
```bash
cp .env.example .env
```

### 4.3 Edit .env with Your Values
```bash
nano .env
# or
code .env
```

Fill in:
- `WHATSAPP_TOKEN`
- `PHONE_NUMBER_ID`
- `OPENAI_API_KEY`
- `VERIFY_TOKEN`
- All other required fields

---

## 📦 Step 5: Install Dependencies

### Python Flask Bot
```bash
pip install -r requirements.txt
```

### TypeScript Render Webhook (Optional)
```bash
cd render-webhook
npm install
# or
pnpm install
```

---

## 🚀 Step 6: Run Application

### Start Flask Bot
```bash
python app.py
```

You should see:
```
🎯 AI Vivek Consultant Bot v2 - LIVE 🚀
* Running on http://0.0.0.0:5000
```

### Access Dashboard
Open browser: `http://localhost:5000/consultant`

---

## 📊 Step 7: Test the Bot

### Test 1: Send WhatsApp Message
1. Open WhatsApp
2. Send message to your phone number
3. Message: `hi`
4. Should receive greeting response

### Test 2: Ask a Question
1. Send: `Mera career stuck hai`
2. Should receive AI Vivek's advice

### Test 3: Check Dashboard
1. Go to `http://localhost:5000/consultant`
2. Should see enquiry appear in "Pending" section
3. Type reply and send
4. Should appear in WhatsApp

---

## 🌐 Step 8: Deploy to Production

### Option A: Deploy to Render
1. Create account on [render.com](https://render.com)
2. Connect GitHub repo
3. Create new **Web Service**
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`
6. Add environment variables from `.env`
7. Deploy

### Option B: Deploy to Heroku
```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set WHATSAPP_TOKEN=xxx
heroku config:set OPENAI_API_KEY=xxx
# ... add all from .env

# Deploy
git push heroku main
```

### Option C: Deploy to AWS / DigitalOcean
See respective platform documentation.

---

## 🔄 Step 9: Setup GitHub Actions (Optional)

### For Render Webhook Integration
1. Get Render API Key: [render.com/api-keys](https://render.com/api-keys)
2. Add to GitHub Secrets:
   - `RENDER_API_KEY`
   - `GITHUB_API_TOKEN`
3. Update `.env` with values

---

## ✅ Verification Checklist

- [ ] WhatsApp token working
- [ ] OpenAI API key valid
- [ ] Webhook receiving messages
- [ ] Dashboard loading
- [ ] Can send/receive replies
- [ ] AI responses generating
- [ ] Enquiries saving to JSON
- [ ] Deployed to production

---

## 🐛 Troubleshooting

### Issue: "Webhook verification failed"
**Solution:** 
- Verify `VERIFY_TOKEN` matches in Meta Platform
- Check webhook URL is accessible
- Ensure `app.py` is running

### Issue: "OpenAI API error"
**Solution:**
- Check `OPENAI_API_KEY` is valid
- Verify API key has billing
- Check monthly usage limit

### Issue: "Messages not sending"
**Solution:**
- Verify `WHATSAPP_TOKEN` is current
- Check `PHONE_NUMBER_ID` is correct
- Ensure phone number is approved in Meta Platform
- Test with `/webhook` endpoint

### Issue: "Dashboard not loading"
**Solution:**
- Check Flask is running on correct port
- Clear browser cache
- Check browser console for errors
- Verify `enquiries.json` exists

---

## 📚 Resources

- [WhatsApp Cloud API Docs](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com)
- [Render Deployment](https://render.com/docs)

---

## 💡 Tips

1. **Test Locally First**: Always test on `localhost:5000` before deploying
2. **Monitor Logs**: Use `tail -f app.log` to watch for errors
3. **Backup Data**: Regularly backup `enquiries.json`
4. **Update Dependencies**: `pip install --upgrade -r requirements.txt`
5. **Use Ngrok for Testing**: `ngrok http 5000` to get public URL for webhook testing

---

## 🎯 What's Next?

- [ ] Customize AI prompts in `app.py`
- [ ] Add more day posts to `day_post_generator.py`
- [ ] Create reels using `reels_script_generator.py`
- [ ] Setup automated daily posts
- [ ] Add database (MongoDB/PostgreSQL) instead of JSON
- [ ] Build mobile app

---

## 📞 Support

For issues, create GitHub Issue or contact:
- 📧 UPI: misharvivek0201@axl
- 📱 Instagram: @vivekmishravoidhissa0007