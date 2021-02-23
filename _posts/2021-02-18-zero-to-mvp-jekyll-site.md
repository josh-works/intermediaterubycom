---
layout: post
title: "Zero to Minimum-Viable-Jekyll-Website"
published: true
description: "A flexible-but-battle-tested field-guide to figuring out how to create a professional Jekyll website in minutes."
permalink: /zero-to-mvp-jekyll-website
image: ""
series_part: ""
---

## How Done Is This Post?

_Anything I write ranges from "super rough notes-as-i-go, don't even expect full sentences" to "this post is done and proven to deliver what it promises to deliver"_

1. Scratch-pad, take-notes-as-I-go **<-- we are here**
1. Review post, clean up for first 'share'
1. I `mkdir` new directory, follow my own steps, clarify
1. Integrate feedback/answer questions from others
1. Final cleanup, post is considered `done` unless someone reaches out with further questions

------------------

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

![github pages](/images/2021-02-18 at 8.10 PM.jpg)

siiiight I'm stuck. It's 8:15, I have to call it for a night.

Provenance of the above `2760c20edcbdf8f5bf9538ef5461489ed7b8e80a`. 

_note: 10:15p, i'm carrying onward a bit! My parents are in town, had a nice time hanging out, everyone's in bed, so I wanna push this onward a bit._

## Step 6.01 Site not reachable

