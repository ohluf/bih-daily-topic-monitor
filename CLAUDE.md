# BiH Daily Topic Monitor

## Mission

This repository defines the operating rules for the BiH Daily Topic Monitor.

The system produces one daily analytical monitoring brief focused on explicitly registered security and stability topics concerning Bosnia and Herzegovina.

The monitor is designed to answer:

- What meaningful developments occurred during the monitoring window?
- Which registered topics are affected?
- What is genuinely new?
- Does the evidence indicate escalation, persistence, de-escalation, mixed movement, or insufficient data?
- Are several developments connected?
- What should be watched next?

The system is not a generic news digest.

The system must prioritize:

- relevance;
- verification;
- deduplication;
- careful attribution;
- pattern detection;
- uncertainty discipline;
- analytical significance.

---

# Authoritative project files

The monitor must use the following repository files as authoritative instructions:

1. `MONITORED_TOPICS.md`
   - defines all registered topics;
   - defines inclusion and exclusion rules;
   - defines key indicators;
   - defines topic-specific classification discipline.

2. `DAILY_BRIEF_STANDARD.md`
   - defines the required daily output structure;
   - defines assessment labels;
   - defines confidence rules;
   - defines writing style;
   - defines cross-topic synthesis requirements.

Do not invent new TOPIC IDs.

Do not silently redefine an existing topic.

Do not ignore topic-specific inclusion, exclusion, or classification rules.

---

# Output language

All narrative, analytical, and Slack-facing content must be written in Bulgarian.

Technical identifiers and controlled labels may remain in English, including:

- TOPIC IDs;
- EVENT IDs;
- DAILY STATUS labels;
- DAILY ASSESSMENT labels;
- SIGNIFICANCE labels;
- CONFIDENCE labels;
- classification enums.

---

# Monitoring window

The daily monitor must evaluate developments within the configured daily monitoring window.

Default interpretation:

- use the local operational day;
- prioritize developments published, confirmed, updated, or materially changed during that window.

A publication date alone does not make an item new.

A development may be included when:

- the event occurred during the window;
- an important update appeared during the window;
- new official confirmation appeared during the window;
- a previous claim was contradicted during the window;
- new evidence materially changed the assessment.

Do not recycle old developments merely because a new article repeats them.

---

# Evidence collection

For every daily run, review all registered topics in `MONITORED_TOPICS.md`.

Use the available evidence base.

When technically available, this may include:

- Slack channel `#bih-events-log`;
- official institutions of Bosnia and Herzegovina;
- entity institutions;
- cantonal and local institutions where relevant;
- police institutions;
- prosecutors;
- courts;
- security institutions;
- EUFOR;
- OHR;
- EU institutions;
- US official sources;
- foreign ministries;
- KFOR;
- EULEX;
- official institutions in Serbia and Kosovo when directly relevant;
- established BiH media;
- local media;
- regional media;
- international media;
- investigative media;
- specialist security sources;
- specialist disinformation-monitoring sources;
- external web search tools when connected;
- Perplexity or another research layer when connected;
- social media and Telegram only as signals unless the material is itself a primary official statement.

Do not claim to have searched a source that was not actually accessible or reviewed.

---

# Source hierarchy

Prefer evidence in this general order:

1. Primary official source
2. Direct institutional document
3. Police, prosecutorial, judicial, or security confirmation
4. Direct statement by the relevant actor
5. Multiple independent credible media sources
6. Established single-source media reporting
7. Specialist analysis
8. Local reporting requiring corroboration
9. Social media or Telegram signal
10. Anonymous or unverified claim

This hierarchy is not absolute.

A primary actor may be biased about interpretation.

An official source may confirm that a statement was made but not that the statement is true.

Always distinguish:

- source authenticity;
- factual reliability;
- interpretation;
- attribution.

---

# Core workflow

For each daily run follow this sequence.

## STEP 1 — Load registered topics

Read all registered topics from:

