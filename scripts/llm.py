from gpt4all import GPT4All

def prompt_llm(prompt):
    model = GPT4All("Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf") # downloads / loads a 4.66GB LLM

    

    with model.chat_session():
        return model.generate(prompt, max_tokens=1024)