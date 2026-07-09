# SEARCH STRATEGY

## Purpose

This file defines the external search strategy for the BiH Daily Topic Monitor.

The purpose is to ensure that external media and official-source monitoring is:

- systematic;
- multilingual;
- topic-specific;
- geographically aware;
- resistant to keyword bias;
- resistant to media-volume bias;
- focused on meaningful developments;
- capable of finding developments missed by `#bih-events-log`.

This file does not replace:

- `MONITORED_TOPICS.md`;
- `SOURCES.md`;
- `CLAUDE.md`;
- `DAILY_BRIEF_STANDARD.md`.

It defines how external discovery should be performed when a web, browser, search, research, MCP, Perplexity, or equivalent external-search capability is technically available.

---

# Core search principle

Do not use one broad query per topic and assume the topic was adequately searched.

Every active daily search should combine:

1. DIRECT TOPIC SEARCH
2. ACTOR SEARCH
3. INSTITUTIONAL SEARCH
4. INCIDENT OR INDICATOR SEARCH
5. GEOGRAPHIC SEARCH
6. CONTRADICTION SEARCH
7. OFFICIAL CONFIRMATION SEARCH

The monitor must search for developments, not merely keywords.

Example:

Searching only:

`Bosnia paramilitary groups`

is insufficient.

The monitor should also search conceptually related indicators such as:

- training;
- recruitment;
- camps;
- armed gatherings;
- extremist networks;
- veterans' networks;
- weapons seizures;
- cross-border organizational contacts;
- police investigations.

Keyword appearance alone does not prove topic relevance.

---

# Search availability rule

Use this strategy only when external search capability is actually accessible.

If external search capability is unavailable:

- do not pretend these searches were performed;
- do not claim comprehensive media monitoring;
- do not fabricate search results;
- do not fabricate links;
- do not fabricate source access.

State the limitation according to the operating rules in `CLAUDE.md`.

---

# Daily search window

Default daily discovery window:

- current operational date;
- from 00:00 local operational time;
- to actual routine execution time.

Prioritize:

- developments occurring today;
- publications today;
- material updates today;
- new confirmations today;
- new contradictions today.

Older material may be included only when today it receives:

- new official confirmation;
- new evidence;
- new actor involvement;
- meaningful update;
- contradiction;
- implementation step.

Do not recycle old developments merely because a new article repeats them.

---

# Search recency discipline

For every result ask:

- When did the underlying event occur?
- When was the article published?
- Is the article reporting something new?
- Is the article repeating an older event?
- Is this an update?
- Is this commentary?
- Is the source using an old video, photo, or statement?

Publication date is not identical to event date.

---

# Language strategy

Where technically possible search in:

- Bosnian;
- Croatian;
- Serbian Latin;
- Serbian Cyrillic;
- English.

For Kosovo-related spillover also search in Albanian when technically possible.

Do not assume that equivalent terms are identical across languages.

Use language variants and concept variants.

---

# General language terms

## Bosnia and Herzegovina

Use variants such as:

- Bosna i Hercegovina
- BiH
- Bosna
- Босна и Херцеговина
- Bosnia and Herzegovina

## Republika Srpska

Use variants such as:

- Republika Srpska
- RS
- Република Српска

## Federation of BiH

Use variants such as:

- Federacija BiH
- FBiH
- Federacija Bosne i Hercegovine

## Security

Use concept variants such as:

- sigurnost
- bezbjednost
- bezbednost
- sigurnosni incident
- bezbjednosni incident
- security incident
- threat
- prijetnja
- pretnja

---

# Search execution model

For every registered topic use a multi-pass search.

Do not perform only one search query.

Use the following sequence.

---

# PASS 1 — Broad daily discovery

Purpose:

Identify major developments that may already be widely reported.

Search combinations of:

- topic concept;
- Bosnia and Herzegovina;
- current date or recent-day filter;
- major actors;
- incident terms.

Examples:

    BiH sigurnost incident danas

    Bosna napetosti institucije

    Republika Srpska bezbjednost incident

    Bosnia security tensions today

