# Sources of the equational target bases

The target equations were checked against the printed originals, not only
their OCR, on October 17, 2026. No replay goal needs to be changed.

The references are:

1. C. A. Meredith and A. N. Prior, “Equational logic,” *Notre Dame Journal of
   Formal Logic* **9** (1968), 212–226.
   [Original article](https://doi.org/10.1305/ndjfl/1093893457).
2. A. N. Prior, “Corrigendum to C. A. Meredith's and my paper: ‘Equational
   logic’,” *Notre Dame Journal of Formal Logic* **10** (1969), 452.
   [Corrigendum](https://doi.org/10.1305/ndjfl/1093893794).

In the originals, `A` means disjunction and `K` means conjunction. In our
paper, these are `O` and `A`, respectively. In the original §3, `Cpq = ANpq`
abbreviates `A(N(p),q)`; it is not an additional primitive in the O/N basis.
The original false constant `0` is our sans-serif `f` (ASCII Polish `F`).

| Target | Exact original location | Translation or correction | Canonical replay |
|---|---|---|---|
| C/f, two equations | 1968, §3(1), p. 221, `{C,0}` | Replace the printed constant `0` by `f`; retain axiom 2 `CCpqp=p`. | [E_Cf.in](proofs/official/prover9/equational/Cf/E_Cf.in) |
| C/N, two equations | 1968, §3(1), p. 221, `{C,N}`, **as corrected in 1969, p. 452** | Correct `CpCqp` to `CNpCqr` in the first equation. | [E_CN.in](proofs/official/prover9/equational/CN/E_CN.in) |
| O/N, two equations | 1968, §3(1), p. 221, `{A,N}` | Expand `C=AN`; use our `O` for the original `A`; rename variables and reverse one equality as detailed below. | [E_ON.in](proofs/official/prover9/equational/ON/E_ON.in) |
| A/N, two equations used in the simplified paper | Boolean dual of the preceding O/N basis | Replace `O` by conjunction `A`, leaving `N` fixed. | Obtained by dualizing the O/N proof; no independent search is required. |
| A/N, four equations retained in the independent archive replay | 1968, §5, p. 222, including Prior's introductory note | Replace the last equation's constant `0` by `KqNq`, as Prior specifies; use our conjunction `A` for `K`. | [E_AN.in](proofs/official/prover9/equational/AN/E_AN.in) |

## C/N: the discrepancy is an explicitly corrected misprint

The original printing gives `CpCqp = CCrpCqp` as its first C/N equation.
Prior's corrigendum specifies the change at **p. 221, line 5**:
`CpCqp` is to be replaced by `CNpCqr`.
The corrected basis, used verbatim apart from variable names in our replay,
is therefore

```text
CNpCqr = CCrpCqp
CCpqp  = p
```

In functional notation:

```text
i(n(P),i(Q,R)) = i(i(R,P),i(Q,P))
i(i(P,Q),P) = P
```

Thus there is no need to prove equivalence to the uncorrected printing or
change the proof certificates. The paper cites both the 1968 article and the
1969 correction.

## C/f: a direct transcription

The `{C,0}` pair on p. 221 is

```text
CCp0Cqr = CCrpCqp
CCpqp   = p
```

Writing `f` for `0` gives the two goals in `E_Cf.in`:

```text
i(i(P,f),i(Q,R)) = i(i(R,P),i(Q,P))
i(i(P,Q),P) = P
```

This is an **equational** basis. It is separate from the unresolved
17-symbol condensed-detachment C/f candidate F17.

## O/N: expand the abbreviation and rename variables

Meredith's first equation for `{A,N}` is

```text
ApAqr = CCrpAqp, with Cxy = ANxy.
```

Expanding `C`, and writing our `O` for the original disjunction `A`, gives

```text
OpOqr = ONONrpOqp.
```

The simultaneous variable renaming `p -> q`, `q -> r`, `r -> p` gives

```text
OqOrp = ONONpqOrq.
```

Reversing that equality yields our second target. Meredith's second axiom
`CCpqp=p` expands to our first target. The pair, in our order, is

```text
ONONpqp   = p
ONONpqOrq = OqOrp
```

This change uses only a definition, bijective variable renaming, equation
symmetry, and equation ordering. It does not require an additional derived
algebraic law. The paper's A/N two-basis is its Boolean dual:

```text
ANANpqp   = p
ANANpqArq = AqArp
```

## The independent four-equation A/N replay

In §5 on p. 222 the source gives

```text
Kpp     = p
KpKqr   = KqKrp
KpNKpNq = Kpq
KpNp    = 0
```

Prior's note immediately above this list specifies replacing the final
`0` by `KqNq` to obtain a pure K/N basis. With our conjunction symbol `A`,
this is exactly the goal conjunction in the retained `E_AN.in`:

```text
a(P,P) = P
a(P,a(Q,R)) = a(Q,a(R,P))
a(P,n(a(P,n(Q)))) = a(P,Q)
a(P,n(P)) = a(Q,n(Q))
```

That independent archived A/N replay uses a separately discovered A/N axiom.
The simplified paper instead obtains its A/N claim by dualizing its O/N
axiom and proof. These are two valid but distinct uses of the source bases.
