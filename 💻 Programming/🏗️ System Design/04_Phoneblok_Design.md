# Phoneblok Design
### A Modular System Design Philosophy — for software, at the scale of billions to trillions of capabilities

---

## 0. Why This Document Exists

This document exists to answer one question precisely: **can a system be built the
way Project Ara / Phonebloks imagined a phone — fully modular, snap-together,
independently replaceable parts — and actually work, at massive scale, without
repeating Ara's failure?**

The answer, argued in full below, is: **yes, but only in software, and only if
you are disciplined about a small number of rules that Ara's physical design
could never obey.** This document is both the philosophy and the warning label.

---

## 1. The Phoneblok Story (and why it matters here)

In 2013, designer Dave Hakkens proposed Phonebloks: a phone built from a single
base board onto which independent "bloks" — camera, battery, CPU, screen — could
be snapped, swapped, and upgraded individually, like Lego. The idea was
beautiful: never throw away a whole phone again, just replace the part that's
outdated or broken. It inspired Google's Project Ara, real engineering effort,
real prototypes, and hundreds of thousands of supporters.

It never shipped as a real product. Not because the *idea* of modularity was
wrong, but because **physics punished the specific way it tried to be modular**:

| Ara's Failure | Root Physical Cause |
|---|---|
| Phone became thick, heavy, fragile | Every physical connector needs mechanical tolerance, casing, shielding — connectors have mass and volume |
| Data transfer lag between components | Signals between physically separated parts must travel real distance through real wires, with real resistance and interference |
| Parts could scatter if dropped | A physical snap-fit connector can mechanically fail under shock; there is no such thing as a connector with zero chance of disconnecting |
| RF/antenna design became a nightmare | Radios need very specific physical geometry and are highly sensitive to nearby materials — you cannot modularize this away |

Every one of these is a tax paid **because the connector between modules exists
in physical space.** This is the single most important insight this whole
philosophy rests on:

> **In software, the connector between modules has no mass, no volume, no
> mechanical tolerance, and (at the scale of a single machine) effectively no
> transmission delay. Phonebloks failed at a cost that software modularity
> does not have to pay.**

This is not a hopeful metaphor. Unix pipes, kernel modules, browser extensions,
plugin architectures, and microservice systems are all real, shipped, massively
successful examples of exactly Phonebloks' idea — "snap together independently
built and independently replaceable parts" — succeeding in software where it
failed in hardware. Phoneblok Design takes that idea seriously and pushes it to
the extreme: a system with not dozens, but potentially **billions of Bricks and
trillions of Sub-System instances**, kept sane by structure rather than by
scale-limiting itself.

---

## 2. The Core Hierarchy (Four Tiers, Not Three)

