from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

def fine_tune_model():
    model_name = "bert-base-uncased"
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    
    training_args = TrainingArguments(output_dir="./models/fine_tuned")
    trainer = Trainer(model=model, args=training_args)
    
    trainer.train()
    model.save_pretrained("./models/fine_tuned")

if __name__ == "__main__":
    fine_tune_model()
