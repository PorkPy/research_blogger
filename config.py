# config.py - Configuration file (safe to commit)

def load_secrets():
    """Load secrets from secrets_config.py file"""
    try:
        from secrets_config import (
            FACEBOOK_ID,
            INSTAGRAM_ACCESS_TOKEN, 
            THREADS_USER_ID,
            THREADS_ACCESS_TOKEN,
            APP_SECRET,
            OPENAI_API_KEY,
            GITHUB_TOKEN,
            GITHUB_REPO,
            GITHUB_PAGES_SITE
        )
        return {
            'FACEBOOK_ID': FACEBOOK_ID,
            'INSTAGRAM_ACCESS_TOKEN': INSTAGRAM_ACCESS_TOKEN,
            'THREADS_USER_ID': THREADS_USER_ID,
            'THREADS_ACCESS_TOKEN': THREADS_ACCESS_TOKEN,
            'APP_SECRET': APP_SECRET,
            'OPENAI_API_KEY': OPENAI_API_KEY,
            'GITHUB_TOKEN': GITHUB_TOKEN,
            'GITHUB_REPO': GITHUB_REPO,
            'GITHUB_PAGES_SITE': GITHUB_PAGES_SITE
        }
    except ImportError:
        print("❌ secrets_config.py not found!")
        print("Please create secrets_config.py with your API keys")
        return None

def get_config():
    """Get configuration with secrets loaded"""
    secrets = load_secrets()
    if not secrets:
        raise Exception("Failed to load secrets")
    return secrets