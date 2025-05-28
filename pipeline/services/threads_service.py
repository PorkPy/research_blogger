"""
Service for interacting with Threads API
"""
import time
import requests
from config import THREADS_HASHTAGS

def create_media_container(access_token, user_id, text, image_url):
    """Create a media container for the Threads post"""
    url = f"https://graph.threads.net/v1.0/{user_id}/threads"
    
    params = {
        "media_type": "IMAGE",
        "image_url": image_url,
        "text": text,
        "access_token": access_token
    }
    
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        print(f"Create Media Container Status Code: {response.status_code}")
        return response.json()
    except requests.RequestException as e:
        print(f"Error creating media container: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return None

def publish_thread(access_token, user_id, creation_id):
    """Publish the thread after creating the media container"""
    url = f"https://graph.threads.net/v1.0/{user_id}/threads_publish"
    
    params = {
        "creation_id": creation_id,
        "access_token": access_token
    }
    
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        print(f"Publish Thread Status Code: {response.status_code}")
        return response.json()
    except requests.RequestException as e:
        print(f"Error publishing thread: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response content: {e.response.text}")
        return None

def format_threads_post(text, blog_post_url, paper_category=None):
    """
    Format the Threads post with the appropriate hashtags and link
    """
    # Base hashtag that will be clickable (only use one primary hashtag)
    primary_hashtag = "#AI"
    
    # Additional non-clickable hashtags based on category
    secondary_hashtags = "#ArtificialIntelligence #Research #Science"
    
    # Add a domain-specific hashtag if category is provided
    if paper_category:
        category_hashtags = {
            "cs.AI": "#MachineLearning",
            "cs.LG": "#DeepLearning",
            "cs.CL": "#NLP",
            "cs.CV": "#ComputerVision",
            "stat.ML": "#MachineLearning"
            # Add more categories as needed
        }
        domain_tag = category_hashtags.get(paper_category, "#TechResearch")
        hashtags = f"{primary_hashtag} {domain_tag} {secondary_hashtags}"
    else:
        hashtags = f"{primary_hashtag} {secondary_hashtags}"
    
    # Format the full post
    full_post = f"{text}\n\n{hashtags}\n\nRead more: {blog_post_url}"
    
    # Make sure it doesn't exceed Threads limit (500 chars)
    if len(full_post) > 500:
        # Prioritize keeping the title intact (typically in the first line)
        first_line_end = text.find('\n')
        if first_line_end > 0:
            title = text[:first_line_end].strip()
            remaining = text[first_line_end:].strip()
            
            # Calculate available space
            available_chars = 500 - len(hashtags) - len(blog_post_url) - len(title) - 20
            
            if available_chars > 30:
                truncated_text = remaining[:available_chars-3] + "..."
                full_post = f"{title}\n\n{truncated_text}\n\n{hashtags}\n\nRead more: {blog_post_url}"
            else:
                # Emergency truncation
                available_chars = 500 - len(hashtags) - len(blog_post_url) - 15
                truncated_text = text[:available_chars-3] + "..."
                full_post = f"{truncated_text}\n\n{hashtags}\n\nRead more: {blog_post_url}"
        else:
            # No line break found, just truncate
            available_chars = 500 - len(hashtags) - len(blog_post_url) - 15
            truncated_text = text[:available_chars-3] + "..."
            full_post = f"{truncated_text}\n\n{hashtags}\n\nRead more: {blog_post_url}"
    
    return full_post

def post_to_threads(text, image_url, access_token, user_id, blog_post_url, initial_wait=30, max_retries=3):
    """
    Post content to Threads with image
    """

    # Format the full post with hashtags and link
    full_post = format_threads_post(text, blog_post_url)
    
    for attempt in range(max_retries):
        try:
            # Step 1: Create media container
            container = create_media_container(access_token, user_id, full_post, image_url)
            if container is None or 'id' not in container:
                print("Failed to create media container.")
                return False

            container_id = container['id']
            print(f"Media container created with ID: {container_id}")

            # Wait before publishing
            print(f"Waiting {initial_wait} seconds before publishing...")
            time.sleep(initial_wait)

            # Step 2: Publish the thread
            publish_result = publish_thread(access_token, user_id, container_id)
            if publish_result is None or 'id' not in publish_result:
                print("Failed to publish thread.")
                return False

            print(f"Successfully posted to Threads with ID: {publish_result['id']}")
            return True

        except Exception as e:
            print(f"Error posting to Threads: {e}")
            
            if attempt < max_retries - 1:
                print(f"Retrying in {initial_wait} seconds...")
                time.sleep(initial_wait)
            else:
                print("Max retries reached. Failed to post to Threads.")
                return False

    return False