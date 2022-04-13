---
title: "Code Review #1"
date: 2021-09-03T06:55:14Z
header_image: https://static.righttobeoffensive.com/i/code-review-t.png
draft: false
---

Part one out of a probable one.  A lot to say about a small script by a beginner.  This script does some web scraping and variable juggling to present the user with a quiz on various chosen topics.

<!--more-->

This is a compilation of a bunch of reddit posts I made on [/r/Python](https://old.reddit.com/r/Python) in response to a new programmer looking for a code review.

{{< expando id="listing" title="Click here for the full listing." >}}
  [review_code.py](posts/review_code.py)

  {{% listing fname="posts/review_code.py" lang="python" %}}
{{< /expando >}}

If I can be bothered, at a later date I'll find the links to my posts - I don't remember how well they were received and it's coming up for a year since I wrote them compared to now.  I'm also now banned from there for being too spicy when Russia invaded Ukraine.  Again.

---

> I recently started to take my interest in programming seriously

Hell yeah my dude welcome to the fold.  Let's do this.

* First up - use hosted version control.  [github](https://github.com) is free to use and has features that would make this review easier for me to do.  It's also instrumental for working as a team.

* Ship your code with a way to run it.  I notice that it has a dependency on `requests`, but nowhere is that described besides in the source.  I only know the dependency is there ahead of time because I happen to be looking at the codebase, and the import happens to be at the top, and I happen to know that `requests` is not part of the standard library.

The best (in my opinion, and therefore in fact) way to do this is to provide one or more `requirements.txt` files, with each dependency having an exactly specified version per line.  In your case, the requirements file would look like this:

```
requests==2.26.0
```

* Adding on to the above, it's more friendly to your users if you tell them how to run it.  Add a README that explains the prerequisites (Python, which OSs, so forth), and how to install and run the project.

* Nitpick - sort your imports.  `random`, `os`, and `json` are all stdlib, but `requests` is third party.  It's hard to tell that without already knowing, just by looking at the top of the file.  Personally I like to have the groups: standard library; framework; third party; first party; local, but feel free to chop and change these as you see fit.  Also on the topic of sorting imports, sort them alphabetically by module too.  It makes it easier to see at a glance whether something has already been imported.

You can use `isort` to handle this for you automatically (which again feeds in to working with other people - an `isort.cfg` at the top level explains to your colleagues in black & white "this is how we do it").

* Instead of setting a flag to break out of a loop, use `break`:

```python
while True:
    main_quiz()
    ...
    if should_quit_for_some_reason:
        break
```

* `GAME_RUNNING = ...` `PLAY_GAME = ...` save `UPPER_SNAKE_CASE` variable names for constants.

* `global correct` `global incorrect` - don't use `global`.  It is _always_ (in my opinion, you know how this goes, I'm right), incorrect to use `global` outside of throwaway "I literally just want this to run once" scripts.  When you find yourself writing `global`, autocorrect that in your mind to "oh I should be using a class here".

* `main_quiz()` is doing a crazy amount.  It's clearly an orchestrator in disguise - some collection of discrete tasks performed in order, but the discrete tasks are all inlined for no great reason.  You'll notice you've already done a lot of breaking down into functions, but you didn't realise it.

```python
def main_quiz():
    amount, difficulty = start_game_options()
    print_categories()
    questions = get_questions()
```

And so forth.

* `dif = ...` prefer to use proper words for names.  You can get away with short or single letter ones where you're using the variable right then and there, for instance in an enumeration, but `dif` isn't used for another fifteen lines.  Call it what it is, `difficulty`.

* Unsanitised user input.  The API you're calling hopefully has input sanitisation (though it's PHP so who knows), but it's still a better idea to sanitise input yourself - you _know_ that the only valid options for `amount` are `in range(1, 50 + 1)`, and you _know_ the only valid options for `difficulty` are `in ["easy", "medium", "hard"]`, so why aren't you forcing the user to pick one of them?  Similar commentary for `category`.

* Whole bunch of `print()`s all stacked atop one another.  Way more typing than is needed.

```python
print(
    "Random: 0\n"
    "General Knowledge: 9\n"
    "Entertainment Film: 11\n"
    "Entertainment Music: 12\n"
    "Entertainment TV: 14\n"
    "Science and Nature: 17\n"
    "Sports: 21\n"
    "Georgphy: 22\n"
    "History: 23\n"
    "Celebrities: 26\n"
    "Vehicles: 28\n"
    "Science: Gadgets: 30"
)
```

In brackets like that, string literals are concatenated together.

