"""
DALL-E prompt generation for research papers
"""

# Domain-specific imagery dictionary
DOMAIN_IMAGERY = {
    "computer vision": [
        "a computer vision system analyzing images with detection boxes and segmentation masks",
        "a facial recognition system with feature points and matching confidence scores",
        "an object detection system identifying multiple objects in a complex scene",
        "a medical imaging AI analyzing scans with highlighted regions of interest"
    ],
    
    "natural language processing": [
        "an NLP system analyzing text with highlighted keywords and semantic connections",
        "a language translation interface showing text conversion between languages",
        "a chatbot or virtual assistant interface with response generation visualization",
        "a document analysis system extracting key information from multiple sources"
    ],
    
    "machine learning": [
        "a neural network with visible layers, nodes, and data flowing through connections",
        "a machine learning training process showing loss curves and model improvement",
        "a decision tree or random forest model with decision paths highlighted",
        "a clustering algorithm grouping similar data points in a multidimensional space"
    ],
    
    "robotics": [
        "a robotic arm or system with sensor inputs and decision pathways visible",
        "an autonomous robot navigating through a complex environment",
        "a robotic manipulation system interacting with physical objects",
        "a swarm of robots collaborating on a complex task"
    ],
    
    "healthcare AI": [
        "a doctor using an AI diagnostic tool to analyze patient data",
        "an AI system analyzing medical scans with diagnostic overlays",
        "a healthcare dashboard showing patient monitoring with AI predictive insights",
        "a medical research lab using AI to analyze biological data"
    ],
    
    "data science": [
        "an interactive dashboard showing complex data visualizations and insights",
        "a predictive analytics system identifying trends in business data",
        "a recommendation engine suggesting personalized content to users",
        "a fraud detection system identifying suspicious patterns in transactions"
    ],
    
    "reinforcement learning": [
        "an AI agent navigating a complex environment with reward signals visible",
        "a game-playing AI showing decision trees and strategic planning",
        "a reinforcement learning system training through multiple scenarios",
        "an autonomous system learning from trial and error with performance metrics"
    ],
    
    "quantum computing": [
        "a quantum computing system with qubits in various states",
        "quantum circuits with gates and operations visualized",
        "quantum entanglement represented through connected particle states",
        "a hybrid classical-quantum computing system solving complex problems"
    ],
    
    "generative AI": [
        "a generative AI creating new images with visible creation process",
        "a text-to-image system generating visual content from descriptions",
        "a style transfer system transforming content between different styles",
        "a music or audio generation system creating sound patterns"
    ]
}

# Human elements to include in images
HUMAN_ELEMENTS = [
    "researchers analyzing results on multiple screens",
    "scientists working with advanced AI interfaces",
    "a person interacting with AI through an intuitive interface",
    "researchers examining visualized data patterns",
    "engineers collaborating on a complex AI system",
    "a diverse team discussing AI results in a modern lab setting",
    "a user benefiting from AI assistance in everyday tasks"
]

# Advanced technical elements for specific techniques
ADVANCED_ELEMENTS = {
    "transformer": "attention mechanism visualization with self-attention patterns between tokens",
    "diffusion": "step-by-step denoising process showing image generation from noise to clear result",
    "reinforcement": "agent exploration patterns and reward optimization process",
    "cnn": "convolutional filters extracting features from input data",
    "lstm": "memory cells preserving information over sequential data",
    "gan": "generator and discriminator networks competing to produce realistic outputs",
    "attention": "attention weights highlighting important parts of the input",
    "embeddings": "vector space representations clustering similar concepts",
    "multimodal": "different data types (text, image, audio) being processed together",
    "graph neural": "information propagation through node connections in a graph",
    "optimization": "gradient descent or other optimization trajectories in a loss landscape",
    "bayesian": "probabilistic inference with uncertainty estimates",
    "federated": "distributed devices collaboratively training while maintaining privacy"
}

def identify_domain(text):
    """
    Identify the research domain based on keywords in the text
    """
    text = text.lower()
    
    # Check for computer vision keywords
    if any(word in text for word in ['image', 'vision', 'visual', 'detection', 'segmentation', 
                                    'object', 'face', 'recognition', 'camera']):
        return "computer vision"
    
    # Check for NLP keywords
    elif any(word in text for word in ['language', 'text', 'nlp', 'translation', 'sentiment', 
                                      'dialogue', 'conversation', 'llm', 'chat', 'word']):
        return "natural language processing"
    
    # Check for robotics keywords
    elif any(word in text for word in ['robot', 'autonomous', 'control', 'manipulation', 
                                      'navigation', 'motion', 'actuator', 'drone']):
        return "robotics"
    
    # Check for healthcare keywords
    elif any(word in text for word in ['medical', 'health', 'diagnosis', 'patient', 
                                      'clinical', 'drug', 'disease', 'hospital']):
        return "healthcare AI"
    
    # Check for data science keywords
    elif any(word in text for word in ['data', 'analytics', 'analysis', 'mining', 'clustering', 
                                      'classification', 'prediction', 'statistics', 'business']):
        return "data science"
    
    # Check for reinforcement learning keywords
    elif any(word in text for word in ['reinforcement', 'reward', 'policy', 'agent', 
                                      'environment', 'game', 'mpc', 'mdp']):
        return "reinforcement learning"
    
    # Check for quantum computing keywords
    elif any(word in text for word in ['quantum', 'qubit', 'entanglement', 'superposition']):
        return "quantum computing"
    
    # Check for generative AI keywords
    elif any(word in text for word in ['generative', 'gan', 'diffusion', 'synthesis', 
                                      'generate', 'creation', 'synthetic', 'style']):
        return "generative AI"
    
    # Default to machine learning
    else:
        return "machine learning"

