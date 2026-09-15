import anthropic
from app.config import ANTHROPIC_API_KEY, LLM_MODEL
from app.generation.prompt_templates import CITATION_SYSTEM_PROMPT

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def generate_answer(prompt: str) -> str:
    """Call Claude API with the built prompt and return the answer text."""
    response = client.messages.create(
        model=LLM_MODEL,
        max_tokens=1024,
        system=CITATION_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text