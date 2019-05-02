[PostMortem] of the Attempt and Results of Solving a [Real World Problem] in 3 - 4 Months.

# INTRODUCTION
## Salutations
Greetings traveller. Have a seat. Let me tell you a story. A story of one traversing a path that’s slowly becoming common as of late. A tale of being a “Self Taught” Developer.

If you're one those whose at the very start of it all, afraid to take the leap, uncertain where to go, stick around. I won't promise you'll gain life changing lessons. But you might gain some breadcrumbs and insights to help you along your own journey.

Buckle up.

## Some Backstory
Back in 2018, circumstances led to be homebound (which is a story for another time.) It was a non-negotiable kinda thing. Now rather than be bummed out about how the situation played out, I decided to be proactive about it. 

Eventually I came to the conclusion; since I’m in a time-skip, might as well make the most of it and **3D2Y** the sh*t out of this opportunity. If you don't get the referrence, it's basically levelling up for an extended period of time. Anyways, I decided to [Acquire a Skill] that is [Portable], [Scalable], and can [Generate Income] regardless where I’m located. **Python** fit the bill.

Roughly 1 year in; bounced around tutorials, articles, documentations, simple projects, attending some conventions, and even participating in a hackathon (this was a fun experience). Suffice to say, I’m not a complete beginner anymore. 

*And thats the problem*.

You see I am now confident that I know enough of the Fundamentals of Python, to the point that I can teach it to someone else for a fee (true story). But it was not enough. Aside from following some good old tutorials, deliberate practice, reading documentation to really understand how a particular code fragment works, something was missing.

It felt like an invisible wall as blocking me. I needed to somehow **break through**, to go further beyond. But how? How do you see the unseen? Basically I’m between *"you don’t know what you don’t know”* and *“you know that you don’t know something.”*

## Illumination
Fortunately, rather than blindly wander in the dark, I was lucky enough to have met some awesome mentors that I frequently converse with. They helped in filling the gaps in my knowledge by pointing me in the rough direction of where I should be looking.

Through our numerous conversations and some research of my own, I came to a conclusion:
> I needed to build something from scratch.

No tutorials or guides. From conceptualization, to blocking it out, and eventually implementing.

Now don’t get me wrong, tutorials and the like are great (I think building a couple of blogs and CRUDS are a right of passage for any developer). But at some point, their returns diminish.

The thing about tutorials is, what your doing is implementing a pre-made solution. Sure it teaches you the syntax, some way to do things, and maybe the thought process behind the code. **But its an entirely different ball game to break down a problem yourself, and come up with your own solution.**

And when that happens, what do you do? Where do you go once “Tutorials” and the like no longer add value as much as they used to?

It took some thinking, then it hit me.
> **[Solve a Real World Problem]**

[Vivacity]:https://www.facebook.com/thevivacityshop

Fortunately, I know of someone who has a problem that needed solving; my wife and [her business][Vivacity].

---
# THE SCOPE
## About The Business
A quick summary; **@thevivacityshop** Sells Local and International Starbucks Merch here in the Philippines. If you’re into **Starbucks Korea Cherry Blossoms** and the like, [check it out][Vivacity]. 

With the quick plug out of the way, lets head back to what’s happening.

The business has been operating for a little more than a year now. It has experienced growth both in its customers, and in its sales, respectively. Pretty impressive for a side hustle done by the owner whilst she was in bed rest for pretty much the entirety of 2018 (Ask my wife, this is her story to tell).

The business is growing. **Thats good, and at the same time, concerning.**

## The Business Problem
> A Growing Customer Base and Sales

This may seem like an odd Business Problem. But you see, a key factor for a growing business is if its *positioned to handle* the said growth. To itemize the symptoms of the problem:

- The current inventory system was chugging.
- Difficult to have a birds eye view of overall inventory and sales.
- Too much time spent on encoding the influx and outflow of items and the sales.
- Task switching which leads to unnecessary amount of cognitive load.
- Fire fighting mode most of the time due to a lack of an optimized Business Process.
- Etc