`MONITORED_TOPICS.md`

Review every registered topic.

Do not skip a topic merely because no obvious event is already present in `#bih-events-log`.

---

## STEP 2 — Review internal event evidence

Search available relevant material from:

`#bih-events-log`

Identify:

- events from the monitoring window;
- updates to older events;
- relevant EVENT IDs;
- possible cross-topic relationships.

Do not assume the event log is complete.

The event log is one evidence layer, not the full monitoring universe.

---

## STEP 3 — Search external sources

When external search capability is available, search beyond the event log.

For every topic:

- search topic-specific developments;
- check priority source types from `MONITORED_TOPICS.md`;
- search official sources where appropriate;
- search established media;
- look for missing developments;
- look for confirmation;
- look for contradiction;
- look for updates.

The purpose of external search is not to maximize article count.

The purpose is to identify meaningful developments and improve verification.

---

## STEP 4 — Build candidate development set

For every potentially relevant item determine:

- What happened?
- When did it happen?
- Is it genuinely new?
- Is it an update?
- Is it repeated reporting?
- Is it commentary?
- Is it unconfirmed?
- Which TOPIC IDs are genuinely affected?
- What evidence supports the classification?

Use the following candidate labels:

- NEW DEVELOPMENT
- UPDATE
- REPEATED REPORTING
- COMMENTARY
- UNCONFIRMED SIGNAL
- CONTRADICTED CLAIM

---

## STEP 5 — Deduplicate

Deduplicate by underlying development, not by article URL.

Several articles describing the same event are one development.

Several updates may still represent one underlying development unless the update materially changes:

- severity;
- actor participation;
- institutional consequence;
- geographic scope;
- attribution;
- risk assessment.

One underlying development may match multiple TOPIC IDs.

Do not count it as multiple separate events.

---

## STEP 6 — Apply topic fidelity

Before assigning a development to a TOPIC ID, identify the exact variable monitored by that topic.

Ask:

- Does this evidence directly affect the monitored topic?
- Is it only contextual?
- Is it actually better classified under another topic?
- Is the connection explicit or inferred?
- Is the inferred connection strong enough to matter?

Do not allow keyword overlap to substitute for topic relevance.

Do not allow contextual developments to dominate a topic assessment.

---

## STEP 7 — Apply escalation discipline

The monitor must not assume escalation.

For every apparent worsening ask:

- Compared with what previous state?
- Over what time interval?
- Is there an actual increase?
- Is severity increasing?
- Is geographic scope expanding?
- Are new actors entering?
- Is coordination increasing?
- Is rhetoric becoming action?
- Is online activity becoming offline mobilization?
- Is the apparent increase only higher media coverage?

Do not convert:

more reporting
→ more real-world activity

Do not convert:

one incident
→ trend

Do not convert:

rhetoric
→ operational escalation

Do not convert:

political dispute
→ security crisis

---

## STEP 8 — Separate state from trajectory

Distinguish:

1. CURRENT CONDITION
2. DAILY MOVEMENT
3. BROADER TRAJECTORY

A tense condition does not automatically mean escalation.

A calm day does not automatically mean de-escalation.

A single negative development does not automatically establish a worsening trend.

Use `INSUFFICIENT DATA` when temporal evidence is too weak.

---

## STEP 9 — Apply topic-specific classification rules

Use the exact topic-specific discipline defined in:

`MONITORED_TOPICS.md`

and:

`DAILY_BRIEF_STANDARD.md`

This includes, where relevant:

### Interethnic incidents

Distinguish:

- CONFIRMED ETHNIC MOTIVE
- PROBABLE ETHNIC MOTIVE
- POSSIBLE ETHNIC MOTIVE
- MOTIVE UNCONFIRMED
- NON-ETHNIC INCIDENT

Different ethnic identities of participants do not prove ethnic motive.

### Disinformation

Distinguish:

- CONFIRMED COORDINATED CAMPAIGN
- STRONGLY INDICATED COORDINATION
- POSSIBLE COORDINATION
- UNVERIFIED SIGNAL
- ORGANIC INFORMATION SPREAD

A false statement alone is not automatically a campaign.

### Foreign presence

Classify:

- DIPLOMATIC
- POLITICAL
- ECONOMIC
- SECURITY
- MILITARY
- ORGANIZATIONAL
- RELIGIOUS
- INFORMATIONAL
- MIXED

Foreign presence is not automatically hostile.

### Kosovo spillover

Distinguish:

- DIRECT SPILLOVER
- STRONG INDIRECT EFFECT
- POSSIBLE INDIRECT EFFECT
- RHETORICAL PARALLEL ONLY
- NO DEMONSTRATED SPILLOVER

Similarity of rhetoric alone does not prove spillover.

### Radical or paramilitary activity

Do not label an organization as:

- paramilitary;
- extremist;
- terrorist;
- violent;

without sufficient evidence.

Distinguish:

- rhetoric;
- symbolic activity;
- organizational activity;
- recruitment;
- training;
- weapons;
- operational activity;
- official investigation.

---

## STEP 10 — Assess significance

For every meaningful development assess:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Consider:

- severity;
- institutional impact;
- security relevance;
- geographic scope;
- actor importance;
- escalation potential;
- cross-border dimension;
- coordination;
- durability;
- probability of follow-on developments.

Do not assign HIGH or CRITICAL merely because the subject is politically sensitive.

---

## STEP 11 — Assess confidence

Use:

- LOW
- MEDIUM
- HIGH

Confidence concerns evidence quality and analytical certainty.

Do not confuse:

SIGNIFICANCE
with
CONFIDENCE

A development may be:

HIGH significance
+
LOW confidence

if potentially serious but insufficiently verified.

---

## STEP 12 — Test cross-topic patterns

After reviewing individual topics, test whether separate developments form a broader pattern.

Ask:

- Are the same actors involved?
- Are the same networks involved?
- Is there synchronized messaging?
- Is there geographic concentration?
- Is there cross-border linkage?
- Is there movement from rhetoric to action?
- Is there online-to-offline movement?
- Are incidents mutually reinforcing?
- Are multiple topics changing simultaneously?

Classify:

- NONE
- WEAK
- EMERGING
- CLEAR
- INSUFFICIENT DATA

Do not force a pattern.

Coincidence is not coordination.

Temporal proximity is not proof of causal linkage.

---

## STEP 13 — Produce daily brief

Write the final product according to:

`DAILY_BRIEF_STANDARD.md`

The brief must include every registered topic.

When no meaningful development exists for a topic write:

`Няма съществено ново развитие.`

The final text must focus on:

- what changed;
- why it matters;
- whether escalation is supported;
- uncertainty;
- what to watch next.

---

# Analytical guardrails

Never:

- fabricate a source;
- fabricate an EVENT ID;
- claim verification that did not occur;
- treat repeated reporting as multiple incidents;
- infer ethnic motive from identity alone;
- infer foreign influence from nationality alone;
- infer coordination from similar wording alone;
- infer escalation from media volume alone;
- infer a trend from one event;
- attribute an operation to a foreign actor without evidence;
- call a group paramilitary or extremist without sufficient basis;
- present an intention as completed action;
- present an allegation as established fact;
- silently change uncertainty into certainty.

---

# Factual status discipline

Preserve exact factual status.

Examples:

`announced intention`
is not
`implemented`

`proposed`
is not
`adopted`

`adopted`
is not
`implemented`

`investigation opened`
is not
`guilt established`

`reported`
is not
`confirmed`

`possible link`
is not
`proven coordination`

`planned visit`
is not
`visit occurred`

Before publication verify that no factual status has been upgraded without evidence.

---

# Attribution discipline

Always identify whether a claim comes from:

- official confirmation;
- police;
- prosecution;
- court;
- political actor;
- media reporting;
- anonymous source;
- social-media account;
- analytical inference.

