---
layout: page
title: Automated Research Paper Summarization and Social Media Sharing: A Data Science Project
permalink: /about/
---

In today's fast-paced world of scientific research, staying up-to-date with the latest findings can be challenging. As a data scientist, I saw an opportunity to bridge this gap by creating an automated system that fetches the latest research papers, summarizes them, and shares the insights on social media. This project not only demonstrates the power of automation in disseminating scientific knowledge but also showcases the integration of various APIs and technologies.

## Project Overview

The goal of this project was to create a Python script that performs the following tasks:

1. Fetch the latest research paper from a specific category on arXiv.
2. Generate a concise blog post summarizing the paper's key findings.
3. Create a GitHub Pages blog post with the summary.
4. Share a brief highlight of the paper on Threads (a social media platform).

To accomplish these tasks, the script integrates several APIs and libraries, each serving a crucial role in the automation process.

## APIs and Libraries Used

### 1. arXiv API (via `arxiv` library)

The arXiv API is the starting point of our automation pipeline. We use it to fetch the most recent paper from a specified category (in this case, Artificial Intelligence). The `arxiv` library provides a convenient Python interface to interact with the arXiv API.

```python
import arxiv

def fetch_latest_paper(category):
    client = arxiv.Client()
    search = arxiv.Search(
        query = f"cat:{category}",
        max_results = 1,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )
    results = list(client.results(search))
    # ... (additional logic)
```

This function allows us to stay at the cutting edge of research by always fetching the most recent publication.

### 2. OpenAI API

The OpenAI API is the brain of our summarization process. We use GPT-3.5-turbo to generate both a detailed blog post and a concise social media post about the fetched paper. This demonstrates the power of AI in understanding and summarizing complex scientific content.

```python
import openai

def generate_blog_post(paper):
    # ... (prompt preparation)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes engaging blog posts about scientific papers."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    # ... (response processing)
```

### 3. GitHub API

We use the GitHub API to programmatically create and publish blog posts on a GitHub Pages site. This automates the process of maintaining a regularly updated blog showcasing the latest research findings.

```python
import requests
import base64

def create_github_blog_post(title, content, date):
    # ... (content preparation)
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/_posts/{file_name}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    # ... (API request and response handling)
```

### 4. Threads API

To share our findings on social media, we integrate with the Threads API. This allows us to automatically post updates about new research papers, potentially reaching a wider audience.

```python
def create_media_container(access_token, user_id, text):
    url = f"https://graph.threads.net/v1.0/{user_id}/threads"
    params = {
        "media_type": "TEXT",
        "text": text,
        "access_token": access_token
    }
    response = requests.post(url, params=params)
    # ... (response handling)
```

## Challenges and Solutions

One of the main challenges in this project was handling the various API responses and ensuring robust error handling. For instance, we implemented retry logic for the Threads API to handle potential server-side errors:

```python
def post_to_threads(text):
    try:
        container = create_media_container(THREADS_ACCESS_TOKEN, THREADS_USER_ID, text)
        if 'id' in container:
            time.sleep(30)  # Wait before publishing
            publish_result = publish_thread(THREADS_ACCESS_TOKEN, THREADS_USER_ID, container['id'])
            # ... (success handling)
    except Exception as e:
        print(f"Error posting to Threads: {e}")
    # ... (additional error handling)
```

Another challenge was creating clean, URL-friendly titles for our blog posts. We solved this using regular expressions to remove special characters and format the title appropriately:

```python
safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
safe_title = re.sub(r'\s+', '-', safe_title)
safe_title = safe_title[:50].rstrip('-')
```

## Conclusion

This project demonstrates the power of combining various APIs and AI technologies to create an automated system for disseminating scientific knowledge. It showcases skills in API integration, natural language processing, web scraping, and automation - all crucial components of a data scientist's toolkit.

By automating the process of summarizing and sharing research papers, we're not only saving time but also making scientific knowledge more accessible to a broader audience. This project serves as a testament to how data science can bridge the gap between complex academic research and public understanding.

The code for this project is available on my GitHub repository, and I welcome any feedback or contributions to further improve this automation pipeline.
Thanks.

---

You can find the full code for this project on my GitHub repository: [GitHub Repository](https://github.com/PorkPy/research_blogger/blob/main/code/research_blogger_example.ipynb)
