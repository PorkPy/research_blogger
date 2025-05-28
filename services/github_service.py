"""
Service for interacting with GitHub API
"""
import base64
import time
import hashlib
import requests
from datetime import datetime

def check_existing_post(short_id, date, github_token, github_repo):
    """Check if a blog post for this paper already exists on GitHub"""
    file_name = f"{date}-{short_id}.md"
    url = f"https://api.github.com/repos/{github_repo}/contents/_posts/{file_name}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def create_github_blog_post(paper, content, date, short_id, image_url, github_token, github_repo, github_pages_site):
    """
    Create a new blog post on GitHub with the generated content
    """
    # Use consistent short_id for the file name
    file_name = f"{date}-{short_id}.md"
    
    # Generate Harvard reference
    from services.arxiv_service import generate_harvard_reference
    harvard_reference = generate_harvard_reference(paper)
    
    # Fixed: No indentation in front matter
    file_content = f"""---
layout: post
title: "{paper.title}"
date: {date} {datetime.now().strftime('%H:%M:%S +0000')}
categories: [blog, AI, research]
image: {image_url}
---
![AI Generated Image]({image_url})

{content}

## Original Research Paper
For more details, please refer to the original research paper:
[{paper.title}]({paper.entry_id})

## Reference
{harvard_reference}
"""
    
    encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")
    url = f"https://api.github.com/repos/{github_repo}/contents/_posts/{file_name}"
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Check if file already exists
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Blog post already exists: {file_name}")
        return False, ""

    # File doesn't exist, create new file
    data = {
        "message": f"Add new blog post: {paper.title}",
        "content": encoded_content
    }

    response = requests.put(url, headers=headers, json=data)
    if response.status_code != 201:
        print(f"GitHub API Error: {response.status_code}")
        print(f"Response content: {response.text}")
        return False, ""
    
    # Construct the URL based on the file name
    post_url = f"https://{github_pages_site}/{date.replace('-', '/')}/{short_id}/"
    return True, post_url

def download_and_save_image(image_url, paper_short_id, date, github_token, github_repo, github_pages_site, github_pages_image_wait=60):
    """
    Download the AI image and save it to GitHub repository
    This prevents the image from expiring
    """
    try:
        # Download the image
        print("Downloading image...")
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        
        # Create filename
        image_filename = f"assets/images/{date}-{paper_short_id}.png"
        
        # Encode image for GitHub API
        encoded_image = base64.b64encode(img_response.content).decode("utf-8")
        
        # Upload to GitHub
        url = f"https://api.github.com/repos/{github_repo}/contents/{image_filename}"
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"  # Use the API version from docs
        }
        
        # Always try to create as new file first (no sha parameter)
        print(f"📤 Creating new file: {image_filename}")
        data = {
            "message": f"Add image for blog post {paper_short_id}",
            "content": encoded_image
        }
        
        response = requests.put(url, headers=headers, json=data)
        print(f"📥 Upload response: {response.status_code}")
        
        if response.status_code == 201:
            # Successfully created new file
            github_image_url = f"https://{github_pages_site}/{image_filename}"
            print(f"✅ Image saved to GitHub: {github_image_url}")
            
            # Wait for GitHub Pages to deploy the image
            print(f"⏳ Waiting for GitHub Pages to deploy image ({github_pages_image_wait} seconds)...")
            time.sleep(github_pages_image_wait)
            
            # Test if the image is accessible
            try:
                test_response = requests.head(github_image_url, timeout=10)
                if test_response.status_code == 200:
                    print("✅ GitHub Pages image is accessible!")
                    return github_image_url
                else:
                    print(f"⚠️ GitHub Pages image not ready (status: {test_response.status_code})")
                    print("📎 Using original OpenAI URL as fallback")
                    return image_url
            except Exception as e:
                print(f"⚠️ Cannot verify GitHub Pages image accessibility: {e}")
                print("📎 Using original OpenAI URL as fallback")
                return image_url
                
        elif response.status_code == 422:
            # File might already exist, try to update it
            print("🔄 File might exist, checking and updating...")
            
            # Get the existing file info
            check_response = requests.get(url, headers=headers)
            if check_response.status_code == 200:
                file_info = check_response.json()
                print(f"📄 File exists, updating with sha: {file_info['sha'][:8]}...")
                
                # Update with sha
                update_data = {
                    "message": f"Update image for blog post {paper_short_id}",
                    "content": encoded_image,
                    "sha": file_info["sha"]
                }
                
                update_response = requests.put(url, headers=headers, json=update_data)
                if update_response.status_code == 200:
                    github_image_url = f"https://{github_pages_site}/{image_filename}"
                    print(f"✅ Image updated on GitHub: {github_image_url}")
                    return github_image_url
                else:
                    print(f"❌ Failed to update: {update_response.status_code}")
                    print(f"Response: {update_response.text}")
                    return image_url
            else:
                print(f"❌ Cannot check file existence: {check_response.status_code}")
                print("📎 Using original OpenAI URL as fallback")
                return image_url
        else:
            print(f"❌ Failed to save image to GitHub: {response.status_code}")
            print(f"Response: {response.text}")
            print("📎 Using original OpenAI URL as fallback")
            return image_url
            
    except Exception as e:
        print(f"❌ Error saving image: {e}")
        print("📎 Using original OpenAI URL as fallback")
        return image_url