Use broad discovery only as the first layer.

Do not stop after this pass.

---

# PASS 2 — Official-source discovery

Purpose:

Find primary confirmation, institutional measures, investigations, warnings, decisions, or formal statements.

Search relevant institutions from `SOURCES.md`.

Possible search patterns:

    site:sipa.gov.ba [term]

    site:msb.gov.ba [term]

    site:tuzilastvobih.gov.ba [term]

    site:euforbih.org [term]

    site:ohr.int [term]

When domain filtering is technically supported, use it.

When not supported, search institution name plus development terms.

Official-source search should be topic-specific.

---

# PASS 3 — Local and geographic discovery

Purpose:

Find incidents that may not yet appear in national media.

For incident-related topics search:

- municipality;
- city;
- settlement;
- canton;
- police jurisdiction;
- local religious object;
- memorial location;
- border area.

Example structure:

    [municipality] incident policija

    [settlement] napad

    [municipality] vjerski objekat incident

    [canton] sigurnosni incident

    [police administration] saopštenje

Do not rely only on Sarajevo- or Banja Luka-based national media.

---

# PASS 4 — Actor and network search

Purpose:

Detect activity by specific organizations, political actors, informal networks, foreign-linked structures, radical groups, or recurring intermediaries.

Search:

- actor name;
- organization name;
- known aliases;
- acronym;
- local-language spelling;
- Cyrillic spelling where relevant;
- associated locations;
- associated events.

Do not infer network linkage merely because two actors appear in the same search result.

---

# PASS 5 — Contradiction and verification search

Purpose:

Actively search against the first apparent narrative.

For important claims search terms such as:

- demanti
- negira
- netačno
- nije tačno
- saopštenje
- policija
- tužilaštvo
- potvrđeno
- nepotvrđeno
- fact check
- false
- denied
- correction

For every HIGH or CRITICAL candidate ask:

- Is there denial?
- Is there official correction?
- Are casualty or incident numbers disputed?
- Is motive disputed?
- Is attribution disputed?
- Is date or location disputed?

Do not only search for confirming evidence.

---

# PASS 6 — Update search

Purpose:

Determine whether the development evolved during the monitoring window.

Search:

- actor + latest;
- incident + police;
- incident + prosecutor;
- event + update;
- location + latest;
- organization + statement;
- institution + response.

Possible local-language terms:

- novo
- najnovije
- ažurirano
- potvrđeno
- istraga
- reakcija
- nastavak
- saopštenje
- odgovor

Do not treat a minor wording change as a material update.

---

# PASS 7 — Cross-topic linkage search

Purpose:

Test whether separate developments are genuinely connected.

Search combinations of:

- actor A + actor B;
- organization + location;
- Kosovo + BiH;
- disinformation narrative + organization;
- foreign actor + local organization;
- radical group + incident;
- same narrative across platforms.

Only perform cross-topic linkage search when there is an evidence-based reason.

Do not manufacture linkage through broad associative searching.

---

# TOPIC-SPECIFIC SEARCH STRATEGY

---

# TOPIC 1

## TOPIC ID

`TOP-BIH-TENSION-ESCALATION`

## Topic focus

Political, institutional, social, ethnic, and security tension with potential escalation relevance.

## Primary search objective

Detect whether current developments indicate:

- movement from rhetoric to action;
- institutional confrontation;
- constitutional crisis indicators;
- mobilization;
- refusal to implement decisions;
- security measures;
- credible escalation warnings.

## Direct search concepts

Search combinations using:

- napetost
- tenzije
- kriza
- politička kriza
- institucionalna kriza
- blokada
- sukob institucija
- ustavna kriza
- eskalacija
- sigurnosna situacija
- bezbjednosna situacija
- protest
- mobilizacija
- prijetnja
- pretnja
- vanredne mjere
- pojačane mjere sigurnosti
- pojačane mjere bezbjednosti

English variants:

- Bosnia tensions
- institutional crisis BiH
- Bosnia escalation
- security warning Bosnia
- constitutional crisis Bosnia
- political confrontation BiH

