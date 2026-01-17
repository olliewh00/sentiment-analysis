import sys
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER
vader = SentimentIntensityAnalyzer()

def get_vibe_check(text):
    blob = TextBlob(text)
    tb_polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    vader_scores = vader.polarity_scores(text)
    compound = vader_scores['compound'] 

    if compound >= 0.05:
        sentiment_label = "POSITIVE 🟢"
    elif compound <= -0.05:
        sentiment_label = "NEGATIVE 🔴"
    else:
        sentiment_label = "NEUTRAL ⚪"

    nuance = "Consistent"
    if (tb_polarity > 0 and compound < 0) or (tb_polarity < 0 and compound > 0):
        nuance = "High (Potential Sarcasm or Mixed Emotions) ⚠️"

    return {
        "label": sentiment_label,
        "compound": compound,
        "subjectivity": subjectivity,
        "nuance": nuance,
        "breakdown": vader_scores
    }

if __name__ == "__main__":
    print("="*40)
    print("🚀 ADVANCED NLP INTELLIGENCE ENGINE v2.0")
    print("Models: VADER (Intensity) + TextBlob (Nuance)")
    print("="*40)
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\n[Analyze Text] > ")

        if user_input.lower() in ['exit', 'quit']:
            print("Shutting down...")
            break

        if not user_input.strip():
            continue

        try:
            res = get_vibe_check(user_input)

            print(f"\nOVERALL VIBE: {res['label']}")
            print(f"├─ Intensity Score: {res['compound']} (-1 to 1)")
            print(f"├─ Fact vs Opinion: {'Mostly Opinion' if res['subjectivity'] > 0.5 else 'Mostly Fact'}")
            print(f"├─ Data Nuance:     {res['nuance']}")
            print(f"└─ Logic Breakdown: [Pos: {res['breakdown']['pos']} | Neg: {res['breakdown']['neg']} | Neu: {res['breakdown']['neu']}]")
            
        except Exception as e:
            print(f"❌ Error processing input: {e}")