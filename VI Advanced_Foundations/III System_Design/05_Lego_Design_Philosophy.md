# The Lego Philosophy of ROSE
### My personal design pattern for building modular AI systems

---

## 1. Why Lego?

I don't want to build software the traditional way, where everything is
tangled together and touching one thing breaks ten others. I want to build
it the way a child builds with Lego bricks — small, simple, standardized
pieces that snap together to create something enormous, and can be pulled
apart, replaced, or expanded without breaking the rest of the build.

This document is **my** vocabulary for my system. It's how I personally
think about the architecture, in my own words, so that a year from now —
or when this system has a billion parts — I can still open this file and
instantly remember *why* everything is shaped the way it is.

---

## 2. The Three Levels of My World

### 🧱 The Lego Brick
> The smallest, simplest, single-purpose piece.

A Lego Brick does **exactly one job** and nothing more. It doesn't know or
care what the rest of the system is doing. It just does its one small task
really well, and passes on the result.

Examples in my current build:
- A brick that **only listens** to the microphone.
- A brick that **only turns sound into text**.
- A brick that **only checks if the word "Rose" was said**.
- A brick that **only plays a tone**.

A brick should be so small and so focused that if I forgot what the whole
system was for, I could still look at one brick alone and understand its
entire job in one sentence.

**Rule of a Brick:** *If you can't describe what it does in one short
sentence, it's not a brick — it's secretly two bricks glued together.
Split it.*

---

### 🏗️ The Sub-System
> A small structure built out of a handful of bricks, snapped together to
> perform one complete feature.

A single brick alone can't "start a 10-minute timer." But a few bricks,
connected together in the right order, can. That connected group is a
**Sub-System** — like building a small Lego car out of wheels, an axle,
and a chassis. None of those pieces alone is a car. Together, they are.

My first Sub-System: **The Timer Sub-System**
- Brick: Duration Parser (turns "10 minutes" into 600 seconds)
- Brick: Countdown Engine (counts down from 600 to 0)
- Brick: Tone Player (rings when it hits 0)

Three simple bricks. One complete feature. That's a Sub-System.

**Rule of a Sub-System:** *A Sub-System should be removable as a whole
unit. If I deleted the entire Timer Sub-System folder, the rest of Rose
should not even notice — it should just no longer be able to run timers.*

---

### 🏙️ The Main System — ROSE
> The baseplate. The city. The whole build that every brick and every
> sub-system ultimately connects to.

Rose is not "a brick" and not "a sub-system." Rose is the **foundation**
— the thing that:
- Wakes everything up when the program starts.
- Gives every brick a place to snap into (a shared connector language).
- Listens for the word **"Rose"** as the signal that means "pay attention,
  something is about to be asked of you."
- Keeps running forever, patiently, in the background, ready for the next
  Sub-System to be triggered.

Rose herself doesn't know how to run a timer, transcribe speech, or play a
tone. She doesn't need to. She just knows how to **hold everything
together** and pass messages between the bricks that do know how.

---

## 3. The Connector Rule (How Bricks Snap Together)

Real Lego bricks all share the same stud size, no matter who made them or
what they look like. That's *why* they can connect to anything.

My bricks need the same thing. Every brick — no matter what it does —
must speak the same "connector language":

- It must be able to **start up** the same way.
- It must be able to **shut down** the same way.
- It must talk to the rest of the system only through **shared messages**
  (events), never by reaching directly into another brick's insides.

This is the single most important promise in my whole design:

> **No brick is allowed to directly touch another brick.**
> **They only ever pass messages through the shared connector (the Event
> Bus).**

This is what lets me eventually have a *billion* bricks without the
system collapsing under its own complexity — because no brick ever needs
to know about any other brick. It only needs to know how to snap into the
baseplate.

---

## 4. Why This Matters For "Billions of Bricks" Later

A pile of a hundred Lego bricks is easy to manage. A pile of a billion
bricks, connected randomly and directly to each other, would be
impossible to build or fix.

But a billion Lego bricks that **all use the same connector standard**,
organized into clearly labeled Sub-Systems, sitting on one baseplate
(Rose) — that's not chaos. That's a city. That's buildable, one small
piece at a time, forever.

So my rule for the future is simple:

> **Every new capability I ever add to Rose — no matter how big or small
> — must be expressible as one or more Bricks, assembled into a
> Sub-System, connected to Rose through the same standard connector.**

If a new idea doesn't fit that shape, I don't add it directly — I first
figure out how to break it down until it *does* fit that shape. That's the
discipline that keeps this buildable at any size.

---

## 5. My Current Build (Milestone 1)

```
ROSE (baseplate)
 │
 ├── Always-On Bricks
 │     ├── 🧱 Ear Brick            (listens to the mic, forever)
 │     ├── 🧱 Transcriber Brick    (turns sound into text)
 │     ├── 🧱 Wake-Word Brick      (listens for "Rose")
 │     └── 🧱 Command Brick        (figures out what was asked)
 │
 └── Timer Sub-System (my first sub-system)
       ├── 🧱 Duration Brick       ("10 minutes" → 600 seconds)
       ├── 🧱 Countdown Brick      (counts down to zero)
       └── 🧱 Tone Brick           (rings when done)
```

When I say:

> **"Rose, start timer of 10 minutes."**

Here's the story, in my own words:
1. The **Ear Brick** hears my voice, like always.
2. The **Transcriber Brick** turns it into text.
3. The **Wake-Word Brick** notices "Rose" was said and perks up.
4. The **Command Brick** reads the rest — "start timer of 10 minutes" —
   and understands it's a Timer request.
5. It hands the number "10 minutes" to the **Duration Brick**, which
   turns it into 600 seconds.
6. The **Countdown Brick** starts silently ticking down from 600.
7. When it hits zero, it tells the **Tone Brick**: *"you're up."*
8. The **Tone Brick** rings.
9. Rose goes right back to quietly listening, waiting to hear her name
   again.

No thinking. No AI. Just clean, small, honest pieces of logic — each one
doing its one job, passed hand to hand like a bucket brigade — exactly
like a Lego build growing one brick at a time.

---

## 6. A Personal Reminder to Future Me

- Keep every brick small enough to explain to a stranger in one sentence.
- Never let two bricks talk to each other directly — always through Rose's
  shared connector.
- A Sub-System is done when it can be deleted entirely without confusing
  anything else in the system.
- Whenever this feels complicated, it means I've stopped following the
  rules above — go back to smaller bricks.
- This system is allowed to grow into something enormous. It is not
  allowed to grow into something tangled.

**Rose starts as a timer. Rose can become anything — one brick at a
time.**
