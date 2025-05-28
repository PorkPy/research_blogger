"""
Threads post prompt generation for research papers
"""

def generate_threads_post_prompt(paper, max_chars=300):
    """
    Generate a prompt for creating a Threads post about the paper
    """
    # Extract publication date
    pub_date = paper.published.strftime("%B %Y") if hasattr(paper, 'published') else ""
    
    # Extract author affiliations if available
    affiliations = ""
    if hasattr(paper, 'authors') and paper.authors:
        # Try to extract affiliations from author information
        # This depends on how the arXiv API provides this data
        # You might need to adjust this based on your specific data structure
        affiliations_list = []
        for author in paper.authors[:2]:  # Just use first two authors
            if hasattr(author, 'affiliation') and author.affiliation:
                affiliations_list.append(author.affiliation)
        
        if affiliations_list:
            # Remove duplicates
            affiliations_list = list(set(affiliations_list))
            affiliations = f" from {', '.join(affiliations_list[:2])}"  # Limit to first two
    
    prompt = f"""Create an engaging social media post for Threads (max {max_chars} characters) about this scientific paper:
    Title: {paper.title}
    Published: {pub_date}
    Abstract: {paper.summary}
    
    The post should:
    1. Start with the paper title in quotes
    2. Include one relevant emoji at the beginning that matches the paper's topic
    3. If publication date is recent (within last 3 months), mention it's a recent publication
    4. If known, mention one or two prestigious institutions{affiliations}
    5. Highlight ONE key finding or innovation in accessible language
    6. Briefly mention a potential real-world impact
    7. End with a thought-provoking question OR call to action
    8. Use conversational, engaging language suitable for a general audience
    9. Do not include any hashtags or "Read more" statements
    
    Keep the entire post under {max_chars} characters, as we'll add hashtags and a link separately.
    """
    
    return prompt