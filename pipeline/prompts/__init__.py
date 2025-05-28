# Import key functions to expose at the prompts package level
from .image_prompts import generate_image_prompt
from .blog_prompts import generate_blog_post_prompt
from .threads_prompts import generate_threads_post_prompt

# This allows you to do: from prompts import generate_image_prompt