An earlier, simpler version of this philosophy used three tiers: Brick,
Sub-System, Main System. At small scale this works. At the scale this document
targets (billions/trillions), it breaks down for a specific reason: it
conflates *"the smallest unit of code"* with *"the smallest unit of product
capability."* Those are not the same thing, and treating them as the same
thing forces an artificial choice between two bad options: either every Brick
does exactly one atomic thing (leading to an explosion of trivial,
over-fragmented pieces — the software version of Ara's data-bottleneck problem)
or a Brick quietly does several unrelated things (leading back to tangled,
unmaintainable spaghetti — the exact problem the philosophy exists to prevent).

The fix is to add a fourth, more fundamental tier underneath Brick.

```
FUNCTION   →   BRICK   →   SUB-SYSTEM   →   MAIN SYSTEM
(atom)         (cohesive     (composed        (the baseplate;
               capability)    capability)      owns the event bus)
```

### 2.1 Function — the true atomic unit
The smallest unit of behavior. Does exactly one verb. Describable in one
sentence with no "and." May be:
- **Pure** — no hidden state, same input always gives same output, callable
  from anywhere, any number of times, safe to test in total isolation
  (example: `parse_duration_to_seconds("10 minutes") -> 600`).
- **Instance-bound** — operates on a specific instance's private state/handle
  (example: `camera_capture(CameraInstance *cam)` — meaningless without
  knowing *which* camera).

Functions are never registered on the event bus directly and never referenced
by anything outside their own Brick. They are implementation detail.

### 2.2 Brick — a cohesive, product-facing capability
A Brick is not defined by "does one thing" in the literal sense of one
function — it is defined by **cohesion**: every Function inside it exists to
serve one describable purpose, even if that requires many Functions to
implement well.

**The Cohesion Test (replaces any hard function-count rule):**
> Can every Function inside this Brick be described using the *same*
> one-sentence purpose, just at different steps? If yes — one Brick, however
> many Functions it takes. If you need "and" to describe what the Functions
> collectively do, you have smuggled two Bricks into one box.

A Camera Brick may reasonably contain `open()`, `set_exposure()`, `capture()`,
`autofocus()`, `close()` — five-plus Functions, one cohesive purpose. This is
correct, not a violation.

**Practical smell alarm (not a hard rule):** if a Brick's Function count
climbs past roughly 8-10 and you're struggling to state its purpose without
"and," stop and re-run the Cohesion Test. The number is a prompt to check,
never itself the law.

A Brick exposes **only** its event contract (what it subscribes to, what it
publishes) to the rest of the system. Its internal Functions are invisible
from outside. It may be a **singleton** (one instance ever, e.g. a
system-wide Event Bus) or **instantiable** (many independent instances, e.g.
a Camera Brick powering several attached camera modules at once) — this must
be a deliberate, documented choice per Brick, never an accident of how the
code happened to be written (see Section 4).

### 2.3 Sub-System — a composed capability
A Sub-System is defined **recursively**:

> A Sub-System = one or more Bricks AND/OR one or more already-built
> Sub-Systems, wired together through the event bus to deliver one
> product-facing purpose.

This recursive definition is what lets Phoneblok Design scale to trillions of
instances without inventing an arbitrary numbering scheme (no "Level 1 /
Level 2 / Level 3" bookkeeping — see Section 6 for why that path was
considered and rejected). A "Timer Core" made only of raw Bricks and a
"Smart Alarm" made of Timer Core plus a Scheduler Brick are both simply
Sub-Systems; one happens to contain the other. Depth is an emergent fact
about the dependency graph, not a category you manage by hand.

### 2.4 Main System — the baseplate
Owns the Event Bus, boots and registers Bricks and Sub-Systems, and keeps the
process alive. The Main System never contains business logic of its own —
its only job is providing the shared surface everything else snaps into.

---

## 3. The Connector Rule (unchanged, and non-negotiable at any scale)

> **No Brick or Sub-System is ever allowed to directly call into another
> Brick or Sub-System's internals. All communication happens through
> published/subscribed events on the shared bus, using shared, versioned
> event-payload definitions.**

This is the single rule most responsible for Phoneblok Design surviving to
billions of Bricks without collapsing into an unmanageable dependency web.
Every other benefit in this document (safe reuse, safe replacement, safe
parallel development, safe scaling) is downstream of this one constraint
being enforced without exception.

---

## 4. Instantiation: Definitions vs. Instances

This is the mechanism that makes large-scale reuse possible without
duplicating code — the direct fix for the "two Sub-Systems share 70-80% of
the same Bricks" problem.

- **A Definition** is the code: the .c/.h pair, the struct, the Functions.
  There is exactly **one** Definition of any given Brick or Sub-System in the
  entire codebase, forever, no matter how many times it is used.
- **An Instance** is a specific, independent, runtime allocation created
  *from* a Definition (an opaque handle, e.g. `CountdownEngine *`), with its
  own private state. Two Instances made from the same Definition share no
  memory and are mutually unaware of each other's existence.

This is intentionally **not** full object-oriented programming. It borrows
exactly one idea from OOP — "many independent objects from one blueprint" —
implemented in plain C (or any language) via the **opaque handle pattern**
(the same technique behind `FILE*`, `pthread_t`, `sqlite3*`). There is no
inheritance, no virtual dispatch, no class hierarchy, and none of the
coupling problems that usually come bundled with OOP. Just: one blueprint,
many independent copies of its runtime state.

**Why this matters at scale:** without instantiation, any Brick two
Sub-Systems both need forces a choice between (a) duplicating its code, which
at a billion-Brick scale turns "fix a bug once" into "fix a bug in an unknown
number of copies scattered across the codebase," or (b) a global singleton,
which forces every user of that Brick to fight over the same shared state
(exhibited directly in an early version of this philosophy's own reference
implementation, where a single global `TimerState` made it impossible for two
features to run independent timers at once). Instantiation is the only
option that avoids both failure modes.

### 4.1 Event Addressing (the consequence of instantiation)
Once multiple Instances of the same Brick can exist, events can no longer be
anonymous. `EVENT_TIMER_START_REQUESTED` must carry an `instance_id` (or
equivalent handle reference), and each Instance only reacts to events
addressed to it. This is a small, mechanical addition to event-payload
structs — not a redesign — but it is mandatory the moment instantiation is
introduced, and it is easy to forget until multiple Instances actually
collide in practice.

---

## 5. The Registry (how billions stay manageable)

At the scale this document targets, you are never actually managing "a
billion things." You are managing:
- However many **unique Definitions** exist in the codebase (realistically:
  thousands, not billions) — this is the number of files a human ever has
  to read, test, and fix bugs in.
- However many **Instances** are alive at runtime — this number can
  legitimately reach into the billions or trillions, but Instances are cheap,
  disposable, and never hand-maintained individually.

A **Definition Registry** — a lookup table keyed by `(brick_id, version)` —
is what makes this distinction operational rather than theoretical. It lets
the Main System (and tooling, dashboards, and future automated systems)
answer "what capabilities exist?" by listing Definitions, and "what is
currently running?" by listing Instances, without ever conflating the two.
Fixing a bug in a Definition automatically fixes every Instance made from it,
because there was only ever one copy of the logic to begin with.

---

## 6. Rejected Alternative: Numbered Levels (L1/L2/L3...)

Before settling on the recursive Sub-System definition (Section 2.3), a
numbered-tier scheme was considered: Level-1 Sub-Systems compose into Level-2
Sub-Systems, which compose into Level-3, and so on. **This was deliberately
rejected**, and it's worth recording why, since it will be tempting to
reintroduce at scale:

- Real reuse graphs are not clean pyramids — they are closer to a tangled
  directed acyclic graph (DAG). A piece shared by an "L2" system and also
  directly used by an "L4" system that skips L3 entirely breaks the
  numbering, forcing renumbering across the tree just to keep labels
  internally consistent.
- Maintaining the numbering becomes its own bureaucratic overhead — exactly
  the kind of tax the philosophy exists to eliminate.
- Depth should be an **emergent property** of the dependency graph, readable
  by walking it, not a category a human has to assign and keep consistent by
  hand across billions of nodes.

If a human-readable label is still wanted for documentation, two informal,
non-enforced tiers are usually the most that stays intuitive: **Primitive
Sub-System** (built only from raw Bricks) and **Composite Sub-System** (built
from other Sub-Systems, possibly plus a few extra Bricks). Beyond that,
everything is simply "a Sub-System," and its real depth lives in the
dependency graph, not in its name.

---

## 7. Danger Zones — Where Phoneblok Design Can Fail Exactly Like Phonebloks Did

Software does not pay Ara's *physical* costs, but it has direct software
analogs of every one of Ara's failure modes, and ignoring them will recreate
the failure in a different medium. Take these as seriously as the physical
originals.

### 7.1 The Distributed Monolith (software's "structural bulk")
Splitting a system into far more Bricks/Sub-Systems than there are genuine
reasons to split it — done for ideological purity ("more modular = always
better") rather than a real need (independent reuse, independent testing,
independent scaling). Symptoms: dozens of Bricks that all have to change
together for any single feature, meaning you've paid all the coordination
cost of modularity with none of its benefit. This is the direct software
analog of Ara's excess thickness and weight: mass added for the sake of
modularity itself, not for a benefit modularity was supposed to provide.
**Rule of thumb:** split into a new Brick only when you can name the specific
future reuse, replacement, or testing benefit — not "because it could
theoretically be separate."

### 7.2 Chatty Connectors (software's "data bottleneck")
At in-process scale (a single running binary, same machine), the event bus
connector is effectively free — nanoseconds. The instant a Sub-System's
Bricks are pulled apart across process boundaries or network boundaries
(distributed deployment, microservices, remote instances), the connector
stops being free and starts costing real milliseconds per hop, with real
failure modes (timeouts, partial failures, retries). A latency-sensitive hot
path (e.g. real-time audio processing) split too finely across network
boundaries will visibly lag — this is Ara's antenna/RF problem reborn:
certain domains genuinely do not tolerate fine-grained physical (or
network-topological) separation, no matter how philosophically appealing
that separation is.
**Rule of thumb:** keep tightly-coupled, latency-sensitive chains of Bricks
co-located (same process) unless there is a specific, named reason
(independent scaling, independent deployment, fault isolation) to separate
them across a real network boundary.

### 7.3 Silent Partial Failure (software's "parts scattering when dropped")
A physical Ara blok could mechanically disconnect. A software Brick's
equivalent failure is **initializing incorrectly and being ignored** — a
system that logs a "Warning" for a critical Brick's failure and continues
running as if nothing happened is functionally identical to a phone that
looks assembled but is missing its camera module, and gives no indication
of this to the user. This is not hypothetical — it is a bug that has already
occurred in this philosophy's own reference implementation (a transcription
engine failed to load, the system printed one easily-missed warning line,
and then announced it was "listening forever" anyway). **Rule of thumb:**
every Brick's failure mode must be explicitly classified as critical
(halt/loudly fail) or non-critical (degrade visibly) at design time — never
left as an accidental byproduct of uniform error-handling code.

