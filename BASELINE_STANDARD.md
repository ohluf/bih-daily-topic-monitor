# BASELINE STANDARD

## Purpose

This file defines the common standard for creating, maintaining, updating, reviewing, and using topic-specific analytical baselines in the BiH Daily Topic Monitor.

Its purpose is to provide a stable and explicit comparison condition for daily monitoring.

The core analytical principle is:

**A daily development can be assessed as change only when the previous known condition is sufficiently understood.**

The baseline must help the monitor distinguish between:

- persistent structural tension;
- already known active developments;
- genuinely new developments;
- continuation;
- repetition;
- implementation;
- acceleration;
- deterioration;
- stabilization;
- de-escalation.

The baseline must prevent reasoning such as:

old dispute
+
new article
=
new escalation

or:

persistent hostile rhetoric
+
another hostile statement
=
worsening

or:

already known foreign presence
+
new media coverage
=
expanded foreign presence

---

# Baseline role

A topic baseline answers:

**What was the best-supported known condition before the current development being assessed?**

It provides the comparison point for:

- DAILY ASSESSMENT;
- escalation judgment;
- trend judgment;
- significance;
- genuinely new development identification;
- watchlist construction.

The baseline is not:

- a news archive;
- a list of every historical event;
- a daily chronology;
- a complete country profile;
- a substitute for current search;
- a substitute for incident normalization;
- a substitute for topic-specific indicators.

---

# Core architecture

The analytical sequence is:

`MONITORED_TOPICS.md`

→ defines what is being monitored

`BASELINE_STANDARD.md`

→ defines how previous known condition is established

topic-specific baseline file

→ defines current comparison condition

`INCIDENT_STANDARD.md`

→ determines what real-world occurrence actually happened

topic-specific indicator framework

→ determines what the development means for the monitored variable

`DAILY_BRIEF_STANDARD.md`

→ determines how the conclusion is published

These functions must remain separate.

---

# Baseline layers

Every topic-specific baseline should contain two analytically distinct layers:

1. STRUCTURAL BASELINE
2. CURRENT OPERATIONAL BASELINE

These must not be collapsed.

---

# 1. STRUCTURAL BASELINE

The STRUCTURAL BASELINE describes persistent or slow-changing conditions.

Examples may include:

- constitutional structure;
- enduring political fragmentation;
- established institutional disputes;
- recurring nationalist narratives;
- long-standing foreign relationships;
- persistent community sensitivities;
- known regional linkages;
- established international presence.

Structural baseline information normally changes slowly.

It should not be rewritten because of every daily development.

---

# 2. CURRENT OPERATIONAL BASELINE

The CURRENT OPERATIONAL BASELINE describes the best-supported current condition relevant to near-term monitoring.

It may include:

- active disputes;
- known implementation stage;
- currently active actors;
- recent incident pattern;
- known organizational capability;
- current foreign footprint;
- active narratives;
- current security posture;
- current spillover condition.

This is the principal comparison layer for daily monitoring.

---

# Exact baseline question

For each monitored topic ask:

**What is already true before today's candidate development is considered?**

Then ask:

**What, if anything, materially changed?**

The baseline must make it possible to distinguish:

ALREADY KNOWN
from
GENUINELY NEW

and:

CONTINUATION
from
CHANGE

---

# Required topic baselines

The repository should contain:

`baselines/01_TENSION_ESCALATION_BASELINE.md`

linked to:

`TOP-BIH-TENSION-ESCALATION`

---

`baselines/02_RADICAL_PARAMILITARY_BASELINE.md`

linked to:

`TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`

---

`baselines/03_INTERETHNIC_INCIDENTS_BASELINE.md`

linked to:

`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

---

`baselines/04_DISINFORMATION_NETWORKS_BASELINE.md`

linked to:

`TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`

---

`baselines/05_FOREIGN_PRESENCE_BASELINE.md`

linked to:

`TOP-BIH-FOREIGN-PRESENCE`

---

`baselines/06_KOSOVO_SPILLOVER_BASELINE.md`

linked to:

`TOP-KOSOVO-BIH-SPILLOVER`

---

# Required baseline metadata

Every topic baseline must begin with:

## BASELINE ID

Format:

`TBASE-[TOPIC-SHORT-NAME]-YYYYMMDD`

Example:

`TBASE-TENSION-ESCALATION-20260710`

---

## LINKED TOPIC

Use exact topic ID.

---

## BASELINE AS OF

Format:

`YYYY-MM-DD HH:MM local time`

This indicates the information cut-off.

---

## CREATED

Date and time of initial creation.

---

## LAST MATERIAL UPDATE

Date and time of latest material baseline revision.

Do not change this field for cosmetic edits.

---

## LAST REVIEW

Date and time of latest review, even if no material change was made.

---

## BASELINE CONFIDENCE

Use:

- LOW
- MEDIUM
- HIGH

---

## BASELINE STATUS

Use:

- ACTIVE
- PARTIALLY STALE
- STALE
- UNDER REVIEW

---

# Required baseline structure

Each topic-specific baseline should normally contain:

1. Baseline Scope
2. Structural Baseline
3. Current Operational Baseline
4. Current Baseline Assessment
5. Already Known Active Developments
6. Already Known Actors / Networks
7. Already Known Geographic Concentrations
8. Already Known Institutional or Organizational Conditions
9. What Is Not New Unless It Changes
10. Current Active Watch Variables
11. Known Escalation Pathways
12. Stabilization / De-escalation Conditions
13. Key Uncertainties
14. Evidence Base
15. Baseline Change Log

Not every field must be equally long.

The baseline should remain operational, not encyclopedic.

---

# Baseline Scope

Define:

- exact monitored variable;
- geographic scope;
- relevant time horizon;
- what the baseline does not cover.

This prevents thematic drift.

Example:

For tension escalation, the baseline should describe:

- confrontation intensity;
- institutional consequences;
- mobilization;
- geographic spread;
- security relevance.

It should not become a general summary of BiH politics.

---

# Structural Baseline section

The structural baseline should identify persistent conditions that form normal background.

Examples:

- long-standing constitutional disagreement;
- recurring entity–state tensions;
- established international institutional presence;
- persistent ethnopolitical fragmentation;
- recurring use of historical narratives.

The structural baseline should answer:

**What persistent conditions are normal enough that their mere continuation does not prove daily change?**

---

# Current Operational Baseline section

The current operational baseline must describe:

**the best-supported current state immediately before new daily developments are assessed.**

It should prioritize:

- active processes;
- implementation stage;
- current actor activity;
- current capability;
- recent incident level;
- current geographic scope;
- current institutional posture;
- current known cross-topic linkages.

This is the most important baseline section.

---

# Current Baseline Assessment

Each topic baseline should provide a concise assessment of the current condition.

Do not confuse this with daily movement.

Possible wording may include:

- persistent elevated tension without broad operational escalation;
- fragmented radical activity without demonstrated capability growth;
- isolated incidents without confirmed pattern;
- recurring manipulative narratives without confirmed coordinated campaign;
- sustained foreign engagement without demonstrated new operational expansion;
- active Kosovo-related rhetoric without demonstrated spillover into BiH.

The baseline assessment is a condition statement.

It is not automatically:

- IMPROVING;
- DETERIORATING;
- ESCALATING.

---

# State vs trajectory discipline

Always distinguish:

CURRENT STATE
from
MOVEMENT

Example:

Current state:

`HIGH POLITICAL TENSION`

Daily movement:

`NO MATERIAL CHANGE`

This may produce:

`STABLE TENSION`

not:

`ESCALATION`

Another example:

Current state:

`LOW CURRENT INCIDENT LEVEL`

New development:

`SECOND RELATED VIOLENT INCIDENT`

This may produce:

`LIMITED ESCALATION`

even if the absolute condition remains below severe crisis level.

---

# Already Known Active Developments

List active developments that are already part of the known condition.

Examples:

- ongoing legal dispute;
- unresolved institutional confrontation;
- already announced protest;
- known investigation;
- existing foreign-funded project;
- already identified narrative campaign;
- known alleged training activity;
- ongoing Kosovo-related political rhetoric.

The purpose is to prevent rediscovery from being treated as new.

---

# Already Known Development Status

Preserve exact status.

Use where relevant:

- DISCUSSED
- PROPOSED
- ANNOUNCED
- ADOPTED
- SIGNED
- UNDER REVIEW
- CHALLENGED
- IMPLEMENTATION PENDING
- PARTIALLY IMPLEMENTED
- IMPLEMENTED
- SUSPENDED
- CANCELLED
- INVESTIGATED
- UNRESOLVED

Do not reset status each day.

---

# Already Known Actors / Networks

Include only actors necessary for understanding the current monitored condition.

Possible categories:

- political actor;
- institution;
- security body;
- organization;
- network;
- foreign actor;
- local intermediary.

Do not turn the baseline into a full actor encyclopedia.

For each actor include only what matters to the monitored variable.

---

# Actor continuity discipline

An actor already known to be active should not be treated as a new actor merely because:

- a new article mentions them;
- they make another statement;
- they attend another routine meeting.

A genuinely new actor development may include:

- entry into the dispute;
- new organizational role;
- new capability;
- new coalition;
- new operational function;
- expanded geographic activity.

---

# Already Known Geographic Concentrations

Where relevant identify:

- municipality;
- canton;
- entity;
- border area;
- multi-location concentration.

This helps distinguish:

continued local activity

from:

geographic spread

Do not infer new spread without new distinct locations.

---

# Already Known Institutional or Organizational Conditions

Record current conditions relevant to comparison.

Examples:

- institution already blocked;
- legal challenge already pending;
- organization already exists;
- investigation already open;
- foreign office already operational;
- mission posture already elevated.

This prevents later reporting of the same condition from being treated as new.

---

# What Is Not New Unless It Changes

Every topic baseline must include this section.

This is a mandatory anti-false-positive control.

The section should list recurring developments that must not automatically be treated as new.

Examples for tension:

- repeated anti-OHR rhetoric;
- repeated constitutional accusations;
- recurring secessionist statements without implementation;
- ordinary opposition-government confrontation.

Examples for radical activity:

- historical allegations without new evidence;
- recurring nationalist rhetoric;
- military-style clothing without capability change.

Examples for incidents:

- repeated articles about same incident;
- political commentary on existing incident;
- old footage.

Examples for disinformation:

- repetition of established narrative;
- ordinary partisan amplification;
- foreign media citation.

Examples for foreign presence:

- routine diplomatic visit;
- recurring embassy engagement;
- existing mission activity within known posture.

Examples for Kosovo spillover:

- rhetorical analogy;
- generic RS–Kosovo comparison;
- regional media attention without domestic effect.

---

# Current Active Watch Variables

Each baseline should identify the limited set of variables most capable of changing the assessment.

Normally:

3–10 variables

Examples:

- whether announced measure is implemented;
- whether incident repeats;
- whether activity spreads geographically;
- whether investigation confirms organizational linkage;
- whether foreign support becomes material;
- whether Kosovo rhetoric produces physical mobilization.

These are variables, not generic topics.

Bad:

`watch political tension`

Good:

`whether formal non-compliance expands from one institution to additional bodies`

---

# Known Escalation Pathways

Each baseline should identify plausible mechanisms by which the current condition could worsen.

Use:

CURRENT CONDITION
→ NEXT MATERIAL STEP
→ CHANGED RISK

Example:

known institutional dispute
→ refusal to implement binding decision
→ increased state-functionality and confrontation risk

Example:

isolated radical network
→ verified recruitment and recurring training
→ increased organizational capability

Example:

single incident
→ retaliatory second incident
→ self-reinforcing local escalation risk

These pathways should be grounded in the topic-specific indicator framework.

---

# Stabilization / De-escalation Conditions

The baseline must also identify what would count as genuine stabilization or improvement.

Examples:

- implementation of court decision;
- restoration of institutional participation;
- no follow-on incidents after cluster;
- verified demobilization;
- reduction of exceptional security posture;
- disruption of coordinated information network;
- withdrawal of foreign operational support;
- absence of domestic effect from Kosovo-related crisis.

Do not define stabilization merely as:

`no major news`

---

# Key Uncertainties

Every baseline must identify important unresolved questions.

Examples:

- motive remains unknown;
- organizational structure unclear;
- foreign linkage unverified;
- implementation timeline uncertain;
- source-chain dependence unresolved;
- actor capability unclear.

Uncertainty must be explicit.

Do not hide data gaps inside confident prose.

---

# Baseline evidence window

For initial baseline creation use a default primary evidence window of:

`30 DAYS`

Extend to:

`90 DAYS`

when necessary to establish:

- current pattern;
- actor continuity;
- organizational capability;
- implementation history;
- foreign footprint;
- repeated incidents;
- narrative persistence.

Older evidence may be used only when structurally essential.

---

# Historical context discipline

Older information may be included when necessary to explain:

- structural condition;
- established organization;
- enduring legal dispute;
- long-term foreign presence;
- persistent conflict mechanism.

Do not allow historical material to dominate current operational baseline.

---

# Evidence recency discipline

Ask:

- Is the actor still active?
- Is the organization still functioning?
- Is the project implemented?
- Is the investigation still open?
- Is the force posture still current?
- Is the narrative still active?
- Is the incident pattern still relevant?

Old evidence must not be carried forward automatically.

---

# Evidence hierarchy

Use source hierarchy from:

`SOURCES.md`

But apply it according to source role.

For baseline creation prioritize:

- official records;
- competent institutions;
- court and prosecutorial records;
- direct organizational material;
- credible local reporting;
- investigative reporting;
- established media;
- international institutional sources;
- specialist research where relevant.

Social media and Telegram may assist discovery.

They should not independently define baseline condition without stronger support.

---

# External-search discipline

When constructing or reviewing a baseline:

- use topic-specific searches;
- search multiple languages where relevant;
- seek official and local sources;
- identify contradictory evidence;
- search for updates to older claims;
- distinguish current from historical material.

Follow:

`SEARCH_STRATEGY.md`

---

# Baseline source-chain discipline

Do not treat:

multiple articles

as:

multiple independent baseline facts

Identify whether sources derive from:

- same agency;
- same press release;
- same official statement;
- same politician;
- same anonymous source;
- same original investigation.

Baseline confidence must account for source dependence.

---

# Contradiction requirement

For material baseline claims actively search where feasible for:

- correction;
- denial;
- updated legal status;
- project cancellation;
- changed actor role;
- closure of organization;
- revised casualty figures;
- disproven foreign link;
- disproven motive;
- outdated mission posture.

A baseline built from old unchallenged claims may become misleading.

---

# Baseline confidence

Assign:

- LOW
- MEDIUM
- HIGH

---

## HIGH confidence

Use when:

- current condition is well supported;
- source quality is strong;
- important claims are corroborated;
- unresolved contradictions are limited.

---

## MEDIUM confidence

Use when:

- overall condition is reasonably supported;
- some important uncertainties remain;
- evidence is uneven.

---

## LOW confidence

Use when:

- current condition depends heavily on uncertain claims;
- evidence is sparse;
- source chains are weak;
- major contradictions remain unresolved.

---

# Confidence scope discipline

Baseline confidence refers to the baseline as a whole.

Specific claims may have different confidence.

Do not imply that every baseline component has identical evidentiary strength.

---

# Baseline freshness

Baseline freshness must be actively managed.

Possible status:

- ACTIVE
- PARTIALLY STALE
- STALE
- UNDER REVIEW

---

## ACTIVE

Use when:

- key comparison conditions remain current;
- major known developments are updated;
- no significant evidence of outdated status exists.

---

## PARTIALLY STALE

Use when:

- some important components may be outdated;
- but the baseline remains partially usable.

Daily assessments relying on stale sections must be more cautious.

---

## STALE

Use when:

- comparison condition is no longer reliable;
- major political, security, organizational, or operational changes occurred;
- current condition cannot safely be inferred.

A STALE baseline must not strongly drive escalation assessment.

---

## UNDER REVIEW

Use when:

- significant change occurred;
- baseline revision is underway;
- old and new conditions are being reconciled.

---

# Review frequency

Baseline review is not the same as baseline update.

Recommended operating principle:

- review regularly;
- update only when needed.

For active daily monitoring, each topic baseline should normally be reviewed at least:

`ONCE EVERY 7 DAYS`

or sooner when a material trigger occurs.

This is a methodological default, not a rigid mechanical requirement.

---

# Material update triggers

A baseline should be updated when one or more of the following occurs:

- binding institutional decision changes current condition;
- major implementation step occurs;
- significant incident pattern emerges;
- geographic spread becomes established;
- new capable actor enters;
- organization changes capability;
- recruitment or training becomes verified;
- major investigation changes factual understanding;
- foreign presence materially expands or contracts;
- security posture changes;
- coordinated information network becomes established or disrupted;
- Kosovo-related transfer mechanism becomes demonstrated;
- previous baseline assumption is contradicted;
- meaningful de-escalation occurs.

---

# Non-material update rule

Do not materially update baseline merely because:

- another article repeats known facts;
- another politician comments;
- media attention rises;
- a known actor repeats position;
- an old report is rediscovered;
- wording changes without underlying condition change.

---

# Baseline drift control

A major risk is:

`BASELINE DRIFT`

This occurs when every new development is immediately absorbed into the baseline, causing the comparison point to move continuously.

Example:

Day 1:
new escalation occurs

Day 2:
baseline is rewritten to include it

Day 3:
follow-on escalation appears normal

To prevent this:

- do not rewrite baseline mechanically after every daily brief;
- preserve material change history;
- record when the baseline changed;
- maintain explicit previous condition;
- distinguish adaptation from normalization.

---

# Change absorption rule

A development should normally be absorbed into the current operational baseline when:

- it is verified;
- it has become part of the continuing condition;
- its immediate novelty has passed;
- future assessments need to compare against the new reality.

The timing depends on:

- persistence;
- implementation;
- reversibility;
- analytical significance.

Do not use a fixed 24-hour rule.

---

# Temporary development rule

Temporary developments should not automatically become permanent baseline conditions.

Examples:

- one-day protest;
- short diplomatic visit;
- temporary police deployment;
- unconfirmed signal;
- isolated incident.

Absorb only the continuing effect if one remains.

---

# Baseline update types

Classify revisions internally as:

- MATERIAL UPDATE
- MINOR UPDATE
- EVIDENCE CORRECTION
- STATUS UPDATE
- CONFIDENCE UPDATE
- STRUCTURAL REVISION

---

## MATERIAL UPDATE

Changes comparison condition.

---

## MINOR UPDATE

Adds useful detail without changing assessment.

---

## EVIDENCE CORRECTION

Fixes factual or source error.

---

## STATUS UPDATE

Changes stage:

announced
→ adopted

or:

investigation
→ indictment

---

## CONFIDENCE UPDATE

Evidence quality materially changes.

---

## STRUCTURAL REVISION

Persistent analytical assumptions change.

Use rarely.

---

# Baseline version continuity

Never silently overwrite major analytical changes.

Maintain:

`BASELINE CHANGE LOG`

For every material update record:

- date;
- previous condition;
- new condition;
- reason;
- strongest evidence;
- effect on monitoring.

Example:

`2026-07-15`

Previous condition:
No verified geographic spread.

New condition:
Related incidents verified in three municipalities.

Reason:
Distinct incidents confirmed by competent local authorities.

Monitoring effect:
Future assessments compare against multi-location pattern rather than isolated local condition.

---

# Daily comparison workflow

Before assessing a candidate development:

1. identify linked topic;
2. read relevant topic baseline;
3. identify current operational condition;
4. identify what is already known;
5. compare candidate development;
6. classify result.

Use:

- NO CHANGE
- CONTINUATION
- REPEATED REPORTING
- IMPLEMENTATION
- NEW DEVELOPMENT
- MATERIAL WORSENING
- STABILIZATION
- DE-ESCALATION
- UNCERTAIN

---

# NO CHANGE

Use when no meaningful movement from baseline is demonstrated.

---

# CONTINUATION

Use when existing condition persists.

Example:

known hostile rhetoric
→ additional similar rhetoric

---

# REPEATED REPORTING

Use when source coverage changes but underlying reality does not.

---

# IMPLEMENTATION

Use when already known announced or adopted action moves into execution.

Implementation may be highly significant.

Do not treat it as merely repetition.

---

# NEW DEVELOPMENT

Use when a genuinely new element appears.

Examples:

- new actor;
- new measure;
- new incident;
- new organizational capability;
- new geographic location;
- new linkage.

---

# MATERIAL WORSENING

Use when the current monitored variable clearly deteriorates relative to baseline.

Requires:

- primary evidence;
- explicit mechanism;
- changed risk.

---

# STABILIZATION

Use when pressure stops growing or a deterioration pathway is constrained.

Stabilization is not necessarily improvement.

---

# DE-ESCALATION

Use when evidence demonstrates actual reduction in pressure, capability, confrontation, or risk.

---

# UNCERTAIN

Use when comparison is unreliable.

This may occur because:

- baseline is stale;
- new evidence is weak;
- time sequence unclear;
- alternative explanations remain strong.

---

# Baseline comparison mechanism

For material change use:

BASELINE CONDITION
→ NEW DEVELOPMENT
→ CHANGED VARIABLE
→ CHANGED RISK

Example:

Baseline:
contested proposal under debate

New development:
binding measure formally adopted

Changed variable:
institutional consequence increased

Changed risk:
higher probability of legal and inter-institutional confrontation

---

# Baseline-independent seriousness

A development may be serious without representing change.

Example:

A severe structural dispute may remain unchanged.

Therefore:

HIGH seriousness
≠
daily escalation

---

# Baseline-relative escalation

A smaller event may represent meaningful change if it shifts the condition.

Example:

Baseline:
no physical incidents

New development:
first verified assault linked to existing confrontation

This may represent:

LIMITED ESCALATION

depending on evidence and mechanism.

---

# Topic-specific baseline discipline

Each baseline must reflect its own monitored variable.

---

## Tension baseline

Focus on:

- confrontation intensity;
- formal action;
- institutional non-compliance;
- mobilization;
- geographic scope;
- security consequences.

Do not become a general political chronology.

---

## Radical / paramilitary baseline

Focus on:

- actor existence;
- organization;
- recruitment;
- training;
- logistics;
- weapons;
- cross-border links;
- operational capability.

Do not become a list of radical statements.

---

## Incident baseline

Focus on:

- distinct incidents;
- frequency;
- severity;
- motive profile;
- target pattern;
- geographic spread;
- retaliation;
- coordination.

Do not use article volume.

---

## Disinformation baseline

Focus on:

- active narratives;
- coordination;
- stable networks;
- foreign linkage;
- platforms;
- behavioral effect;
- offline consequences.

Do not list every false claim.

---

## Foreign presence baseline

Focus on:

- current footprint;
- access;
- implementation;
- persistence;
- material support;
- dependence;
- leverage;
- operational effect.

Do not become a diplomatic calendar.

---

## Kosovo spillover baseline

Focus on:

- current domestic effect;
- transfer mechanisms;
- actor overlap;
- mobilization;
- organizational linkage;
- security posture;
- demonstrated spillover level.

Do not summarize Kosovo news generally.

---

# Incident interaction

When baseline depends on incidents, apply:

`INCIDENT_STANDARD.md`

before updating:

- incident count;
- pattern;
- geographic spread;
- motive profile;
- retaliation status.

Do not update baseline with duplicate incidents.

---

# Indicator interaction

Use relevant topic-specific framework to determine whether a development changes the monitored variable.

Baseline answers:

**Compared with what?**

Indicator framework answers:

**What does the change mean?**

Do not reverse these functions.

---

# Cross-topic baseline discipline

A development may affect several baselines.

Update more than one baseline only when distinct evidence supports each linkage.

Example:

A verified organized group receives foreign training.

Possible impact:

Radical / paramilitary baseline
→ capability change

Foreign presence baseline
→ operational support change

Cross-topic linkage may be justified.

Do not update all topics merely because the event is serious.

---

# Negative baseline findings

Valid baseline conclusions include:

- no verified pattern;
- no geographic spread;
- no organizational growth;
- no foreign support demonstrated;
- no behavioral effect demonstrated;
- no Kosovo spillover demonstrated.

These negative findings are important comparison conditions.

---

# Absence-of-evidence discipline

Distinguish:

`NO EVIDENCE FOUND`

from:

`EVIDENCE OF ABSENCE`

Example:

No public evidence of mobilization found

does not always prove:

No mobilization exists

Use confidence appropriately.

---

# Baseline uncertainty rule

Where the baseline is weak:

do not force precise daily movement.

Prefer:

`INSUFFICIENT DATA`

or:

`UNCERTAIN`

rather than false comparison.

---

# Baseline length discipline

A topic baseline should be long enough to establish comparison condition but short enough for operational use.

Normal target:

`800–1800 words per topic baseline`

A more complex topic may exceed this when necessary.

Avoid:

- long historical essays;
- duplicated source summaries;
- generic geopolitical background.

---

# Baseline evidence section

Each baseline should end with:

## Evidence Base

Organize evidence as:

### Primary / Official

### Independent Reporting

### Specialist / Investigative

### Unconfirmed Signals

For each important item preserve where possible:

- source;
- date;
- role;
- what fact it supports.

Do not overload with every article found.

---

# Baseline source selection

Prioritize evidence that establishes:

- current condition;
- current status;
- implementation;
- continuity;
- capability;
- pattern.

Do not select sources merely because they are recent.

A recent article repeating old information may be less useful than an older primary source establishing current status.

---

# Baseline review workflow

During a review:

1. read current baseline;
2. identify all material claims;
3. test whether each remains current;
4. search for status changes;
5. search for contradictions;
6. identify missing developments;
7. assess whether current operational baseline still holds;
8. update confidence;
9. update freshness status;
10. record material revisions.

---

# Baseline creation workflow

For a new topic baseline:

1. Read:
   - `MONITORED_TOPICS.md`
   - relevant indicator file
   - `SOURCES.md`
   - `SEARCH_STRATEGY.md`
   - `INCIDENT_STANDARD.md` when relevant.

2. Define exact monitored variable.

3. Search default 30-day evidence window.

4. Extend to 90 days when necessary.

5. Use older context only when structurally essential.

6. Identify structural baseline.

7. Identify current operational baseline.

8. Separate:
   - already known;
   - current;
   - uncertain.

9. Identify active actors and geographic concentrations.

10. Write:
    `What Is Not New Unless It Changes`.

11. Identify current watch variables.

12. Identify escalation pathways.

13. Identify stabilization conditions.

14. Record key uncertainties.

15. Build evidence base.

16. Assign confidence.

17. Perform final audit.

---

# Final baseline audit

Before finalizing or materially updating a topic baseline verify:

1. What exact variable is being baselined?
2. Is structural background separated from current operational condition?
3. Is the baseline current as of the stated cut-off?
4. Are active developments distinguished from historical context?
5. Are announced and implemented actions separated?
6. Are existing actors distinguished from new actor entry?
7. Are repeated reports being mistaken for new developments?
8. Are incident duplicates removed?
9. Are old claims being carried forward without update checks?
10. Are source chains genuinely independent?
11. Are contradictions acknowledged?
12. Is current state separated from trajectory?
13. Does the baseline state what is not new unless changed?
14. Are active watch variables specific?
15. Are escalation pathways explicit?
16. Are de-escalation conditions explicit?
17. Are key uncertainties visible?
18. Is confidence justified?
19. Is the baseline too broad or encyclopedic?
20. Can the monitor clearly answer:
    “Compared with what?”

If the final question cannot be answered clearly:

the baseline is not operationally sufficient.