My site seems to be trying to get published here: [https://josh.works/aftd/](https://josh.works/aftd/)

It also 404s, and I get a page build error. In my inbox, specifically, I get more info:

> The page build failed for the `main` branch with the following error:
> 
> No `/docs` folder was found to build GitHub Pages. Check the source setting for this repository. For more information, see [https://docs.github.com/github/working-with-github-pages/troubleshooting-jekyll-build-errors-for-github-pages-sites#missing-docs-folder](https://docs.github.com/github/working-with-github-pages/troubleshooting-jekyll-build-errors-for-github-pages-sites#missing-docs-folder).
> 
> For information on troubleshooting Jekyll see:
> 
>   [https://docs.github.com/articles/troubleshooting-jekyll-builds](https://docs.github.com/articles/troubleshooting-jekyll-builds)

Bleh. It's _possible_ that if I didn't already have a site published on Github pages (`josh.works` is "published" on `josh-works.github.io`. If you visit `josh-works.github.io` you'll get a `301 Moved Permanently` redirect to `http://josh.works`)[^http]

[^http]: I wonder if that should redirect to `https://josh.works'`. Here's how I can see:

  `$ curl -v josh-works.github.io`
  
Fortunately, this site (`intermediateruby.com` is hosted on Github pages with a custom domain, so let me go check the settings for this very own page. [git repo for intermediateruby](https://github.com/josh-works/intermediaterubycom/))

![gh page settings](/images/intermediate-ruby-gh-page-settings.jpg)

So I wonder if it's as simple as putting in a custom domain?

Nooope, that doesn't seem right. I finally figured it out. I think I have the branch name wrong. Let me try publishing everything off of a `gh-pages` branch.

Gosh, I think that's it. I remember trying to rename the `master` branch of my personal site to `main`, couldn't, etc. I didn't think I'd remember `gh-pages`, so I just left it as master.

When I `jekyll new`'ed, and grabbed the screenshot of my terminal, I was like 

> ew, I don't want to put a screenshot out there foreveryone to see with my git branch named `master`. That's dumb. 

So I did `gb -b main`, `gpo`, and expected the right branch to be up there. I remember the github support team emailing me back saying "eh, we don't support a branch named `main` yet".

Anyway, lets fix our branch situation:

![fix branch](/images/terminal-gh-pages.jpg)

```shell
git branch -mv gh-pages
gpo gh-pages
gpo :main # I was hoping this gonna delete the `main` branch on gh, but didn't work. ¯\_(ツ)_/¯ 
```

Update settings:

![use correct branch](/images/gh-page-branch.jpg)

## Step 6.02 Still Broken, nothing at `https://josh.works/aftd/`

Still broken - supposedly site is published at [https://josh.works/aftd/](https://josh.works/aftd/), but it just loads an empty page.

When I `curl https://josh.works/aftd/`, nothing comes back. Try it yourself, in your terminal. If you get _anything_ back, besides a single new line, I've fixed this.

![lol nothing came back with curl](/images/2021-02-18 at 10.38 PM.jpg)



## Step 6.03 try adding custom domain (our end goal anyway)

Lets try adding a custom domain instead. So, back to your settings. I punch in `afailuretodisagree.com`, because I own the domain, and...

I'm suspicious:

![no way this worked](/images/too-easy.jpg)

there's no way this worked. I don't belive Github. There's nothing stopping me from entering `stonks.com` (which I don't own, but check it out, it's awesome: [https://stonks.com/](https://stonks.com/))

![stonks.com](/images/2021-02-18 at 10.43 PM-stonks.jpg)

## Step 7: Set up Google Domains

off to [domains.google.com/registrar](https://domains.google.com/registrar/):

![i own these](/images/2021-02-18 at 10.44 PM-domain-01.jpg)

If you don't have a domain here you want/can use, buy another one. Smash the `get a new domain` button, or visit [https://www.domainhole.com/generator/](https://www.domainhole.com/generator/) for inspiration and ideas on cheap domains. 

Find an available domain _anywhere_, and buy it in your Google Domains account. If you don't have a google domains account, create one, add a credit card, etc. 

Ooooh gosh, custom nameservers. That's Cloudflare. I just looked to see how I have `intermediateruby.com` configured in `domains.google.com`, and it's got custom nameservers pointing to Cloudflare.

Cloudflare... runs the internet, IMO. Not quite the same as AWS, but Cloudflare is _everywhere_. They sit "between" AWS and people's devices, same as how Amazon's warehouses sit close to the end-user[^in-the-us].

[^in-the-us]: Amazon Prime is entirely dependent on pre-placing items close to the customer. I don't actually like this service, as it's horrific for the environment and economy. (super wasteful, hidden costs because... _waves hands in air_ everything, and they're opening up a distribution facility near my house. Amazon cannabolizes local economy with externalized costs. I don't blame them for it, but I don't like it.)

## Step 7.01 Set up cloudflare

Gosh this is getting complicated. I'm way over my target time of "having a new website set up from scratch in 10 minutes". I'm about two hours into this, though, admittedly, I'm writing this blog post as I work through the process.

I last went through this process over a year ago (with `intermediateruby.com`) and I remember it being surprisingly difficult. So, I'm not surprised that when I say "go figure this out" to people that _have run zero websites, instead of the 5+ I've dealt with over the years_ they feel sandbagged.

Onward...

Set up an account at [https://www.cloudflare.com/](https://www.cloudflare.com/). It's free.[^1-password] 

[^1-password]: Please use 2fa and a strong password. I use [1password](https://1password.com/) religiously. (really, it's religious). My wife uses it, my mother-in-law, my whole family, it's such a powerful tool for managing passwords. 

  As a software developer, I have to manage dozens-to-hundreds of logins to various systems. I just checked my account. I've got almost 900 _items_ in 1password. Many of those are logins. If creating a strong, random password on a new site isn't painless to you, _it needs to be_. Use 1Password. I don't make money from you being their customer.

I have a free Cloudflare plan, so you should be able to have one too. 

Log into your account, on the `home` page, click `Add a Site`:

![add a site](/images/2021-02-18 at 11.02 PM-cloudflare.jpg)

## Step 7:02 Cloudflare: Select the free plan (I often see upsells here. Hunt around for the free plan button.)

## Step 7.03 Cloudflare: CNAME? MX records? huh?

You'll see something like this:

![what the heck does this mean?](images/2021-02-18 at 11.06 PM.jpg)

> Review your DNS records
> 
> 1 CNAME
> Verify that DNS records below are configured correctly. These records take effect in Cloudflare after you update your nameservers.

What does that mean?

Time to check what I've got configured for `intermediateruby`:

![wow a lot](/images/2021-02-18 at 11.09 PM-cloudflare-dns.jpg)

Sigh - this still isn't what I need.

## Step 7.04 add a file to your repo (`CNAME`)

I googled around, found [Using Github Pages with Google Domains and Cloudflare](https://www.randydeng.com/website/2019/07/08/using-github-pages-with-google-domains-and-cloudflare.html). They said:

> Github Pages Configuration

> To configure Github Pages, add a file called CNAME to the root directory of your Github repository. Inside this file, you’ll put your domain name (e.g. www.randydeng.com). This tells Github where your domain is located.

Oh right! 

```
Echo "www.aftd.com" >> CNAME
git add . && git commit -m "Adds CNAME" && git push
```

When you `git push` you'll probably run into some conflicts; when you added the custom domain setting in Step 6, git added a `CNAME` file to the repo. I didn't know that, so I was getting merge conflicts when trying to push this branch, unexpectedly. 

I didn't want to force push without knowing what I was overwriting.

Here's what I did:

![scoping problems](/images/2021-02-18 at 11.19 PM-git-conflict.jpg)

Anyway, now the repo has a `CNAME` file in it, the content of which is `www.afailuretodisagree.com`, overwrote an earlier commit: [0e901771d27ae3ec454ffc05bb83b278be738ec9](https://github.com/josh-works/aftd/commit/0e901771d27ae3ec454ffc05bb83b278be738ec9)

When I visit [https://www.afailuretodisagree.com/](https://www.afailuretodisagree.com/), I get nothing.

Wow. Now 11:28, another hour has passed, and I don't have a website online. I'm glad I'm writing this out, as I'm way farther into this than I would have expected. Check out this commit here: [02951b582dece6d59024dbca7000bdbea5bc58e2](https://github.com/josh-works/intermediaterubycom/commit/02951b582dece6d59024dbca7000bdbea5bc58e2)

JK doing a little more

## Step 7.05 Get Cloudflare nameservers, add to google domains account

OK, so you don't have to guess on the cloudflare nameservers - they'll probably be the same for you as they are for me, I've been using these for years. They are:

```
elaine.ns.cloudflare.com
elliot.ns.cloudflare.com
```

![cloudflare nameservers](/images/2021-02-18 at 11.33 PM-dns.jpg)

And here's how you add them:

![cloudapp](/images/dns.gif)

OK, NOW you can take a break. Cloudflare and Google both say that it can take two days for these changes to fully propogate throughout.

As of 2021-02-18 11:40p, [https://www.afailuretodisagree.com/](https://www.afailuretodisagree.com/) doesn't go anywhere.

but what about:

```
https://www.afailuretodisagree.com/
http://www.afailuretodisagree.com/
www.afailuretodisagree.com/
afailuretodisagree.com
```

Nothing. Two hours in, and I think I'm making a smidgen of progress. I'm remembering now why it felt so complicated to me last time around. It _was_ complicated, I remember googling a lot about various record types, how they worked, etc.

I'm figuring it out, slowly. I might be able to appreciate bits of my copy of [High Performance Browser Networking](https://www.amazon.com/High-Performance-Browser-Networking-performance/dp/1449344763) now.

Sigh. Do I need CNAME records? A? AAA? I don't even know what it all means.

Found something useful in Github docs: [https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

## Step ???: IT WORKS

![it works](/images/2021-02-19 at 9.12 AM-its-live.jpg)

Yay! I can _finally_ visit: [https://afailuretodisagree.com/](https://afailuretodisagree.com/) and it loads my Jekyll site.

Wow. That was difficult, confusing, full of uncertainty, and I'm not actually sure what made the difference. 

I'll do this whole thing a second time on another site at some point. 

This is one more hour in (not quite a full hour, maybe 40 minutes + some email).

## Step 9: Change Theme, see updates on your website

OK, lets try changing the theme again, now that we know the changes will propogate to `afailuretodisagree.com`.

OK. I changed to the `minimal-mistakes-jekyll` theme with two configuration changes, now it looks like:

![minimal-mistakes](/images/2021-02-19 at 11.50 PM.jpg)

### Notes

- [Why a domain’s root can’t be a CNAME — and other tidbits about the DNS](https://www.freecodecamp.org/news/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c/)
- [Managing a custom domain for your GitHub Pages site](https://docs.github.com/en/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site)
- [Using Github Pages with Google Domains and Cloudflare (randydeng.com)](https://www.randydeng.com/website/2019/07/08/using-github-pages-with-google-domains-and-cloudflare.html)