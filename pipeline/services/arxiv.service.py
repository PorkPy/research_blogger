"""
Service for interacting with the arXiv API
"""
import arxiv
from datetime import datetime, timedelta, timezone
from config import VERBOSE_OUTPUT

def fetch_latest_papers(categories, max_results, days_back):
    """
    Fetch the latest papers from arXiv based on categories and time range
    """
    client_arxiv = arxiv.Client()
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_back)
    
    category_query = " OR ".join([f"cat:{cat}" for cat in categories])
    
    search = arxiv.Search(
        query = f"({category_query})",
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    
    results = list(client_arxiv.results(search))
    recent_papers = [paper for paper in results if paper.published.replace(tzinfo=timezone.utc) > cutoff_date]
    
    if VERBOSE_OUTPUT:
        print(f"📊 Fetched {len(results)} papers, {len(recent_papers)} from last {days_back} days")
    
    return recent_papers

def generate_harvard_reference(paper):
    """
    Generate a Harvard-style reference for the paper
    """
    authors = paper.authors
    
    if len(authors) == 1:
        author_str = authors[0].name
    elif len(authors) == 2:
        author_str = f"{authors[0].name} and {authors[1].name}"
    else:
        author_str = f"{authors[0].name} et al."
    
    year = paper.published.year
    title = paper.title
    
    reference = f"{author_str} ({year}) '{title}', arXiv preprint arXiv:{paper.get_short_id()}."
    
    return reference