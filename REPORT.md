# Scientific Report

## Organizational Communication Resilience Under Key-Actor Loss

### Executive summary

Organizations often depend on a small number of highly connected people to move information across teams. When those people leave, become unavailable, or stop participating in a communication network, the structural pathways through which information can potentially travel may become less efficient.

This study examines that vulnerability using the Enron temporal email hypergraph distributed through XGI and Zenodo. The released dataset contains 148 nodes and 10,885 timestamped email hyperedges. Each hyperedge represents the sender and recipients associated with an email event among a core set of Enron addresses.

The analysis projects those hyperedges into an undirected employee co-participation graph. It then asks a deliberately narrow resilience question:

**How much does network-level communication accessibility decline when highly connected actors are removed, compared with removing the same number of actors at random?**

The baseline projection contains 2,583 undirected edges and has global efficiency 0.5601. Actors are ranked once by degree in the intact projection. Static degree-targeted removal is then compared with 200 seeded same-count random removal draws at k = 5, 10, 15, 20, and 30.

At every tested removal level, targeted removal produces lower retained global efficiency than the 5th percentile of the random comparator. At k = 5, targeted retained efficiency is 0.9735 versus a random mean of 0.9973. At k = 30, targeted retained efficiency falls to 0.8608 while the random mean remains 0.9912.

The targeted-versus-random mean gap therefore increases from 0.0238 at k = 5 to 0.1304 at k = 30.

This pattern supports a structural vulnerability interpretation: the projected communication network is more sensitive to the loss of highly connected actors than to same-count random actor loss under this operationalization.

The study does **not** show that highly connected email actors possess unique knowledge, that organizational performance would fall by the same amount, or that targeted departures cause learning failure. Email connectivity is used only as a proxy for potential communication access.

The practical Learning and Development contribution is a measurement framework for thinking about knowledge continuity risk. It shows how an organization could distinguish ordinary turnover exposure from structural dependence on highly connected communication actors before deciding whether cross-training, succession planning, documentation, communities of practice, or mentoring interventions are warranted.

### Research questions

1. How quickly does retained global efficiency decline under static degree-targeted actor removal?
2. How does targeted loss compare with same-count random actor loss?
3. Does the targeted-versus-random resilience gap increase as more actors are removed?
4. Is the targeted result consistently outside the lower tail of the released random comparator?

### Data source

Canonical source:

**email-enron temporal hypergraph, XGI / Zenodo**

- dataset version: v0.1
- Zenodo DOI: 10.5281/zenodo.21909507
- published: 12 August 2026
- source file: `email-enron.json`
- pinned MD5: `3666af1fc5a190d93f7fd98cff58e283`

The Zenodo record reports:

- 148 nodes;
- 10,885 timestamped hyperedges;
- one connected component of 143 nodes;
- five isolated nodes.

The dataset represents email communication among a core set of Enron addresses. A hyperedge contains the sender and recipients of an email event.

The original Enron corpus was made public during the Federal Energy Regulatory Commission investigation and later underwent substantial correction and cleaning. The released XGI dataset does not include attachments and reflects historical redaction and data-cleaning decisions.

### Unit of analysis

The raw observational unit is a timestamped email hyperedge.

The resilience analysis is performed on an undirected simple projection in which two nodes are adjacent if they co-occur in at least one email hyperedge.

Repeated recipients within one event are deduplicated before projection.

### Why a projection is used

A simple graph projection makes standard shortest-path global efficiency available as a transparent resilience metric.

That choice has a cost: it discards higher-order structure, direction, repeated interaction frequency, temporal order, and message content.

The release therefore treats the projection as one explicit operationalization rather than a complete representation of organizational communication.

### Network construction

The released projection contains:

- 148 nodes;
- 2,583 undirected projection edges;
- baseline global efficiency 0.5601.

Global efficiency is the average inverse shortest-path distance over node pairs. Disconnected pairs contribute zero.

The metric follows the network-efficiency concept introduced by Latora and Marchiori.

### Resilience operationalization

The primary outcome is:

```text
retained efficiency =
global efficiency after removal
/
global efficiency of the intact projection
```

The ratio is recomputed among surviving nodes.

Because the denominator and survivor set differ conceptually, the retained-efficiency ratio is **not bounded above by 1**. Removing peripheral nodes can occasionally increase average accessibility among the remaining nodes.

It should therefore not be called a survival percentage or an organizational performance score.

### Targeted removal

Actors are ranked by degree in the intact projection.

For each k in:

```text
5, 10, 15, 20, 30
```

the top k actors from that original ranking are removed.

This is a **static degree-targeted stress test**.

The actors are not re-ranked after each removal.

### Random comparator

At each removal level, 200 same-count random actor sets are sampled using seed 20260925.

For each k, the release reports:

- random mean retained efficiency;
- empirical 5th-percentile order-statistic bound;
- empirical 95th-percentile order-statistic bound;
- difference between random mean and targeted result;
- difference between random 5th percentile and targeted result.

The random comparator is descriptive. It is not presented as a causal design or preregistered statistical test.

