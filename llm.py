from gpt4all import GPT4All

def prompt_llm():
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
    with model.chat_session():
        return model.generate("In 150 characters or less how can I run LLMs efficiently on my laptop?", max_tokens=1024)