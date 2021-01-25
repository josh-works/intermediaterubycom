---
layout: default
title: Articles
permalink: /articles
---

## All Articles

{% for post in site.posts %}
  * [ {{ post.title }} ]({{ post.url }}) <time class="archive-date">{{ post.date | date: '%b %Y' }}</time>
{% endfor %}