* Style: it'd be easier to read that menu if the inputs were on the left, aligned, and the descriptions were on the right:

```
 0: Random
 9: General Knowledge
11: Entertainment Film
12: Entertainment Music
...
```

* `if category == 0:` in Python 3, this will never be true.  `input()` takes input from the user and provides it to te program as a string.  If you want to compare it to an int, you need to cast it yourself:

```python
try:
    category = int(category)
except ValueError:
    # handle the duff input somehow, maybe ask again
    pass

if category == 0:
    ...
```

Of course it would be easier to compare the string input: `if category == "0":`.

If you're in Python 2, `input()` attempts to do some basic conversion, but you shouldn't be relying on that, (use `raw_input()` instead, for Python 3 behaviour), and for the LOVE of god don't start new projects in Python 2.

* UX: as a user, I might be quite reasonable in expecting that `0` and `0 ` are the same, but of course they're not.  Perhaps add some deburring to the input such as "category = category.strip()`.

* Going back to `main_quiz()` being an orchestrator in disguise, using that line of thought as a tool you can see that the following is out of place:

```python
# Score Variables
correct = 0
incorrect = 0
```

Let's rewrite it and its surroundings as if it was an orchestrator and we'll see where it all falls down:

```python
def main_quiz():
    ...
    category, random = get_category()
    correct, incorrect = setup_scores()
    questions = get_questions(category, random)
```

You see how the scoring setup is completely interrupting?  Asking the user for the category is inherently part of getting the questions, and should be as close to it as possible.  There's also an argument to be made for the question getter to do the getting of categories, (and difficulty and amount), which I'll make later unless I forget, which I won't, because I'm perfect.

* `# Score Variables` it's not a title, comments are prose - `# Score variables.`

* `f"https://..."` I do love f-strings, but there are tools to build URLs, which you should be using.  [`urlencode`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode) for the query string, and if you want to be super proper about it, [`urlunparse`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlunparse) for the whole URL.

```python
query = urlencode(query_params)
url = f"https://example.com/?{query}"
```

I'll get back to `query_params`.

