---
   layout: default
   title: Blog
   ---

   # Blog Posts

   {% raw %}
   {% for post in site.posts %}
     <article>
       <h2><a href="{{ post.url | absolute_url }}">{{ post.title }}</a></h2>
       <time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time>
       {{ post.excerpt }}
     </article>
   {% endfor %}
   {% endraw %}