### Primary results

| Actors removed | Removed share | Targeted retained efficiency | Random mean | Random 5th percentile | Random 95th percentile | Gap vs random mean |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 3.4% | 0.9735 | 0.9973 | 0.9860 | 1.0101 | 0.0238 |
| 10 | 6.8% | 0.9465 | 0.9970 | 0.9808 | 1.0139 | 0.0505 |
| 15 | 10.1% | 0.9245 | 0.9968 | 0.9761 | 1.0221 | 0.0723 |
| 20 | 13.5% | 0.8986 | 0.9960 | 0.9710 | 1.0197 | 0.0974 |
| 30 | 20.3% | 0.8608 | 0.9912 | 0.9606 | 1.0288 | 0.1304 |

### Targeted degradation

The targeted curve declines monotonically:

```text
0.9735 → 0.9465 → 0.9245 → 0.8986 → 0.8608
```

By k = 30, removing 20.3% of actors from the intact network under the static degree rule reduces retained global efficiency by 13.9% relative to the intact baseline ratio.

### Random-loss behavior

The random mean remains close to the intact baseline:

```text
0.9973 → 0.9970 → 0.9968 → 0.9960 → 0.9912
```

At k = 30, mean random retained efficiency is still 0.9912.

The comparison is not that random removal has no effect. Rather, under this metric and these draws, the average structural accessibility among surviving nodes remains much closer to the intact value than under degree-targeted loss.

### Widening resilience gap

The difference between the random mean and targeted retained efficiency is:

```text
0.0238 → 0.0505 → 0.0723 → 0.0974 → 0.1304
```

The gap increases at every tested removal level.

The total increase from k = 5 to k = 30 is 0.1066.

### Distributional diagnostic

At all five tested k values, the targeted retained-efficiency value is below the random 5th-percentile order-statistic bound.

This is stronger descriptive evidence than comparing only two means because it shows the targeted result lies below the lower tail of the released 200-draw comparator at every tested stress level.

It still should not be presented as a formal p value.

### Learning and Development interpretation

The most defensible L&D interpretation is about **knowledge continuity exposure**, not measured knowledge.

A communication network that depends heavily on a small number of central actors can indicate where an organization may want to investigate:

- succession coverage;
- cross-training;
- mentoring redundancy;
- documentation practices;
- communities of practice;
- onboarding access to expertise;
- boundary-spanning roles;
- concentration of communication load.

The network stress test can help identify where questions should be asked.

It does not answer whether the central actors possess unique expertise, whether their information is correct, or whether learning interventions would improve resilience.

### Why the result matters

A simple headcount view treats all actor loss as equivalent.

The released stress test shows that, structurally, the identity of the removed actors matters much more than the number alone.

That distinction is important for workforce resilience. An organization can have the same turnover count under two scenarios while facing very different communication-network exposure.

### What this study supports

The release supports these descriptive statements:

- the pinned source contains 148 nodes and 10,885 timestamped hyperedges;
- the released undirected projection contains 2,583 edges;
- baseline global efficiency is 0.5601;
- static degree-targeted removal produces a monotonically decreasing retained-efficiency curve;
- targeted retained efficiency is below the random mean at every tested k;
- targeted retained efficiency is below the released random 5th percentile at every tested k;
- the targeted-versus-random mean gap increases from 0.0238 to 0.1304.

### What this study does not support

The release does not establish:

- tacit knowledge ownership;
- expertise quality;
- employee performance;
- learning effectiveness;
- causal knowledge transfer;
- business performance loss;
- individual replaceability;
- optimal succession decisions;
- generalization to contemporary organizations.

### Threats to validity

**Construct validity.** Email co-participation represents observed communication connectivity, not knowledge itself.

**Projection validity.** Hypergraph projection discards higher-order, directed, weighted, and temporal information.

**Attack-model validity.** The released targeted rule uses static degree ranking. Adaptive re-ranking could yield a different curve.

**Metric validity.** Global efficiency captures shortest-path accessibility and is only one dimension of network resilience.

**Comparator validity.** The random distribution is based on 200 seeded draws, not an exhaustive enumeration.

**Historical validity.** Enron is a historically unusual organization and cannot be treated as a generic modern workplace.

**Data validity.** The corpus has known historical cleaning, correction, deletion, and redaction processes.

**Causal validity.** The analysis is a structural stress test on observed historical network data, not an intervention or causal study.

### Reproducibility

Offline verification:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

Source verification:

```bash
python scripts/fetch_and_analyze.py --check
```

Release regeneration:

```bash
python scripts/fetch_and_analyze.py --write
python scripts/generate_figures.py
```

The source rebuild verifies the pinned Zenodo file MD5 before analysis. There is no synthetic fallback.

### Research integrity statement

This is a secondary analysis of public historical communication data.

The analysis plan was documented after source selection and is not a preregistration.

The repository deliberately separates network structure from organizational knowledge claims. Communication connectivity is treated as a proxy for potential information access, and the L&D interpretation is limited to structural knowledge-continuity risk and diagnostic use.
