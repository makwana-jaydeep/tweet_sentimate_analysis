from transformers import BertForSequenceClassification
import torch
from my_tokenizer import tokenized_text

model = BertForSequenceClassification.from_pretrained('fine_tuned_bert_model_directory')

def find_sentimate(text):
   

    input_id = tokenized_text(text)

    tn=torch.tensor([input_id])

    with torch.no_grad():
            outputs = model(tn)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1)
    return preds

if __name__ == "__main__":
    tweet_text = "This is a tweet text" 
    preds = find_sentimate(tweet_text)
    print("Predicted Sentiment:", "Positive" if preds == 1 else "Negative")