### 7.4 Economic/Ecosystem Fragmentation (software's "limited blok selection")
Ara's open marketplace of third-party bloks never reached critical mass,
leaving the ecosystem thin. The software analog: a plugin/extension system
with a connector contract too unstable, too undocumented, or too
frequently-broken to attract independent contributors will suffer the same
fate — technically modular, practically empty. **Rule of thumb:** if
Phoneblok Design is ever opened to external contributors (third-party
Bricks), the event-contract stability guarantee (versioning, backward
compatibility) matters more than almost anything else in this document —
this is the software equivalent of Ara's economic feasibility problem.

### 7.5 Well-Intentioned Complexity Creep (software's "more waste, not less")
Critics warned Phonebloks could increase e-waste if constant micro-upgrades
encouraged more frequent replacement than a normal upgrade cycle would. The
software analog: infinite modularity inviting infinite, low-value variation
— thousands of near-duplicate Bricks and Sub-Systems built for marginal
personalization, none individually harmful, collectively making the system
harder to understand, secure, and maintain than a less "flexible" one would
have been. **Rule of thumb:** the existence of an easy mechanism to add a new
Brick is not, by itself, a justification for adding one. Every new
Definition added to the Registry is a permanent maintenance commitment.

---

## 8. Scale Considerations — Specifically for Billions/Trillions

