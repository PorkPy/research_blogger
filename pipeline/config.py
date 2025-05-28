"""
Configuration settings for the Research Blogger application
"""

# arXiv paper settings
ARXIV_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL", "cs.CV", "stat.ML"]
MAX_PAPERS_TO_PROCESS = 5       # Number of papers to fetch and potentially process
DAYS_BACK_TO_SEARCH = 7         # How many days back to search for new papers

# Content generation settings
BLOG_POST_LENGTH = "300-400"    # Target word count for blog posts
BLOG_POST_MAX_TOKENS = 500      # Max tokens for GPT response
BLOG_POST_TEMPERATURE = 0.7     # Creativity level (0.0-1.0)

# Threads post settings
THREADS_MAX_CHARS = 350         # Max characters for main Threads text
THREADS_HASHTAGS = "#AI #ArtificialIntelligence #MachineLearning #DataScience #Latest #Research #Arxiv #OpenAI"
THREADS_WAIT_TIME = 30          # Seconds to wait before publishing
THREADS_MAX_RETRIES = 3

# Image generation settings (DALL-E 3)
IMAGE_MODEL = "dall-e-3"        # "dall-e-2" or "dall-e-3"
IMAGE_QUALITY = "standard"      # "standard" or "hd" (hd costs more)
IMAGE_STYLE = "natural"         # "natural" or "vivid"
IMAGE_SIZE = "1024x1024"        # "1024x1024", "1792x1024", or "1024x1792"

# Processing settings
SKIP_EXISTING_POSTS = True      # Skip papers that already have blog posts
SAVE_IMAGES_TO_GITHUB = True    # Download and save images to prevent expiration
LINK_PREVIEW_WAIT = 30          # Seconds to wait for link preview generation
GITHUB_PAGES_IMAGE_WAIT = 60    # Seconds to wait for image deployment

# Testing/debugging settings
TEST_MODE = False               # Set to True to process only 1 paper for testing
VERBOSE_OUTPUT = True           # Show detailed processing information