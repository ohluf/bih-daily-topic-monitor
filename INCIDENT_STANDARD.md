# INCIDENT STANDARD

## Purpose

This file defines the common incident-identification, normalization, deduplication, verification, classification, update, and analytical-use standard for the BiH Daily Topic Monitor.

Its purpose is to prevent the monitor from confusing:

- articles with incidents;
- claims with facts;
- allegations with confirmed events;
- updates with new incidents;
- political reactions with additional incidents;
- repeated reporting with corroboration;
- different ethnic identities with ethnic motive;
- serious events with escalation;
- high media visibility with high real-world significance.

The core principle is:

**One underlying real-world occurrence must be represented as one incident record, regardless of how many articles, posts, statements, or follow-up reports describe it.**

---

# Scope

Apply this standard whenever the monitoring process encounters a potentially relevant real-world occurrence involving one or more of the following:

- violence;
- threat;
- intimidation;
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
- Kosovo-related domestic effect;
- institutional-security confrontation.

This standard may also be used for other occurrences when incident normalization is analytically useful.

---

# Core incident rule

Always distinguish:

1. SOURCE ITEM
2. CLAIM
3. UNDERLYING INCIDENT
4. INCIDENT UPDATE
5. REACTION
6. CONTEXT
7. ANALYTICAL ASSESSMENT

These are not interchangeable.

Example:

Article A reports an assault.

Article B reports police confirmation.

Article C reports a politician's reaction.

Article D reports prosecutor involvement.

Article E repeats the original report.

This may still represent:

`1 UNDERLYING INCIDENT`

with:

- one initial report;
- one verification update;
- one political reaction;
- one legal-status update;
- one duplicate report.

Do not count five incidents.

---

# Internal incident record

For every potentially relevant incident create or maintain an internal normalized record using the following structure where information is available.

---

## INCIDENT ID

Format:

`INC-YYYYMMDD-LOC-NNN`

Example:

`INC-20260709-BANJALUKA-001`

Where exact location is unknown use:

`INC-YYYYMMDD-UNK-NNN`

The ID is an internal normalization tool.

Do not invent false precision.

---

## INCIDENT DATE

Record the best-supported date of occurrence.

Possible values:

- exact date;
- estimated date;
- date range;
- unknown.

Distinguish:

`DATE OF INCIDENT`

from:

`DATE OF PUBLICATION`

and:

`DATE OF DISCOVERY`

These are not interchangeable.

---

## INCIDENT TIME

Record where known:

- exact time;
- approximate time;
- daypart;
- unknown.

Do not invent time from publication metadata.

---

## DISCOVERY DATE

Record when the monitor first identified the incident.

This helps distinguish:

newly discovered old incident

from:

new current incident.

---

## LAST UPDATE TIME

Record the latest meaningful evidentiary or status update.

Do not update this field merely because another article repeats the same facts.

---

## LOCATION

Record where possible:

- settlement;
- municipality;
- canton;
- entity;
- Brčko District;
- border area;
- multi-location;
- unknown.

Use the most precise verified location.

---

## GEOGRAPHIC SCOPE

Classify:

- SINGLE SITE
- LOCAL
- MUNICIPAL
- MULTI-MUNICIPAL
- CANTONAL
- ENTITY-WIDE
- STATE-WIDE
- CROSS-BORDER
- UNKNOWN

Do not infer broad scope from national media attention.

---

## INCIDENT TYPE

Assign one primary incident type.

Possible primary types include:

- VERBAL THREAT
- WRITTEN THREAT
- ONLINE THREAT
- INTIMIDATION
- HARASSMENT
- PHYSICAL ASSAULT
- SERIOUS ASSAULT
- HOMICIDE
- ATTEMPTED HOMICIDE
- WEAPON DISPLAY
- WEAPON DISCHARGE
- SHOOTING
- EXPLOSIVE INCIDENT
- ARSON
- PROPERTY DAMAGE
- VANDALISM
- HATE SYMBOL / GRAFFITI
- RELIGIOUS-SITE INCIDENT
- MEMORIAL-SITE INCIDENT
- RETURNee-RELATED INCIDENT
- PUBLIC DISORDER
- PROTEST INCIDENT
- CLASH
- POLICE USE OF FORCE
- SECURITY DEPLOYMENT
- ARREST
- RAID
- SEARCH
- WEAPONS SEIZURE
- EXPLOSIVES SEIZURE
- RECRUITMENT ACTIVITY
- TRAINING ACTIVITY
- SUSPECTED PARAMILITARY ACTIVITY
- MOBILIZATION
- ORGANIZED PROVOCATION
- BORDER INCIDENT
- CROSS-BORDER MOVEMENT
- FOREIGN-LINKED SECURITY ACTIVITY
- INFORMATION-ENABLED INCIDENT
- INSTITUTIONAL SECURITY INCIDENT
- OTHER

