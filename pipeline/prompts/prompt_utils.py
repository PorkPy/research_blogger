"""
Shared utilities for prompt generation across different prompt types
"""

def extract_keywords(title, abstract):
    """Extract important keywords from paper title and abstract"""
    combined_text = f"{title.lower()} {abstract.lower()}"
    return combined_text

def identify_domain(combined_text):
    """
    Identify the research domain based on combined text
    Returns domain_context and visual_elements
    """
    visual_elements = []
    domain_context = ""
    
    # Computer Vision / Image Processing
    if any(word in combined_text for word in ['image', 'vision', 'visual', 'detection', 'segmentation', 'object', 'face', 'recognition']):
        domain_context = "computer vision and image processing"
        visual_elements.extend([
            "digital image grids with highlighted features",
            "geometric detection boxes and annotations",
            "layered visual processing pipelines",
            "camera or sensor imagery with analytical overlays"
        ])
    
    # Natural Language Processing
    elif any(word in combined_text for word in ['language', 'text', 'nlp', 'translation', 'sentiment', 'dialogue', 'conversation', 'llm']):
        domain_context = "natural language processing and text analysis"
        visual_elements.extend([
            "flowing text streams transforming between languages",
            "word clouds with connecting semantic relationships",
            "chat bubbles and conversation interfaces",
            "linguistic trees and grammar structures"
        ])
    
    # Add all your other domain detection logic here...
    
    return domain_context, visual_elements

def extract_specific_concepts(combined_text):
    """
    Extract specific techniques or models mentioned in the paper
    """
    specific_concepts = []
    
    # Look for specific techniques or models mentioned
    techniques = ['transformer', 'cnn', 'rnn', 'lstm', 'bert', 'gpt', 'diffusion', 'gan', 'vae', 'attention']
    for tech in techniques:
        if tech in combined_text:
            specific_concepts.append(tech)
    
    # Look for application domains
    applications = ['autonomous driving', 'medical imaging', 'speech recognition', 'recommendation', 'translation']
    for app in applications:
        if app.replace(' ', '') in combined_text.replace(' ', ''):
            specific_concepts.append(app)
            
    return specific_concepts

def detect_title_focus(title):
    """
    Extract key insights from the title for visual focus
    """
    title_lower = title.lower()
    
    if any(word in title_lower for word in ['novel', 'new', 'improved', 'efficient', 'robust']):
        return " showcasing innovation and advancement"
    elif any(word in title_lower for word in ['multi', 'cross', 'joint', 'unified']):
        return " emphasizing integration and connectivity"
    elif any(word in title_lower for word in ['real-time', 'fast', 'rapid', 'efficient']):
        return " conveying speed and efficiency"
    
    return ""