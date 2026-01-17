from textblob import TextBlob

def vibe(text):
    # FIX 1: You must pass the text into TextBlob()
    blob = TextBlob(text)
    
    # FIX 2: Access the sentiment tuple directly to prevent the 'cached_property' error
    sentiment_data = blob.sentiment 
    polarity = sentiment_data.polarity
    subjectivity = sentiment_data.subjectivity

    # Complexity Upgrade: Basic Sarcasm Check
    # High subjectivity + Positive words + specific trigger words
    sarcasm_triggers = ['wow', 'great', 'brilliant', 'amazing', 'thanks']
    is_sarcastic = False
    if polarity > 0 and subjectivity > 0.6:
        if any(word in text.lower() for word in sarcasm_triggers):
            is_sarcastic = True

    if polarity > 0.5:
        label = "EXTREMELY POSITIVE 🌟"
    elif polarity > 0:
        label = "POSITIVE 🙂"
    elif polarity == 0:
        label = "NEUTRAL 😐"
    elif polarity > -0.5:
        label = "NEGATIVE 😟"
    else:
        label = "VERY NEGATIVE 😡"

    if is_sarcastic:
        label += " (CAUTION: Sarcasm Detected 🤨)"

    return label, polarity, subjectivity

if __name__ == "__main__":
    print("--- AI Sentiment Bot Initialized ---")
    print("Type 'exit' to stop")

    while True:
        user_input = input("\nEnter Text to be analysed: ")
        
        if user_input.lower() == "exit":
            break
        
        try:
            label, pol, subj = vibe(user_input)
            print(f"Analysis: {label}")
            print(f"Polarity Score: {round(pol, 2)}")
            print(f"Subjectivity (0=Fact, 1=Opinion): {round(subj, 2)}")
        except Exception as e:
            print(f"Error: {e}. Ensure you ran 'python -m textblob.download_corpora'")