This section addresses what changes, mechanically, once instance counts get
very large.

- **Definitions stay small in number; Instances do not.** Design tooling,
  dashboards, and registries around this asymmetry from day one. A system
  browsable "by Definition" (thousands of entries) remains comprehensible
  even when the live Instance graph reaches into the billions.
- **The Event Bus itself must evolve as instance count grows.** A
  single-process, mutex-protected linked-list queue (fine for hundreds of
  events per second) will not survive billions of Instances publishing
  concurrently. At this scale, the *contract* (publish/subscribe, addressed
  events, no direct calls) stays fixed while the *implementation* evolves —
  sharded queues, lock-free structures, or eventually a distributed message
  broker behind the same interface. This is the payoff of keeping the
  Connector Rule (Section 3) sacred: the entire system underneath it is free
  to be re-engineered for scale without a single Brick's code changing.
- **Instance lifecycle must be explicit and cheap.** At trillions of
  Instances, "forgot to destroy an Instance" is not a minor leak — it's a
  scaling catastrophe. Every instantiable Brick's create/destroy contract
  must be paired and enforced (reference counting, ownership rules, or an
  equivalent discipline) as a first-class part of its Definition, not an
  afterthought.
- **The Registry becomes infrastructure, not documentation.** At small
  scale, a list of Bricks in a README is sufficient. At the scale this
  document targets, the Registry must be a real, queryable system — it
  becomes the thing that answers "does a Brick like this already exist?"
  before someone accidentally creates Definition #4,001 of something
  Definition #37 already does, silently reintroducing the exact duplication
  problem instantiation was meant to solve.