When necessary, record secondary types separately.

Do not create several incident records merely because one occurrence fits several types.

---

## SECONDARY INCIDENT TYPES

Optional.

Use when one underlying occurrence contains several meaningful dimensions.

Example:

Primary:

`PHYSICAL ASSAULT`

Secondary:

- POSSIBLE HATE-RELATED
- PROTEST-RELATED

---

## INCIDENT STATUS

Classify:

- REPORTED
- PARTIALLY VERIFIED
- VERIFIED
- DISPUTED
- CONTRADICTED
- FALSE REPORT
- UNRESOLVED

### REPORTED

A claim exists, but independent or competent verification remains incomplete.

### PARTIALLY VERIFIED

The occurrence itself is supported, but important details remain uncertain.

### VERIFIED

The core occurrence is supported by sufficiently strong evidence.

### DISPUTED

Credible sources materially disagree about the occurrence or a central fact.

### CONTRADICTED

Strong evidence materially undermines the original claim.

### FALSE REPORT

The alleged incident is shown not to have occurred as claimed.

### UNRESOLVED

Available evidence is insufficient to choose a stronger status.

---

# Incident existence vs incident interpretation

Always separate:

`DID SOMETHING HAPPEN?`

from:

`WHAT DID IT MEAN?`

Example:

A physical assault may be:

`VERIFIED INCIDENT`

while:

`ETHNIC MOTIVE`

remains:

`UNCONFIRMED`

This is valid.

Do not lower the existence confidence merely because motive is unclear.

Do not raise motive confidence merely because the incident itself is verified.

---

# People and actor fields

Where known record:

## VICTIM / TARGET

Possible categories:

- INDIVIDUAL
- POLITICAL ACTOR
- PUBLIC OFFICIAL
- JOURNALIST
- POLICE
- SECURITY PERSONNEL
- RETURNee
- RELIGIOUS COMMUNITY
- ETHNIC COMMUNITY
- POLITICAL PARTY
- INSTITUTION
- RELIGIOUS SITE
- MEMORIAL SITE
- BUSINESS
- INFRASTRUCTURE
- PUBLIC EVENT
- UNKNOWN

Avoid unnecessary publication of personal data.

---

## ALLEGED OFFENDER / ACTOR

Classify carefully:

- IDENTIFIED INDIVIDUAL
- UNIDENTIFIED INDIVIDUAL
- INFORMAL GROUP
- ORGANIZED GROUP
- POLITICAL ACTOR
- SECURITY ACTOR
- FOREIGN ACTOR
- UNKNOWN

Preserve legal status.

Do not describe a suspect as offender when guilt is unproven.

---

## ACTOR STATUS

Possible values:

- ALLEGED
- SUSPECTED
- IDENTIFIED
- DETAINED
- ARRESTED
- CHARGED
- INDICTED
- ON TRIAL
- CONVICTED
- ACQUITTED
- UNKNOWN

These are not interchangeable.

---

# Casualty and harm fields

## INJURIES

Classify where supported:

- NONE REPORTED
- MINOR
- SERIOUS
- LIFE-THREATENING
- FATAL
- MULTIPLE CASUALTIES
- UNKNOWN

Preserve uncertainty.

Do not infer injury severity from emotional language.

---

## FATALITIES

Record:

- confirmed number;
- provisional number;
- unknown.

Do not use preliminary casualty counts as final.

---

## PROPERTY DAMAGE

Classify:

- NONE
- MINOR
- SIGNIFICANT
- SEVERE
- DESTROYED
- UNKNOWN

---

# Weapons and means

## WEAPON STATUS

Classify:

- NO WEAPON REPORTED
- ALLEGED
- DISPLAYED
- THREATENED
- USED
- FIRED
- SEIZED
- UNKNOWN

---