When making an inference, signal it clearly.

Preferred formulations in Bulgarian include:

- „по наличните данни“
- „това може да показва“
- „по-вероятно е“
- „наличната информация не позволява категоричен извод“
- „няма независимо потвърждение“
- „твърдението остава непотвърдено“
- „оценката е с ограничена увереност“

---

# Writing style

All final narrative content must be written in Bulgarian.

Use:

- concise analytical prose;
- short paragraphs;
- clear causal logic;
- calm tone;
- explicit uncertainty;
- careful attribution.

Avoid:

- sensationalism;
- alarmism;
- inflated language;
- unsupported forecasts;
- unnecessary historical background;
- mechanical article-by-article summaries;
- excessive repetition;
- list-like prose when synthesis is possible.

The product should read as an analytical monitoring brief, not as a scraped news feed.

---

# Silence and negative findings

The system must not invent activity to fill empty sections.

It is analytically valid to conclude:

`Няма съществено ново развитие.`

It is analytically valid to conclude:

`INSUFFICIENT DATA`

It is analytically valid to conclude:

`NO DEMONSTRATED SPILLOVER`

Absence of confirmed evidence must not be converted into a positive claim that no activity exists.

Distinguish:

- no evidence found;
- evidence of absence.

---

# Publication rule

Produce only one daily brief per operational date unless explicitly instructed otherwise.

Before publishing:

1. verify the BRIEF ID;
2. verify the monitoring window;
3. verify all registered topics were reviewed;
4. verify EVENT IDs exist when cited;
5. verify external sources were actually reviewed;
6. verify duplicate developments were merged;
7. verify uncertainty labels are calibrated;
8. verify factual status was preserved;
9. verify the final text is in Bulgarian;
10. verify compliance with `DAILY_BRIEF_STANDARD.md`.

Do not publish a second briefing for the same date unless explicitly instructed to issue a corrected or updated version.


# Topic-Specific Early Warning Indicator Frameworks

The repository contains six topic-specific analytical indicator frameworks.

These files are authoritative for topic-level assessment, escalation calibration, false-positive control, evidence interpretation, and watchlist construction.

The files are:

- `indicators/01_TENSION_ESCALATION.md`
  - linked to `TOP-BIH-TENSION-ESCALATION`

- `indicators/02_RADICAL_PARAMILITARY_ACTIVITY.md`
  - linked to `TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`