* If `if random:` passes, (which it currently never will, but let's ignore that), you'll make a request to the server, then immediately overwrite the response by doing a different request.  To fix this most simply, use an `else`:

```python
if random:
    response = requests.get(...)
else:
    response = requests.get(...)
```

But there's an even better way, combined with the previous point.

`urlencode()` takes a mapping (or some other stuff I'll ignore), so we can progressively build that, then construct the URL (which is the only thing that changes), then bring the `requests.get()` call out of the `if` statement and only write it once.

```python
query_params = {
    'amount': amount,
    'difficulty': difficulty,
    'type': 'multiple',
}

if not random:
    query_params['category'] = category

query = urlencode(query_params)
url = ...

response = requests.get(url)
```

I remember not quite grokking dictionaries as a beginner, so feel free to write this out line by line in the REPL and make predictions about what the contents of certain variables will be at certain points, then inspect them to prove yourself right.  (In that order.  You _must_ generate a mental model first).

* line length!  [Look how trash this is](https://imgur.com/LkJcw4c.png)!  Your code should be a love letter to your fellow developer, (who may be you in three months).  Newspapers and publishers have figured out hundreds of years ago that people tire of reading overly long lines.  That's why broadsheets have columns, and why books have large margins (or layout).  There's a design book I had a flick through one time that I forget the name of that you should check out.  I've asked a friend to remind me of it, so we'll see if his memory is better than mine.  (It was, [here](https://www.amazon.co.uk/Grid-Systems-Graphic-Design-Communication/dp/3721201450) you go).

Keep your lines to 79 characters or less.  If they're lines of prose (block text or comments) keep them to 72.

Note that with the above suggested changes, the lines will just so happen to become shorter than 79 characters naturally.  Enforcing line length encourages good code practices because it discourages overly indented blocks, overly verbose variable names, and rewards breaking things down into parts as described above.

People _will_ disagree with me on this hardline stance, and I _will_ die on this hill.  See above points about me always being right about everything.

* You call `requests.get(...)` and then never check the result, assuming that it will succeed with 200.  One day the server will go offline.  Sometimes your users will be offline (and might like to know they need network connectivity before they go through all the setup).  Maybe the server will go offline very briefly so you should retry.  Maybe it will stay online but the endpoint will change, and you'll need to update the URL rather than retrying.

Because you never checked the result, you were never forced to think about these things.

* `# Create a formated` *formatted

* `jsonDatabase`, `questionArray`, `qIndex` and so forth are all using `camelCase` naming, which doesn't match Python conventions, nor what you've written in the rest of the file.  Use `snake_case` for variable names.

* `x = json.dumps(response.json(), ...); json.loads(x)` why?  `Response().json()` returns a Python object (if it can), so there's no reason to convert it to JSON (from a Python object) and then back into a Python object, unless I'm missing something to do with `sort_keys`.

(And if I am, there's a better way to do it).

* Nitpick: `#Index of array search` missing a space.

* `# Randomize awnsers ... for correct awnser` *answers, *answer.  I notice this is misspelt in the same way in future variable names with reasonable consistency.

* This upcoming `for` loop is a data transform which doesn't describe its input shape or output shape.  What should I expect to see in `questionArray` from the API?  More importantly, why aren't you checking that it's the right shape?  If the API returns an object that doesn't have `'results` as a top level key, your program will crash instantly and exit.

* `for i in questionArray['results']:` `i` is generally used for an index only, (and there are good arguments floating around against ever using single letter variable names).  It looks like it would be better named here as `for question in questionArray['results']:`.  Also I just noticed it's never used.  Name unused variables a single underscore to make it obvious they're unused, but there's a bigger issue - read on...

* This is bizarre:

```python
i = 0
for _ in some_object['array']:
    some_object['array'][index]  # Repeated like eighty times.

    i += 1
```

As a small point, there's a construct for index tracking, called `enumerate()`:

```python
for i, _ in enumerate(some_object['array']):
    some_object['array'][index]
```

But that's beside the point.  I believe you have a fundamental misunderstanding of iterables.  The variable named in the for loop (the "target") will become the item in the collection as it's iterated over.  There's no need to do index nonsense.

```python
for item in some_object['array']:
    item  # Here it is.
```

* This data transform is pretty confusing.  This is a combination of your inexperience (no shame in that), and that the format returned by the server is a bit sub-standard, requiring some extra work.  Here's a rough breakdown of why I'm confused:

1. No description of the expected data shape

2. Mutation of state

3. Strangeness to do with randomisation interrupting the flow

4. A weird implementation of a mapping

5. The comment that heads the section talks about randomisation and assigning a letter, but _not_ fixing the bizarre input format

Point い can be fixed by including an example of the expected return in a comment.  The best place for this is the docstring of a function that returns the data.

Point ろ I'll go over shortly, but to evangelise on the topic of immutable state for a bit in this context - with mutable state, the reader has to keep in mind what shape the data is in _on each line_.  Let's say they went and got an example of what was returned from the API, and then they glance ahead and see that `incorrect_answers` somehow contains the correct answer.  Very confusing.

Point は I'll also go over shortly, but keep in mind this interruption idea.  I would identify it as a current weakness of yours that you can easily improve on and become stronger and more powerful.  Too powerful.

Point に is simple enough:

```python
correct_answer_letter = {0: "a", 1: "b", 2: "c", 3: "d"}[correct_answer_index]
```

You could be super duper clever and use `chr()` or whatever, but I don't like that for a good amount of reasons - forces sequentiality, silently removes bounds (suddenly you can get a "letter" for the index 150), requires the reader to know ASCII by heart or try it out themselves...  Best to just not.

Point ほ is also simple enough - write good comments.  As a beginner it's hard to understand what a good or bad comment is, but now I've explained why this block is confusing, and what the comment was missing that would have helped, fixing this one seems easy.

Anyway I'm rambling.  Let's talk about this block on the high level, and then set to a solution.

I snagged a response for myself to work off to understand your code, here it is:

```python
{
    "category": "History",
    "type": "multiple",
    "difficulty": "hard",
    "question": "In addition to his career as an astrologer and &quot;prophet&quot;, Nostradamus published a 1555 treatise that included a section on what?",
    "correct_answer": "Making jams and jellies",
    "incorrect_answers": [
        "Teaching parrots to talk",
        "Cheating at card games",
        "Digging graves"
}
```

This structure has one data type (answer) split into two parts based on a property of another data type (correctness, based on the question).  Personally I would have gone with something like:

```python
{

    "question": "Is Nostradamus a hella cool fella?",
    "answers": [
        "Yeah",
        "No",
        "Maybe",
        "I don't know, can you repeat the question"
    ],
    "correct_answer": 0
}
```

I notice you're doing a transform that's something _like_ this, but it's very haphazard as it modifies things in place and doesn't respect variable names and such, - `incorrect_answers` gains a correct answer among its ranks, for instance.

Once I had a sensible data structure, (and my goodness I wish I could convince API developers to provide them in the first place, but here we are), if I was going to encode the display logic in the data at this point as you have, the next step would be to randomise the order of the answers.  There's a value being used as an index into the list of answers though, so randomising the order of them must also update that value.

There are a few ways around this.  A nice simple one is to store the contents of the correct answer, shuffle the list, then look up the index and store it.

```python
import random

correct_answer = data["answers"][data["correct_answer"]]
random.shuffle(data["answers"])
data["correct_answer"] = data["answers"].index(correct_answer)
```

Note that `random.shuffle()` shuffles a list in place, so that is mutation.  If you don't like that, (and that's quite reasonable), you can use  `.sample()` instead:

```python
data["answers"] = random.sample(data["answers"], k=len(data["answers"])
```

Whatever.

Next up is the third part of the task, rendering the letter choices.  Again, let's approach this from the high level first by realising that the answers are _already_ keyed by something, just not letters.  `data["answers"][0]` that `0` is the key.  You want those to be specific letters instead.  Let's bring back an old friend.

```python
indices_to_letters = {0: "a", 1: "b", 2: "c", 3: "d"}
data["answers"] = {
    indices_to_letter[index]: answer
    for index, answer in enumerate(data["answers"])
}
data["correct_answer"] = indices_to_letters[data["correct_answer"]]
```

That there is a dictionary comprehension, which is just a fancy way to write the following:

```python
new_answers = {}
for index, answer in enumerate(data["answers"]):
    new_answers[indices_to_letter[index]] = answer

data["answers"] = new_answers
```

You'll notice that each of these three steps is nicely self-contained and makes plenty of sense as its own function.  This is an ultimate-level good idea because then the function can take the input, create the output and return it, (preserving immutability), and the functions can have a docstring each that documents the returned shape, an important part of understanding the code as a reader.

Now, you could add a fourth step in this to transform the data structure you'd have at this point into the one that matches your current `questions` structure, and on an actual project with deadlines and pay and stuff, you or your manager might decide that that's more cost effective than rewriting `main_display()` to accept the new and more sensible data structure.  This, however, is a learning project, so I would recommend you keep the data structure as is after these three steps, and reap the benefits of a good data structure with the rewrite.

Data structures are the most important thing in this craft.  Literally nothing else matters if your data is shit.

Whew.

* `NEW_ARRAY = ...` again, save `UPPER_SNAKE_CASE` for constants, but more importantly, this line is THREE HUNDRED AND SEVENTY FOUR CHARACTERS LONG!  PLEASE for the LOVE of god split your lines!  How can any reader possibly be expected to keep track of what index each element is at?  How can they be expected to understand what each of the elements is going to be?

Also as a stylistic note, when building up a list of flat collections (1D tuples or lists), generally the name for the temporary variable is `row`.  This is generally only used when a temporary variable is required because the row is being incrementally built:

```python
data = []
for item in collection:
    row = [item]
    row.append(some_data())
    row.append(some_other_data())

    data.append(row)
```

In your case, you have all the data in the first place, so you may as well nupe the temporary variable:

```python
for ...:
    questions.append([
        question["question"],
        question["incorrect_answers"][0],
        question["incorrect_answers"][1],
        ...,
    ])
```

* `def main_display(...):` Line length.  Also, it's not _really_ incorrect, but it's a bit strange that this function is indented at this level, thus defining it within another function.  I don't see much of a reason for this to not be top level.

* This function is, like the other one, doing too much.  It's called "main display", but it displays a _question_, takes user input, checks user input, interacts with the operating system, and modifies global state.

* Plenty more `print(); print(); print(); ...` in this function.  That can be improved.

* `print("")` you can simply do `print()` to output a newline.  You could make an argument for _always_ providing the first argument to make it obvious you haven't forgotten it, but given that there are no others, and the function is almost always called with at most one argument, I'm not sure how strong that argument is.

* `print("Correct"); input("")` `input()` has a prompt - why not just `input("Correct")`?

* `print("The correct awnser was: " + correctAFull)` what happened to using f-strings?  I love those!

* Style: `correct = correct + 1` can be `correct += 1`.  Similar commentary for `incorrect` a little further on.

* `clear_c = input(...)` this variable is unused.

* `clear_c = input ('')` again, this variable is unused.  Also this time (stylistically) there's a space between the `input` function name and its invocation.  Nothing wrong with that per se, but that's against conventions and you haven't done it anywhere else in this file.

* `# Reset qIndex to be reused` I am perfectly capable of reading the next couple of lines, that comment is just noise.  You might want to put a comment there if it was `qIndex = 6` instead, because that would actually be something about which I, the reader, would want to know about.

As a sidenote, that's a pretty contrived example because in that case I'd complain about the "magic number" and tell you to turn it into a constant like `qIndex = SKIP_HEADER_OFFSET` or something.

* `for i in questions: ...` another misuse of a `for` loop here.  See above for details.

* `print("Correct: " + str(correct))` f-striiings!  There's no need for the string cast in f-strings.  `print(f"Correct: {correct}")`.

* There is all sorts of mixing of levels of interaction all over the place here.  You have interface display, user input parsing, interaction with the OS, interaction with the network, maintenance of game state, all in the same breath.  It's kind of difficult to point out how to fix that in a general manner.  It's also difficult to point out why it's problematic and requires fixing without you having first added all the error handling that should be there.

Let's go back to the question getter I alluded to way back when.

The inputs are an integer in `range(1, 50 + 1)`, a string from the collection `["easy", "medium", "hard"]`, an integer from the set `{0, 9, 11, 12, 14, 17, 21, 22, 23, 26, 28, 30}`.  The outputs are some interface elements, and an array of questions as returned by the server.  Right now it's all jumbled together and full of potential vulnerabilities as discussed above.

Here's how I might do it:

```python
import os
import platform
import random  # Usage not shown.

import requests

def get_choice(prompt, valid_choices, transform=lambda x: x):
    """
    Prompts the user with the given string, and returns their chosen
    option assuming it's present in `valid_choices`.

    `valid_choices` should be a collection of strings, but in the case
    where a typed input is expected, and looking it up in the collection
    is cheaper as that type, a `transform` function can be provided,
    taking one argument and returning the value to look up in the
    collection.

    >>> get_choice(
    ...     "Pick a number between 1-50 inclusive: ",
    ...     range(1, 50 + 1),
    ...     transform=lambda x: int(x),
    ... )

    Where a transform is provided, the transformed value is returned.
    """
    choice = None
    while True:
        try:
            choice = transform(input(prompt))
        except Exception:
            # Something went wrong in the provided transform - assume
            # that means the input is not valid.
            pass

        if choice in valid_choices:
            return choice

        print("Invalid choice.")

def clear_screen():
    if platform.uname().system == "Windows":  # Probably, haven't checked.
        os.system("cls")
    else:
        os.system("clear")

def build_url(amount, difficulty, category):
    query_params = {
        'amount': amount,
        'difficulty': difficulty,
        'type': 'multiple',
    }

    ...  # You've seen this before

    return url

class ServiceError(Exception):
    pass

def get_response(url):  # Maybe this should implement retrying.
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.ConnectionError as e:
        raise ServiceError("Connection to the server failed.") from e
    except requests.exceptions.Timeout as e:
        raise ServiceError("Connection to the server timed out.") from e
    except requests.exceptions.TooManyRedirects as e:
        raise ServiceError("The server is misconfigured.") from e

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Maybe there's something the user cares about in this error
        # from the server, like a message saying "you have requested
        # too many questions today, come back at 18:45 tomorrow".
        raise ServiceError(
            "The server responded with an error: "
            f"{response.status_code}",
        )

    return response

def parse_response(response):  # Maybe `parse_and_validate` is better`.
    bad_return = ServiceError("The server returned malformed data.")
    try:
        decoded = response.json()
    except requests.exceptions.JSONDecodeError as e:
        raise bad_return from e

    try:
        validate_questions(decoded)
    except ValidationError as e:
        raise bad_return from e

    return decoded

def get_questions_from_api(amount, difficulty, category):  # Orchestrator.
    url = build_url(amount, difficulty, category)
    response = get_response(url)
    decoded = parse_response(response)

    return decoded

# The script starts, as does interaction with the user.
amount = get_choice(
    "Enter amount of questions you would like 1-50: ",
    range(1, 50 + 1),
    transform=int,
)
clear_screen()

difficulty = get_choice(
    "Enter difficulty [easy, medium, hard]: ",
    ["easy", "medium", "hard"],
)
clear_screen()

category_prompt = """Select a category from the following options:

    0: Random
    9: General Knowledge
11: ...
12: ...

Category: """
category = get_choice(category_prompt, [0, 9, 11, 12, ...], transform=int)
clear_screen()

# Maybe let the user know what's going on.
try:
    questions = get_questions_from_api(amount, difficulty, category)
except ServiceError:
    ... # Render the error for the user.
```

Note how obvious it is that I haven't completed `get_questions_from_api()` and how completing it would just be another couple of steps in the orchestration.  Also important to note is that I have tested exactly none of that so not only will it probably not work, (at one point I `return url` without defining it, for instance), it will also probably burn down your house and steal your money.
