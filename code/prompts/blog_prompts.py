"""
Blog post prompt generation for research papers
"""

def generate_blog_post_prompt(paper, word_count="300-400"):
    """
    Generate a prompt for creating a blog post about the paper
    """
    authors = ', '.join([author.name for author in paper.authors])
    
    prompt = f"""Write an engaging blog post about the following scientific paper:

Title: {paper.title}
Authors: {authors}
Abstract: {paper.summary}

The blog post should:
1. Explain the main findings in simple terms
2. Discuss potential real-world implications
3. Be engaging and accessible to a general audience
4. Be around {word_count} words long

Blog Post:"""
    
    return prompt