The business was still doing the same thing, despite its growth. It has become time consuming, and very taxing for a single person operation. In dev terms, **complexity**!

Essentially, the business, as it was, wasn't positioned to **scale** effectively.

That's where I come in.

## The Proposed Solution
Now rather than try to tackle all the pain points the business was facing in one go, we decided to focus on the ones that when handled, will yield immediate improvement on the business; Inventory and Sales.

The proposed solution was to create an Inventory and Sales Dashboard that would:
- Simplify the process of recording an Item in Inventory, and an Item to be sold, thereby cutting the encoding time from 2 to 1
- Provide an Overview of the Items in the Inventory, and the Sales Performance of the business.
- Gain Time and Lessen the Cognitive Load, allowing her to focus *on the business*, rather than focus on *making sure the business runs*.

With that, I set off to Build a Business Dashboard using Django, Bootstrap, and Charts.js

---
# EXPECTATION
## Vs Reality
So with that, everything was set. I’m doing a real project. No guides, and what not. All on me. *What could possibly go wrong?*

> And thus, a glorious flag was raised.

Reality though, was easier said than done. What I hoped would be a 2 week job ended up becoming a **3 - 4 month Uphill Battle that really pushed me and my wife to the brink**. Well, not that intense, but it was certainly challenging.

The kicker? The final solution ended up being **Non-Dev Related** at all. But I'm getting ahead of myself.

## The First 3 Months
Going through the whole rounds of what happens could take longer, so will focus on the highlights instead:

> Process Mapping

The business had a loose process. Normally, a Dev Project would have the processs already [Mapped] out by the client. And the dev would simply extract the [Requirements] and [Implement] the [Code]. This was not the case.

> Business Development

Building up on the previous point, aside from *working **IN** the business*, an entrepreneur must also be able to *work **ON** the business*. But as mentioned, the core problem is that at the time, the client **does not** have the time to do so.

> Lack of Direction

This was inevitable. From the previous 2 points, how could I build something when I don't know what to build? And going deeper, how could I identify what to build when it became increasingly difficult to have a meeting to identify the requirements? Time was **THAT SCARCE**. How scarce? Well.

> 4 Hour Workday

*And that's when things are favorable.* More often than not, I had **way less**. Mostly due to my duties and responsibilities in the household and being a parent. No getting around that.

> Marathon

Since I only had so little time, I readjusted my tact. Rather than attempt to sprint through the whole course in one go, I had to break it down. Smaller than a Sprint. Smaller than a Micro Sprint. That's how scarse time was for me. I had to make sure that I was taking a step forward, even a tiny step.

> Context Saturation

Aside from tackling the problem, I also had to manage to learn something new every day. This was challenging, especially when you're juggling between carrying a baby + doing household stuff + etc. Requires some creativity.

> TL-DR

**Lack of time. Lack of Direction. Minimal Progress.**

## The Final Month
Without going into details, our situation turned around and we managed to regain our time. It was no longer *just 4 hours* a day. Time **for the both of us**.

With that, we finally managed to have a long overdue talk about the business; The pain points, the options, and the solution.

The Conclusion? **A Case of Over Engineering**

The Problem was Solved by working on Improving the **Actual Business Process** and Implementing a Simple Google Sheets Dashboard.

As for the Dashboard? I managed to build it over the entirety of this timeline. I capped it of as a *Working Demo*, even though the requirements for it has become outdated, and merely serves as a "Failed Project".

---
# TAKEAWAYS
I’ve managed to learn quite a bit this past 3 - 4 months. Ranging from the Dev side of things, to some productivity stuff, and all the way to some personal stuff.

Here’s a brief run down of the main ones.

## Dev Stuff
Gonna be a bit technical. If you're a none dev who happen to pass by, feel free to skip this part.

> Python

My strongest point at the moment. Mastery really begins once you are able to teach it to someone. Really glad I was given the opportunity to tutor someone last December.

> Django

I can still remember last year when I struggled at the installation part of django. Seems like eons ago now. Progress.


> Feature Driven

