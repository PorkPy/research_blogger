"""
Threads post prompt generation for research papers
"""

def generate_threads_post_prompt(paper, max_chars=350):
    """
    Generate a prompt for creating a Threads post about the paper
    """
    prompt = f"""Create a short, engaging post for Threads (max {max_chars} characters) about this scientific paper:
    Title: {paper.title}
    
    Include a brief highlight of the research and its potential impact. 
    Do not include any hashtags or 'Read more' statements.
    """
    
    return prompt