# **Week #5**

## Feedback

### Sessions

We conducted three interviews with people who enjoy reading and could be potential users. Each session was structured
into three parts:

- A tutorial segment, where the interviewer explained the features available to the user.
- A hands-on session, where the user explored the application independently.
- A question-and-answer segment.

#### First interview
Q: First impression of the website?

A: Umm... It looks kinda old? Like something from a few years ago. I mean, it's not ugly, but it's not modern either. I
thought it might be a blog at first.

Q: How did it feel using it on your phone?

A: It was okay. Some of the text was a bit small, but overall is good.

Q: How was logging in and using it?

A: Logging in worked fine. I clicked "Sign up" and register used my email, and it was smooth. After that I log in.
No issues there.

Q: What did you think of the calendar view?

A: The calendar is nice and big — easy to see my streak. But the little button to mark the day? It’s kind of small.
I’d prefer it more obvious. I liked seeing my streak on the calendar.

Q: Will you use this application after release?

A: I like seeing the streak build up. That little "don’t break the chain" thing works on me. And I saw the book
section — I might use it to find something new to read.

Q: Overall experience (1–10)?

A: I’d say 7 now that I understand it. Make that button bigger though!

#### Second interview

Q: Anything that annoyed you or stood out?

A: There's no dark mode or anything—everything's just white and gray. Kind of boring.

Q: Was it easy to find what you wanted?

A: Kind of. I clicked around and found the book list stuff. But the page could use
icons of covers for each book, not the default one. It feels very plain.

Q: Thoughts on the calendar and streak?

A: The calendar is cool — really visual. I like seeing which days I missed. But it can be a bit smaller, on my monitor
it does not fit on the screen

Q: What the most interesting feature you see in this app?

A: I liked the "bookshelf" in the app, sometimes I forget about books I want to read and here I can find it and mark "To
Read", so I can remember them. But it would be nice to add the covers of the books, not the default images) Ah yes, the
collection feature also nice, I can store books I liked, for example

Q: Will you use this application after release?

A: I wanna see how long I can keep it going. It's like a personal challenge. And the book section — it’s basic, but
I found a couple things I didn't know about.

Q: Overall experience (1–10)?

A: Solid 8. It is already usable, just add covers, smaller calendar maybe, bigger streak button and this could be
something I use daily.

#### Third interview

Q: Easy to use?

A: After your tutorial - yes, but I guess there will be cool to add small tutorial in the app.

Q: Do you like how it shows your books?

A: It’s okay. I like lists, but maybe add more colors or categories. Everything feels the same, like it's all in boxes
without covers.

Q: What the most interesting feature you see in this app?

A: I liked notes and reviews features. I think this is fun to open info about book I read month ago and check my
thought through the book. And it's great that I can check recommendations (i.e. reviews) from other people, so it's
easier
to check next book to read. It's great that all of this in one application

Q: Would you use this regularly?

A: Yeah, maybe! It's kind of satisfying to see progress like that. And I saw a few books on the site I didn't know —
   so it's like a tracker and a bookshelf. And, of course, the notes feature - wonderful

Q: Overall experience (1–10)?
   
A: I'd give it a 7

### Analyze

The interviews were useful to us, we analyzed the feedback and overall, for this point, the app is good, but, of course,
we need improvements.

#### Frontend

- The streak button should be bigger, and maybe we should move it
- We should add covers to books - not a big issue
- Calendar may be smaller
- We should fix the "Read" counter

## Iteration & Refinement

### Performance & Stability

We used Yandex Test Load to monitor performance and stability of the app

The server successfully withstood a load of 240 requests per second, demonstrating stable operation without failures,
while the response at the 95th percentile remained consistently below 200 ms, errors of type 500 were not recorded.

The breakdown point is 300 rps, but the server withstands a constant load of 250 rps.

The link to the screenshot of the monitoring results: https://disk.yandex.ru/i/-IBPZ029_zNWNA

### Documentation

We have got openapi documentation with structured information of our API. Also, README file with quick set up of the app
on the local machine.

# Weekly commitments

## Individual contribution of each participant

- Ivan Isakov wrote UserBooks segment and updated the backend according to the modified database schema.
- Ivan Savelev did frontend for main page, fix of styles and structure of "Create account" page
- Darya added routes for subscriptions, curl tests for them, wrote the report, interviews potential users
- Batraz updated database and wrote new database methods for subscriptions
- Andrey fixed and optimized stores and api methods of the frontend. Changed routes and data for new backend standards

- Andrey & Dasha did load testing

## Plan for Next Week

Make edits in all parts of the service, because there are small errors that require attention.

## Confirmation of the code's operability

We confirm that the code in the main branch:

- [ ] In working condition.
- [ ] Run via docker-compose (or another alternative described in the `README.md`).
