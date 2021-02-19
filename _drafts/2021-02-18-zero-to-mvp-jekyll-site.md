---
layout: post
title: "Zero to Minimum-Viable-Jekyll-Website"
published: true
description: "A flexible-but-battle-tested field-guide to figuring out how to create a professional Jekyll website in minutes."
permalink: /zero-to-mvp-jekyll-website
image: ""
series_part: ""
---

I was chatting with a turing Alumni recently, about blogging and setting up a personal website. 

I've told _so many Turing students_ that they should blog, at least via Medium, but sometime shortly thereafter, they should move to a personal website.[^i-can-explain-why]

[^i-can-explain-why]: I could write list of reasons for why I think this. It's not the most important thing in the world, but I consider it a broadly defensible statement.

Someone just said:

> Also working on my website as well and having a tough time grasping Jekyll so thats next on my to-do list. I not sure how to get the page layout like your while using markdown :thinking_face: or did you use HTML and CSS?

And I wrote back with:

![A promise](/images/2021-02-18 at 7.19 PM.jpg)

>I just bought a new domain recently - `afailuretodisagree.com`
I want to set it up as a bare jekyll site, via google domains, tied to github pages.
> I don't know what theme I'll use - something from https://jekyllthemes.io/.
> And I'll write down all the steps, including how to set up a bare version of something that looks like my site.
>I've been wanting to write this guide for a while. It'll >live on.... https://intermediateruby.com/

So, let me hook up `afailuretodisagree` with a jekyll template. 

I made this statement about ten minutes ago, lets see how long it takes.[^proof]

[^proof]: commiting the above: `3bf541cf4561981af76177e2a81d712cb8046465`. [Dropping hashes: an idiom used to demonstrate provenance of documents](https://www.kalzumeus.com/essays/dropping-hashes/)

## Step 1: mkdir new directory

I plan on doing something Interesting with this new website, so it lives in my `/me` directory. `aftd` stands for `A Failure To Disagree`:

```
$ mdir aftd
```

![mkdir](/images/2021-02-18 at 7.32 PM.jpg)



## Step 2: Pick theme from Jekyllthemes.io

Pick a theme. I'll be using a free theme from [https://jekyllthemes.io/](https://jekyllthemes.io/). They have many beautiful-looking themes. 

At least - they're beautiful to this _mostly_ back-end software developer. (That's why I'm using a theme. Couldn't roll-my-own.)

I'm choosing https://jekyllthemes.io/theme/almace-scaffolding:

Check out this live demo: [https://sparanoid.com/lab/amsf/](https://sparanoid.com/lab/amsf/)

I like it. So, next, hit the "get this on Github"

![get on github](/images/get-on-gh.jpg)

## 2.01 `git clone` the theme

Head to to [https://github.com/sparanoid/almace-scaffolding](https://github.com/sparanoid/almace-scaffolding)

And grab the `git clone` url, and paste it into your new empty directory:

```
git clone https://github.com/sparanoid/almace-scaffolding
cd almace-scaffolding
bundle install
bundle exec jekyll server
```


Gar, super stuck, making it easier...

Start here: [https://jekyllrb.com/docs/themes/](https://github.com/jekyll/minima)

We're installing [https://github.com/jekyll/minima][https://github.com/jekyll/minima]

# TAKE TWO

## Step 1: `jekyll new`

```
gem install jekyll
jekyll new aftd
cd aftd
```

## Step 2: `jekyll server`


run `jekyll server` in your terminal

Open your browser, visit [http://localhost:4000/]

Boom. You've got a website:

![localhost](/images/localhost.jpg)

Lets customize it a bit to _you_:

## Step 3: Update config file?

Open everything up in Atom:

```
atom .
```

Open up `_config.yml` in Atom, edit your name:

![edit config](/images/2021-02-18 at 8.00 PM.jpg)

## Step 4: Restart jekyll server

Now, critically, you must restart your jekyll server.

It usually can live-reload content changes, but it reads from the `_config` file only once, when starting, so you _must_ restart the server to catch updates to the `config` file.

Stop it with `ctrl-c` in your terminal, run it again with `jekyll server`. Check out the changes:

![changes](/images/2021-02-18 at 8.01 PM.jpg)

OK, lets call this good enough, push to github pages somewhere. 

## Step 5: git init, git push

```shell
git init
git add
hub create # creates new repo from cli, look up github cli utility or "github hub"
git push origin main # i have aliased to `gpo`
git branch reveal # ??? I don't know what it means. i have aliased to gbr, opens up repo in browser
```

Now I'm looking at [https://github.com/josh-works/aftd/tree/main](https://github.com/josh-works/aftd/tree/main)



## Step 6, configure github account

So, in [https://github.com/josh-works/aftd/tree/main](https://github.com/josh-works/aftd/tree/main), I navigate to settings, scroll down to "github pages"

[github pages](/images/2021-02-18 at 8.10 PM.jpg)

siiiight I'm stuck. It's 8:15, I have to call it for a night.

## Step 7: IT LIVES! Your site is live on the internet

## Step 8: Connect your custom domain

## Step 9: 

### Notes

