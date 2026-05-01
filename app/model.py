def load_model(config):
    # Mock model (fast + no heavy dependencies)
    return None, None


def generate_text(model, tokenizer, prompt, max_tokens):
    # Simulated inference
    return f"[Generated response | max_tokens={max_tokens}] -> {prompt}"