## WEAPON TYPE

Where supported:

- FIREARM
- KNIFE / BLADED WEAPON
- BLUNT OBJECT
- EXPLOSIVE
- INCENDIARY DEVICE
- VEHICLE
- OTHER
- UNKNOWN

---

## Weapons analytical discipline

Distinguish:

- weapon present;
- weapon displayed;
- weapon threatened;
- weapon used;
- weapon fired;
- injury caused;
- organizational weapons access.

A weapon in one individual criminal case does not prove:

- paramilitary capability;
- extremist network;
- organized mobilization;
- foreign support.

---

# Motive classification

For any incident with possible ethnic, national, religious, political, ideological, extremist, or foreign-linked relevance, record motive separately.

---

## ETHNIC / INTER-COMMUNITY MOTIVE STATUS

Use exactly one:

- CONFIRMED
- PROBABLE
- POSSIBLE
- UNCONFIRMED
- NON-ETHNIC
- NOT APPLICABLE

### CONFIRMED

Use only when strong direct evidence exists.

Examples:

- official classification;
- judicial finding;
- direct authenticated offender statement;
- verified explicit ethnic slurs linked to the act;
- clear identity-based target selection supported by evidence.

### PROBABLE

Use when several strong indicators point toward ethnic motive but formal confirmation remains incomplete.

### POSSIBLE

Use when ethnic motive is plausible but materially uncertain.

### UNCONFIRMED

Use when ethnic relevance is alleged or discussed but evidence does not establish it.

### NON-ETHNIC

Use when evidence supports another motive.

### NOT APPLICABLE

Use when ethnic motive is irrelevant to the occurrence.

---

## POLITICAL MOTIVE STATUS

Use:

- CONFIRMED
- PROBABLE
- POSSIBLE
- UNCONFIRMED
- NON-POLITICAL
- NOT APPLICABLE

---

## IDEOLOGICAL / EXTREMIST MOTIVE STATUS

Use:

- CONFIRMED
- PROBABLE
- POSSIBLE
- UNCONFIRMED
- NON-IDEOLOGICAL
- NOT APPLICABLE

Do not infer extremist motive from unpopular or radical opinion alone.

---

## FOREIGN-LINKED MOTIVE OR SUPPORT STATUS

Use:

- CONFIRMED
- STRONGLY INDICATED
- POSSIBLE
- UNVERIFIED
- NONE DEMONSTRATED
- NOT APPLICABLE

Foreign nationality alone does not establish foreign linkage.

---

# Motive evidence hierarchy

Stronger evidence may include:

1. COURT FINDING
2. PROSECUTORIAL CLASSIFICATION
3. POLICE CLASSIFICATION
4. AUTHENTICATED OFFENDER STATEMENT
5. VERIFIED DIRECT THREAT
6. MULTIPLE CREDIBLE WITNESSES
7. DOCUMENTED TARGET PATTERN
8. STRONG CONTEXTUAL INFERENCE
9. POLITICAL ALLEGATION
10. MEDIA SPECULATION

Do not treat all levels as equivalent.

---

# Organizational character

Classify:

- INDIVIDUAL
- SPONTANEOUS GROUP
- INFORMAL GROUP
- ORGANIZED GROUP
- STRUCTURED NETWORK
- UNKNOWN

Do not infer an organization from:

- several people appearing together;
- same clothing;
- same symbols;
- same ethnicity;
- same political opinion.

Look for:

- leadership;
- recurring membership;
- communications;
- logistics;
- financing;
- task division;
- repeated coordinated activity.

---

# Coordination status

Use:

- CONFIRMED
- STRONGLY INDICATED
- POSSIBLE
- UNCONFIRMED
- NO COORDINATION DEMONSTRATED
- NOT APPLICABLE

Coordination requires more than simultaneity.

---

# Incident severity

Assign an internal severity level:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Severity is not the same as significance.

Severity is not the same as escalation.

---

## LOW severity

Examples:

- isolated verbal insult;
- low-level graffiti;
- minor symbolic provocation;
- minor property damage;
- unexecuted low-capability threat.

---

## MEDIUM severity

Examples:

- physical assault;
- credible threat;
- meaningful property damage;
- repeated intimidation;
- organized provocation;
- non-lethal weapon use;
- local public disorder.

---

## HIGH severity

Examples:

- serious injury;
- firearm discharge;
- organized violent attack;
- repeated linked assaults;
- serious arson;
- significant coordinated unrest;
- credible operational threat by capable actor.

---

## CRITICAL severity

Examples:

- mass-casualty violence;
- coordinated armed attack;
- large-scale organized inter-community violence;
- imminent high-confidence attack preparation;
- widespread violent unrest;
- major security breakdown.

CRITICAL must remain exceptional.

---

# Analytical significance

Separately assign:

- LOW
- MEDIUM
- HIGH
- CRITICAL

Significance reflects analytical importance for the monitored topics.

A low-severity incident may have high significance if it demonstrates:

- a new network;
- geographic spread;
- retaliation sequence;
- cross-border linkage;
- new operational capability.

A severe isolated crime may have limited relevance to the monitored topics.

Do not equate:

`SEVERITY`

with:

`SIGNIFICANCE`

---

# Confidence

Assign:

- LOW
- MEDIUM
- HIGH

Confidence must reflect:

- evidence quality;
- source independence;
- factual consistency;
- official confirmation;
- unresolved contradictions.

Do not use confidence as a substitute for significance.

---

# Source record

For every incident maintain an internal source set.

For each source capture where possible:

- source name;
- source type;
- publication time;
- URL or retrievable reference;
- role in evidence chain;
- original or derivative;
- primary fact contributed;
- independence status.

---

# Source role classification

Classify each source as one or more of:

- PRIMARY OFFICIAL
- PRIMARY PARTICIPANT
- PRIMARY ORGANIZATIONAL
- DIRECT WITNESS
- LOCAL REPORTING
- INVESTIGATIVE REPORTING
- NATIONAL MEDIA
- INTERNATIONAL MEDIA
- AGENCY
- FACT-CHECK
- SOCIAL MEDIA
- TELEGRAM
- COMMENTARY
- DERIVATIVE REPORT

The role matters more than outlet prestige alone.

---

# Source-chain independence

Always determine whether reports are genuinely independent.

Possible relationships include:

- INDEPENDENT
- PARTIALLY INDEPENDENT
- SAME AGENCY CHAIN
- SAME PRESS RELEASE
- SAME POLITICAL STATEMENT
- SAME ANONYMOUS SOURCE
- DERIVATIVE
- UNKNOWN

Do not convert:

`5 ARTICLES`

into:

`5 INDEPENDENT CONFIRMATIONS`

Example:

SRNA publishes a report.

Three portals reproduce it.

A regional outlet summarizes those portals.

This may still be:

`1 PRIMARY SOURCE CHAIN`

---

# Discovery vs confirmation

A source may be useful for:

`DISCOVERY`

but insufficient for:

`CONFIRMATION`

Examples:

Anonymous Telegram post
→ discovery signal

Police statement
→ stronger confirmation

Local witness video
→ possible direct evidence

National media article copying local report
→ derivative evidence

Do not confuse source roles.

---

# Primary evidence

For incident existence prioritize where relevant:

- competent police statement;
- prosecutor statement;
- court record;
- official institutional record;
- authenticated direct imagery;
- direct verified witness evidence;
- reliable original local reporting;
- multiple genuinely independent sources.

No source type is automatically infallible.

---

# Contradiction search

For every HIGH-significance, CRITICAL-significance, or serious disputed incident actively search for:

- official denial;
- correction;
- location mismatch;
- date mismatch;
- old footage;
- recycled image;
- manipulated media;
- mistaken identity;
- duplicate incident;
- alternative motive;
- casualty revision;
- legal-status correction.

A serious claim requires stronger contradiction testing.

---

# Duplicate detection

Before creating a new incident record compare:

- date;
- approximate time;
- exact location;
- municipality;
- victim;
- alleged actor;
- incident type;
- weapon;
- injury;
- police case;
- wording;
- photographs;
- video;
- quoted witnesses.

---

# Duplicate classification

Classify new information as:

- NEW INCIDENT
- UPDATE TO EXISTING INCIDENT
- DUPLICATE REPORT
- REACTION TO EXISTING INCIDENT
- CONTEXT
- UNRELATED

---

## NEW INCIDENT

Use when a distinct real-world occurrence is demonstrated.

---

## UPDATE TO EXISTING INCIDENT

Use when new information materially changes knowledge about an existing incident.

Examples:

