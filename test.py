import llama_cpp

# Load the model with optimized settings
llm = llama_cpp.Llama(
    model_path="D:/blog_generator/llama-2-7b-chat.Q4_K_M.gguf",  # Use a quantized model
    n_threads=8,  # Use available CPU threads for better speed
    n_batch=512,  # Increase batch size for efficient processing
    n_ctx=512,    # Context window size (keeps response relevant)
)

def generate_blog(topic):
    prompt = f"""
    Write a short, engaging, and well-structured blog post on "{topic}".
    
    **Structure:**
    - **Introduction** (1 sentence): Briefly introduce the topic.
    - **Key Points** (2-3 sentences): Explain its impact or importance.
    - **Conclusion** (1 sentence): End with a strong takeaway.

    **Guidelines:**
    - Keep it within **4-5 sentences** (max 80 words).
    - Use **clear, natural language** with proper grammar.
    - Avoid filler phrases like "In this blog, we discuss...".
    - Include **relevant emojis** for better readability.
    """

    response = llm(
        prompt,
        max_tokens=100,  # Keeps output short and relevant
        temperature=0.6,  # Reduces randomness for better quality
        top_p=0.85,       # Ensures coherent sentence flow
        stop=["\n\n", "###"],  # Prevents excessive text generation
    )

    return response["choices"][0]["text"].strip()

