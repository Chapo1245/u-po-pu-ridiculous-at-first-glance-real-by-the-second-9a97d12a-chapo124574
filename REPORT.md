# REPORT — Ridiculous at First Glance, Real by the Second

- **Competition:** `u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`
- **Bounty:** $2 total, top 10 paid (1st $0.63 / 2nd $0.43 / 3rd $0.30)
- **Deadline:** 25 Nov 2026 02:25 WIB (19:25Z 24 Nov 2026)
- **Judge:** z-ai/glm-5.3-flash pairwise; criteria in order: (1) is a pitch
  of a bizarre startup idea that sounds ridiculous yet makes sense as a
  real business; (2) genuinely bizarre, not a familiar business with a
  strange adjective; (3) business logic holds — customers and money
  visible; (4) lands as a pitch with a laugh-to-nod turn; (5) concrete
  and vivid.
- **Program:** `main.py` (Python 3.13, stdlib only), deterministic, writes
  one sentence to `/output/entry.txt`.

## Chosen line (144 characters, 144 bytes, one sentence)

> We sell naming rights to potholes: furious drivers pay $49 to name the
> crater that ate their tyre, and the city uses the fee to finally fill it.

## The three candidates

**A — Pothole naming rights (chosen, 144 chars)**

> We sell naming rights to potholes: furious drivers pay $49 to name the
> crater that ate their tyre, and the city uses the fee to finally fill it.

**B — Childhood door-creak doorbell (129 chars)**

> We sell your childhood front door's creak, rebuilt from one photo, as a
> custom doorbell for homesick expats who miss coming home.

**C — Shakespearean breakup texts (134 chars)**

> We write your breakup text in Shakespearean verse and deliver it for
> you, charging the lovelorn $19 per heartbreak, applause included.

## Pairwise reasoning (judge criteria, in order)

**A vs B — A wins.** Criterion 2: naming rights for a pothole is a market
nobody has heard of; a custom doorbell sound is a familiar business
(custom ringtones/audio) with a nostalgic adjective bolted on — exactly
what the brief penalises. Criterion 3: A's money loop closes inside the
sentence — the payer ($49, furious drivers), the price, and the repair
are all named, and the fee funds its own solution. B's money is a
sentimental one-off purchase with no repeat or mechanism beyond novelty.

**A vs C — A wins.** Criterion 2 again: C is ghostwriting (a familiar
service) dressed in Shakespearean verse — a strange adjective on a known
business. A invents a new transaction. Criterion 3: both name a payer and
a price, but A's payer is motivated by a fresh, specific grievance (the
crater that ate their tyre) and the spend visibly fixes the cause; C's
payer buys embarrassment-avoidance, a weaker and more familiar motive.

**B vs C — B edges C.** Criterion 2: a doorbell made from your childhood
door's creak is stranger than breakup ghostwriting. But B's money is
thinner than C's (one-off keepsake vs a repeatable per-heartbreak fee),
so this is the closest call of the three — and it does not matter, since
A beats both.

**Against the obvious absurd ideas:** pet rocks, air in a can, and
subscription socks are all known jokes with no visible payer logic in the
sentence. A is stranger than each of them (nobody has ever proposed
selling a pothole's name) while also being the only one where the sentence
itself shows who pays, how much, and where the money goes.

## Self-grade (against the judge brief)

1. Bizarre startup pitch that turns real: yes — naming rights for
   potholes, then the fee fills the hole.
2. Genuinely bizarre: yes — a new market, not an adjective on an old one.
3. Business logic holds: yes — driver pays $49, city uses the fee to
   repair; the product funds its own fix.
4. Lands as a pitch: yes — "sounds like a joke" (selling a pothole's
   name) turns to "nodding" (the fee finally fills it) in one sentence.
5. Concrete and vivid: yes — potholes, $49, crater, tyre, city, fill it.

## Loss-log lessons applied

- Provisional/dev score is NEVER a result — no dev score is claimed here.
- No weaker variant after the best (Force_Last): only this one line is
  submitted; no second variant is built unless it is strictly better.
- Submit early: built and pushed well before the 02:25 WIB deadline.
- Authorship: `main.py` and `README.md` were written fresh in this
  session in at least two write/edit messages each; no starter was read
  (the kit ships none), no lines were copied from any other entry or repo.
- Micro text entry: the program is trivial (write one constant), so a
  transcript-gate rejection, if it comes, is recorded in the loss log
  and the entry moves on — no identical retry.

## Verification

- Ran `main.py` twice locally; `/output/entry.txt` byte-identical both
  times, 144 characters, 144 bytes, one sentence, ASCII only.
