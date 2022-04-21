---
title: "Developer Story"
draft: false
standalone: true
weight: 3
---

# Developer story

God rest the developer story.  We [welcomed](https://meta.stackoverflow.com/questions/313960/introducing-the-developer-story) you with as much enthusiasm as we [waved you goodbye](https://meta.stackoverflow.com/questions/415293/sunsetting-jobs-developer-story).  Got me a couple of my best jobs too.

Well, the lesson learnt is to never rely on anything you don't directly control.  I won't be making that mistake again, so here's roughly what I had in my developer story when it died, and more recent additions.

---

Details are correct at the time of writing - generally during the date range listed in the heading.  Work that I have done can cease to be available at any time, I generally can't control that.  Tenses have been changed over time to read more naturally.

---

## Profile

Professionally programming since 2012, (2016 with professional colleagues), after self-teaching from scratch.  I love the craft with a passion, and can easily lose track of time working on a problem if it catches my interest.

I'm driven by helping others, whether directly by teaching them, or indirectly by optimising some database query to make their work take 1% less time.

I like to think I possess excellent written and spoken English skills, and I know for a fact I'm a complete beginner at Japanese, though my Japanese friends always say I'm very good indeed.  One of them said I could easily be a translator, so I know they're blowing smoke, but I still appreciate it.

In my own time I play competitive video games at a non-competitive level, (except Atomic Chess I guess, where I rank around top 10%), practice piano way too little, and bake bread.  I also have a cat that hates me, which is pretty cool.

**Expert in**:  Python; Django.

**Professionally useful in**:  React; React Native; Redux; thunk; SQL (PostgreSQL, MySQL, SQLite, and more), Django REST Framework; Linux; systemd; wxPython.

**Hobby level interests**:  C++; make; Hugo; Go; Twisted.

**Dislikes**:  WordPress; PHP.

## Experience

### Mar 2019 - today, [Employer name withheld]({{< ref "about" >}}) - Full-stack developer

I work in a team of two people in an in-house tech department maintaining the giant piece of software that runs the business, which (in contrast to my previous roles at software agencies) does family law related forensic drug and alcohol testing.  I also work on odd side projects that crop up from time to time.

The main software I maintain and for which I author features on a daily basis (hereafter referred to as Eee) was initially written nearly a decade ago by someone who had no professional guidance, nor much experience, and probably not a great deal of budget.  As you might imagine, I have gained a great deal of experience with the ins and outs of maintaining legacy code working on this codebase.  As has been a theme, Eee is a Django-based rich web application, with a PostgreSQL backing store, and various pieces of JavaScript on the frontend.

Outside of Eee, I have created a mobile app for sample collection team to use when interviewing clients with regards to their drug usage, researched and suggested the issue ticketing system currently in use, and thoroughly instilled a PR-driven culture with regards to what makes it to `master`, having gone from nearly a hundred PRs when I joined, to over a thousand less than three years later.

### Jul 2018 - Mar 2019, [CommonCode](https://commoncode.io) - Full-stack developer

I worked in a team of variable size depending on the project, from as few as two people, to as many as "I don't know".  In the smaller teams, I often fell into somewhat of a mentorship role, as I had more experience with React than the team members who were assigned the tasks.

Similar to my time at my previous employer, I mainly used Python, Django, and React, backed by relational databases, usually PostgreSQL.  Dissimilar to my time at my previous employer, I attended and contributed to meetings with clients.

I worked remotely from England for the Australian company as a self-employed contractor until my hours dried up, and I was put on a PHP project too often.

### Mar 2016 - Mar 2018, JP74 - Junior developer

I worked in a team of four backend developers, one frontend developer, and three designers, creating and maintaining rich web applications,

Most of the time, the applications were written entirely in Django, with Celery managing long running tasks, and MySQL or PostgreSQL as the backing database, though occasionally we used Django REST Framework in addition to the aforementioned as an API for a React SPA.

I helped maintain the existing web applications, hunting down issues on behalf of clients, fixing them, and deploying them to production in the same day the client gave the go-ahead.

The deployments that I managed were to several different AWS setups.  Our main production server was a standalone EC2 instance in AWS, though we had a much more interesting CloudFormation-configured autoscaling high-availability cluster with blue-green deployments which I championed, hosting a global wordpress site for a multinational company.

We also did regular expeditions into unknown territory, to prepare for upcoming projects, or as a special request from a client.  We were asked to provide big data insights for a pharmaceutical company, for whom we were unable ptovide a satisfactory result, and - more happily - we were exploring React Native and GPS integration as a favour for a local nature conservation organisation.

I was made redundant from JP74 as it slowly died.  I have a story about that.  The domain has now been bought by a squatter, and read simply "fin" before that, so please excuse the lack of a link.

### Jun 2012 - Mar 2016, [John Hunt Photography](https://jhpschools.co.uk/) - Lab assistant

I worked in a team of two to three people, managing two professional digital photo labs (printers), editing photographs, and managing stock.

Towards the end of my stint, I also developed several Python programs, some to automate my own job, and some to run processes in the company.  This gave me the confidence to seek my way into the software engineering industry proper, so I left as I outgrew the company.

## Qualifications

* Computing, Economics, and Mathematics A levels
* Physics AS level

---

## Projects

Projects marked with an asterisk were personal projects entirely separate from my employer(s) at the time.  As you might imagine, the further back in time you read, the less impressive and relevant the projects might be, so feel free to stop whenever.  I won't judge.

Since starting at JP74 (Mar 2016), all of my non-personal work has been PR'd, and I have also had PRs to do as a regular part of working life.  It's not interesting so I don't mention it hereafter.

### Apr 2022, Eee maintenance

From the beginning of my employment at my current employer, general maintenance of Eee has been a constancy.  This has involved but isn't limited to: responding to and investigating user support tickets (which often require code changes); upgrading of Django and other libraries, changing the database schema and dealing with migrations; fixing and improving the test suite; linting the project; authoring developer conveniences; and refactoring out general insanity as and when possible.

### *May 2020, msim

In the search for which mortgage deal I should take, I found that I understood way less of the maths that goes into compound interest calculations and amortisation than I thought, so I wrote [msim](https://msim.righttobeoffensive.com) ([GitHub](https://github.com/Asday/msim)) in Django, to simulate a mortgage and certain overpayment schedules.

Initially it was rather simple, showing only a readout of the mortgage simulation and some CRUD functionality to modify the simulation, but has since gained some other features such as end date prediction, discrepancy recording (because my mortgage always differs from the simulation a bit month to month), messages detailing the real cost of overpaying less than planned, average overpayment readout, and so on.

It remains small and simple, but I do wish I architected the data shapes more sensibly.  Were I to do it again, comparisons, overpayment charges, and a better data model would be on the cards.

msim is hosted on a single Arch VM behind nginx, with a local PostgreSQL backing store, all managed by systemd.  In the future I plan to explore high availability with a cluster of servers, but for now the mortgage comes first.

### Oct 2019, Collector's App

Once Eee was up and running in my environment, my main task for the following six months or so was to create a mobile application for the sample collection team members to use while out on collections to quiz clients and record answers regarding their drug and alcohol use habits.  This was to replace the at-the-time current paper-based and rather freeform process.

I was essentially given carte blanche to do as I saw fit, owning the product from start to finish.  I held meetings with stakeholders, created InVision prototypes and iterated rapidly on them based on feedback, chose the Expo framework, bootstrapped the project, picked all the supporting cast of modules (redux, redux-form, redux-thunk, reselect, lodash, axios, redux-persist, jest, storybook, and pixi all being major players), wrote every line of JavaScript/JSX, completely subverted the Apple app store ecosystem in a way I'm not sure anyone else has thought to, AND wrote this really long run-on sentence.

One major challenge which still remains in my mind is the work I did to create a signature input, for clients to sign off on the answers they gave.  Existing solutions were all commercial, and I thought "I'm not paying for that, I can do it myself", and I indeed could, but Expo and its many pieces of abandonware made it much more difficult than it needed to be.

I am older and wrinklier now, and every single thing I did was a mistake.  The code is nice, the PRs went well and were a great source of teaching material for my manager who learnt as he PR'd my work.  The app works quite reasonably on real devices, and the integration with Eee, while wanting, wasn't the worst thing ever.  I even still really like the docs I wrote describing the redux store layout.

The problems, however, are numerous.

There was little-to-no employee nor leadership buy-in, so all the time I spent has been completely wasted because nobody uses the app.

The data structure and form description is all very static for a business reason that turned out to not matter at all, making changes many times more difficult than they need to be for no benefit.  Delivering the desired data shape from Eee as a JSON schema would have been infinitely preferable.

There were a great many awkward and annoying hoops through which I had to jump to use Expo that wouldn't have been the case had I made the (scary) decision to learn Swift or Objective-C instead.  One example is that Expo holds the keys bundling and distribution themselves, so you're forced to stay on SDK versions they support, which keep changing and deprecating/removing features my admittedly simple app relied on.

The docs I wrote for the store, while nice, are essentially a weird reinvention of TypeScript without any of the good features like transpiler static checking.  I avoided using TypeScript because I was apprehensive that I should be delivering a product rather than learning new things.

### Apr 2019, Eee documents feature

A method of storing and serving SOP documents from within Eee was requested.  Access to uploading new versions was to be restricted with some managers being able to make changes to SOPs visible to their reports, some others to theirs, and yet some other managers being able to control everything.

I wrote a self contained Django app to handle all of this with group-based authorisation, and pre-emptive caching with invalidation such that group membership could reliably be checked without a database query.

I remain particularly proud of how the whole app was written, and it has in the three years since constantly been referred back to both in an individual reference context, and between my manager and myself when hunting for an example of "how it should be done" in the course of an MR.

### Apr 2019, Dockerisation of Eee

Python projects have a habit of sprawling into the host system, and in environments which have a "system" Python, this is a constant source of wailing and gnashing of teeth.  The problem is exacerbated when pinning library versions, but even outside of those, running a given Python proejct might require Redis, PostgreSQL, RabbitMQ, three different SNES emulators, and `cowsay` installed.

Eee was no different.  During my first few weeks at the company, I couldn't for the life of me get tests to pass that were passing in other developers' environments, so I spent some time duplicating the production environment as a set of docker containers wrangled by docker-compose.  In doing so I also wrote brief but detailed documentation to help with onboarding future developers with regards to project setup.

### Jan 2019, CH2 Direct basket discounts

[CH2](https://direct.ch2.net.au/index.php?mode=ch2), a medical equipment supplier, wanted to offer discounts on products based on other products in the shopping basket.  I had previously made the grave error of demonstrating competence with PHP, and so was one of the two main developers on the feature, the other being my direct superior who had plenty of important superior things to do.

I designed the data structure, implemented it and its queries in the (awful home-grown) ORM, optimised other (awful) queries that were making everything I wanted to do very slow, and edited the (awful) PHP files to update the frontend.

I respect that I am paid to do what's asked of me, and I've done far less relevant things than program PHP, so I won't refuse to, but know this:  I will find another job.  Loyalty is earnt and can be spent.

### *Dec 2018, The Traitor

A simple program that consumes the [trade API from Path of Exile](https://www.pathofexile.com/trade) searching for a specific low price item available only in small quantities from each selling player, then listens globally for a hotkey using the Win32 API, injecting trade request messages into the clipboard also using the Win32 API, such that the user can quickly message the next seller with one keypress rather than four including a context switch to the web browser.

Due to how much time and effort would otherwise be wasted waiting for people who never replied, this small program offered me a competitive advantage in the market for that item.

### Nov 2018, AgriNous REST work

I worked for a little time each week in a large team sprinting from one fortnight to the next, implementing endpoints and their related models, querysets, and tests, for [AgriNous](https://agrinous.com.au/) - a livestock trading application for use at livestock markets, or perhaps one specific livestock market.  I was never sure.

### Oct 2018, MEERQAT node reordering optimisation

Part of the [MEERQAT](https://meerqat.com.au/) product involves a drag and drop re-ordering interface for a collection of items.  For a large amount of nodes, the reordering grew to take an inordinate amount of time, and froze the interface while it worked.

I set to investigating and found that nodes were Django model instances, and the ordering for a collection of them was defined by a field on that node.  When a node was reordered, it caused every other node in the collection to be resaved one by one.

I dreamt up and implemented a solution whereby the relative position of a node in a collection was stored as a decimal rather than an integer and could be updated to any position with a single database query, along with a periodic task that could evenly redistribute the positions to save from running out of room between numbers.

### *Aug 2018, Server-side rendering exploration

In an attempt to better understand server-side rendering, which was getting ever-so-popular at the time, I decided to try to work out how to do it myself from first principles.  I'd take a toy example of an SPA, a backing API in Django, and have Django pre-render and server the SPA with its state as if the URLs were navigated to in the SPA itself.

The result was a [repository](https://github.com/Asday/server-side-rendering-exploration) that achieved many of the goals I set out to achieve.  It turned out that server-side rendering isn't all that complex at all once I dared to investigate.

Doing so also deepened my understanding of a good amount of modules I used with React a lot, including but not limited to `react-router` and `thunk`.

### *Aug 2018, keiyakusha

Recording my time worked on each task in a spreadsheet was getting grinding, and having now had experience of both doing it in that low-tech way, and the more fully-featured offering of [Teamwork](https://www.teamwork.com/project-management-software/project-time-tracking-software/), I decided to write [keiyakusha](https://github.com/Asday/keiyakusha).  It is named after the word for "contractor" in Japanese, which I at the time had picked up from Darker than Black, and have since refused to confirm if I was correct.

I didn't achieve all my goals - I wanted to automatically generate my invoices to send off to my employer, and do currency conversions for instance, but it made tracking and totalling up my time much smoother.  Working with datetimestamps in spreadsheets is always hell.

keiyakusha is written entirely in Django and HTML, leveraging a couple of HTML5 features to avoid JavaScript.  I revisited the project at a later date to completely dockerise it as I had done in the meantime for other projects.

### Jul 2018, Karista

Throughout my time at CommonCode, one of the two most common projects upon which I worked was [Karista](https://www.karista.com.au/), a React SPA with a Django backend.  I worked primarily on the frontend, adding features and debugging chugging performance.

As work on the project lessened, my involvement too lessened, (don't have to pay contractors for hours they don't work), and I took on more of a mentor role for the at the time less experienced full-time developer remaining on the project.  I enjoyed that - I think it sparked my want to teach.

### *Feb 2018, Home server

For my own archival ("data hoarding") purposes, I designed and built a fileserver.  I chose 16GiB of ECC RAM, a Celeron G3930, and six 2TB hard Western Digital Green hard drives in a RAIDZ2 configuration.

For the OS I chose a derivative of FreeBSD - FreeNAS - for its soft landing of a web interface for my introduction to ZFS.  This choice has been a source of constant problems whenever I want to do anything at all with the server, and I would definitely not make the same choice again, instead I'd probably use Arch.

I have since upgraded the RAM to 64GiB for better ARC hit ratio and a virtual machine running an OS that is just a bit less horrible to run services I care to keep running, and the drives to 18TB drives.

### Jan 2018, Egencia blue-green deployments

The [Egencia website](https://www.egencia.com/en/) was a highly-available load-balanced WordPress site, hosted within AWS.

Regrettably, we encountered some issues with the previous deployment, which was in-place.  I researched the issue, and could so no reason not to switch to blue-green deployments.  The main reason to switch besides fixing the deployment issue, was the ability to privately inspect the instances before switching traffic to them and destroying the old instances.

This allowed us to safely have an internal check of new features after deployment to staging, and also allowed for no chance for an instance to become overloaded during a traffic spice coinciding with deployment.

It also meant we could never fail a deployment and put ourselves in a halfway state.

Since blue-green deployments were operational, we didn't have an issue with deployments, and our time to deploy was reduced by around 20%.

As it stood, the solution was "good enough", which is what business needs dictate, but afforded the extra budget, I would have liked to investigate involving CodePipeline, SNS, and Lambda functions in the deployment process.  Doing so would have let us scale down the web server instances, saving the client money.

### Jan 2018, Unreleased project

A client approached us to create an application in which many people can enter their card details, and payments will be taken from them at regular intervals dictated by groups of which the people are members.

I contributed heavily to the design for separation of concerns, leading to data/logic, and display apps, for the first time in the company's history.  Upon reflection, I'm happy with the way that decision went.

The project was comprised of three separate sites:

* one for the client, to add new groups;
* one for group leaders, to view transactions, forecasts, and set up recurring invoices; and
* one for paying customers, showing their transaction history and allowing them to add payment details.

I implemented the permissions system to allow each user type to only log in to the appropriate site.  This was done with the help of django-polymorphic for the `User` type.

I also implemented the email system to send customers receipts for successful payments, and weekly reminders for failed payments.

Finally, I implemented recurring payments.  As the potential number of customers was huge, and payments must be taken not in response to a request, this required being made asynchronous, and concurrent, with Celery.

This went through several iterations, until we came upon a system which was so robust that only the deletion of the backing database would have caused any issues - we were able to lose the Redis instance used as a message queue, and the web server instance(s) at any point in the billing process, and fully recover simply by bringing the instances back online.

I achieved this by spawning a task to determine which groups needed billing, which spawns tasks that create intent objects in the database for each group to bill.  Next, billing dates were updated, and another process picked up the intents, creating further intents to create invoices, and so on, until a task at the end of the waterfall picked up an invoice, and enacts it.

Each intent and invoice could be acted upon independently, and as such were fully concurrent, meaning we could scale up our Celery workers to any amount up to `n`, and get the billin done on time.

The project was never released for business reasons.

### Nov 2017, Captivise self-signup and payment

Captivise entered phase two of development, which comprised of adding a [registration](https://app.captivise.com/register/) feature, along with online payment.

Up to this point, users had been registered in the system by an administrator, and charged out of band - Captivise wanted to change this and reach a wider audience, by opening signup to anyone.

With anyone being able to sign up, checks Captivise had been doing manually had to be translated into Python, similar to the [initial Scripts](story#captivise), though this time they were business requirements described in prose.

These checks involved enumerating the prospective customer's AdWords account, and deciding upon a fee, hinting to the customer things within their account that may hinder their experience with the tool.

Once the prospective customer had agreed to the terms, payment details were (effectively) taken, against which to make Continuous Authority payments in future, in a billing cadence matching AdWords' - every thirty days at least, with billing on the next day once a certain spend threshold was met.

To implement payments, we utilised a library which I wrote to integrate with a payment provider with whom JP74 were able to secure a good business deal, in order to provide the client lower costs.

In addition to the above, I also improved the graphs shown to the customers - aggregating the data points if the chart was displaying too much data, and switching to a monthly view, instead of daily.

### Sep 2017, Ecom6 integration for Django

[Ecom6](https://ecom6.com) struck a deal with JP74 to be a payment gateway for them.  As most of our projects were in Django, we needed to write a library to integrate with Ecom6's API.

Amongst expected simple development such as designing models and writing REST calls, I added an identifier translation layer between Django and Ecom6, in the forms sent from and received into from Ecom6, which swapped variable names out from being `snake_case` on Django's side to being `camelCase`.  This allowed the library to feel much more native to use than it otherwise would have.

The initial version shipped with support for Continuous Authority (recurring) payments, and a similar process for refunds was added shortly thereafter.

I was responsible for all the substantial commits on the project.

### Aug 2017, Captivise {#captivise}

[Captivise](https://app.captivise.com) is a company that manages peoples' AdWords campaigns on their behalf, for a fee.

With some Google Scripts they'd developed and honed over years, and their expertise, they reduce customers' costs and increase their conversions.

Their Google Scripts had grown slightly cumbersome, so the client approached us, looking to convert them into Python, using the Google API instead of Scripts, and package it in a nice website with some simple dashboards, to serve as added value for their customers.

For the initial release, I translated all but one of the Scripts, implemented the non-styling side of the frontend, the adapter to marshal intents and data between the AdWords client and our application, and the tables on the website, amongst less impressive basic implementation such as setting up views, templates, and models.

### Jun 2017, House by Urban Splash configurator

Urban Splash are a real estate construction company, who build houses to order, floor by floor, in a factory, then ship each floor to site, and assemble the house onsite.

As part of their marketing campaign, they approached us to create a configurator similar to what one might find on a car website, [but for houses](https://www.housebyurbansplash.co.uk/configurator).

With an extremely tight budget, both monetary and time-wise, we produced something to be proud of.

As a whole, the configurator is a React SPA, powered by a Django REST Framework API, contained in a custom wordpress theme.

We built a spreadsheet of product components in Google Sheets, such that Urban Splash could edit it easily in future, and update the configurator without needing to incur a service charge.  The product components were deduced from the product catalogue.

I wrote the implementation to unmarshal the data from the spreadsheet into Django models, which later was used to automatically import the spreadsheet directly from Google with a single click in the Django admin of the API.

We were provided a 3D orthographic render of each possible floor layout, with and without a timber floor, and an SVG of a floorplan for each floor layout.  To have these update in the configurator in response to the user choice, I implemented the following:

For the floorplans, I first learnt move about SVGs and their interaction with browsers - discovering that SVGs can be targeted by CSS, and liaised with the design team to outline certain areas, (such as the floor, kitchen units, etc.), with transparent shapes, which I could then fill with CSS later.

I included the SVGs inline in the final DOM with `react-inlinesvg`, and added inline CSS to the component, which updated based upon the state in Redux.

For the 3D renders, we needed to colour in the customer's choice of floor, kitchen unit, and the like, but the renders were more realistic than the floorplans, so simple masking wouldn't suffice.  Using my knowledge of image manipulation from my previous role at John Hunt Photography, I suggested the "multiply" blend mode to the designers, who approved of it after experimentation.

I pushed for an in-browser solution, in which we would provide each layer, and each colour mask, to the user, then use the new CSS blend modes to recreate the effect, but this was shut down after passionate discussion.

We instead created an image for every configuration of floor.  The design team couldn't do the task, as somewhere in the region of fifty thousand images were needed.  I instead implemented the manipulations using PIL and a small library called `blend_modes`.  The process took over ten hours to complete when fully parallelised on my powerful home PC.

### Apr 2017, Store First dynamic price slider and reservations

[Store First](https://www.storefirst.com/price/) previously had a price slider on their site which had values set statically in the code, and was more indicative of price than anything else.  They asked us to integrate their existing site which we created with their management system.

We were do to so through the use of several stored procedures on the database of their management system.

I owned all commits on that part of the website.

I updated the Angular-based price slider to accept a lot more data from the server, and change how it renders based on that, with some locations having more or less sizes than others, and sizes being different prices in different locations.

I then added proxy models in Django for models on the management system side, and implemented a system to call stored procedures in SQLAnywhere 12, which was much more trouble than it should have been, due to some stored functions with return values, which required a lot of effort to capture.

Finally, as fetching of the prices took an inordinate aount of time, I cached them for a day, and set up a cron to refresh the cache every morning at 0500 - after the updated routines in the management system had run for that day.

In addition to the above, we were asked to implement paid reservations - a customer would pay an amount through the website, which would register their reservation against a unit, marking it as "in use".  I used the `django-paypal` library for this, though the functionality was removed a few months later, for business reasons.

### Feb 2017, Unreleased project

We were asked to produce an aggregation system for a client's car park network, integrating with the first party car parking API, and taking payments from a specific payment provider.  We delivered, but the project never went live for business reasons.

I was mostly responsible for the whole project, with styling being taken care of by a colleague.

The most challenging part of the project was writing the API client, as the API had some idiosyncrasies which required some substandard programming to get around.

Pleasingly, the website was very fast, and the newer version of `django-cms` made things easier to work with than our previous projects.

### Jan 2017, Arjowiggins Academy of Certified Printers

Arjowiggins, a creative paper manufacturer, needed a web presence for their new Academy of Certified Printers initiative.  This required some copy display, a map with pins that cluster when zoomed out, ICC and PDF downloads, and integration with the existing Django CMS-powered website.

I championed the project, taking it from a brief to the [current product](https://arjowigginscreativepapers.com/en/printing/academy), with guidance from my at-the-time tech director, and a colleague doing the styling (with guidance from the design team).

The Arjowiggins website is heavily data-driven, so their team is comfortable with uploading CSVs and zip files for import and editing content through the Django CMS frontend.  To that end, I implemented a method for them to provide a CSV detailing certified printers, and have that power the generation of the PDFs and resultant zip file downloads, using `django-import-export` for unmarshalling the data, putting it into the correct place with `django-filer`, and `wkhtmltopdf` for converting it to PDF.

I also implemented a new map plugin on which for the certified printers to be located, which utilised Google Maps' pin clustering.

### Jun 2016, Arjowiggins HTTPS migration

[Arjowiggins](https://arjowigginscreativepapers.com) provided us with an SSL certificate, with a view to migrating their marketing website to HTTPS for SEO reasons.

I researched the deployment process for HTTPS on nginx, documented a migration plan, then enacted it.  This involved running the django test server as HTTPS locally and manually testing it, resolving issues such as mixed content and hardcoded links.

### Apr 2016, Store First HTTPS migration

[Store First](https://storefirst.com) asked us to migrate the site we made and hosted for them to HTTPS.

I investigated the best way to do so, and after a false start down an expensive path, I heard that LetsEncrypt had left beta, and so implemented that to the best of my abilities.

Whilst doing so, I also wrote an internal guide for other tech team members, so implementation was easier the next time.

I did as much as I was able to do in the time I had available, and scored an A+ on Qualys' SSL test tool - a score that remained as high at the time of writing.

### Apr 2016, Arjowiggins importer upgrade

[Arjowiggins](https://arjowigginscreativepapers.com) exports a product catalogue from their product management system as a CSV, and updates the website by uploading it to the admin section.

The product catalogue has grown in complexity over time, and had outgrown the foresight of the product importer on the website.  This manifested as several 500 internal server errors, and no clear tracebacks from which to work backwards.

I was tasked with investigation and correction.  To do so, I narrowed down the offending imported CSV to a few rows which reproduced the problem, and discovered that there were now products that were essentially children of other products.

I planned a way to represent this in the database with minimal changes, exposed the products in a discoverable manner on the website, and maintained the working order of the sample purchasing process for website users.

The result stood to the time of writing, as evidenced by the links to subproducts in this exemplary [product description](https://arjowigginscreativepapers.com/en/catalog/conqueror/laid/brilliant-white/).

### Jan 2016, Daimen Sucks v2.0

In this final update to [Daimen Sucks](story#daimen-sucks) before I left for a job actually doing programming, I enacted a very painful database migration.  Up to that point I'd only done simple things like add a column, or rename something, but at this point the horrible decision to use pack codes (used by Halse to identify which set of layouts to print) as a primary key came to light.

While a pack code does uniquely identify something to be printed, Daimen Sucks was concerned not only with printing, but also with pricing.  This meant that for orders which had something extra such as a t-shirt or a mug, but still the same paper prints, the user had to select the paper prints, then add a price adjustment, and a note lest the difference is missed.

This release saw me add a new field to the packs table, set a unique value for all rows, modify the table so the primary key was on that column instead, and then changed the database adapter in Daimen Sucks to use the primary key instead.  This allowed for the addition of augmented packs, saving time and effort when counting, and mistakes out the door lessened.

I also fixed some minor bugs.

### Dec 2015, ID disc burner v2.0

The previous spartan implementation of the [ID disc burner](story#id-disc-burner) which relied on being comfortable with simple command line use to use was deemed user-unfriendly, and I was asked to upgrade it such that it had a nice GUI.  Once again I chose to use wxPython in the rewrite.

### *Aug 2015, What are the Chances?

In the game Path of Exile, randomised loot is a core part of the game.  Every "rare" item has a randomised name of two words, picked from a pool applicable to that item's base type.  An axe could be called "Foe Render" for example.

If you happen upon two items with the same name, you can sell them to an NPC vendor for a moderate amount of currency - an Orb of Chance.  The intention is a very occasional small bonus for acquiring loot.

In practice, I had a great deal of spare inventory space due to financially supporting the game, so I simply kept every item I acquired, instead of selling them for meagre currency.

Mathematically, the more items one keeps, the higher percentage of those items will be usable in the so-called "chance recipe", though the time to manually find each match will increase drastically.

To that end, I wrote [What are the Chances?](https://github.com/asday/whatarethechances), a program that searches one's stash for recipes, and displays them in the most efficient format possible.

I only ever expected it to be used by myself, but the [original release video](https://www.youtube.com/watch?v=5gffb8iLKc0) has 13,000+ views on youtube, and I have serendipitously connected with two people who have used What are the Chances? for their own benefit.

### Aug 2015, MySQL backup

With so much now-important data in [Daimen Sucks](story#daimen-sucks), I wanted to take backups should anything go wrong.  MySQL Backup was a simple wrapper around `mysqldump` that ran in the background and handled writing the dumps to specific locations, deleting old dumps, and notifying me when it went wrong.

### Aug 2015, Daimen Sucks v1.2

I added several small features to [Daimen Sucks](story#daimen-sucks) for the v1.2 release, mostly aimed around providing users opportunities and prompts to double check their work, such as highlighting input barcodes it things are suspicious because they're too high, or not numeric, and showing the user the numeric range of barcodes entered for a single job, by the logic that all the photos for one school will have likely been imported at the same time, and thus have a small numerical range.

I also added some features to improve workflow, such as the ability to hide product types the user doesn't deem relevant for the job at hand, and the ability to export a collection of jobs at once by providing a list of school IDs, which helped me in my job personally as I chose which jobs to submit to the printer at the start of the day based on the physicality of the stack of proof cards.

Finally this release also included over a dozen improvements and bugfixes spanning from UX to workflow to data loss, authorisation cadence, and startup time.

### May 2015, Daimen Sucks v1.1

I fixed several bugs in [Daimen Sucks](story#daimen-sucks), and added some small features, such as confirmation dialogues to prevent users accidentally deleting all their work, and order total readouts to more efficiently ignore empty orders for printing.

The headline feature for v1.1 was reporting.  Using `matplotlib` and some almost completely undocumented features thereof, I integrated charts into the wxPython interface.  These were used by management to keep track of how the business' revenue was doing on a per-school basis, see which photographers' work brought in the most money, and which packs brought in the most money.

A quickly-removed feature was calculation of commission.

### Jan 2015, Daimen Sucks v1.0 {#daimen-sucks}

Named after a less-than-savoury ex-employee, Daimen Sucks was a well-featured management suite for the production side of a school photography company's daily doings, with a GUI interface using wxPython, because I liked the native feel.

When proof cards and their associated bags of money came back from a school, the counting department registered the orders along with how much money was received.  Daimen Sucks displayed thumbnails of the selected images for confirmation, and a running total of price, so the users could double check at the end of each job for discrepancies.  These two features saved many hours of checking someone's work from two weeks ago, and untold amounts of real money that was miscounted or not accounted for.

Daimen Sucks ran from a MySQL database I hosted first on my PC in the office, and later on an OpenBSD fileserver I built.  When counting had finished a collection bag from a school, Daimen Sucks saved the entered information to the database.  It was then able to export a custom file format for the Halse lab management software suite to consume, thereby producing the printed photographs.

Daimen Sucks also produced report-like text files which the order packing department wanted, so they could count how many of which order they have packed, as a double check to make sure they haven't missed some orders before sending the job to the customers.

### Oct 2014, Gift pack burner

A product was launched whereby an ordered image was composited into a bunch of templates for different situations - father's day, birthday, christmas, particular seasons, and so forth.  These composited images were then burnt to CD for the customer to presumably print out on their home printer and distribute to family and friends depending on the occasion.

In a similar vein to the [web order compositor](story#web-order-compositor) I had written previously, I wrote an application that leveraged PyGame to manipulate the images and save them out to a disc, though the differentiator here is that this was to be used by other employees, so I wrote a GUI for it, again in wxPython.  The placement and sizing of the photographs was also different this time - using a configuration file rather than a Python dictionary.

I also implemented drive enumeration and checking that a disc was present using the Win32 API.

Despite the name, this was mostly used to author flash drives, so ImgBurn was not used as with the [ID disc burner](story#id-disc-burner) project.

### Sep 2014, Renamer

Photographers coming back from photoshoots at schools were required to upload their images to the server, so they could be worked on by the rest of the team as needed.  There was a requirement to have the images named in a sensible manner - starting from `0000` and ascending from there.  This used to be achieved by "formatting" the flash card with the camera before a shoot, but that had several issues - photographers often forgot to do it, when more than one was on the same job there were conflicts, jobs split over multiple days tied up too much equipment, and there was suspicion about corrupting flash cards by formatting them too much.

I wrote a small client server application.  The client ran on each photographer's PC, and used wxPython and raw sockets to guide the user through selecting the right school for the photos and location of their flash card, and to connect to the server half of the application to query the current highest filename number for that school and that season.

The application would then rename and copy the files to the server and provide user feedback during the process.

The server process used twisted to implement the custom network protocol.

### Mar 2014, Halse integration library

The Halse lab management software suite was not fantastic, but it was incumbent, and did do reasonably well when it came to printing photos, so I dug around in it and found its underlying SQL connection details, then used those to read some information from its database, which was essentially canonical for the company with regards to UIDs for files, colour correction data, and file location.

I reused this library in a great many projects small and large in my time at JHP.

### Sep 2013, Web order integration for Daimen Sucks

While "main orders" came directly from schools, in big bags of smaller bags filled with proof cards filled with money, "web orders" came through our online shop.

At this point in the chronology, [Daimen Sucks](story#daimen-sucks) had not yet been released, but was in experimental use.  The problem was Daimen Sucks was concerned only with main orders, so I wrote web order integration as a collection of small modules separate from Daimen Sucks.

One module was a custom "barcode" implementation that let me go from some disparate details on the order sheet and my experience in the company to that point, to a compact textual identifier that I would type manually, which would fetch the exact image ordered.

Another was a thumbnailing preview that I could use to sense check I'd typed the right identifier and wouldn't waste paper and chemicals printing something useless like a photo of a whiteboard with "Year 6" scrawled upon it.  The thumbnailer worked in a thread to fetch the image over the network, scale it with PyGame, and show it in the wxPython interface.

Another was the order building interface to input barcodes, view the associated thumbnails, select the ordered products, and export a stack of orders to a file.  This process was highly streamlined, with focus jumping between inputs based on what input will likely be needed next, the barcode input split into multiple sections so retyping the parts that changed less often was less frequent, and hotkeys for everything.

This exported job file was imported into Daimen Sucks, which registered it as a normal job in its database.

### Jul 2013, ID disc burner {#id-disc-burner}

We often provided schools with very scaled down copies of their photographs, with the same filenames as on our file server.  This allowed parents to choose off-shots we had decided against using, just in case, and also occasionally to provide name registers for special products.

To get rid of another horrible Photoshop-based process, I leveraged PyGame to resize the images, and ImgBurn by way of a custom-written template file to burn a disc.

### Apr 2013, Web order compositor {#web-order-compositor}

After working as an unskilled Photoshop monkey for a season, but not being seasonal staff, I was tasked with producing the prints for web orders in the hopes that I would be worth my wage.

The process for this was a horrifyingly slow and expensive one, involving Photoshop and a wealth of actions (macros).  Given the actions take over the photoshop instance, photoshop only allowed one instance to be running at a time, and I only had one computer at my disposal with unimpressive specs, something had to change.

The actions simply took an input folder of images, composited them with proper aspect aware scaling, and saved them to an output folder for printing.  The main labours were fetching and organising the images into the correct input folders to produce the right compositings for the ordered "pack", and sorting the out of order prints into single orders with their printed order sheet for cutting, framing, and delivery.

I converted the actions to Python, using PyGame to handle the image manipulation, and expanded upon the input/output folder situation to allow for much simpler printing and sorting - as I wrote it, everything went through the process and there were no special one-offs that caused mental context-switching and cost time (such as single prints), and all prints for a specific pack came off the same printer, so packs weren't interleaved half and half between the 8x10" and 4x6" printers.  This eased sorting, and arguably provided better colour matching within a pack.

The process was fully concurrent and worked well when parallelising, and ran much faster even single-threaded due to how slow and awful Photoshop is.

### Sep 2012, Autoprinter

Occasionally customers turned up in the shop looking to buy a print then and there, whether one we'd taken or one they brought to us.  This process saw our customer service prepare the photo for them, then walk into the back to ask me to print it, as I was given control of two small photo printers.

I wrote a pair of small scripts that watched some folders I created on the network, sending their contents to the printers automatically, by shelling out to IrfanView.  This was well-received, and afforded me the freedom to implement further tools for the company going forwards.

### *Age 13, Began teaching myself programming

Beginning with a tutorial in an issue of Computer Shopper on VB.NET, and quickly evolving into several online Python tutorials, my self-initiated journey into software began.
