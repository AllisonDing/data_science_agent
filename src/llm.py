from crewai import LLM

def get_llm() -> LLM:
    api_key = ""
    base_url = "https://integrate.api.nvidia.com/v1"
    model = "nvidia/llama-3.3-nemotron-super-49b-v1.5"

    if not api_key:
        raise RuntimeError("NVIDIA API Key not properly set")
    
    return LLM(
        model = model,
        base_url = base_url,
        api_key = api_key
    )
