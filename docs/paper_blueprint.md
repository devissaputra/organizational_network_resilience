# Paper Blueprint

## Working title

**When Communication Networks Depend on Key Actors: A Stress Test of Structural Knowledge-Continuity Risk in the Enron Email Network**

Alternative title:

**Targeted Actor Loss and Communication-Network Resilience: An L&D-Oriented Secondary Analysis of the Enron Email Hypergraph**

## Paper identity

This should be written as a focused Learning and Development, knowledge continuity, and organizational network analysis paper.

It is not a paper claiming that email communication equals organizational knowledge.

The contribution is a transparent structural stress-test framework for identifying communication-network dependence on highly connected actors and translating that evidence cautiously into knowledge-continuity questions.

## One sentence contribution

Using the Enron email hypergraph, the study shows that static removal of highly connected communication actors degrades global accessibility much more rapidly than same-count random loss, while explicitly separating structural network vulnerability from direct claims about employee knowledge or performance.

## Draft abstract

Organizations can lose communication continuity when central actors leave, but headcount loss alone does not capture the structural consequences of who becomes unavailable. This study evaluates communication-network resilience using the Enron temporal email hypergraph distributed through XGI and Zenodo. The released source contains 148 nodes and 10,885 timestamped email hyperedges. Hyperedges are projected into an undirected simple co-participation graph with 2,583 edges and baseline global efficiency of 0.5601. Actors are ranked once by projection degree, and static targeted removal is compared with 200 version-stable same-count comparator draws at k = 5, 10, 15, 20, and 30. Targeted retained efficiency declines monotonically from 0.9735 at k = 5 to 0.8608 at k = 30, while the random mean remains between 0.9917 and 0.9978. The targeted-versus-random mean gap widens from 0.0243 to 0.1309, and the targeted result lies below the released random 5th-percentile order-statistic bound at all five stress levels. The findings indicate structural dependence on highly connected actors under the released network operationalization. The paper interprets this as a diagnostic signal for knowledge-continuity investigation rather than direct evidence of tacit knowledge, expertise, employee value, or causal organizational performance loss.

## Introduction logic

### Paragraph 1: L&D and continuity problem

Turnover, absence, succession transitions, and organizational change can interrupt access to people who connect otherwise distant parts of a workplace communication structure.

### Paragraph 2: headcount limitation

Two organizations can lose the same number of employees but experience very different structural disruption depending on which communication positions disappear.

### Paragraph 3: measurement opportunity

Organizational network analysis provides a way to stress-test structural access patterns before inferring what intervention might be appropriate.

### Paragraph 4: construct caution

Communication ties are not direct observations of knowledge. Structural vulnerability should therefore be treated as diagnostic evidence rather than a knowledge score.

### Paragraph 5: contribution

This study compares static degree-targeted actor loss with a seeded random-loss distribution and evaluates how the resilience gap changes across increasing stress levels.

## Research questions

**RQ1.** How does retained global efficiency change under static degree-targeted actor removal?

**RQ2.** How does targeted loss compare with same-count random loss?

**RQ3.** Does the targeted-versus-random mean gap widen with removal level?

**RQ4.** Does targeted retained efficiency remain below the lower tail of the random comparator?

## Data section

Report:

- XGI / Zenodo email-enron v0.1;
- DOI 10.5281/zenodo.21909507;
- 148 nodes;
- 10,885 timestamped hyperedges;
- one 143-node component and five isolates in the source description;
- historical Enron provenance;
- no attachments;
- historical cleaning, correction, deletion, and redaction caveats.

## Network construction section

Explain:

- node identity;
- hyperedge meaning;
- undirected simple projection;
- duplicate removal inside events;
- repeated-event ties collapsed;
- projection edge count 2,583.

Discuss explicitly what projection discards:

- direction;
- frequency;
- time;
- higher-order structure;
- content.

## Resilience metric

Define global efficiency and cite Latora and Marchiori.

Define retained efficiency as the ratio to intact-network efficiency.

Make clear that values above 1 are mathematically possible after actor removal.

## Attack design

### Targeted

Static intact-network degree ranking.

### Random

200 seeded same-count samples per stress level.

### Stress levels

5, 10, 15, 20, 30 actors.

Also report the corresponding network shares:

3.4%, 6.8%, 10.1%, 13.5%, 20.3%.

## Results structure

### 1. Baseline network

Nodes, hyperedges, incidences, projection edges, baseline efficiency.

### 2. Stress curve

Show targeted curve and random comparator band.

### 3. Gap growth

Report:

```text
0.0243 → 0.0506 → 0.0726 → 0.0968 → 0.1309
```

### 4. Lower-tail diagnostic

Targeted result is below random p05 at all five levels.

## Key k = 30 result

At removal of 30 actors:

- removal share = 20.3%;
- targeted retained efficiency = 0.8608;
- random mean = 0.9917;
- random p05 = 0.9572;
- random p95 = 1.0304;
- gap vs random mean = 0.1309.

Do not translate 0.1309 into an equivalent business-performance loss.

## Discussion

### Structural interpretation

The projection is disproportionately dependent on actors with high intact-network degree.

### L&D interpretation

The result can motivate investigation of succession, cross-training, mentoring, documentation, communities of practice, and onboarding access.

### Decision-support interpretation

Network diagnostics should identify where to ask questions, not automatically prescribe who is critical or which intervention to fund.

### Metric interpretation

Global efficiency captures shortest-path accessibility, not knowledge quality or volume.

## Limitations

Include at least:

1. historical Enron setting;
2. core-address subset rather than all employees;
3. email activity only;
4. no message content;
5. no attachments;
6. historical redactions and cleaning;
7. undirected projection;
8. unweighted projection;
9. temporal information collapsed;
10. higher-order information collapsed;
11. static degree ranking;
12. one network metric;
13. 200 rather than exhaustive random draws;
14. no causal intervention;
15. no direct learning, expertise, or performance outcomes.

## Figures

**Figure 1. Resilience stress-test curve.**  
Targeted retained efficiency against random mean and random 5th to 95th percentile band at all five removal levels.

**Figure 2. Empirical processing pipeline.**  
Zenodo hypergraph, projection, baseline efficiency, degree ranking, targeted and random removal, diagnostics, bounded L&D interpretation.

**Figure 3. Resilience gap growth.**  
Targeted-versus-random mean gap across stress levels.

**Figure 4. Evidence and construct boundary.**

## Tables

**Table 1.** Dataset and network baseline.  
**Table 2.** Complete five-level resilience results.  
**Table 3.** Threats to validity and possible future sensitivity analyses.

## Writing rules

- Say **communication actor**, not knowledge holder.
- Say **potential information access**, not knowledge flow as an observed fact.
- Say **static degree-targeted removal**, not optimal attack.
- Distinguish structural resilience from organizational performance.
- Do not describe random comparator bands as confidence intervals.
- Do not convert the descriptive comparator into a causal treatment effect.
- Do not call the analysis preregistered.
- Keep the Enron external-validity limitation visible.
- Frame L&D actions as investigation or intervention candidates, not conclusions generated directly by the network.

## Completion checklist

A manuscript draft is ready for external feedback when:

- every numerical claim matches the released CSV and JSON;
- source dimensions and provenance match Zenodo;
- global efficiency is properly cited;
- projection losses are described explicitly;
- static ranking is stated;
- random-band construction is stated;
- all five stress levels are reported;
- L&D interpretation remains inside the construct boundary;
- limitations are explicit;
- the repository release or commit is cited.
