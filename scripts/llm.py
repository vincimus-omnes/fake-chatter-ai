from gpt4all import GPT4All

def prompt_llm(speech):
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM

    prompt = "In 150 characters or less "
    prompt += "ask an interesting question or make an interesting observation about the following text: "

    prompt += speech

    with model.chat_session():
        return model.generate(prompt, max_tokens=1024)