## Actor and institution combinations

Search with:

- Presidency of BiH;
- Council of Ministers;
- Parliament of BiH;
- NSRS;
- Government of RS;
- Government of FBiH;
- Constitutional Court;
- EUFOR;
- OHR;
- SIPA;
- police institutions.

Examples:

    BiH institucionalna blokada danas

    NSRS kriza institucije BiH

    Predsjedništvo BiH blokada

    EUFOR sigurnosna situacija BiH

    OHR escalation Bosnia

## Escalation indicator searches

Search for:

- refusal to implement;
- withdrawal from institutions;
- emergency security measures;
- mass mobilization;
- serious protests;
- threats of violence;
- institutional nullification;
- parallel structures;
- constitutional confrontation.

Possible terms:

- odbija provesti
- neće provoditi
- povlačenje iz institucija
- napuštanje institucija
- vanredna sjednica
- krizni štab
- poništavanje odluke
- ne priznaje odluku
- mobilizacija
- masovni protest

## Exclusion discipline

Do not treat as escalation:

- routine political insults;
- repeated nationalist rhetoric;
- normal party conflict;
- old constitutional disputes without new action;
- media commentary without new fact.

---

# TOPIC 2

## TOPIC ID

`TOP-BIH-RADICAL-PARAMILITARY-ACTIVITY`

## Topic focus

Activity by radical, extremist, violent, paramilitary, or potentially violence-oriented organizations and networks.

## Primary search objective

Detect:

- organization;
- recruitment;
- training;
- weapons;
- mobilization;
- cross-border contacts;
- operational preparation;
- police interest;
- investigations.

## Direct search concepts

Bosnian/Croatian/Serbian Latin:

- paravojna grupa
- paravojne formacije
- radikalna organizacija
- ekstremistička organizacija
- ekstremistička grupa
- nasilni ekstremizam
- obuka
- vojna obuka
- kamp
- trening kamp
- naoružana grupa
- uniformisana grupa
- regrutovanje
- vrbovanje
- mobilizacija
- oružje
- ilegalno oružje
- veteranska mreža
- radikalna mreža
- hapšenje
- istraga
- terorizam

Serbian Cyrillic variants where relevant:

- паравојна група
- паравојне формације
- радикална организација
- екстремистичка организација
- обука
- камп
- наоружана група
- регрутовање
- мобилизација
- оружје

English:

- Bosnia paramilitary group
- Bosnia extremist organization
- Bosnia radical network
- armed group Bosnia
- recruitment extremist Bosnia
- training camp Bosnia
- violent extremism BiH

## Concept-expansion searches

Do not search only explicit labels.

Also search:

- veterans;
- motorcycle groups;
- ultras;
- training associations;
- armed gatherings;
- military-style training;
- cross-border visits;
- foreign radical networks.

Only include when evidence shows actual relevance.

## Official confirmation searches

Prioritize combinations with:

- SIPA;
- MUP RS;
- FUP;
- cantonal police;
- prosecutors;
- Court of BiH.

Examples:

    SIPA ekstremizam

    MUP RS oružje grupa

    FUP radikalna organizacija

    Tužilaštvo BiH terorizam

## High-risk claim rule

For claims involving:

- paramilitary training;
- weapons;
- planned violence;
- terrorism;
- foreign operational coordination;

actively search for:

- official confirmation;
- court documents;
- police statements;
- genuinely independent corroboration.

Do not rely on one politically aligned outlet.

---

# TOPIC 3

## TOPIC ID

