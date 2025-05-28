"""
DALL-E prompt generation for research papers
"""
from .prompt_utils import extract_keywords, identify_domain, extract_specific_concepts, detect_title_focus

# Dictionary of domain-specific color palettes
DOMAIN_COLOR_PALETTES = {
    "computer vision and image processing": "vibrant blues, greens, and digital highlights",
    "natural language processing and text analysis": "warm oranges, soft whites, and typographic elements",
    "machine learning and neural networks": "deep purples, electric blues, and gradient flows",
    "robotics and autonomous systems": "industrial grays, precise reds, and mechanical details",
    "data science and analytics": "analytical blues, data-point reds, and statistical patterns",
    "medical AI and healthcare technology": "medical whites, diagnostic blues, and gentle healing greens",
    "quantum computing and quantum information": "quantum blues, probability purples, and uncertainty patterns",
    "reinforcement learning and intelligent agents": "reward golds, strategic blues, and environmental greens",
    "artificial intelligence research": "technological blues, innovative purples, and conceptual gradients"
}

def generate_image_prompt(paper):
    """
    Generate a DALL-E prompt based on paper content
    """
    title = paper.title
    abstract = paper.summary
    
    # Extract combined text
    combined_text = extract_keywords(title, abstract)
    
    # Identify domain and visual elements
    domain_context, visual_elements = identify_domain(combined_text)
    
    # Extract specific concepts
    specific_concepts = extract_specific_concepts(combined_text)
    
    # Get title focus
    title_focus = detect_title_focus(title)
    
    # Create the enhanced prompt
    base_elements = ", ".join(visual_elements[:2]) if visual_elements else "abstract AI concept visualization"
    
    concept_addition = ""
    if specific_concepts:
        concept_addition = f", specifically highlighting {specific_concepts[0]} concepts"
    
    # Get the domain-specific color palette
    color_palette = DOMAIN_COLOR_PALETTES.get(domain_context, "modern professional colors with subtle gradients")
    
    prompt = f"""
    Create a modern, sophisticated illustration representing {domain_context}. 
    The image should feature {base_elements}{concept_addition}{title_focus}.
    
    Use a palette of {color_palette}. 
    The style should be clean, minimalist, and technically accurate, suitable for 
    a research publication or technical blog. 
    
    Avoid any text, human figures, or company logos. Show concrete, recognizable 
    technical elements and concepts that directly relate to {domain_context.split(' ')[0]} 
    research. Make the connection to the research topic immediately clear and visually 
    representative of the actual work being done.
    """
    
    # Debug info to return
    debug_info = {
        "domain": domain_context,
        "concepts": specific_concepts[:2] if specific_concepts else [],
        "color_palette": color_palette
    }
    
    return prompt, debug_info