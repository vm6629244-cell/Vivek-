"""
Instagram Reels / YouTube Shorts Script Generator
15-second video scripts for Day 1-365 Challenge
"""

# Reels scripts with timing and on-screen text
reels_scripts = {
    1: {
        "topic": "Mindset",
        "hook": "Suno, 365 din alag person banane ke liye bas 1 cheez chahiye.",
        "hook_text": "365 DAYS = 1 PERSON",
        "hook_duration": "0-3 sec",
        
        "body": "Roz ek kaam. Sirf ek. Wo suno. Notebook nikalo, likho 'aaj ka 1 kaam'. Khatam. Kal repeat. Itna hi. Badal jao 365 din me.",
        "body_text": "1 KAAM = 1 PROGRESS\nNOTEBOOK > PLANNING",
        "body_duration": "3-12 sec",
        
        "cta": "Follow karo, kal ka hack miss mat karo. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 2 HACK →",
        "cta_duration": "12-15 sec"
    },
    2: {
        "topic": "Career Growth",
        "hook": "Naukri same toh life same. Iska kya solution hai?",
        "hook_text": "SAME JOB = SAME LIFE",
        "hook_duration": "0-3 sec",
        
        "body": "Ek skill jo tum nahi jante. 30 min. Google kar, YouTube dekh, seekh le. Kisi ko batao. Bas itna. Month ke end dekh, 4 naye skills. Career badal jayega.",
        "body_text": "30 MIN = 1 SKILL\n1 MONTH = 4 SKILLS\n= PROMOTION READY",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, har din 1 hack. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 3 HACK →",
        "cta_duration": "12-15 sec"
    },
    3: {
        "topic": "Relationship",
        "hook": "Close person ko samjhte nahi, dosti tutti. Galti tum kar rahe ho.",
        "hook_text": "MISUNDERSTAND ≠ BROKEN",
        "hook_duration": "0-3 sec",
        
        "body": "Jo bhi tense ho, ek message likho. Ek line. 'Misunderstanding hua. Clear karte hain?' Bas. Call kar, 5 min baat kar. Solution. Jo aaj thin, kal mast rhenge.",
        "body_text": "1 MESSAGE = CLARITY\n5 MIN TALK = SOLUTION\n= RELATIONSHIP FIXED",
        "body_duration": "3-12 sec",
        
        "cta": "Follow karo, relationships fix hogi. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 4 HACK →",
        "cta_duration": "12-15 sec"
    },
    4: {
        "topic": "Money",
        "hook": "Paise kama rahe ho par kyu baki sab karte ho?",
        "hook_text": "EARNING ≠ SAVING",
        "hook_duration": "0-3 sec",
        
        "body": "Aaj se 1 jar. 100 rupay aaj. Dekh kya se bach sakta hai. Chocolate? Netflix? Ek chai wagairah. Mahine ke end 3000 rupay. Saal ka 36000. Badha invest kar. Done.",
        "body_text": "DAY 1: 100 RS\nMONTH: 3000 RS\nYEAR: 36,000 RS",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, financial freedom chahiye toh. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 5 HACK →",
        "cta_duration": "12-15 sec"
    },
    5: {
        "topic": "Focus",
        "hook": "Phone use karte karte productive baitha hun, ya sirf busy?",
        "hook_text": "PRODUCTIVE ≠ BUSY",
        "hook_duration": "0-3 sec",
        
        "body": "Aaj ek experiment. Phone silence kar. 1 ghanta. 1 kaam. Sirf wo. Timer lagao. Phone matte tak nahi kholunga. Dekh, kya ho gaya 1 ghante me. Game changer hoga.",
        "body_text": "1 HOUR NO PHONE\n= DEEP WORK MODE\n= 3X PRODUCTIVITY",
        "body_duration": "3-12 sec",
        
        "cta": "Follow karo, life organized ho jayegi. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 6 HACK →",
        "cta_duration": "12-15 sec"
    },
    6: {
        "topic": "Overthinking",
        "hook": "Dimag me 100 baatein. Kaunsi ko solve kare?",
        "hook_text": "100 THOUGHTS = PARALYSIS",
        "hook_duration": "0-3 sec",
        
        "body": "Ek kagaz nikalo. 5 baatein likho jo tension de rahi hain. Dekh. Ab sabme se 1 par action karo. Sirf 1. Baaki 4 bhul jao. Dekh, stress gayab ho gaya.",
        "body_text": "5 PROBLEMS → 1 ACTION\n= STRESS GONE\n= PEACE BACK",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, mental peace chahiye toh. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 7 HACK →",
        "cta_duration": "12-15 sec"
    },
    7: {
        "topic": "Mindset",
        "hook": "Fail hue toh sirf negative? Seekha kuch nahi?",
        "hook_text": "FAILURE ≠ END\nFAILURE = LESSON",
        "hook_duration": "0-3 sec",
        
        "body": "Ek time yaad kar jab fail hue the. Ruko. Usme se kya seikh a? Likho. Ek line. 'Mene ye seekha.' Bas itna seekhna bahut hai. Next time same mistake nahi. Done.",
        "body_text": "FAILURE → LESSON → SUCCESS\nREPEAT 365 TIMES",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, winner mindset banegi. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 8 HACK →",
        "cta_duration": "12-15 sec"
    },
    8: {
        "topic": "Career Growth",
        "hook": "LinkedIn dekha? Sab successful. Tu kya kar raha hai?",
        "hook_text": "COMPARISON KILLS\nVS\nINSPIRATION BUILDS",
        "hook_duration": "0-3 sec",
        
        "body": "LinkedIn pe ek successful dekh. Kya skill hai uske pass jo tere pas nahi? Likho. Aaj se wo seekhne ka 1 step utho. 30 min time nikalo. Start kar.",
        "body_text": "SEE SKILL GAP\n→ PLAN LEARNING\n→ TAKE 1 STEP TODAY",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, promotion lock. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 9 HACK →",
        "cta_duration": "12-15 sec"
    },
    9: {
        "topic": "Relationship",
        "hook": "Grudge hai? Uske liye kya, 5 sal wait karega?",
        "hook_text": "GRUDGE = POISON\nCLARITY = PEACE",
        "hook_duration": "0-3 sec",
        
        "body": "Aaj hi. Message likho. Ek line. Seedha. 'Misunderstanding hua. Baatein kar lete hain?' Press send. Dekh relationship fix hote time kitna lagta hai.",
        "body_text": "1 MESSAGE = BRIDGE\nCOURAgE = INSTANT",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, healthy relationships bangi. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 10 HACK →",
        "cta_duration": "12-15 sec"
    },
    10: {
        "topic": "Money",
        "hook": "Paisa earn kar ke khatam kar rahe ho? Kab save karega?",
        "hook_text": "EARN + SAVE = WEALTH",
        "hook_duration": "0-3 sec",
        
        "body": "Virtual savings jar. Aaj se 100 rupay. Roz likho kaha se save kiya. 1 month = 3000. 1 saal = 36000. Invest kar. 5 saal = 2 lakh+. Richness.",
        "body_text": "DAY 1: 100\nMO 1: 3K\nYEAR 1: 36K\nYEAR 5: 200K+",
        "body_duration": "3-12 sec",
        
        "cta": "Follow, rich ho jayega. AI Vivek, 365 Days Challenge.",
        "cta_text": "FOLLOW FOR DAY 11 HACK →",
        "cta_duration": "12-15 sec"
    }
}

