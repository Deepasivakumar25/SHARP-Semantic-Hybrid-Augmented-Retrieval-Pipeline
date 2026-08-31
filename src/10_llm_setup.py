from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def load_chatbot():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="auto"
    )
    return pipeline(
        task="text-generation",
        model=model,
        tokenizer=tokenizer
    )