def extract_techniques(text):
    """
    Extract specific techniques mentioned in the text
    """
    text = text.lower()
    techniques = []
    
    # List of techniques to look for
    technique_keywords = {
        "transformer": ["transformer", "attention", "bert", "gpt"],
        "diffusion": ["diffusion", "latent diffusion", "stable diffusion"],
        "reinforcement": ["reinforcement", "rl", "q-learning", "policy gradient"],
        "cnn": ["cnn", "convolutional", "convolution"],
        "lstm": ["lstm", "rnn", "recurrent", "gru"],
        "gan": ["gan", "generative adversarial"],
        "attention": ["attention mechanism", "self-attention"],
        "embeddings": ["embedding", "word vector", "vector representation"],
        "multimodal": ["multimodal", "multi-modal", "cross-modal"],
        "graph neural": ["graph neural", "gnn", "graph convolution"],
        "optimization": ["optimization", "gradient descent", "adam"],
        "bayesian": ["bayesian", "probabilistic", "uncertainty"],
        "federated": ["federated", "distributed learning"]
    }
    
    for technique, keywords in technique_keywords.items():
        if any(keyword in text for keyword in keywords):
            techniques.append(technique)
    
    return techniques

def extract_applications(text):
    """
    Extract application domains mentioned in the text
    """
    text = text.lower()
    applications = []
    
    # List of applications to look for
    application_areas = {
        "autonomous driving": ["autonomous driving", "self-driving", "vehicle"],
        "medical imaging": ["medical imaging", "radiology", "x-ray", "mri", "ct scan"],
        "speech recognition": ["speech recognition", "voice", "audio", "spoken"],
        "recommendation systems": ["recommendation", "recommender", "personalization"],
        "machine translation": ["translation", "translator", "multilingual"],
        "financial forecasting": ["financial", "finance", "stock", "market prediction"],
        "drug discovery": ["drug discovery", "pharmaceutical", "molecule"],
        "gaming": ["game", "gaming", "play", "player"],
        "security": ["security", "surveillance", "monitoring", "threat detection"],
        "environmental": ["climate", "environmental", "weather", "sustainability"]
    }
    
    for application, keywords in application_areas.items():
        if any(keyword in text for keyword in keywords):
            applications.append(application)
    
    return applications

def is_theoretical_paper(text):
    """
    Determine if the paper is theoretical rather than applied
    """
    theoretical_terms = [
        "theory", "theoretical", "framework", "formulation", "mathematical",
        "proof", "theorem", "lemma", "algorithm", "complexity", "convergence"
    ]
    
    # Count theoretical terms
    theoretical_count = sum(1 for term in theoretical_terms if term in text.lower())
    
    # If there are several theoretical terms, it's likely a theoretical paper
    return theoretical_count >= 3

def generate_image_prompt(paper):
    """
    Generate a DALL-E prompt based on paper content
    """
    title = paper.title
    abstract = paper.summary
    combined_text = f"{title.lower()} {abstract.lower()}"
    
    # Identify domain and techniques
    domain = identify_domain(combined_text)
    techniques = extract_techniques(combined_text)
    applications = extract_applications(combined_text)
    is_theoretical = is_theoretical_paper(combined_text)
    
    # Select specific subject based on domain
    import random
    specific_subject = random.choice(DOMAIN_IMAGERY.get(domain, DOMAIN_IMAGERY["machine learning"]))
    
    # Add technique-specific visual elements
    technique_elements = ""
    if techniques:
        selected_technique = techniques[0]  # Use the first identified technique
        if selected_technique in ADVANCED_ELEMENTS:
            technique_elements = f" Include {ADVANCED_ELEMENTS[selected_technique]}."
    
    # Add application-specific context
    application_context = ""
    if applications:
        application_context = f" Show this technology being applied to {applications[0]}."
    
    # Decide if human elements should be included (less likely for theoretical papers)
    human_element = ""
    if not is_theoretical and random.random() < 0.7:  # 70% chance for applied papers
        human_element = f" Include {random.choice(HUMAN_ELEMENTS)}."
    
    # Create final prompt
    prompt = f"""
    Create a photorealistic, detailed visualization of {specific_subject}.
    
    The image should be high-resolution with professional lighting and composition.{technique_elements}{application_context}{human_element}
    
    Make it suitable for a scientific publication or technology news article about {domain} research.
    Ensure it's technically accurate and clearly represents advanced research in this field.
    The visualization should have the quality of a professional stock photo or scientific illustration.
    """
    
    # Debug info to return
    debug_info = {
        "domain": domain,
        "techniques": techniques[:2] if techniques else [],
        "applications": applications[:1] if applications else [],
        "is_theoretical": is_theoretical
    }
    
    return prompt, debug_info