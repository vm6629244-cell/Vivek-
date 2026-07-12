"""
365 Days Challenge Post Generator
Generates daily posts with theme rotation for social media
"""

themes = ["Mindset", "Career Growth", "Relationship", "Money", "Focus", "Overthinking"]

posts = {
    1: {
        "theme": "Mindset",
        "hook": "Aaj se 365 din badalne ka resolve?",
        "action": "Ek notebook khol. Likho: 'Mera aaj ka 1 kaam'. Bas wahi kar. Raat ko tick mark lagana.\nKal dobara.",
        "cta": "Type START 365 for daily hack"
    },
    2: {
        "theme": "Career Growth",
        "hook": "Naukri se aage jaane ka tarika kya hai?",
        "action": "Aaj ek skill Google kar jo tum nahi jante. 30 min seekhne ka time nikalo.\nKisi ko bata ki tu ye seekh raha hai.",
        "cta": "Type START 365 for daily hack"
    },
    3: {
        "theme": "Relationship",
        "hook": "Close person ko galat samjhna band karega kab?",
        "action": "Ek person ko call kar jo tum expect karते ho but nahi call karte ho.\nBas 5 min baat kar. Koi advice nahi, just suno.",
        "cta": "Type START 365 for daily hack"
    },
    4: {
        "theme": "Money",
        "hook": "Paise kamai se zyada important kya hai?",
        "action": "Apne din ka 1 rupay ka expense likho. Roz likha to mahine me pattern dikha jayega.\nAb decide kar: ye zaruri tha?",
        "cta": "Type START 365 for daily hack"
    },
    5: {
        "theme": "Focus",
        "hook": "Distractions se bachna itna mushkil kyun lagta hai?",
        "action": "Phone silence kar. 1 ghante sirf 1 kaam kar. Timer lagao.\nItna hi. Bass aaj ke liye.",
        "cta": "Type START 365 for daily hack"
    },
    6: {
        "theme": "Overthinking",
        "hook": "Dimag me 100 baatein ek saath kyun chalti hain?",
        "action": "Jab overthink hone lage, kagaz par 5 lines likho jo tension de rahi hain.\nFir sabme se 1 par sirf action karo. Baaki bhul jao.",
        "cta": "Type START 365 for daily hack"
    },
    7: {
        "theme": "Mindset",
        "hook": "Failure se seekhna start kab karoge?",
        "action": "Ek pal socho jab tum fail hue the. Waha se kya seikh a?\nLikho ek line: 'Mene ye seekha'.",
        "cta": "Type START 365 for daily hack"
    },
    8: {
        "theme": "Career Growth",
        "hook": "Same job, same paisa, agle 5 saal bhi yahi rahega?",
        "action": "LinkedIn profile dekh ek successful person ka. Dekh kya skill hai wo jisse tum alag ho.\nAaj 1 step utho us direction me.",
        "cta": "Type START 365 for daily hack"
    },
    9: {
        "theme": "Relationship",
        "hook": "Jisse baat nahi ho rahe, uske liye grudge rakhte ho?",
        "action": "Ek message likho (bhejne se pehle rough draft bana).\nSeedha bol: 'Misunderstanding hua. Clear karte hain?'",
        "cta": "Type START 365 for daily hack"
    },
    10: {
        "theme": "Money",
        "hook": "Paise save karoge ya sirf earn karoge?",
        "action": "Aaj se ek savings jar virtual ya physical banao.\nChota sa target: 100 rupay aaj. Dekh kya se bach sakta hai.",
        "cta": "Type START 365 for daily hack"
    }
}

# Generate hashtags
def get_hashtags(day_number):
    return f"#AIVivek #Day{day_number} #{themes[(day_number - 1) % 6]}"

# Generate footer
def get_footer():
    return """
💰 UPI: misharvivek0201@axl

Follow for more:
📱 @vivekmishravoidhissa0007
📱 @vivekmishra77771
📱 @viv.ek00047
📱 @viekvoidhissa0369
"""

# Generate full post
def generate_post(day_number):
    if day_number not in posts:
        # Generate for days beyond our predefined list
        theme_index = (day_number - 1) % 6
        theme = themes[theme_index]
        hook = f"Day {day_number}: {theme} hack padhai de raha hai?"
        action = f"Aaj ka 1 action kar jo tere {theme.lower()} ko badal de.\nSoch aur kar."
    else:
        post = posts[day_number]
        theme = post["theme"]
        hook = post["hook"]
        action = post["action"]
    
    cta = "Type START 365 for daily hack"
    hashtags = get_hashtags(day_number)
    footer = get_footer()
    
    full_post = f"""
🎯 DAY {day_number} - {theme.upper()}

{hook}

📌 ACTION FOR TODAY:
{action}

👇 {cta}

{hashtags}

{footer}
"""
    
    return full_post.strip()

# Example usage
if __name__ == "__main__":
    for day in [1, 2, 3, 7, 15, 30]:
        print(generate_post(day))
        print("\n" + "="*60 + "\n")
