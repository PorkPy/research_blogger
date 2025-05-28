"""
Service for interacting with OpenAI API (GPT and DALL-E)
"""
import openai
from IPython.display import display, Image

from prompts import generate_blog_post_prompt, generate_image_prompt
from config import (
    BLOG_POST_MAX_TOKENS, 
    BLOG_POST_TEMPERATURE,
    IMAGE_MODEL,
    IMAGE_SIZE,
    IMAGE_QUALITY,
    IMAGE_STYLE
)

# Initialize the OpenAI client
client = None

def init_openai(api_key):
    """Initialize the OpenAI client with the provided API key"""
    global client
    client = openai.OpenAI(api_key=api_key)

def generate_blog_post(paper, word_count):
    """
    Generate a blog post about the paper using GPT
    """
    prompt = generate_blog_post_prompt(paper, word_count)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes engaging blog posts about scientific papers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=BLOG_POST_MAX_TOKENS,
            temperature=BLOG_POST_TEMPERATURE
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return None

def generate_ai_image(paper):
    """
    Generate an AI image using DALL-E 3 based on the research paper
    """
    try:
        # Get the optimized prompt and debug info
        prompt, debug_info = generate_image_prompt(paper)
        
        print(f"Generating DALL-E 3 image for: {paper.title[:50]}...")
        print(f"🎨 Domain: {debug_info['domain']}")
        if debug_info['concepts']:
            print(f"🔍 Concepts: {', '.join(debug_info['concepts'])}")
        print(f"🎨 Color palette: {debug_info['color_palette']}")
        
        response = client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            n=1,
            size=IMAGE_SIZE
        )

        
        image_url = response.data[0].url
        print("✅ DALL-E 3 image generated successfully!")
        
        # Display the image in the notebook (if running in Jupyter)
        try:
            display(Image(url=image_url))
        except ImportError:
            print(f"Image URL: {image_url}")
        
        return image_url
        
    except Exception as e:
        print(f"❌ Error generating DALL-E 3 image: {e}")
        
        # Fallback: try with a simpler but still specific prompt
        try:
            print("Trying with simplified prompt...")
            simple_prompt = f"A clean, modern illustration of {debug_info['domain']}, minimalist style, blue and purple gradient, technical diagram aesthetic"
            
            response = client.images.generate(
                model=IMAGE_MODEL,
                prompt=simple_prompt,
                n=1,
                size=IMAGE_SIZE,
            )
            
            image_url = response.data[0].url
            print("✅ Fallback image generated successfully!")
            return image_url
            
        except Exception as e2:
            print(f"❌ Fallback also failed: {e2}")
            return None

def generate_threads_post(paper, blog_post_url, max_chars):
    """
    Generate a Threads post about the paper
    """
    from prompts import generate_threads_post_prompt
    
    prompt = generate_threads_post_prompt(paper, max_chars)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates engaging social media posts about scientific papers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=BLOG_POST_TEMPERATURE
        )
        return response.choices[0].message.content.strip().replace(":", "")
    except Exception as e:
        print(f"Error generating Threads post: {e}")
        return None