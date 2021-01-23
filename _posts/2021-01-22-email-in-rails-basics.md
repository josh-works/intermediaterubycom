---
layout: post
title:  "Guiding Principles"
published: false
description: ""
date:  2020-01-31 06:00:00 -0700
categories: []
tags: []
permalink: simple-email-in-rails-localhost-mailcatcher
image: /images/title_image.jpg
---

What I thought I would do when I sat down at my laptop 2 hours ago:

- Using google, blogs, and rails docs, figure out how to mail something in Rails that gets caught up in Mailcatcher, from `rails new` on Rails 6.x.x.
- Desired maximum level of sophistication: "i'm sending myself and anyone else who signs up emails from an app on Heroku that I deployed 10 minutes ago". Aka "hobbyist"
- I wanted a page, served on localhost, that had a button titled "send an email" and I'd see in mailcatcher something show up.
- Email runs the world. I want to learn to do cool things with it, and teach others to do cool stuff so they'll do things I never even thought of.
- I think I have a "budget" of ~2hr~ ~1hr~ ~30min~ ~5 min~ of _your_ time, to teach you something really interesting, in order to justify the time I'm going to end up requesting.

The top-ranked result for "email in rails" (according to Duck Duck Go) is:

[Sending Emails in Rails Applications LaunchSchool](https://launchschool.com/blog/handling-emails-in-rails) from 2014.

That's OVER SIX YEARS AGO!

I really wanted to grok the full basics of email in Rails apps - for a bunch of reasons.

I've spent a lot of time professionally dealing with email, but never from the technical "insider's technical perspective". 

I worked on a codebase for a few years that sent email (simulated phishing attacks) but I never actually really dug into the email sending. It was done in such a complicated, feature-rich way that I never could hold more than a tiny sliver of the emailing infrastructure in my head at a time.

ALSO the app was built in 2013. A long time ago.

So, I was looking to bring my rails knowledge up to speed, in the domain of email. (Is it _easy_ to add "email" to a Rails application? A day? A week?)

I sorta want an MVP email-sending infrastructure.

I want to start with emailing _myself_ stats about an application that I build, and from there, maybe, build an MVP "recurring customer email" at an application level. 

I have a bunch of long-term plans around this. 

_It's been surprisingly difficult_. I've already spent more than 4 hours on the topic, and I think I should have made _way more progress_ by this point than I should have.

I'm taking notes as I go, we'll see how far I get, and I'll be able to help someone else learn what I know in 1/5th the time it'll take me.





### Resources

- https://launchschool.com/blog/handling-emails-in-rails
- https://guides.rubyonrails.org/action_mailer_basics.html