---

## 9. Further Improvements (open directions, not yet solved here)

- **Automated cohesion checking.** The Cohesion Test (Section 2.2) is
  currently a human judgment call. At Registry scale, tooling that flags
  Bricks whose Functions statistically diverge in purpose (e.g., by
  analyzing what event types a Function's code path touches) could catch
  drift before a human notices.
  
- **Formal event-contract versioning.** This document assumes versioned
  event payloads but does not yet define a compatibility policy (can a v2
  event payload ever break a v1 subscriber?). This needs the same rigor
  major API-design systems (e.g. protobuf, OpenAPI) apply to schema
  evolution, adapted to an event-bus context.

- **Discoverable capability negotiation.** At true ecosystem scale (Section
  7.4), Instances may need to query the Registry at runtime to discover
  whether a needed capability exists before assuming it does — moving from
  a fully static, compile-time-known Brick set toward a dynamically
  discoverable one, closer to how Project Ara imagined its Blokstore.

- **Fault isolation boundaries.** Section 7.3's "silent partial failure"
  problem is addressed here only at the level of "classify failures as
  critical/non-critical." A more complete answer borrows from supervisor-tree
  patterns (as in Erlang/OTP) — where a Sub-System can automatically
  restart a failed Instance of one of its Bricks without the whole system
  going down, and without silently pretending nothing happened either.

- **Cross-machine instantiation.** This document mostly assumes Instances
  live within a single machine/process. A mature version of Phoneblok Design
  at true trillions-scale will need a clear answer for what changes when an
  Instance's Definition runs on a different machine than the Sub-System that
  owns it — this is where the Connector Rule gets tested hardest (Section
  7.2), and where the philosophy has the most work left to do.

---

## 10. One-Paragraph Summary

Phoneblok Design takes Project Ara's dream — a system built from independent,
snap-together, individually replaceable modules — and applies it to software,
where the physical costs that killed Ara (mass, signal distance, mechanical
fragility) mostly don't exist. It replaces Ara's single "blok" concept with
four honest tiers (Function, Brick, Sub-System, Main System), makes Bricks
instantiable rather than singleton so the same Definition can be reused
without duplication, keeps a strict Connector Rule so nothing is ever
tangled by direct dependency, and tracks scale through a Definition/Instance
split rather than pretending billions of things can each be reasoned about
individually. Its real dangers are not physical but organizational — and
every one of them has a direct, nameable analog in exactly what made
Phonebloks fail in hardware.