For the longest time, my approach to things was by “batch”. Example would be *today I’ll do all the template related stuff, then tomorrow I’ll do all the model related stuff*, without any regards to domain separation. Seems silly now that I think about it. But I learned that I should do it per feature.

> Git

 A continuation to me doing things per feature now. Specifically, I’m adopting the [Git Flow approach](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). I’m pretty sure I’m just at the tip of the iceberg on this one, but hey, I’m on the tip now. 

> Bootstrap

It’s a great feeling to be able to rapidly prototype a template as well as a functionality and letting the user interact with the system. Immediate and great feedback. Currently my weak point though. Need to practice on this one at a future project.

> Charts.js

t’s a watershed moment once you manage to work in another language. Although I say worked, but it’s really just managing to pass an array of values from the back to the front. But hey, baby steps.

> TDD

Still a concept at this point. Although I understand its importance and a paradigm shift in how to view it; its not a test. It’s like a mathematical proof. A guarantee that your code works. Additionally, it’s also a way of *formalizing what your business requirements is through code*. **Mind blown**


> Snippets / Bash Scripts

 Coding is mostly about patterns and repetition. Once you identify repeating patterns, in this context, repeating code / commands you type often, surely you could DRY it up and make snippets / bash scripts. Speed of thought. Improvements like this should be passive. Not a switch you flip every now and then.

## Stuff Outside the Code

> Document Better

Life is a journey. It would be nice to look back every now and then, to see how far you’ve come. And on a more practical sense, so it’d be easier to Post Mortem something because it’s documented, rather than what I’m doing now which is trying to recall what has transpired for the past 3 - 4 months.

> Clarity

How do you defeat clutter? Vigilance. Or in this case, Since I only have 4 hours a day to GTD, It’d be better to allocate my when I’m working on the [Most Important Work], not on Management / Tasking. Current Solution? A More Sensible Task List; Monkeyfying your Tasks. [Action] [Context] [Project]

> It starts with Paper

If you can’t explain what you’re trying to do in a few sentences, or even write it down in paper, then its probably too complicated / unclear what you’re trying to do. [Process Mapping], **the stuff before the code**, where code usually is the final step. The implementation.

> Battle Song

The term *“Thats my jam!”* really works. You know how in games, once the boss battle music kicks in, you know its on? The same holds true when you wanna GTD. Currently, I cycle between [Psychedelic Space Rock](https://www.youtube.com/watch?v=ors0wpcVDcc), [Synthwave](https://www.youtube.com/watch?v=vsyp-jaKAnA), and some Lo Fi Hip Hop. It varies depending on the mode I'm in.

> Context Saturation

There are many kinds of learning. For my purposes, I divided it into Active and Passive learning. Active is the part I get to apply through actual building and prototyping. Passive would be listening to podcasts, watching a youtube video about some context, and on on. Time is scarce. So even if its a bit, try to fit in some Context, some Learning material, even subconsciously. 

## Side Quests
So interestingly, aside from the Project itself, I was also able to do some Side Projects for the business. Namely:

> Scraping

An interesting side project I did for TVS was when I saw my wife needing to grab some large number of photos for her purposes and she was doing it manually. Enter Requests + Selenium. I felt like a wizard.

> Pandas + Google Sheets

Used a simple Pandas script for seperating some sales and inventory data. Clean up work. The functionality ffall() blew my mind.

## Personal Stuff

# CONCLUSION
In the end, what I initially thought was a 2 week job, ended up being a 3-4 month endeavor that ultimately pushed me to improve as a Developer, and then some.

The world isn’t as clean and controlled where a Problem is laid out for you. Sometimes, before you solve the Problem itself, you have to figure out what the real Problem is.

## Summary
Did I Solve the problem of the Business Owner? Mostly. It’s an ongoing thing.
Did I use code for the actual implementation? Not quite.
Did I learn a lot these past 3-4 months? A resounding yes.

## Punchline
Earlier I brought up that I there was something missing in my knowledge base. I think I got a glimpsed of that something:

That something? The ability to solve a problem.

**A [Problem Solving] Mindset.**

## What's Next?
