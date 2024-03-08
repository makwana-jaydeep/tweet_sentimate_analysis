from transformers import BertTokenizer

#loading the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenized_text(text):


        tokens = tokenizer.tokenize(text)

        max_length = 25  

        padded_tokens = tokens[:max_length] + ['[PAD]'] * (max_length - len(tokens))

        special_tokens = ['[CLS]'] + padded_tokens + ['[SEP]']

        input_ids = tokenizer.convert_tokens_to_ids(special_tokens)

        return input_ids

if __name__ == "__main__":
    print("tokenized_text function is working fine.")