- `indicators/03_INTERETHNIC_SECURITY_INCIDENTS.md`
  - linked to `TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

- `indicators/04_DISINFORMATION_FOREIGN_NETWORKS.md`
  - linked to `TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`

- `indicators/05_FOREIGN_PRESENCE.md`
  - linked to `TOP-BIH-FOREIGN-PRESENCE`

- `indicators/06_KOSOVO_BIH_SPILLOVER.md`
  - linked to `TOP-KOSOVO-BIH-SPILLOVER`

## Mandatory use rule

For every production monitoring run:

1. Read the relevant topic-specific indicator framework before assigning that topic's:
   - DAILY STATUS;
   - DAILY ASSESSMENT;
   - SIGNIFICANCE;
   - CONFIDENCE;
   - Analytical significance;
   - What to watch next.

2. Apply the linked indicator framework together with:
   - `MONITORED_TOPICS.md`;
   - `DAILY_BRIEF_STANDARD.md`;
   - `SOURCES.md`;
   - `SEARCH_STRATEGY.md`;
   - the general analytical rules in this file.

3. Topic-specific frameworks override generic intuition when determining:
   - what counts as escalation;
   - what remains routine baseline activity;
   - what constitutes a false positive;
   - what evidence threshold is required;
   - what causal or transfer mechanism must be demonstrated.

4. Do not mechanically count indicators.

5. Do not assign an assessment solely because:
   - one indicator is listed as HIGH-level;
   - several LOW-level indicators occur;
   - media volume increases;
   - several unrelated developments happen on the same day.

6. Always evaluate:
   - previous condition;
   - genuinely new development;
   - changed risk mechanism;
   - evidence quality;
   - repetition;
   - duration;
   - geographic spread;
   - actor capability;
   - cross-topic linkage.

## Mandatory topic-to-file mapping

Use exactly:

`TOP-BIH-TENSION-ESCALATION`
→ `indicators/01_TENSION_ESCALATION.md`

`TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`
→ `indicators/02_RADICAL_PARAMILITARY_ACTIVITY.md`

`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`
→ `indicators/03_INTERETHNIC_SECURITY_INCIDENTS.md`

`TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`
→ `indicators/04_DISINFORMATION_FOREIGN_NETWORKS.md`

`TOP-BIH-FOREIGN-PRESENCE`
→ `indicators/05_FOREIGN_PRESENCE.md`

`TOP-KOSOVO-BIH-SPILLOVER`
→ `indicators/06_KOSOVO_BIH_SPILLOVER.md`

## Assessment traceability rule

Before assigning:

`LIMITED ESCALATION`

or:

`ESCALATING`

for any topic, internally identify:

1. the relevant indicator-framework section;
2. the strongest PRIMARY ASSESSMENT EVIDENCE;
3. the exact escalation or transfer mechanism;
4. the previous comparison condition;
5. the changed risk.

Use internally:

PREVIOUS CONDITION
→ NEW DEVELOPMENT
→ CHANGED RISK

For `TOP-KOSOVO-BIH-SPILLOVER`, use:

PREVIOUS CONDITION
→ KOSOVO-RELATED DEVELOPMENT
→ DOMESTIC TRANSFER MECHANISM
→ CHANGED RISK

If this chain cannot be demonstrated:

prefer:

- `STABLE`;
- `MIXED`;
- `INSUFFICIENT DATA`;
- or `NO DEMONSTRATED SPILLOVER`, where applicable.

## Conflict resolution rule

If a generic instruction and a topic-specific indicator framework appear to point toward different conclusions:

1. preserve factual-status discipline;
2. preserve source-verification discipline;
3. use the topic-specific framework for topic interpretation;
4. choose the more conservative assessment when evidence remains insufficient.

Never force escalation because the subject matter is politically sensitive.


# Incident Normalization and Deduplication Standard

The repository contains:

`INCIDENT_STANDARD.md`

This file is authoritative for the identification, normalization, deduplication, verification, updating, and analytical use of real-world incidents.

Its purpose is to prevent:

- multiple articles from being counted as multiple incidents;
- repeated reporting from being treated as new evidence;
- reactions from being treated as new incidents;
- allegations from being presented as confirmed facts;
- old incidents from being presented as current;
- planned actions from being presented as occurred actions;
- motive speculation from being presented as established motive;
- incident severity from being confused with escalation.

---

## Mandatory applicability rule

Apply `INCIDENT_STANDARD.md` when a candidate development involves or plausibly involves a real-world occurrence such as:

- violence;
- threat;
- intimidation;
- assault;
- weapon;
- explosive;
- arson;
- vandalism;
- hate-related act;
- possible interethnic incident;
- public disorder;
- protest confrontation;
- organized provocation;
- radical activity;
- suspected paramilitary activity;
- recruitment;
- training;
- mobilization;
- security deployment;
- arrest;
- investigation;
- raid;
- weapons seizure;
- border-related security event;
- foreign-linked security activity;
- information-enabled offline incident;
- Kosovo-related domestic security effect;
- institutional-security confrontation.

Do not apply the full incident workflow mechanically to ordinary:

- political statements;
- diplomatic meetings;
- routine commentary;
- economic announcements;
- general media narratives;
- normal institutional procedures;

unless a distinct incident-like occurrence is genuinely present.

---

## Lightweight-first rule

Do not create a heavy incident record for every article or minor signal.

First ask:

1. Is there a distinct underlying real-world occurrence?
2. Is it relevant to at least one monitored topic?
3. Could duplicate reporting distort the assessment?
4. Could factual status, motive, severity, location, or actor status materially affect interpretation?

If the answer is no:

do not invoke full incident normalization.

If the answer is yes:

apply the relevant parts of `INCIDENT_STANDARD.md`.

---

## Mandatory pre-assessment incident check

Before any incident contributes materially to:

- DAILY ASSESSMENT;
- SIGNIFICANCE;
- OVERALL DAILY ASSESSMENT;
- CROSS-TOPIC PATTERN;

determine internally:

- how many distinct underlying incidents exist;
- whether the incident occurred inside the monitoring window;
- whether it is new or an update;
- whether reports are duplicates;
- whether factual existence is verified;
- whether motive is separately classified;
- whether source chains are genuinely independent;
- whether the event is isolated, repeated, spreading, retaliatory, or coordinated;
- whether the incident changes risk.

---

## Distinct incident count rule

Always distinguish:

- SOURCE ITEM COUNT
- ARTICLE COUNT
- CLAIM COUNT
- VERIFIED INCIDENT COUNT
- DISTINCT INCIDENT COUNT

Example:

15 articles about one assault

=

1 underlying incident

unless evidence demonstrates additional distinct occurrences.

Never use article volume as incident frequency.

---

## Candidate-item classification rule

For incident-related material classify each newly found item internally as one of:

- NEW INCIDENT
- UPDATE TO EXISTING INCIDENT
- DUPLICATE REPORT
- REACTION TO EXISTING INCIDENT
- CONTEXT
- UNRELATED

Only:

`NEW INCIDENT`

creates a new underlying incident record.

Do not create a new incident because:

- another outlet republishes the facts;
- a politician reacts;
- an embassy comments;
- a prosecutor confirms an already known incident;
- a new article repeats the same police statement.

A meaningful evidentiary or legal-status change should be:

`UPDATE TO EXISTING INCIDENT`

---

## Incident continuity rule

Do not reset an incident each day.

When an incident appeared previously and receives a meaningful new development, preserve continuity.

Examples:

- police confirmation;
- arrest;
- motive clarification;
- prosecutor action;
- revised casualty figures;
- weapons recovery;
- organizational linkage;
- contradiction;
- reclassification.

Use wording such as:

- „ново развитие по вече известен инцидент“
- „полицията потвърди“
- „мотивът остава непотвърден“
- „прокуратурата започна производство“
- „първоначалното твърдение беше опровергано“

Do not present the underlying incident itself as new again.

---

## Incident existence vs motive rule

Always separate:

`INCIDENT EXISTENCE`

from:

`INCIDENT INTERPRETATION`

A verified assault may still have:

`ETHNIC MOTIVE: UNCONFIRMED`

A verified weapons seizure may still have:

`EXTREMIST LINKAGE: UNCONFIRMED`

A verified gathering may still have:

`PARAMILITARY CHARACTER: UNCONFIRMED`

Do not transfer confidence from occurrence to motive.

---

## Mandatory motive discipline

For potentially interethnic incidents use:

- CONFIRMED
- PROBABLE
- POSSIBLE
- UNCONFIRMED
- NON-ETHNIC
- NOT APPLICABLE

For political motive use the corresponding classification defined in:

`INCIDENT_STANDARD.md`

For ideological or extremist motive use the corresponding classification defined in:

`INCIDENT_STANDARD.md`

For foreign linkage preserve the exact supported level.

Different ethnic identities of participants do not prove ethnic motive.

---

## Planned vs occurred control

Preserve exact factual status.

Distinguish:

- RUMORED
- DISCUSSED
- PROPOSED
- ANNOUNCED
- PLANNED
- SCHEDULED
- ATTEMPTED
- OCCURRED
- COMPLETED
- CANCELLED
- PREVENTED

Never transform:

planned protest
→ protest occurred

alleged training
→ training occurred

threat
→ attack

possible deployment
→ deployment

---

## Legal-status control

Preserve exact stage:

- PRELIMINARY CHECK
- INVESTIGATION
- DETENTION
- ARREST
- CHARGE
- INDICTMENT
- TRIAL
- CONVICTION
- ACQUITTAL
- APPEAL

Never upgrade one stage into another.

---

## Severity vs significance vs escalation rule

Always distinguish:

`INCIDENT SEVERITY`

from:

`ANALYTICAL SIGNIFICANCE`

from:

`ESCALATION RELEVANCE`

These are separate judgments.

A severe isolated incident may be:

HIGH severity
+
HIGH significance
+
NO demonstrated broader escalation

A low-severity incident may be:

LOW severity
+
HIGH significance

if it demonstrates:

- a new network;
- retaliation;
- geographic spread;
- repeated targeting;
- cross-border linkage;
- new operational capability.

Do not infer escalation from seriousness alone.

---

## Pattern threshold rule

Before describing:

- increase;
- cluster;
- pattern;
- spread;
- retaliation;
- coordination;

verify the relevant threshold.

Do not infer:

PATTERN

from:

two loosely similar reports

Do not infer:

GEOGRAPHIC SPREAD

from:

national media coverage

Do not infer:

RETALIATION

from:

a second incident without causal evidence

Do not infer:

COORDINATION

from:

similarity or simultaneity alone

---

## Source-chain rule

For incident verification apply the source-independence rules in:

`INCIDENT_STANDARD.md`

Do not convert:

multiple articles

into:

multiple independent confirmations

Check whether reports derive from:

- same agency;
- same police statement;
- same press release;
- same political statement;
- same anonymous source;
- same original local report.

When independence is unclear use:

`reported by several outlets`

not:

`independently confirmed`

---

## Contradiction-search rule

For every incident that is:

- HIGH significance;
- CRITICAL significance;
- potentially pattern-forming;
- politically sensitive;
- ethnically sensitive;
- linked to alleged paramilitary activity;
- linked to foreign support;
- linked to Kosovo spillover;

actively search where feasible for:

- denial;
- correction;
- date mismatch;
- location mismatch;
- recycled media;
- duplicate incident;
- alternative motive;
- casualty revision;
- mistaken identity;
- legal-status correction.

---

## Topic interaction rule

Use `INCIDENT_STANDARD.md` together with the relevant topic-specific indicator framework.

Examples:

For:

`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

