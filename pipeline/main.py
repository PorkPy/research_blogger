"""
Main entry point for Research Blogger application
"""
import hashlib
import time
from datetime import datetime
from IPython.display import display, Markdown, Image

# Import configuration
from config import (
    ARXIV_CATEGORIES,
    MAX_PAPERS_TO_PROCESS,
    DAYS_BACK_TO_SEARCH,
    BLOG_POST_LENGTH,
    SKIP_EXISTING_POSTS,
    SAVE_IMAGES_TO_GITHUB,
    LINK_PREVIEW_WAIT,
    GITHUB_PAGES_IMAGE_WAIT,
    THREADS_WAIT_TIME,
    THREADS_MAX_RETRIES,
    VERBOSE_OUTPUT,
    TEST_MODE
)

# Import secrets
from secrets_config import (
    OPENAI_API_KEY,
    THREADS_USER_ID,
    THREADS_ACCESS_TOKEN,
    GITHUB_TOKEN,
    GITHUB_REPO,
    GITHUB_PAGES_SITE
)

# Import services
from services.arxiv_service import fetch_latest_papers
from services.openai_service import init_openai, generate_blog_post, generate_ai_image, generate_threads_post
from services.github_service import check_existing_post, create_github_blog_post, download_and_save_image
from services.threads_service import post_to_threads

def main():
    try:
        # Initialize OpenAI client
        init_openai(OPENAI_API_KEY)
        
        # Auto-adjust settings based on test mode
        papers_to_process = 1 if TEST_MODE else MAX_PAPERS_TO_PROCESS
        
        if VERBOSE_OUTPUT:
            print("🚀 Starting automated blog creation process...")
            if TEST_MODE:
                print("🧪 TEST MODE ENABLED - Processing only 1 paper")
            print(f"📝 Configuration: {papers_to_process} papers, {DAYS_BACK_TO_SEARCH} days back")
            print(f"🔍 Categories: {', '.join(ARXIV_CATEGORIES)}")
        
        # Fetch papers
        papers = fetch_latest_papers(ARXIV_CATEGORIES, papers_to_process, DAYS_BACK_TO_SEARCH)
        if not papers:
            print(f"No recent papers found in categories: {ARXIV_CATEGORIES}")
            return

        processed_count = 0
        for paper in papers:
            display(Markdown(f"## Processing: {paper.title}"))
            
            # Generate a consistent ID for the paper
            short_id = hashlib.md5(paper.title.encode()).hexdigest()[:8]
            
            # Use today's date for the blog post
            date = datetime.now().strftime("%Y-%m-%d")
            
            # Skip if blog post already exists
            if SKIP_EXISTING_POSTS and check_existing_post(short_id, date, GITHUB_TOKEN, GITHUB_REPO):
                print(f"Blog post already exists for: {paper.title}")
                print("Skipping to next paper...")
                continue

            # Generate blog post content
            blog_post = generate_blog_post(paper, BLOG_POST_LENGTH)
            if not blog_post:
                print(f"Failed to generate blog post for: {paper.title}")
                print("Skipping to next paper...")
                continue

            # Display information
            display(Markdown(f"### Original Paper: [{paper.entry_id}]({paper.entry_id})"))
            display(Markdown(blog_post))
            
            # Generate a temporary post URL
            temp_post_url = f"https://{GITHUB_PAGES_SITE}/{date.replace('-', '/')}/{short_id}/"
            
            # Generate Threads post text
            threads_text = generate_threads_post(paper, temp_post_url, 350)
            if not threads_text:
                print("Failed to generate Threads post. Skipping to next paper...")
                continue
            
            # Generate image based on paper content
            image_url = generate_ai_image(paper)
            if not image_url:
                print("Failed to generate AI image. Skipping to next paper...")
                continue
            
            # Download and save the image to prevent expiration
            if SAVE_IMAGES_TO_GITHUB:
                image_url = download_and_save_image(
                    image_url, 
                    short_id, 
                    date, 
                    GITHUB_TOKEN, 
                    GITHUB_REPO, 
                    GITHUB_PAGES_SITE, 
                    GITHUB_PAGES_IMAGE_WAIT
                )
            
            # Create GitHub blog post with the generated image
            success, post_url = create_github_blog_post(
                paper, 
                blog_post, 
                date, 
                short_id, 
                image_url, 
                GITHUB_TOKEN, 
                GITHUB_REPO, 
                GITHUB_PAGES_SITE
            )
            
            if success:
                print(f"Successfully created blog post on GitHub: {post_url}")
                
                # Add delay to allow for link preview generation
                print(f"Waiting {LINK_PREVIEW_WAIT} seconds for link preview generation...")
                time.sleep(LINK_PREVIEW_WAIT)
                
                # Construct Threads post with hashtags and link
                full_threads_post = post_to_threads(
                    threads_text,
                    image_url,
                    THREADS_ACCESS_TOKEN,
                    THREADS_USER_ID,
                    post_url,
                    initial_wait=THREADS_WAIT_TIME,
                    max_retries=THREADS_MAX_RETRIES
                )
                
                if full_threads_post:
                    print("Successfully posted to Threads with image!")
                else:
                    print("Failed to post to Threads.")
                
                processed_count += 1
            else:
                print("Failed to create blog post on GitHub.")
        
        if VERBOSE_OUTPUT:
            print(f"\n✅ Processing complete! Created {processed_count} new blog posts.")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()