def generate_reels_script(day_number):
    """Generate a complete 15-second reel script for any day"""
    
    if day_number not in reels_scripts:
        # Generate dynamic script for days beyond predefined
        themes = ["Mindset", "Career Growth", "Relationship", "Money", "Focus", "Overthinking"]
        theme = themes[(day_number - 1) % 6]
        
        script = {
            "day": day_number,
            "topic": theme,
            "hook": f"Day {day_number}: {theme} nahi seekha?",
            "hook_text": f"DAY {day_number}\n{theme.upper()}",
            "hook_duration": "0-3 sec",
            
            "body": f"Aaj ka 1 action. {theme} ko lekar. Socho mat, kar le. 2 min me solve.",
            "body_text": f"1 ACTION = GROWTH\n{theme.upper()} HACK",
            "body_duration": "3-12 sec",
            
            "cta": f"Follow, Day {day_number + 1} ka hack miss mat karo. AI Vivek, 365 Days Challenge.",
            "cta_text": f"FOLLOW FOR DAY {day_number + 1} →",
            "cta_duration": "12-15 sec",
            
            "hashtags": f"#AIVivek #Day{day_number} #{theme} #365DaysChallenge #YoungIndia #MindsetHack"
        }
    else:
        script = reels_scripts[day_number].copy()
        script["day"] = day_number
        script["hashtags"] = f"#AIVivek #Day{day_number} #{reels_scripts[day_number]['topic']} #365DaysChallenge #YoungIndia #MindsetHack"
    
    return script

def format_script_for_video(script):
    """Format script for video production"""
    
    output = f"""
╔════════════════════════════════════════════════════════════════════╗
║          📱 15-SECOND INSTAGRAM REELS / YOUTUBE SHORTS           ║
║                    DAY {script['day']} - {script['topic'].upper()}                  
╚════════════════════════════════════════════════════════════════════╝

🎬 VIDEO SCRIPT:

[0-3 SEC] HOOK - ATTENTION GRABBER
═══════════════════════════════════════════════
Voiceover: {script['hook']}
On-Screen Text: {script['hook_text']}
Tone: Loud, energetic, conversational
Visual: Hook text animation, eye contact

[3-12 SEC] BODY - THE HACK/LESSON/TRUTH
═══════════════════════════════════════════════
Voiceover: {script['body']}
On-Screen Text: {script['body_text']}
Tone: Fast-paced, practical, Gen-Z casual
Visual: Demo/action/text overlays, B-roll if needed

[12-15 SEC] CTA - CALL TO ACTION
═══════════════════════════════════════════════
Voiceover: {script['cta']}
On-Screen Text: {script['cta_text']}
Tone: Encouraging, FOMO-inducing
Visual: Follow button animation, social handles

📺 HASHTAGS:
{script['hashtags']}

💡 PRODUCTION TIPS:
✓ Fast cuts every 1-2 seconds
✓ Trending background music (Hinglish/English mix)
✓ Bold, readable fonts
✓ Face close-up in hook + CTA
✓ B-roll matching voiceover
✓ Captions for sound-off watching

📍 PLATFORM SPECS:
• Instagram Reels: 9:16 aspect ratio, 1080x1920px
• YouTube Shorts: 9:16 aspect ratio, 1080x1920px
• Duration: Exactly 15 seconds
"""
    
    return output

# Example usage
if __name__ == "__main__":
    # Generate scripts for Days 1, 5, 10
    for day in [1, 5, 10]:
        script = generate_reels_script(day)
        print(format_script_for_video(script))
        print("\n\n")
