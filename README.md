# 🧠 Automated arXiv Research Blog Generator

Description
This project is an automated content pipeline that monitors arXiv for new research papers and generates structured, visually enriched blog posts for technical content sharing. The system intelligently detects and tracks previously processed papers, ensuring that only fresh, relevant content is published.

# ✨ Key Features
🔍 Automated Paper Discovery
Integrates with the arXiv API to retrieve the latest research papers by category and time window.

🧠 Intelligent Duplicate Detection
Tracks previously processed papers using persistent storage to avoid redundancy.

🎨 AI-Generated Visual Content
Uses DALL·E 3 to generate technically relevant illustrations based on paper abstracts and domains.

🚀 Cross-Platform Content Distribution
Automatically publishes blog posts to GitHub Pages and shares them to Meta Threads.

⏰ Scheduled Execution via GitHub Actions
Runs daily or weekly with zero manual intervention.

🌐 Static Site Deployment
Posts are compiled and deployed to a GitHub Pages-powered site.

# 🛠 Technologies Used
Tech	Purpose
Python	Core scripting and API integration
arXiv API	Research paper discovery
DALL·E 3 / OpenAI API	AI-generated image creation
Meta Threads API	Social media automation and posting
GitHub Actions	Workflow automation and scheduling
GitHub Pages	Static site hosting for generated blogs
JSON	Local state tracking of processed papers
Git	Version control and CI/CD for publishing

# 📈 Impact
Developed a fully automated research-to-content pipeline that transforms dense academic papers into multi-format, engaging blog posts. This system reduces manual effort from hours to near zero while amplifying reach via visual storytelling and seamless cross-posting.

# 🧪 Sample Output
```bash
🚀 Starting automated blog creation process...
📝 Configuration: 5 papers, 7 days back
🔍 Categories: cs.AI, cs.LG, cs.CL, cs.CV, stat.ML
📊 Fetched 5 papers, 5 from last 7 days
...
Generating DALL-E 3 image for: How does Alignment Enhance LLMs' Multilingual Capa...
🎨 Domain: natural language processing
🔍 Concepts: machine translation
🎨 Color palette: warm oranges, soft whites, and typographic elements
✅ DALL-E 3 image generated successfully!

📤 Creating new file: assets/images/2025-05-28-95a4152d.png
📥 Upload response: 422
🔄 File might exist, checking and updating...
✅ Image updated on GitHub: https://porkpy.github.io/research_blogger/assets/images/2025-05-28-95a4152d.png

✅ Blog post created: https://porkpy.github.io/research_blogger/2025/05/28/95a4152d/

🧵 Posted to Threads:
Successfully posted to Threads with ID: 18145788115384311
Successfully posted to Threads with image!
```

# 🌐 Live Blog
➡️ View Latest Posts