- arrest;
- motive classification;
- revised casualty count;
- prosecutor opens case;
- weapon recovered;
- new verified participant;
- official contradiction;
- evidence of organizational linkage.

---

## DUPLICATE REPORT

Use when the same underlying facts are repeated without material new information.

---

## REACTION TO EXISTING INCIDENT

Use for:

- political statement;
- community condemnation;
- embassy reaction;
- protest announcement;
- institutional commentary.

A reaction may itself become a separate incident only if it produces a distinct real-world occurrence.

Example:

Politician condemns assault
→ REACTION

Protest called in response
→ initially reaction / planned event

Protest occurs and clashes happen
→ NEW INCIDENT

---

# Incident merge rule

If two initially separate records are later shown to describe the same occurrence:

merge them.

Preserve:

- source history;
- previous uncertainty;
- important updates.

Do not keep artificial duplicate records.

---

# Incident split rule

If one initial report later proves to contain several distinct occurrences:

split only when:

- separate times;
- separate locations;
- separate victims;
- separate actors;
- separate police cases;
- or analytically distinct events

are demonstrated.

Do not split merely because several consequences followed one occurrence.

---

# Update significance rule

Not every new article is an incident update.

A meaningful update must change at least one of:

- existence confidence;
- incident status;
- motive;
- severity;
- casualty count;
- actor identity;
- organizational linkage;
- legal status;
- geographic scope;
- source confidence;
- escalation relevance.

Otherwise classify as:

`DUPLICATE REPORT`

or:

`REPEATED REPORTING`

---

# Planned vs occurred discipline

Always preserve exact status:

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

Do not transform:

`planned protest`

into:

`protest`

Do not transform:

`alleged training`

into:

`training occurred`

Do not transform:

`threatened attack`

into:

`attack`

---

# Legal-status discipline

Preserve exact legal stage:

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

Do not upgrade one into another.

Examples:

`police questioned person`

≠

`person arrested`

`investigation opened`

≠

`indictment filed`

---

# Official response

Record response where relevant:

- NONE IDENTIFIED
- POLICE AWARE
- POLICE CHECK
- INVESTIGATION
- ARREST
- PROSECUTOR REVIEW
- CHARGE
- INDICTMENT
- COURT ACTION
- SECURITY MEASURE
- PUBLIC WARNING
- OTHER

An official response may increase confidence in occurrence.

It does not automatically confirm motive or guilt.

---

# Incident pattern analysis

For every relevant incident test whether it is:

- ISOLATED
- REPEAT OF SAME TYPE
- LOCAL CLUSTER
- MULTI-LOCATION CLUSTER
- EMERGING PATTERN
- COORDINATED PATTERN
- UNKNOWN

---

## ISOLATED

No meaningful related incidents identified.

---

## REPEAT OF SAME TYPE

A similar incident exists, but linkage remains unclear.

---

## LOCAL CLUSTER

Several distinct incidents occur in the same limited area within a meaningful time window.

---

## MULTI-LOCATION CLUSTER

Similar incidents occur across several locations.

---

## EMERGING PATTERN

Evidence indicates meaningful repetition, common targeting, common actors, or common mechanism.

---

## COORDINATED PATTERN

Use only when coordination is supported by evidence.

Do not infer coordination from similarity alone.

---

# Pattern variables

Assess:

- frequency;
- severity;
- target similarity;
- geographic proximity;
- timing;
- actor overlap;
- method similarity;
- motive similarity;
- communication evidence;
- retaliation;
- copycat behavior.

---

# Retaliation status

Classify where relevant:

- NONE IDENTIFIED
- POSSIBLE
- PROBABLE
- CONFIRMED
- NOT APPLICABLE

A second incident is not automatically retaliation.

Look for:

- explicit statements;
- timing;
- target relationship;
- actor linkage;
- claimed motive.

---

# Copycat status

Classify:

- CONFIRMED
- PROBABLE
- POSSIBLE
- UNCONFIRMED
- NONE DEMONSTRATED

Similar method alone does not prove copying.

---

# Geographic spread

Classify:

- NONE
- POSSIBLE
- CONFIRMED
- UNKNOWN

Spread requires distinct underlying incidents in additional locations.

More reporting from additional locations does not prove spread.

---

# Escalation relevance

For each significant incident determine whether it represents:

- NO CHANGE
- PRESSURE SIGNAL
- LIMITED WORSENING
- MATERIAL WORSENING
- ACUTE DETERIORATION
- UNCERTAIN

This is an internal analytical aid.

It does not mechanically determine topic assessment.

---

# Required escalation mechanism

Before using an incident to support:

`LIMITED ESCALATION`

or:

`ESCALATING`

state internally:

PREVIOUS CONDITION
→ NEW INCIDENT OR INCIDENT CHANGE
→ CHANGED RISK

Examples:

single isolated vandalism case
→ second similar attack against same target category
→ increased probability of local pattern formation

or:

verbal hostility
→ verified physical attack
→ increased severity of confrontation

or:

local incident
→ retaliatory incident in second municipality
→ increased geographic and self-reinforcing escalation risk

Bad reasoning:

serious incident occurred
→ escalation

A serious event can remain isolated.

---

# Topic mapping

Map every incident only to topics genuinely affected.

Possible linked topics:

- `TOP-BIH-TENSION-ESCALATION`
- `TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`
- `TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`
- `TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`
- `TOP-BIH-FOREIGN-PRESENCE`
- `TOP-KOSOVO-BIH-SPILLOVER`

---

# Primary topic

Assign one primary topic when possible.

Do not assign all six topics merely because an incident is serious.

---

# Secondary topics

Assign only when a distinct analytical linkage exists.

Example:

Verified attack with probable ethnic motive
→ primary:
`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

If a coordinated false narrative then amplifies the event:
→ secondary:
`TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`

Do not infer cross-topic linkage from temporal overlap.

---

# Cross-topic linkage evidence

A cross-topic link may be:

- CONFIRMED
- STRONGLY INDICATED
- POSSIBLE
- UNCONFIRMED
- NONE DEMONSTRATED

Use evidence such as:

- same actors;
- same organization;
- same infrastructure;
- direct communications;
- common financing;
- explicit causal sequence;
- verified mobilization transfer.

---

# Information-enabled incident discipline

When an offline incident may be linked to information activity distinguish:

- exposure to narrative;
- amplification;
- mobilization call;
- physical gathering;
- incident.

Do not assume online content caused offline behavior merely because it preceded it.

---

# Kosovo spillover discipline

For Kosovo-related incidents classify:

- DIRECT
- STRONG INDIRECT
- POSSIBLE INDIRECT
- RHETORICAL PARALLEL ONLY
- NO DEMONSTRATED SPILLOVER

A Kosovo mention does not create spillover.

A transfer mechanism is required.

---

# Foreign-link discipline

For suspected foreign-linked incident distinguish:

- FOREIGN NATIONALITY
- FOREIGN ORIGIN
- FOREIGN CONTACT
- FOREIGN ORGANIZATIONAL LINK
- FOREIGN MATERIAL SUPPORT
- FOREIGN OPERATIONAL SUPPORT
- FOREIGN DIRECTION
- FOREIGN CONTROL

These are not interchangeable.

---

# Radical / paramilitary discipline

Do not label an incident:

`PARAMILITARY`

without evidence of relevant characteristics such as:

- organized structure;
- hierarchy;
- training;
- coercive capability;
- weapons access;
- operational role.

Military-style clothing alone is insufficient.

---

# Training incident discipline

Distinguish:

- FITNESS
- SPORT
- AIRSOFT
- HUNTING
- SHOOTING PRACTICE
- CIVIL PROTECTION
- MILITARY-STYLE TRAINING
- TACTICAL TRAINING
- WEAPONS TRAINING
- OPERATIONAL REHEARSAL
- UNKNOWN

Do not use:

`PARAMILITARY TRAINING`

without sufficient evidence.

---

# Camp incident discipline

For alleged camp activity record:

- location;
- date;
- organizer;
- participants;
- recurring use;
- instructors;
- training type;
- weapons evidence;
- official response;
- source chain.

A remote gathering is not automatically a training camp.

Unverified camp allegations should remain:

`UNCONFIRMED SIGNAL`

until stronger evidence emerges.

---

# Protest incident discipline

Distinguish:

- ANNOUNCED
- PLANNED
- OCCURRED PEACEFULLY
- DISRUPTED
- CONFRONTATIONAL
- CLASHES
- VIOLENT
- CANCELLED

Do not treat a planned protest as an occurred event.

---

# Security deployment discipline

For police, EUFOR, military, or other security deployment identify:

- routine or exceptional;
- stated reason;
- scale;
- location;
- duration;
- change from baseline.

Routine deployment must not be treated as escalation.

---

# Historical incident discipline

An older incident discovered today is not a current incident.

Record:

- actual incident date;
- discovery date.

Use it as:

- BACKGROUND;
- PATTERN CONTEXT;
- HISTORICAL COMPARISON;

unless a new current development changes its relevance.

---

# Recycled-content discipline

For images, videos, or claims:

check whether content is:

- current;
- old;
- from another country;
- from another incident;
- edited;
- mislabeled.

Do not create a new incident from recycled media.

---

# Publication discipline

The final daily brief does not need to publish the full internal incident record.

Publish only analytically necessary information.

Normally include:

- what occurred;
- where;
- factual status;
- relevant motive status;
- why it matters;
- what remains uncertain.

Avoid drowning the brief in incident metadata.

---

# Negative findings

Valid findings include:

- no new distinct incidents identified;
- no repeat pattern demonstrated;
- no ethnic motive confirmed;
- no geographic spread identified;
- no organizational linkage demonstrated;
- no Kosovo spillover demonstrated;
- no foreign support demonstrated.

Negative findings are analytically valuable.

Do not manufacture incidents or patterns to fill a topic section.

---

# Incident inclusion threshold

Include an incident in the final daily brief when at least one applies:

- materially affects a monitored topic;
- changes current risk assessment;
- represents a meaningful new pattern;
- increases severity;
- demonstrates repetition;
- demonstrates geographic spread;
- introduces a new capable actor;
- shows organizational growth;
- has significant cross-topic relevance;
- requires explicit monitoring due to plausible high-impact risk.

Do not include merely because:

- it received many articles;
- a politician commented;
- it was emotionally striking;
- it fits a broad keyword.

---

# Incident exclusion rule

Normally exclude from the final brief:

- duplicates;
- ordinary unrelated crime;
- repeated reporting;
- unsupported speculation;
- minor personal disputes without topic relevance;
- old incidents presented as current;
- reactions without analytical consequence;
- politically amplified but non-relevant events.

The information may still be retained internally as context.

---

# Incident update rule for daily monitoring

When an incident already appeared in an earlier monitoring window:

do not present it as new unless a meaningful change occurred.

Use language such as:

- „ново развитие по вече известен инцидент“
- „полицията потвърди“
- „мотивът остава непотвърден“
- „прокуратурата започна производство“
- „първоначалното твърдение беше опровергано“

Do not reset the incident history each day.

---

# Daily incident audit

Before finalizing each topic assessment ask:

1. How many source items were found?
2. How many distinct underlying incidents remain after deduplication?
3. Which incidents actually occurred inside the monitoring window?
4. Which are older incidents newly reported today?
5. Which items are only updates?
6. Which are reactions?
7. Which are duplicates?
8. Is incident existence verified?
9. Is motive separately classified?
10. Are severity and significance separated?
11. Are casualty figures stable?
12. Are weapons claims verified?
13. Are actor identities preserved at correct legal status?
14. Are local competent authorities checked?
15. Are source chains genuinely independent?
16. Is there a repeat pattern?
17. Is geographic spread real?
18. Is retaliation demonstrated?
19. Is coordination demonstrated?
20. Is cross-topic linkage demonstrated?
21. Is the escalation mechanism explicit?
22. Would the assessment remain the same if duplicate media coverage were removed?
23. Would the assessment remain the same if unconfirmed motive claims were removed?
24. Are old incidents being mistaken for current events?
25. Are planned actions being mistaken for occurred actions?

---

# Final incident normalization rule

Before an incident contributes to:

- DAILY ASSESSMENT;
- SIGNIFICANCE;
- OVERALL DAILY ASSESSMENT;
- CROSS-TOPIC PATTERN;

the monitor must be able to answer:

**What exactly happened?**

**When did it happen?**

**Where did it happen?**

**How many distinct incidents are there?**

**What is verified?**

**What remains alleged?**

**What is the motive status?**

**What materially changed?**

**Why does this change risk?**

If these questions cannot be answered with sufficient confidence:

downgrade the analytical weight of the incident.

Prefer:

`INSUFFICIENT DATA`

over false precision.