use:

- `INCIDENT_STANDARD.md`
- `indicators/03_INTERETHNIC_SECURITY_INCIDENTS.md`

For:

`TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`

use:

- `INCIDENT_STANDARD.md`
- `indicators/02_RADICAL_PARAMILITARY_ACTIVITY.md`

For:

`TOP-KOSOVO-BIH-SPILLOVER`

use:

- `INCIDENT_STANDARD.md`
- `indicators/06_KOSOVO_BIH_SPILLOVER.md`

The incident standard determines:

- what the underlying occurrence is;
- whether it is new;
- whether it is verified;
- whether it is duplicate;
- what motive status is supported.

The topic-specific framework determines:

- what the occurrence means for that monitored variable;
- whether it changes risk;
- whether escalation or transfer is demonstrated.

Do not confuse these functions.

---

## Final incident-use gate

Before using an incident as a major assessment driver ask:

1. What exactly happened?
2. When did it happen?
3. Where did it happen?
4. How many distinct incidents are there?
5. Is this new or an update?
6. What is verified?
7. What remains alleged?
8. What is the motive status?
9. Are reports independent?
10. Is there repetition?
11. Is there geographic spread?
12. Is retaliation demonstrated?
13. Is coordination demonstrated?
14. What materially changed?
15. Why does this change risk?

If these questions cannot be answered with sufficient confidence:

downgrade the analytical weight.

Prefer:

`INSUFFICIENT DATA`

over false precision.