`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

## Topic focus

Interethnic incidents and security incidents with potential impact on community tension and stability.

## Primary search objective

Detect distinct incidents and determine:

- what happened;
- severity;
- location;
- motive status;
- repetition;
- geographic spread;
- official response.

## Direct incident terms

Search:

- incident
- sigurnosni incident
- bezbjednosni incident
- napad
- fizički napad
- prijetnja
- pretnja
- sukob
- pucnjava
- eksplozija
- oružje
- bomba
- vandalizam
- grafiti
- vjerski objekat
- verski objekat
- džamija
- crkva
- povratnik
- povratnici
- mezarje
- groblje
- spomenik
- provokacija
- nacionalistički incident
- međuetnički incident
- međunacionalni incident

English:

- interethnic incident Bosnia
- ethnic attack Bosnia
- religious site attack BiH
- returnee attack Bosnia
- security incident Bosnia

## Geographic search rule

For every detected incident search:

    [location] policija

    [location] MUP

    [location] tužilaštvo

    [location] incident

    [location] napad

Search the competent local police authority where identifiable.

## Motive verification search

Search specifically for:

- motiv
- etnički motiv
- nacionalna mržnja
- zločin iz mržnje
- policija motiv
- tužilaštvo motiv
- istraga motiv

Do not classify ethnic motive from identities alone.

## Repeat-pattern search

When an incident is found, search:

- same location;
- same community;
- same type of target;
- same symbolic date;
- similar incidents in preceding days.

Do not declare a pattern only because similar events exist historically.

---

# TOPIC 4

## TOPIC ID

`TOP-BIH-DISINFORMATION-FOREIGN-NETWORKS`

## Topic focus

Disinformation campaigns and activity of foreign-linked or externally connected organizations and networks affecting BiH.

## Primary search objective

Detect:

- false or manipulated claims;
- coordinated amplification;
- synchronized narratives;
- foreign-linked network activity;
- organized information influence;
- transition from online messaging to offline effects.

## Direct search concepts

Search:

- dezinformacije
- dezinformaciona kampanja
- dezinformacijska kampanja
- lažne vijesti
- lažne vesti
- manipulacija
- koordinisana kampanja
- koordinirana kampanja
- propaganda
- mreža naloga
- koordinisani nalozi
- koordinirani računi
- bot mreža
- strani uticaj
- strani utjecaj
- informacione operacije
- informacijske operacije
- hibridne prijetnje
- hibridne pretnje
- FIMI

English:

- Bosnia disinformation campaign
- coordinated influence Bosnia
- foreign information manipulation BiH
- influence network Bosnia
- coordinated accounts Bosnia
- foreign-linked organization BiH

## Narrative-target searches

Search developments involving narratives about:

- EUFOR;
- NATO;
- OHR;
- EU;
- USA;
- Russia;
- Ukraine;
- Kosovo;
- elections;
- ethnic communities;
- secession;
- war;
- foreign intervention.

Examples:

    EUFOR dezinformacije BiH

    NATO lažne vijesti Bosna

    Kosovo propaganda Republika Srpska

    Russia influence network Bosnia

## Coordination verification

For suspected campaigns search for:

- identical wording;
- same links;
- synchronized timing;
- shared channels;
- same administrators;
- cross-platform spread;
- fact-checking evidence;
- platform transparency.

Search specialist sources from `SOURCES.md`.

## Attribution rule

Do not search only for confirmation of foreign attribution.

Also search:

- denial;
- alternative origin;
- organic spread;
- domestic political source;
- satire;
- misquotation.

A false claim is not automatically foreign influence.

---

# TOPIC 5

## TOPIC ID

`TOP-BIH-FOREIGN-PRESENCE`

## Topic focus

Changes in foreign political, diplomatic, economic, organizational, religious, security, military, or information-related presence in BiH.

## Primary search objective

Detect measurable or strategically relevant changes in foreign presence.

## Direct search concepts

Search:

- delegacija
- posjeta
- poseta
- ambasada
- diplomatska aktivnost
- predstavništvo
- ured
- kancelarija
- centar
- sporazum
- saradnja
- suradnja
- investicija
- strateška investicija
- bezbjednosna saradnja
- sigurnosna suradnja
- vojna saradnja
- policijska saradnja
- organizacija
- fondacija
- vjerska organizacija
- religijska organizacija
- strani državljani
- strani predstavnici

English:

- foreign presence Bosnia
- foreign delegation BiH
- security cooperation Bosnia
- foreign organization Bosnia
- strategic investment Bosnia
- military cooperation BiH

## Country-specific search layer

Where relevant search combinations with:

- Russia;
- Serbia;
- Croatia;
- Turkey;
- China;
- United States;
- EU member states;
- Gulf states;
- Iran;
- other relevant actors.

Examples:

    Rusija organizacija BiH

    Srbija bezbjednosna saradnja RS

    Kina strateška investicija BiH

    Turska organizacija Bosna

    Gulf investment Bosnia strategic

## Presence-change discipline

Search for evidence of:

- new office;
- new center;
- new personnel;
- new agreement;
- repeated high-level visits;
- funding;
- durable infrastructure;
- institutional partnership;
- expanded geographic reach.

Do not treat a routine diplomatic meeting as increased foreign presence.

## Security sensitivity rule

When claims involve:

- intelligence activity;
- covert structures;
- foreign security personnel;
- secret networks;

require especially strong corroboration.

---

# TOPIC 6

## TOPIC ID

`TOP-KOSOVO-BIH-SPILLOVER`

## Topic focus

Transfer of tension, narratives, mobilization, organizational networks, tactics, or security risk from Kosovo-related developments into BiH.

## Primary search objective

Detect a demonstrable BiH connection.

## Direct search concepts

Bosnian/Croatian/Serbian Latin:

- Kosovo BiH
- Kosovo Bosna
- Kosovo Republika Srpska
- Kosovo RS
- prelijevanje krize
- prelivanje krize
- prenos napetosti
- prenos tenzija
- sigurnosni rizik Kosovo BiH
- bezbjednosni rizik Kosovo RS
- regionalna eskalacija
- mobilizacija Kosovo
- protest Kosovo BiH
- nacionalističke grupe Kosovo BiH

Serbian Cyrillic:

- Косово БиХ
- Косово Република Српска
- преливање кризе
- пренос тензија
- безбедносни ризик
- мобилизација

English:

- Kosovo Bosnia spillover
- Kosovo tensions Bosnia
- Kosovo crisis Republika Srpska
- regional spillover BiH
- Kosovo security impact Bosnia

Albanian where technically possible:

- Bosnja Kosovë tensione
- ndikim në Bosnje
- përshkallëzim rajonal
- grupe nacionaliste
- siguri Bosnje Kosovë

## Actor-link searches

Search for:

- same organization;
- same individual;
- same nationalist network;
- same veterans' network;
- same Telegram channel;
- same protest organizers;
- cross-border travel;
- shared messaging.

## Institutional reaction searches

Search combinations with:

- EUFOR;
- KFOR;
- EULEX;
- BiH security institutions;
- Serbian institutions;
- Kosovo institutions;
- police.

Examples:

    EUFOR Kosovo BiH

    KFOR Bosnia spillover

    MUP RS Kosovo sigurnost

    BiH security Kosovo tensions

## Spillover proof discipline

Look for:

- explicit action in BiH triggered by Kosovo;
- same network operating in both contexts;
- copied tactics;
- linked mobilization;
- synchronized messaging;
- local security measures;
- explicit institutional warning.

Do not classify ordinary commentary about Kosovo as spillover.

---

# Official-source query strategy

For every material candidate development identify the competent institution.

Possible routing examples:

## State-level security issue

Search:

- Ministry of Security BiH;
- SIPA;
- Prosecutor's Office of BiH;
- Court of BiH;
- Border Police;
- Directorate for Coordination of Police Bodies.

## RS incident

Search:

- MUP RS;
- relevant police administration;
- prosecutor;
- local authority.

## FBiH incident

Search:

- FUP;
- relevant cantonal MUP;
- prosecutor;
- local authority.

## International-security issue

Search:

- EUFOR;
- OHR;
- EU;
- US Embassy;
- OSCE;
- NATO where relevant.

## Kosovo-linked issue

Search:

- KFOR;
- EULEX;
- Kosovo Police;
- Serbian institutions;
- EU statements;
- BiH institutions.

---

# Priority-source targeting

Use `SOURCES.md` for source hierarchy.

Where technically possible, prioritize:

1. official source;
2. direct institutional source;
3. police/prosecution/court source;
4. direct actor statement;
5. multiple independent established media sources;
6. established single-source reporting;
7. specialist analysis;
8. local reporting;
9. social-media signal;
10. unverified claim.

Do not use this hierarchy mechanically.

Source role matters.

---

# Media diversity rule

For active or high-significance topics, avoid relying entirely on one media environment.

Where relevant search across:

- Sarajevo-based sources;
- RS-based sources;
- local sources;
- regional sources;
- international sources;
- official sources.

The purpose is not artificial political balance.

The purpose is:

- discovery diversity;
- contradiction detection;
- source-chain independence.

---

# Search query construction rules

Prefer short, targeted queries.

Bad:

    Tell me everything happening in Bosnia today about security, foreign influence, ethnic tensions and paramilitary organizations

Good:

    BiH sigurnosni incident danas

    MUP RS naoružana grupa

    Sarajevo etnički incident policija

    EUFOR sigurnosna situacija BiH

    Kosovo Republika Srpska mobilizacija

Use several targeted searches instead of one overloaded query.

---

# Query expansion rule

For each topic use:

- exact term;
- synonym;
- related behavior;
- institutional consequence;
- geographic variant.

Example:

Do not search only:

    paravojna grupa

Also search:

    obuka
    kamp
    naoružana grupa
    uniformisana grupa
    regrutovanje
    mobilizacija
    oružje
    veteranska mreža

Do not assume the correct article uses the analyst's preferred terminology.

---

# Named-entity expansion

When a relevant actor appears:

1. search exact full name;
2. search surname where distinctive;
3. search organization;
4. search local spelling;
5. search Cyrillic variant where relevant;
6. search linked location.

Do not broaden into unrelated actors without evidence.

---

# Event follow-up rule

For every HIGH or CRITICAL candidate development perform at least one follow-up search focused on:

- confirmation;
- contradiction;
- official response;
- update;
- second independent source.

Do not publish a high-significance claim based only on the first result when additional verification is technically possible.

---

# Local incident rule

For every potentially significant local incident:

1. identify exact location;
2. identify competent police jurisdiction;
3. search local authority;
4. search prosecutor if relevant;
5. search at least one independent media source when available.

This is especially important for:

`TOP-BIH-INTERETHNIC-SECURITY-INCIDENTS`

---

# Disinformation search rule

For suspected information campaigns perform separate searches for:

1. original claim;
2. earliest visible source;
3. amplification;
4. fact-check;
5. denial;
6. attribution evidence.

Do not jump directly from:

false claim

to:

coordinated campaign

or:

foreign campaign.

---

# Foreign presence search rule

For foreign-presence developments search separately for:

1. visit or event;
2. agreement;
3. institutional partner;
4. funding;
5. duration;
6. physical or organizational footprint;
7. follow-on activity.

One visit does not automatically equal increased presence.

---

# Cross-border linkage rule

For suspected cross-border activity search:

- both locations;
- same actor;
- same organization;
- same date range;
- transport or travel;
- official security response;
- shared narrative.

Do not infer cross-border linkage from ideological similarity alone.

---

# Social-media search discipline

When social-media content is accessible:

Use it for:

- discovery;
- primary actor statements;
- mobilization calls;
- organizational announcements;
- narrative propagation.

For each relevant post assess:

- authentic account?
- original post?
- current date?
- original location?
- primary or repost?
- evidence of real-world action?

Do not treat a post as proof that the claimed event occurred.

---

# Telegram search discipline

When Telegram monitoring becomes technically available:

Use it for:

- radical-network signals;
- mobilization calls;
- cross-border narratives;
- Kosovo-related spillover;
- information campaigns;
- organization announcements.

Unless authenticated primary material, classify as:

- SIGNAL;
- UNCONFIRMED CLAIM;
- NETWORK ACTIVITY EVIDENCE;
- NARRATIVE EVIDENCE.

A call for action is evidence that the call was published.

It is not evidence that action occurred.

---

# Search-result triage

Every discovered result should be internally triaged as one of:

- HIGH-RELEVANCE CANDIDATE
- MEDIUM-RELEVANCE CANDIDATE
- LOW-RELEVANCE CONTEXT
- DUPLICATE
- COMMENTARY
- UNCONFIRMED SIGNAL
- OUT OF SCOPE

Only HIGH-RELEVANCE and selected MEDIUM-RELEVANCE candidates should normally enter the final analytical candidate set.

---

# Candidate development record

For every meaningful candidate internally capture:

- DEVELOPMENT SUMMARY
- EVENT DATE
- PUBLICATION DATE
- SOURCE
- SOURCE TYPE
- PRIMARY SOURCE AVAILABLE: YES / NO
- TOPIC IDs
- NEW / UPDATE / REPEAT / COMMENTARY / SIGNAL / CONTRADICTED
- SIGNIFICANCE
- CONFIDENCE
- CORROBORATION STATUS
- CONTRADICTION STATUS
- LINK
- NOTES

This internal structure does not need to be published unless required.

---

# Deduplication rule

Deduplicate by underlying development.

Example:

- Klix reports incident;
- N1 reports same incident;
- local outlet reports same incident;
- police later confirms same incident.

This is one underlying development with:

- several reports;
- potentially stronger verification after police confirmation.

Do not count it as four incidents.

---

# Source-chain independence rule

Ask:

- Did outlet B independently verify?
- Or did outlet B copy outlet A?
- Are several outlets using the same agency?
- Are all reports based on one politician?
- Are all reports based on one anonymous source?

Apparent multiplicity is not necessarily independent corroboration.

---

# Negative search discipline

For significant claims actively search for disconfirmation.

Examples:

    [claim] demanti

    [actor] negira

    [incident] policija

    [incident] nije tačno

    [organization] fact check

    [claim] correction

This reduces confirmation bias.

---

# Coverage completeness check

Before ending external discovery, verify that every registered topic received at least one deliberate search pass when external search was technically available.

Do not assume:

no obvious result
means
no search required.

For each topic internally record:

- SEARCHED;
- NOT SEARCHED DUE TO TECHNICAL LIMITATION.

Never claim comprehensive coverage for a topic that was not searched.

---

# Empty-result discipline

If no meaningful development is found:

Do not invent activity.

Do not inflate marginal commentary.

Use:

`Няма съществено ново развитие.`

But distinguish:

- no meaningful development found;
- proof that no activity exists.

---

# Search stopping rule

Stop expanding searches when:

- meaningful developments are identified and sufficiently verified;
- additional results are repetitive;
- marginal searches produce only commentary;
- no further evidence changes confidence;
- all registered topics have received adequate deliberate coverage.

Do not maximize search volume for its own sake.

---

# Daily search audit

Before producing the final brief verify:

1. Every registered TOPIC ID was deliberately reviewed.
2. External search was used only if actually accessible.
3. Search was not limited to English.
4. High-significance candidates received follow-up verification.
5. Official sources were checked when relevant.
6. Local incidents were searched geographically.
7. Repeated reporting was deduplicated.
8. Source-chain independence was assessed.
9. Contradictory evidence was actively sought for major claims.
10. Publication date was not confused with event date.
11. Increased article volume was not treated as increased incident volume.
12. Ethnic motive was not inferred from identity alone.
13. Foreign influence was not inferred from nationality alone.
14. Kosovo spillover was not inferred from thematic similarity alone.
15. Radical or paramilitary labels were not inferred from political rhetoric alone.
16. Search limitations were disclosed honestly.
17. No source or link was fabricated.

---

# Final operating principle

External search exists to improve:

- discovery;
- verification;
- contradiction detection;
- pattern testing;
- confidence calibration.

It must not become a mechanism for:

- collecting maximum article volume;
- confirming a predetermined escalation thesis;
- amplifying unverified security claims;
- manufacturing connections between unrelated developments.

The correct output is not:

“More information was found.”

The correct output is:

“Meaningful developments were identified, verified as far as technically possible, deduplicated, classified, and assessed with calibrated uncertainty.”
