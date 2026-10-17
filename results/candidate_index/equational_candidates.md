# Equational elimination totals and unresolved candidates

These are the paper's C/f, C/N, and O/N screens. A/N follows by duality. The archived independent A/N screen used a different target basis and is not substituted for the dual O/N results.

Individual eliminated-equation outcomes were not preserved by the historical instrumentation. The table gives the actual aggregate method counts; it does not invent per-formula attribution. Every unresolved formula is individually listed in [equational_survivors.tsv](equational_survivors.tsv).

| System | Weight | Generated | Truth table | Cached model | New model | Saturation | Unresolved |
|---|---:|---:|---:|---:|---:|---:|---:|
| BACF | 5 | 9 | 9 | 0 | 0 | 0 | 0 |
| BACF | 7 | 72 | 65 | 7 | 0 | 0 | 0 |
| BACF | 9 | 750 | 719 | 31 | 0 | 0 | 0 |
| BACF | 11 | 9422 | 8936 | 486 | 0 | 0 | 0 |
| BACF | 13 | 137004 | 131874 | 5130 | 0 | 0 | 0 |
| BACF | 15 | 2244792 | 2167128 | 77663 | 1 | 0 | 0 |
| BACN | 6 | 15 | 14 | 1 | 0 | 0 | 0 |
| BACN | 7 | 30 | 29 | 1 | 0 | 0 | 0 |
| BACN | 8 | 200 | 194 | 6 | 0 | 0 | 0 |
| BACN | 9 | 525 | 492 | 33 | 0 | 0 | 0 |
| BACN | 10 | 2975 | 2879 | 96 | 0 | 0 | 0 |
| BACN | 11 | 9520 | 9167 | 353 | 0 | 0 | 0 |
| BACN | 12 | 51378 | 49926 | 1452 | 0 | 0 | 0 |
| BACN | 13 | 189015 | 183348 | 5667 | 0 | 0 | 0 |
| BACN | 14 | 1004399 | 979855 | 24544 | 0 | 0 | 0 |
| BACN | 15 | 4093254 | 3995506 | 97741 | 0 | 0 | 7 |
| BACN | 16 | 21764418 | 21302281 | 462120 | 0 | 1 | 16 |
| BAON | 6 | 15 | 15 | 0 | 0 | 0 | 0 |
| BAON | 7 | 30 | 27 | 3 | 0 | 0 | 0 |
| BAON | 8 | 200 | 199 | 1 | 0 | 0 | 0 |
| BAON | 9 | 525 | 497 | 28 | 0 | 0 | 0 |
| BAON | 10 | 2975 | 2960 | 15 | 0 | 0 | 0 |
| BAON | 11 | 9520 | 9195 | 325 | 0 | 0 | 0 |
| BAON | 12 | 51378 | 51093 | 285 | 0 | 0 | 0 |
| BAON | 13 | 189015 | 184544 | 4471 | 0 | 0 | 0 |
| BAON | 14 | 1004399 | 998091 | 6308 | 0 | 0 | 0 |
| BAON | 15 | 4093254 | 4021398 | 71856 | 0 | 0 | 0 |
| BAON | 16 | 21764418 | 21619684 | 144734 | 0 | 0 | 0 |
| BAON | 17 | 95946305 | 94615706 | 1330587 | 0 | 0 | 12 |
| BAON | 18 | 514972892 | 511520887 | 3451961 | 0 | 0 | 44 |
| BAON | 19 | 2416921652 | 2389169001 | 27752033 | 144 | 179 | 295 |

The source reports and exact survivor lists are under [equational_lower_bounds](../equational_lower_bounds/README.md). `manifest.json` supplies the statistics filenames for each row. A timeout is unresolved, not an elimination.

## Individual unresolved formulas

| Stable ID | System / weight | Polish | TPTP | Source ledger |
|---|---|---|---|---|
| `EQ_CN_15_s0_0000` | EQ_CN / 15 | `CCCpqCqrNCqNr=q` | `i(i(i(A,B),i(B,C)),n(i(B,n(C))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard0.jsonl#L1) |
| `EQ_CN_15_s0_0001` | EQ_CN / 15 | `CCpCqrNCqNCpr=q` | `i(i(A,i(B,C)),n(i(B,n(i(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard0.jsonl#L2) |
| `EQ_CN_15_s1_0000` | EQ_CN / 15 | `CCCCpqrNqNCrq=r` | `i(i(i(i(A,B),C),n(B)),n(i(C,B)))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard1.jsonl#L1) |
| `EQ_CN_15_s1_0001` | EQ_CN / 15 | `CCCpqCrNqNCrq=r` | `i(i(i(A,B),i(C,n(B))),n(i(C,B)))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard1.jsonl#L2) |
| `EQ_CN_15_s1_0002` | EQ_CN / 15 | `CCpCqNCrpNCqp=q` | `i(i(A,i(B,n(i(C,A)))),n(i(B,A)))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard1.jsonl#L3) |
| `EQ_CN_15_s1_0003` | EQ_CN / 15 | `CCpNCCqprNCrp=r` | `i(i(A,n(i(i(B,A),C))),n(i(C,A)))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard1.jsonl#L4) |
| `EQ_CN_15_s1_0004` | EQ_CN / 15 | `CCpNqNCCprCqp=q` | `i(i(A,n(B)),n(i(i(A,C),i(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length15_shard1.jsonl#L5) |
| `EQ_CN_16_s0_0000` | EQ_CN / 16 | `CCpCqNCNprNCqp=q` | `i(i(A,i(B,n(i(n(A),C)))),n(i(B,A)))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L1) |
| `EQ_CN_16_s0_0001` | EQ_CN / 16 | `CCpCqNCNrpNCqp=q` | `i(i(A,i(B,n(i(n(C),A)))),n(i(B,A)))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L2) |
| `EQ_CN_16_s0_0002` | EQ_CN / 16 | `CCpNCCNpqrNCrp=r` | `i(i(A,n(i(i(n(A),B),C))),n(i(C,A)))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L3) |
| `EQ_CN_16_s0_0003` | EQ_CN / 16 | `CCpNCCNqprNCrp=r` | `i(i(A,n(i(i(n(B),A),C))),n(i(C,A)))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L4) |
| `EQ_CN_16_s0_0004` | EQ_CN / 16 | `CCCpNqCrqNCrNq=r` | `i(i(i(A,n(B)),i(C,B)),n(i(C,n(B))))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L5) |
| `EQ_CN_16_s0_0005` | EQ_CN / 16 | `CCNpCqpNCqNCrp=q` | `i(i(n(A),i(B,A)),n(i(B,n(i(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L6) |
| `EQ_CN_16_s0_0006` | EQ_CN / 16 | `NCCCNpqrNCCrpp=r` | `n(i(i(i(n(A),B),C),n(i(i(C,A),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L7) |
| `EQ_CN_16_s0_0007` | EQ_CN / 16 | `NCCpqNCNCCprqp=q` | `n(i(i(A,B),n(i(n(i(i(A,C),B)),A))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L8) |
| `EQ_CN_16_s0_0008` | EQ_CN / 16 | `NCCpqNCCprCNqp=q` | `n(i(i(A,B),n(i(i(A,C),i(n(B),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L9) |
| `EQ_CN_16_s0_0009` | EQ_CN / 16 | `NCCpqNCCqrCNqp=q` | `n(i(i(A,B),n(i(i(B,C),i(n(B),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard0.jsonl#L10) |
| `EQ_CN_16_s1_0000` | EQ_CN / 16 | `CCCCpNqrqNCrNq=r` | `i(i(i(i(A,n(B)),C),B),n(i(C,n(B))))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L1) |
| `EQ_CN_16_s1_0001` | EQ_CN / 16 | `CCCpqNrNCpCrNp=r` | `i(i(i(A,B),n(C)),n(i(A,i(C,n(A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L2) |
| `EQ_CN_16_s1_0002` | EQ_CN / 16 | `CCpCqNpNCqNCpr=q` | `i(i(A,i(B,n(A))),n(i(B,n(i(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L3) |
| `EQ_CN_16_s1_0003` | EQ_CN / 16 | `CCpNqNCCNqrCqp=q` | `i(i(A,n(B)),n(i(i(n(B),C),i(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L4) |
| `EQ_CN_16_s1_0004` | EQ_CN / 16 | `CCpNqNCCpNrCqp=q` | `i(i(A,n(B)),n(i(i(A,n(C)),i(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L5) |
| `EQ_CN_16_s1_0005` | EQ_CN / 16 | `NCCCpqrNCNCprq=r` | `n(i(i(i(A,B),C),n(i(n(i(A,C)),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BACN/length16_shard1.jsonl#L6) |
| `EQ_ON_17_s0_0000` | EQ_ON / 17 | `NONONOpqrNOpOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard0.jsonl#L1) |
| `EQ_ON_17_s0_0001` | EQ_ON / 17 | `NONONOpqrNOqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard0.jsonl#L2) |
| `EQ_ON_17_s0_0002` | EQ_ON / 17 | `NONOOpqpNOqNOpr=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard0.jsonl#L3) |
| `EQ_ON_17_s0_0003` | EQ_ON / 17 | `NONOOpqpNOqNOrp=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard0.jsonl#L4) |
| `EQ_ON_17_s1_0000` | EQ_ON / 17 | `NONONOpqrNOOprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L1) |
| `EQ_ON_17_s1_0001` | EQ_ON / 17 | `NONONOpqrNOOprq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L2) |
| `EQ_ON_17_s1_0002` | EQ_ON / 17 | `NONONOpqrNOOqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L3) |
| `EQ_ON_17_s1_0003` | EQ_ON / 17 | `NONONOpqrNOOqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L4) |
| `EQ_ON_17_s1_0004` | EQ_ON / 17 | `NONOpOqpNOqNOpr=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L5) |
| `EQ_ON_17_s1_0005` | EQ_ON / 17 | `NONOpOqpNOqNOrp=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L6) |
| `EQ_ON_17_s1_0006` | EQ_ON / 17 | `NONOpOqrNOqNOpr=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L7) |
| `EQ_ON_17_s1_0007` | EQ_ON / 17 | `NONOpOqrNOqNOrp=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length17_shard1.jsonl#L8) |
| `EQ_ON_18_s0_0000` | EQ_ON / 18 | `ONONOpqNrNOOpNrp=r` | `o(n(o(n(o(A,B)),n(C))),n(o(o(A,n(C)),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L1) |
| `EQ_ON_18_s0_0001` | EQ_ON / 18 | `ONONOpqNrNOOpNrq=r` | `o(n(o(n(o(A,B)),n(C))),n(o(o(A,n(C)),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L2) |
| `EQ_ON_18_s0_0002` | EQ_ON / 18 | `ONONOpqNrNOOqNrp=r` | `o(n(o(n(o(A,B)),n(C))),n(o(o(B,n(C)),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L3) |
| `EQ_ON_18_s0_0003` | EQ_ON / 18 | `ONONOpqNrNOOqNrq=r` | `o(n(o(n(o(A,B)),n(C))),n(o(o(B,n(C)),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L4) |
| `EQ_ON_18_s0_0004` | EQ_ON / 18 | `ONONOpqpNONqNOpr=q` | `o(n(o(n(o(A,B)),A)),n(o(n(B),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L5) |
| `EQ_ON_18_s0_0005` | EQ_ON / 18 | `ONONOpqpNONqNOrp=q` | `o(n(o(n(o(A,B)),A)),n(o(n(B),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L6) |
| `EQ_ON_18_s0_0006` | EQ_ON / 18 | `ONOpONqpNONqNOpr=q` | `o(n(o(A,o(n(B),A))),n(o(n(B),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L7) |
| `EQ_ON_18_s0_0007` | EQ_ON / 18 | `ONOpONqpNONqNOrp=q` | `o(n(o(A,o(n(B),A))),n(o(n(B),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L8) |
| `EQ_ON_18_s0_0008` | EQ_ON / 18 | `ONOpONqrNONqNOpr=q` | `o(n(o(A,o(n(B),C))),n(o(n(B),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L9) |
| `EQ_ON_18_s0_0009` | EQ_ON / 18 | `ONOpONqrNONqNOrp=q` | `o(n(o(A,o(n(B),C))),n(o(n(B),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L10) |
| `EQ_ON_18_s0_0010` | EQ_ON / 18 | `ONOpNOpqNONqNOpr=q` | `o(n(o(A,n(o(A,B)))),n(o(n(B),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L11) |
| `EQ_ON_18_s0_0011` | EQ_ON / 18 | `ONOpNOpqNONqNOrp=q` | `o(n(o(A,n(o(A,B)))),n(o(n(B),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L12) |
| `EQ_ON_18_s0_0012` | EQ_ON / 18 | `NONONONpqrNOqOrq=r` | `n(o(n(o(n(o(n(A),B)),C)),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L13) |
| `EQ_ON_18_s0_0013` | EQ_ON / 18 | `NONONOpNqrNOOprp=r` | `n(o(n(o(n(o(A,n(B))),C)),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L14) |
| `EQ_ON_18_s0_0014` | EQ_ON / 18 | `NONOOpqpNOqNONrp=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(n(C),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L15) |
| `EQ_ON_18_s0_0015` | EQ_ON / 18 | `NONOpOqpNOqNOpNr=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(A,n(C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L16) |
| `EQ_ON_18_s0_0016` | EQ_ON / 18 | `NONOpqNOONOprqNp=q` | `n(o(n(o(A,B)),n(o(o(n(o(A,C)),B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L17) |
| `EQ_ON_18_s0_0017` | EQ_ON / 18 | `NONOpqNOONOrpqNp=q` | `n(o(n(o(A,B)),n(o(o(n(o(C,A)),B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L18) |
| `EQ_ON_18_s0_0018` | EQ_ON / 18 | `NONOpqNONOprOqNp=q` | `n(o(n(o(A,B)),n(o(n(o(A,C)),o(B,n(A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L19) |
| `EQ_ON_18_s0_0019` | EQ_ON / 18 | `NONOpqNONOrpOqNp=q` | `n(o(n(o(A,B)),n(o(n(o(C,A)),o(B,n(A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L20) |
| `EQ_ON_18_s0_0020` | EQ_ON / 18 | `NONOpqNOONpqNOpr=q` | `n(o(n(o(A,B)),n(o(o(n(A),B),n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L21) |
| `EQ_ON_18_s0_0021` | EQ_ON / 18 | `NONOpqNOONpqNOrp=q` | `n(o(n(o(A,B)),n(o(o(n(A),B),n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L22) |
| `EQ_ON_18_s0_0022` | EQ_ON / 18 | `NONOpqNONpOqNOpr=q` | `n(o(n(o(A,B)),n(o(n(A),o(B,n(o(A,C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L23) |
| `EQ_ON_18_s0_0023` | EQ_ON / 18 | `NONOpqNONpOqNOrp=q` | `n(o(n(o(A,B)),n(o(n(A),o(B,n(o(C,A)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard0.jsonl#L24) |
| `EQ_ON_18_s1_0000` | EQ_ON / 18 | `ONONOpqNrNONOrpp=r` | `o(n(o(n(o(A,B)),n(C))),n(o(n(o(C,A)),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L1) |
| `EQ_ON_18_s1_0001` | EQ_ON / 18 | `ONONOpqNrNONOrqq=r` | `o(n(o(n(o(A,B)),n(C))),n(o(n(o(C,B)),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L2) |
| `EQ_ON_18_s1_0002` | EQ_ON / 18 | `ONONOpqNrNOpONrp=r` | `o(n(o(n(o(A,B)),n(C))),n(o(A,o(n(C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L3) |
| `EQ_ON_18_s1_0003` | EQ_ON / 18 | `ONONOpqNrNOqONrq=r` | `o(n(o(n(o(A,B)),n(C))),n(o(B,o(n(C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L4) |
| `EQ_ON_18_s1_0004` | EQ_ON / 18 | `ONONOpqNrNOpNOrp=r` | `o(n(o(n(o(A,B)),n(C))),n(o(A,n(o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L5) |
| `EQ_ON_18_s1_0005` | EQ_ON / 18 | `ONONOpqNrNOqNOrq=r` | `o(n(o(n(o(A,B)),n(C))),n(o(B,n(o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L6) |
| `EQ_ON_18_s1_0006` | EQ_ON / 18 | `ONOOpNqpNONqNOpr=q` | `o(n(o(o(A,n(B)),A)),n(o(n(B),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L7) |
| `EQ_ON_18_s1_0007` | EQ_ON / 18 | `ONOOpNqpNONqNOrp=q` | `o(n(o(o(A,n(B)),A)),n(o(n(B),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L8) |
| `EQ_ON_18_s1_0008` | EQ_ON / 18 | `NONOONOpqrNpNOrp=r` | `n(o(n(o(o(n(o(A,B)),C),n(A))),n(o(C,A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L9) |
| `EQ_ON_18_s1_0009` | EQ_ON / 18 | `NONOONOpqrNqNOrq=r` | `n(o(n(o(o(n(o(A,B)),C),n(B))),n(o(C,B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L10) |
| `EQ_ON_18_s1_0010` | EQ_ON / 18 | `NONONOpqOrNpNOrp=r` | `n(o(n(o(n(o(A,B)),o(C,n(A)))),n(o(C,A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L11) |
| `EQ_ON_18_s1_0011` | EQ_ON / 18 | `NONONOpqOrNqNOrq=r` | `n(o(n(o(n(o(A,B)),o(C,n(B)))),n(o(C,B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L12) |
| `EQ_ON_18_s1_0012` | EQ_ON / 18 | `NONOONpqNOprNOqp=q` | `n(o(n(o(o(n(A),B),n(o(A,C)))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L13) |
| `EQ_ON_18_s1_0013` | EQ_ON / 18 | `NONOONpqNOrpNOqp=q` | `n(o(n(o(o(n(A),B),n(o(C,A)))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L14) |
| `EQ_ON_18_s1_0014` | EQ_ON / 18 | `NONONpOqNOprNOqp=q` | `n(o(n(o(n(A),o(B,n(o(A,C))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L15) |
| `EQ_ON_18_s1_0015` | EQ_ON / 18 | `NONONpOqNOrpNOqp=q` | `n(o(n(o(n(A),o(B,n(o(C,A))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L16) |
| `EQ_ON_18_s1_0016` | EQ_ON / 18 | `NONONONpqrNOOqrq=r` | `n(o(n(o(n(o(n(A),B)),C)),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L17) |
| `EQ_ON_18_s1_0017` | EQ_ON / 18 | `NONONOpNqrNOpOrp=r` | `n(o(n(o(n(o(A,n(B))),C)),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L18) |
| `EQ_ON_18_s1_0018` | EQ_ON / 18 | `NONOpOqpNOqNONrp=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(n(C),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L19) |
| `EQ_ON_18_s1_0019` | EQ_ON / 18 | `NONOOpqpNOqNOpNr=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(A,n(C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length18_shard1.jsonl#L20) |
| `EQ_ON_19_s0_0000` | EQ_ON / 19 | `ONOONOpqNrNpNONrp=r` | `o(n(o(o(n(o(A,B)),n(C)),n(A))),n(o(n(C),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L1) |
| `EQ_ON_19_s0_0001` | EQ_ON / 19 | `ONOONOpqNrNqNONrq=r` | `o(n(o(o(n(o(A,B)),n(C)),n(B))),n(o(n(C),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L2) |
| `EQ_ON_19_s0_0002` | EQ_ON / 19 | `ONOONpNqNOprNONqp=q` | `o(n(o(o(n(A),n(B)),n(o(A,C)))),n(o(n(B),A)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L3) |
| `EQ_ON_19_s0_0003` | EQ_ON / 19 | `ONOONpNqNOrpNONqp=q` | `o(n(o(o(n(A),n(B)),n(o(C,A)))),n(o(n(B),A)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L4) |
| `EQ_ON_19_s0_0004` | EQ_ON / 19 | `ONOONpNqNOrqNONqp=q` | `o(n(o(o(n(A),n(B)),n(o(C,B)))),n(o(n(B),A)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L5) |
| `EQ_ON_19_s0_0005` | EQ_ON / 19 | `ONONOpqONqNrNONqr=q` | `o(n(o(n(o(A,B)),o(n(B),n(C)))),n(o(n(B),C)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L6) |
| `EQ_ON_19_s0_0006` | EQ_ON / 19 | `ONONOpqONrNpNONrp=r` | `o(n(o(n(o(A,B)),o(n(C),n(A)))),n(o(n(C),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L7) |
| `EQ_ON_19_s0_0007` | EQ_ON / 19 | `ONONOpqONrNqNONrq=r` | `o(n(o(n(o(A,B)),o(n(C),n(B)))),n(o(n(C),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L8) |
| `EQ_ON_19_s0_0008` | EQ_ON / 19 | `ONONpNONOpqrNONrp=r` | `o(n(o(n(A),n(o(n(o(A,B)),C)))),n(o(n(C),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L9) |
| `EQ_ON_19_s0_0009` | EQ_ON / 19 | `ONONpNONOqprNONrp=r` | `o(n(o(n(A),n(o(n(o(B,A)),C)))),n(o(n(C),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L10) |
| `EQ_ON_19_s0_0010` | EQ_ON / 19 | `ONONOpqONqrNONqNr=q` | `o(n(o(n(o(A,B)),o(n(B),C))),n(o(n(B),n(C))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L11) |
| `EQ_ON_19_s0_0011` | EQ_ON / 19 | `ONONONpqNrNOOqNrq=r` | `o(n(o(n(o(n(A),B)),n(C))),n(o(o(B,n(C)),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L12) |
| `EQ_ON_19_s0_0012` | EQ_ON / 19 | `ONONOpNqNrNONOrpp=r` | `o(n(o(n(o(A,n(B))),n(C))),n(o(n(o(C,A)),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L13) |
| `EQ_ON_19_s0_0013` | EQ_ON / 19 | `ONONOpNqNrNOpONrp=r` | `o(n(o(n(o(A,n(B))),n(C))),n(o(A,o(n(C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L14) |
| `EQ_ON_19_s0_0014` | EQ_ON / 19 | `ONONOpNqNrNOpNOrp=r` | `o(n(o(n(o(A,n(B))),n(C))),n(o(A,n(o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L15) |
| `EQ_ON_19_s0_0015` | EQ_ON / 19 | `ONONOpqpNONqNONrp=q` | `o(n(o(n(o(A,B)),A)),n(o(n(B),n(o(n(C),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L16) |
| `EQ_ON_19_s0_0016` | EQ_ON / 19 | `ONOpONqpNONqNONrp=q` | `o(n(o(A,o(n(B),A))),n(o(n(B),n(o(n(C),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L17) |
| `EQ_ON_19_s0_0017` | EQ_ON / 19 | `ONOpNOpqNONqNONrp=q` | `o(n(o(A,n(o(A,B)))),n(o(n(B),n(o(n(C),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L18) |
| `EQ_ON_19_s0_0018` | EQ_ON / 19 | `ONOOpNqpNONqNOpNr=q` | `o(n(o(o(A,n(B)),A)),n(o(n(B),n(o(A,n(C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L19) |
| `EQ_ON_19_s0_0019` | EQ_ON / 19 | `ONONpNqNONOqrONqp=q` | `o(n(o(n(A),n(B))),n(o(n(o(B,C)),o(n(B),A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L20) |
| `EQ_ON_19_s0_0020` | EQ_ON / 19 | `ONOpNqNOONOprNqNp=q` | `o(n(o(A,n(B))),n(o(o(n(o(A,C)),n(B)),n(A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L21) |
| `EQ_ON_19_s0_0021` | EQ_ON / 19 | `ONOpNqNOONOrpNqNp=q` | `o(n(o(A,n(B))),n(o(o(n(o(C,A)),n(B)),n(A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L22) |
| `EQ_ON_19_s0_0022` | EQ_ON / 19 | `ONOpNqNOONpNqNOpr=q` | `o(n(o(A,n(B))),n(o(o(n(A),n(B)),n(o(A,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L23) |
| `EQ_ON_19_s0_0023` | EQ_ON / 19 | `ONOpNqNOONpNqNOqr=q` | `o(n(o(A,n(B))),n(o(o(n(A),n(B)),n(o(B,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L24) |
| `EQ_ON_19_s0_0024` | EQ_ON / 19 | `ONOpNqNOONpNqNOrp=q` | `o(n(o(A,n(B))),n(o(o(n(A),n(B)),n(o(C,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L25) |
| `EQ_ON_19_s0_0025` | EQ_ON / 19 | `ONOpNqNONOprONqNp=q` | `o(n(o(A,n(B))),n(o(n(o(A,C)),o(n(B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L26) |
| `EQ_ON_19_s0_0026` | EQ_ON / 19 | `ONOpNqNONOqrONqNp=q` | `o(n(o(A,n(B))),n(o(n(o(B,C)),o(n(B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L27) |
| `EQ_ON_19_s0_0027` | EQ_ON / 19 | `ONOpNqNONOrpONqNp=q` | `o(n(o(A,n(B))),n(o(n(o(C,A)),o(n(B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L28) |
| `EQ_ON_19_s0_0028` | EQ_ON / 19 | `ONOpNqNONpNOqNOpr=q` | `o(n(o(A,n(B))),n(o(n(A),n(o(B,n(o(A,C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L29) |
| `EQ_ON_19_s0_0029` | EQ_ON / 19 | `ONOpNqNONpNOqNOrp=q` | `o(n(o(A,n(B))),n(o(n(A),n(o(B,n(o(C,A)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L30) |
| `EQ_ON_19_s0_0030` | EQ_ON / 19 | `NONOONONpqrpNOrNp=r` | `n(o(n(o(o(n(o(n(A),B)),C),A)),n(o(C,n(A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L31) |
| `EQ_ON_19_s0_0031` | EQ_ON / 19 | `NONOpOqNONprNOqNp=q` | `n(o(n(o(A,o(B,n(o(n(A),C))))),n(o(B,n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L32) |
| `EQ_ON_19_s0_0032` | EQ_ON / 19 | `NONONONNpqrNOpOrp=r` | `n(o(n(o(n(o(n(n(A)),B)),C)),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L33) |
| `EQ_ON_19_s0_0033` | EQ_ON / 19 | `NONONONNpqrNOqOrq=r` | `n(o(n(o(n(o(n(n(A)),B)),C)),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L34) |
| `EQ_ON_19_s0_0034` | EQ_ON / 19 | `NONONOpNNqrNOOprp=r` | `n(o(n(o(n(o(A,n(n(B)))),C)),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L35) |
| `EQ_ON_19_s0_0035` | EQ_ON / 19 | `NONONOpNNqrNOOqrq=r` | `n(o(n(o(n(o(A,n(n(B)))),C)),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L36) |
| `EQ_ON_19_s0_0036` | EQ_ON / 19 | `NONONNNOpqrNOpOrp=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L37) |
| `EQ_ON_19_s0_0037` | EQ_ON / 19 | `NONONNNOpqrNOqOrq=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L38) |
| `EQ_ON_19_s0_0038` | EQ_ON / 19 | `NONNNONOpqrNOOprp=r` | `n(o(n(n(n(o(n(o(A,B)),C)))),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L39) |
| `EQ_ON_19_s0_0039` | EQ_ON / 19 | `NONNNONOpqrNOOqrq=r` | `n(o(n(n(n(o(n(o(A,B)),C)))),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L40) |
| `EQ_ON_19_s0_0040` | EQ_ON / 19 | `NONOONNpqpNOqNOpr=q` | `n(o(n(o(o(n(n(A)),B),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L41) |
| `EQ_ON_19_s0_0041` | EQ_ON / 19 | `NONOONNpqpNOqNOrp=q` | `n(o(n(o(o(n(n(A)),B),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L42) |
| `EQ_ON_19_s0_0042` | EQ_ON / 19 | `NONOOpOpqrNOqNOpr=q` | `n(o(n(o(o(A,o(A,B)),C)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L43) |
| `EQ_ON_19_s0_0043` | EQ_ON / 19 | `NONOOpOpqrNOqNOrp=q` | `n(o(n(o(o(A,o(A,B)),C)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L44) |
| `EQ_ON_19_s0_0044` | EQ_ON / 19 | `NONOOpOqprNOqNOpr=q` | `n(o(n(o(o(A,o(B,A)),C)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L45) |
| `EQ_ON_19_s0_0045` | EQ_ON / 19 | `NONOOpOqprNOqNOrp=q` | `n(o(n(o(o(A,o(B,A)),C)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L46) |
| `EQ_ON_19_s0_0046` | EQ_ON / 19 | `NONONONpqrNOONprq=r` | `n(o(n(o(n(o(n(A),B)),C)),n(o(o(n(A),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L47) |
| `EQ_ON_19_s0_0047` | EQ_ON / 19 | `NONONONpqrNOOqrNp=r` | `n(o(n(o(n(o(n(A),B)),C)),n(o(o(B,C),n(A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L48) |
| `EQ_ON_19_s0_0048` | EQ_ON / 19 | `NONONNOpqpNOqNOpr=q` | `n(o(n(o(n(n(o(A,B))),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L49) |
| `EQ_ON_19_s0_0049` | EQ_ON / 19 | `NONONNOpqpNOqNOrp=q` | `n(o(n(o(n(n(o(A,B))),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L50) |
| `EQ_ON_19_s0_0050` | EQ_ON / 19 | `NONOOppOqpNOqNOpr=q` | `n(o(n(o(o(A,A),o(B,A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L51) |
| `EQ_ON_19_s0_0051` | EQ_ON / 19 | `NONOOppOqpNOqNOrp=q` | `n(o(n(o(o(A,A),o(B,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L52) |
| `EQ_ON_19_s0_0052` | EQ_ON / 19 | `NONOOppOqrNOqNOpr=q` | `n(o(n(o(o(A,A),o(B,C))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L53) |
| `EQ_ON_19_s0_0053` | EQ_ON / 19 | `NONOOppOqrNOqNOrp=q` | `n(o(n(o(o(A,A),o(B,C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L54) |
| `EQ_ON_19_s0_0054` | EQ_ON / 19 | `NONOOpqOppNOqNOpr=q` | `n(o(n(o(o(A,B),o(A,A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L55) |
| `EQ_ON_19_s0_0055` | EQ_ON / 19 | `NONOOpqOppNOqNOrp=q` | `n(o(n(o(o(A,B),o(A,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L56) |
| `EQ_ON_19_s0_0056` | EQ_ON / 19 | `NONOOpqOprNOqNOpr=q` | `n(o(n(o(o(A,B),o(A,C))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L57) |
| `EQ_ON_19_s0_0057` | EQ_ON / 19 | `NONOOpqOprNOqNOrp=q` | `n(o(n(o(o(A,B),o(A,C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L58) |
| `EQ_ON_19_s0_0058` | EQ_ON / 19 | `NONOOpqOqpNOqNOrp=q` | `n(o(n(o(o(A,B),o(B,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L59) |
| `EQ_ON_19_s0_0059` | EQ_ON / 19 | `NONOOpqOrpNOqNOpr=q` | `n(o(n(o(o(A,B),o(C,A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L60) |
| `EQ_ON_19_s0_0060` | EQ_ON / 19 | `NONOOpqOrpNOqNOrp=q` | `n(o(n(o(o(A,B),o(C,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L61) |
| `EQ_ON_19_s0_0061` | EQ_ON / 19 | `NONOOpqOrpNOrNOpq=r` | `n(o(n(o(o(A,B),o(C,A))),n(o(C,n(o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L62) |
| `EQ_ON_19_s0_0062` | EQ_ON / 19 | `NONOOpqOrpNOrNOqp=r` | `n(o(n(o(o(A,B),o(C,A))),n(o(C,n(o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L63) |
| `EQ_ON_19_s0_0063` | EQ_ON / 19 | `NONOOpqOrqNOrNOpq=r` | `n(o(n(o(o(A,B),o(C,B))),n(o(C,n(o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L64) |
| `EQ_ON_19_s0_0064` | EQ_ON / 19 | `NONOOpqOrqNOrNOqp=r` | `n(o(n(o(o(A,B),o(C,B))),n(o(C,n(o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L65) |
| `EQ_ON_19_s0_0065` | EQ_ON / 19 | `NONOOpqOrrNOqNOpr=q` | `n(o(n(o(o(A,B),o(C,C))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L66) |
| `EQ_ON_19_s0_0066` | EQ_ON / 19 | `NONOOpqOrrNOqNOrp=q` | `n(o(n(o(o(A,B),o(C,C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L67) |
| `EQ_ON_19_s0_0067` | EQ_ON / 19 | `NONOOpqNNpNOqNOpr=q` | `n(o(n(o(o(A,B),n(n(A)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L68) |
| `EQ_ON_19_s0_0068` | EQ_ON / 19 | `NONOOpqNNpNOqNOrp=q` | `n(o(n(o(o(A,B),n(n(A)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L69) |
| `EQ_ON_19_s0_0069` | EQ_ON / 19 | `NONOpOqNNpNOqNOpr=q` | `n(o(n(o(A,o(B,n(n(A))))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L70) |
| `EQ_ON_19_s0_0070` | EQ_ON / 19 | `NONOpOqNNpNOqNOrp=q` | `n(o(n(o(A,o(B,n(n(A))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L71) |
| `EQ_ON_19_s0_0071` | EQ_ON / 19 | `NONOpOqNNrNOqNOrp=q` | `n(o(n(o(A,o(B,n(n(C))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L72) |
| `EQ_ON_19_s0_0072` | EQ_ON / 19 | `NONOpNOpNqNOqNOpr=q` | `n(o(n(o(A,n(o(A,n(B))))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L73) |
| `EQ_ON_19_s0_0073` | EQ_ON / 19 | `NONOpNOpNqNOqNOrp=q` | `n(o(n(o(A,n(o(A,n(B))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L74) |
| `EQ_ON_19_s0_0074` | EQ_ON / 19 | `NONNNOpOqpNOqNOpr=q` | `n(o(n(n(n(o(A,o(B,A))))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L75) |
| `EQ_ON_19_s0_0075` | EQ_ON / 19 | `NONNNOpOqpNOqNOrp=q` | `n(o(n(n(n(o(A,o(B,A))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L76) |
| `EQ_ON_19_s0_0076` | EQ_ON / 19 | `NONNNOpOqrNOqNOrp=q` | `n(o(n(n(n(o(A,o(B,C))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L77) |
| `EQ_ON_19_s0_0077` | EQ_ON / 19 | `NONONOpqrNOOOpprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,A),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L78) |
| `EQ_ON_19_s0_0078` | EQ_ON / 19 | `NONONOpqrNOOOpprq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,A),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L79) |
| `EQ_ON_19_s0_0079` | EQ_ON / 19 | `NONONOpqrNOOOpqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,B),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L80) |
| `EQ_ON_19_s0_0080` | EQ_ON / 19 | `NONONOpqrNOOOpqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,B),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L81) |
| `EQ_ON_19_s0_0081` | EQ_ON / 19 | `NONONOpqrNOOOprpq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,C),A),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L82) |
| `EQ_ON_19_s0_0082` | EQ_ON / 19 | `NONONOpqrNOOOprrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(A,C),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L83) |
| `EQ_ON_19_s0_0083` | EQ_ON / 19 | `NONONOpqrNOOOqprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(B,A),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L84) |
| `EQ_ON_19_s0_0084` | EQ_ON / 19 | `NONONOpqrNOOOqprq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(B,A),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L85) |
| `EQ_ON_19_s0_0085` | EQ_ON / 19 | `NONONOpqrNOOOqqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(B,B),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L86) |
| `EQ_ON_19_s0_0086` | EQ_ON / 19 | `NONONOpqrNOOOqqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(B,B),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L87) |
| `EQ_ON_19_s0_0087` | EQ_ON / 19 | `NONONOpqrNOOOqrrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(o(B,C),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L88) |
| `EQ_ON_19_s0_0088` | EQ_ON / 19 | `NONONOpqrNOOpNNrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,n(n(C))),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L89) |
| `EQ_ON_19_s0_0089` | EQ_ON / 19 | `NONONOpqrNOOqNNrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,n(n(C))),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L90) |
| `EQ_ON_19_s0_0090` | EQ_ON / 19 | `NONONOpqrNOOqNNrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,n(n(C))),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L91) |
| `EQ_ON_19_s0_0091` | EQ_ON / 19 | `NONONOpqrNONNpOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(A)),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L92) |
| `EQ_ON_19_s0_0092` | EQ_ON / 19 | `NONONOpqrNONNqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(B)),o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L93) |
| `EQ_ON_19_s0_0093` | EQ_ON / 19 | `NONONOpqrNOpONNrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(n(n(C)),A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L94) |
| `EQ_ON_19_s0_0094` | EQ_ON / 19 | `NONONOpqrNOqONNrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(n(n(C)),B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L95) |
| `EQ_ON_19_s0_0095` | EQ_ON / 19 | `NONONOpqrNOpOqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(B,o(C,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L96) |
| `EQ_ON_19_s0_0096` | EQ_ON / 19 | `NONONOpqrNOpOrOpp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,o(A,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L97) |
| `EQ_ON_19_s0_0097` | EQ_ON / 19 | `NONONOpqrNOpOrOpq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L98) |
| `EQ_ON_19_s0_0098` | EQ_ON / 19 | `NONONOpqrNOpOrOqp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L99) |
| `EQ_ON_19_s0_0099` | EQ_ON / 19 | `NONONOpqrNOpOrOqq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,o(B,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L100) |
| `EQ_ON_19_s0_0100` | EQ_ON / 19 | `NONONOpqrNOpOrOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,o(C,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L101) |
| `EQ_ON_19_s0_0101` | EQ_ON / 19 | `NONONOpqrNOqOpOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(A,o(C,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L102) |
| `EQ_ON_19_s0_0102` | EQ_ON / 19 | `NONONOpqrNOqOrOpp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,o(A,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L103) |
| `EQ_ON_19_s0_0103` | EQ_ON / 19 | `NONONOpqrNOqOrOpq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L104) |
| `EQ_ON_19_s0_0104` | EQ_ON / 19 | `NONONOpqrNOqOrOqp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L105) |
| `EQ_ON_19_s0_0105` | EQ_ON / 19 | `NONONOpqrNOqOrOqq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,o(B,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L106) |
| `EQ_ON_19_s0_0106` | EQ_ON / 19 | `NONONOpqrNOqOrOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,o(C,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L107) |
| `EQ_ON_19_s0_0107` | EQ_ON / 19 | `NONONOpqrNOpNONrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,n(o(n(C),A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L108) |
| `EQ_ON_19_s0_0108` | EQ_ON / 19 | `NONONOpqrNOqNONrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,n(o(n(C),B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L109) |
| `EQ_ON_19_s0_0109` | EQ_ON / 19 | `NONONpOqrNOqNONpr=q` | `n(o(n(o(n(A),o(B,C))),n(o(B,n(o(n(A),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L110) |
| `EQ_ON_19_s0_0110` | EQ_ON / 19 | `NONOpOqNrNOqNOpNr=q` | `n(o(n(o(A,o(B,n(C)))),n(o(B,n(o(A,n(C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L111) |
| `EQ_ON_19_s0_0111` | EQ_ON / 19 | `NONONOpqrNOpNNOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,n(n(o(C,A)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L112) |
| `EQ_ON_19_s0_0112` | EQ_ON / 19 | `NONONOpqrNOqNNOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,n(n(o(C,B)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L113) |
| `EQ_ON_19_s0_0113` | EQ_ON / 19 | `NONONOpqrNNNOOprp=r` | `n(o(n(o(n(o(A,B)),C)),n(n(n(o(o(A,C),A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L114) |
| `EQ_ON_19_s0_0114` | EQ_ON / 19 | `NONONOpqrNNNOOqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(n(n(o(o(B,C),A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L115) |
| `EQ_ON_19_s0_0115` | EQ_ON / 19 | `NONONOpqrNNNOOqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(n(n(o(o(B,C),B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L116) |
| `EQ_ON_19_s0_0116` | EQ_ON / 19 | `NONOpOqpNOqNONNpr=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(n(n(A)),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L117) |
| `EQ_ON_19_s0_0117` | EQ_ON / 19 | `NONOpOqpNOqNONNrp=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(n(n(C)),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L118) |
| `EQ_ON_19_s0_0118` | EQ_ON / 19 | `NONOOpqpNOqNOpNNr=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(A,n(n(C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L119) |
| `EQ_ON_19_s0_0119` | EQ_ON / 19 | `NONOOpqpNOqNOrNNp=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(C,n(n(A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L120) |
| `EQ_ON_19_s0_0120` | EQ_ON / 19 | `NONOpOqpNOqNNNOpr=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(n(n(o(A,C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L121) |
| `EQ_ON_19_s0_0121` | EQ_ON / 19 | `NONOpOqpNOqNNNOrp=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(n(n(o(C,A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L122) |
| `EQ_ON_19_s0_0122` | EQ_ON / 19 | `NONOpOqrNOqNNNOpr=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(n(n(o(A,C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L123) |
| `EQ_ON_19_s0_0123` | EQ_ON / 19 | `NONOpOqrNOqNNNOrp=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(n(n(o(C,A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L124) |
| `EQ_ON_19_s0_0124` | EQ_ON / 19 | `NONOpOqpNNNOqNOpr=q` | `n(o(n(o(A,o(B,A))),n(n(n(o(B,n(o(A,C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L125) |
| `EQ_ON_19_s0_0125` | EQ_ON / 19 | `NONOpOqpNNNOqNOrp=q` | `n(o(n(o(A,o(B,A))),n(n(n(o(B,n(o(C,A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L126) |
| `EQ_ON_19_s0_0126` | EQ_ON / 19 | `NONONpqNOONONprqp=q` | `n(o(n(o(n(A),B)),n(o(o(n(o(n(A),C)),B),A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L127) |
| `EQ_ON_19_s0_0127` | EQ_ON / 19 | `NONONpqNOpOqNONpr=q` | `n(o(n(o(n(A),B)),n(o(A,o(B,n(o(n(A),C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard0.jsonl#L128) |
| `EQ_ON_19_s1_0000` | EQ_ON / 19 | `ONONONOpqrNpNONrp=r` | `o(n(o(n(o(n(o(A,B)),C)),n(A))),n(o(n(C),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L1) |
| `EQ_ON_19_s1_0001` | EQ_ON / 19 | `ONONONOpqrNqNONrq=r` | `o(n(o(n(o(n(o(A,B)),C)),n(B))),n(o(n(C),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L2) |
| `EQ_ON_19_s1_0002` | EQ_ON / 19 | `ONONpONqNOprNONqp=q` | `o(n(o(n(A),o(n(B),n(o(A,C))))),n(o(n(B),A)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L3) |
| `EQ_ON_19_s1_0003` | EQ_ON / 19 | `ONONpONqNOrpNONqp=q` | `o(n(o(n(A),o(n(B),n(o(C,A))))),n(o(n(B),A)))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L4) |
| `EQ_ON_19_s1_0004` | EQ_ON / 19 | `ONOOpNqNOrqNONqNp=q` | `o(n(o(o(A,n(B)),n(o(C,B)))),n(o(n(B),n(A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L5) |
| `EQ_ON_19_s1_0005` | EQ_ON / 19 | `ONONONpqNrNONOrqq=r` | `o(n(o(n(o(n(A),B)),n(C))),n(o(n(o(C,B)),B)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L6) |
| `EQ_ON_19_s1_0006` | EQ_ON / 19 | `ONONONpqNrNOqONrq=r` | `o(n(o(n(o(n(A),B)),n(C))),n(o(B,o(n(C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L7) |
| `EQ_ON_19_s1_0007` | EQ_ON / 19 | `ONONONpqNrNOqNOrq=r` | `o(n(o(n(o(n(A),B)),n(C))),n(o(B,n(o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L8) |
| `EQ_ON_19_s1_0008` | EQ_ON / 19 | `ONONOpNqNrNOOpNrp=r` | `o(n(o(n(o(A,n(B))),n(C))),n(o(o(A,n(C)),A)))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L9) |
| `EQ_ON_19_s1_0009` | EQ_ON / 19 | `ONOOpNqpNONqNONrp=q` | `o(n(o(o(A,n(B)),A)),n(o(n(B),n(o(n(C),A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L10) |
| `EQ_ON_19_s1_0010` | EQ_ON / 19 | `ONONOpqpNONqNOpNr=q` | `o(n(o(n(o(A,B)),A)),n(o(n(B),n(o(A,n(C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L11) |
| `EQ_ON_19_s1_0011` | EQ_ON / 19 | `ONOpONqpNONqNOpNr=q` | `o(n(o(A,o(n(B),A))),n(o(n(B),n(o(A,n(C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L12) |
| `EQ_ON_19_s1_0012` | EQ_ON / 19 | `ONOpNOpqNONqNOpNr=q` | `o(n(o(A,n(o(A,B)))),n(o(n(B),n(o(A,n(C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L13) |
| `EQ_ON_19_s1_0013` | EQ_ON / 19 | `ONONpNqNOOpNqNOqr=q` | `o(n(o(n(A),n(B))),n(o(o(A,n(B)),n(o(B,C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L14) |
| `EQ_ON_19_s1_0014` | EQ_ON / 19 | `ONOpNqNONOqNOprNp=q` | `o(n(o(A,n(B))),n(o(n(o(B,n(o(A,C)))),n(A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L15) |
| `EQ_ON_19_s1_0015` | EQ_ON / 19 | `ONOpNqNONOqNOrpNp=q` | `o(n(o(A,n(B))),n(o(n(o(B,n(o(C,A)))),n(A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L16) |
| `EQ_ON_19_s1_0016` | EQ_ON / 19 | `ONOpNqNONpONqNOpr=q` | `o(n(o(A,n(B))),n(o(n(A),o(n(B),n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L17) |
| `EQ_ON_19_s1_0017` | EQ_ON / 19 | `ONOpNqNONpONqNOrp=q` | `o(n(o(A,n(B))),n(o(n(A),o(n(B),n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L18) |
| `EQ_ON_19_s1_0018` | EQ_ON / 19 | `NONOONONpqrNqNOrq=r` | `n(o(n(o(o(n(o(n(A),B)),C),n(B))),n(o(C,B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L19) |
| `EQ_ON_19_s1_0019` | EQ_ON / 19 | `NONOONOpNqrNpNOrp=r` | `n(o(n(o(o(n(o(A,n(B))),C),n(A))),n(o(C,A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L20) |
| `EQ_ON_19_s1_0020` | EQ_ON / 19 | `NONONONpqOrNqNOrq=r` | `n(o(n(o(n(o(n(A),B)),o(C,n(B)))),n(o(C,B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L21) |
| `EQ_ON_19_s1_0021` | EQ_ON / 19 | `NONONOpNqOqNrNOqr=q` | `n(o(n(o(n(o(A,n(B))),o(B,n(C)))),n(o(B,C))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L22) |
| `EQ_ON_19_s1_0022` | EQ_ON / 19 | `NONONOpNqOrNpNOrp=r` | `n(o(n(o(n(o(A,n(B))),o(C,n(A)))),n(o(C,A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L23) |
| `EQ_ON_19_s1_0023` | EQ_ON / 19 | `NONOONpqNONrpNOqp=q` | `n(o(n(o(o(n(A),B),n(o(n(C),A)))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L24) |
| `EQ_ON_19_s1_0024` | EQ_ON / 19 | `NONOONpqNOpNrNOqp=q` | `n(o(n(o(o(n(A),B),n(o(A,n(C))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L25) |
| `EQ_ON_19_s1_0025` | EQ_ON / 19 | `NONOONpqNOrNqNOqp=q` | `n(o(n(o(o(n(A),B),n(o(C,n(B))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L26) |
| `EQ_ON_19_s1_0026` | EQ_ON / 19 | `NONONpOqNONrpNOqp=q` | `n(o(n(o(n(A),o(B,n(o(n(C),A))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L27) |
| `EQ_ON_19_s1_0027` | EQ_ON / 19 | `NONONpOqNOpNrNOqp=q` | `n(o(n(o(n(A),o(B,n(o(A,n(C)))))),n(o(B,A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L28) |
| `EQ_ON_19_s1_0028` | EQ_ON / 19 | `NONOONOpNqrqNOrNq=r` | `n(o(n(o(o(n(o(A,n(B))),C),B)),n(o(C,n(B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L29) |
| `EQ_ON_19_s1_0029` | EQ_ON / 19 | `NONONONpqOrpNOrNp=r` | `n(o(n(o(n(o(n(A),B)),o(C,A))),n(o(C,n(A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L30) |
| `EQ_ON_19_s1_0030` | EQ_ON / 19 | `NONONOpNqOqrNOqNr=q` | `n(o(n(o(n(o(A,n(B))),o(B,C))),n(o(B,n(C)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L31) |
| `EQ_ON_19_s1_0031` | EQ_ON / 19 | `NONONOpNqOrqNOrNq=r` | `n(o(n(o(n(o(A,n(B))),o(C,B))),n(o(C,n(B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L32) |
| `EQ_ON_19_s1_0032` | EQ_ON / 19 | `NONOOpqNONprNOqNp=q` | `n(o(n(o(o(A,B),n(o(n(A),C)))),n(o(B,n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L33) |
| `EQ_ON_19_s1_0033` | EQ_ON / 19 | `NONOOpqNOrNpNOqNp=q` | `n(o(n(o(o(A,B),n(o(C,n(A))))),n(o(B,n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L34) |
| `EQ_ON_19_s1_0034` | EQ_ON / 19 | `NONOOpqNOrNqNOqNp=q` | `n(o(n(o(o(A,B),n(o(C,n(B))))),n(o(B,n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L35) |
| `EQ_ON_19_s1_0035` | EQ_ON / 19 | `NONOpOqNOrNpNOqNp=q` | `n(o(n(o(A,o(B,n(o(C,n(A)))))),n(o(B,n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L36) |
| `EQ_ON_19_s1_0036` | EQ_ON / 19 | `NONONONNpqrNOOprp=r` | `n(o(n(o(n(o(n(n(A)),B)),C)),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L37) |
| `EQ_ON_19_s1_0037` | EQ_ON / 19 | `NONONONNpqrNOOqrp=r` | `n(o(n(o(n(o(n(n(A)),B)),C)),n(o(o(B,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L38) |
| `EQ_ON_19_s1_0038` | EQ_ON / 19 | `NONONONNpqrNOOqrq=r` | `n(o(n(o(n(o(n(n(A)),B)),C)),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L39) |
| `EQ_ON_19_s1_0039` | EQ_ON / 19 | `NONONOpOqrsNOOpsq=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(A,D),B))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L40) |
| `EQ_ON_19_s1_0040` | EQ_ON / 19 | `NONONOpOqrsNOOpsr=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(A,D),C))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L41) |
| `EQ_ON_19_s1_0041` | EQ_ON / 19 | `NONONOpOqrsNOOqsp=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(B,D),A))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L42) |
| `EQ_ON_19_s1_0042` | EQ_ON / 19 | `NONONOpOqrsNOOqsr=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(B,D),C))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L43) |
| `EQ_ON_19_s1_0043` | EQ_ON / 19 | `NONONOpOqrsNOOrsp=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(C,D),A))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L44) |
| `EQ_ON_19_s1_0044` | EQ_ON / 19 | `NONONOpOqrsNOOrsq=s` | `n(o(n(o(n(o(A,o(B,C))),D)),n(o(o(C,D),B))))=D` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L45) |
| `EQ_ON_19_s1_0045` | EQ_ON / 19 | `NONONOpNNqrNOpOrp=r` | `n(o(n(o(n(o(A,n(n(B)))),C)),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L46) |
| `EQ_ON_19_s1_0046` | EQ_ON / 19 | `NONONOpNNqrNOqOrq=r` | `n(o(n(o(n(o(A,n(n(B)))),C)),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L47) |
| `EQ_ON_19_s1_0047` | EQ_ON / 19 | `NONONNNOpqrNOOprp=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L48) |
| `EQ_ON_19_s1_0048` | EQ_ON / 19 | `NONONNNOpqrNOOprq=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(o(A,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L49) |
| `EQ_ON_19_s1_0049` | EQ_ON / 19 | `NONONNNOpqrNOOqrp=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(o(B,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L50) |
| `EQ_ON_19_s1_0050` | EQ_ON / 19 | `NONONNNOpqrNOOqrq=r` | `n(o(n(o(n(n(n(o(A,B)))),C)),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L51) |
| `EQ_ON_19_s1_0051` | EQ_ON / 19 | `NONONOpqNNrNOOprp=r` | `n(o(n(o(n(o(A,B)),n(n(C)))),n(o(o(A,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L52) |
| `EQ_ON_19_s1_0052` | EQ_ON / 19 | `NONONOpqNNrNOOqrp=r` | `n(o(n(o(n(o(A,B)),n(n(C)))),n(o(o(B,C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L53) |
| `EQ_ON_19_s1_0053` | EQ_ON / 19 | `NONONOpqNNrNOOqrq=r` | `n(o(n(o(n(o(A,B)),n(n(C)))),n(o(o(B,C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L54) |
| `EQ_ON_19_s1_0054` | EQ_ON / 19 | `NONNNONOpqrNOpOrp=r` | `n(o(n(n(n(o(n(o(A,B)),C)))),n(o(A,o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L55) |
| `EQ_ON_19_s1_0055` | EQ_ON / 19 | `NONNNONOpqrNOqOrq=r` | `n(o(n(n(n(o(n(o(A,B)),C)))),n(o(B,o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L56) |
| `EQ_ON_19_s1_0056` | EQ_ON / 19 | `NONOOOppqpNOqNOpr=q` | `n(o(n(o(o(o(A,A),B),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L57) |
| `EQ_ON_19_s1_0057` | EQ_ON / 19 | `NONOOOppqpNOqNOrp=q` | `n(o(n(o(o(o(A,A),B),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L58) |
| `EQ_ON_19_s1_0058` | EQ_ON / 19 | `NONOOOppqrNOqNOpr=q` | `n(o(n(o(o(o(A,A),B),C)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L59) |
| `EQ_ON_19_s1_0059` | EQ_ON / 19 | `NONOOOppqrNOqNOrp=q` | `n(o(n(o(o(o(A,A),B),C)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L60) |
| `EQ_ON_19_s1_0060` | EQ_ON / 19 | `NONOOOpqprNOqNOpr=q` | `n(o(n(o(o(o(A,B),A),C)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L61) |
| `EQ_ON_19_s1_0061` | EQ_ON / 19 | `NONOOOpqqpNOqNOpr=q` | `n(o(n(o(o(o(A,B),B),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L62) |
| `EQ_ON_19_s1_0062` | EQ_ON / 19 | `NONOOOpqqpNOqNOrp=q` | `n(o(n(o(o(o(A,B),B),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L63) |
| `EQ_ON_19_s1_0063` | EQ_ON / 19 | `NONOOOpqrpNOrNOpq=r` | `n(o(n(o(o(o(A,B),C),A)),n(o(C,n(o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L64) |
| `EQ_ON_19_s1_0064` | EQ_ON / 19 | `NONOOOpqrpNOrNOqp=r` | `n(o(n(o(o(o(A,B),C),A)),n(o(C,n(o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L65) |
| `EQ_ON_19_s1_0065` | EQ_ON / 19 | `NONOOOpqrqNOrNOpq=r` | `n(o(n(o(o(o(A,B),C),B)),n(o(C,n(o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L66) |
| `EQ_ON_19_s1_0066` | EQ_ON / 19 | `NONOOOpqrqNOrNOqp=r` | `n(o(n(o(o(o(A,B),C),B)),n(o(C,n(o(B,A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L67) |
| `EQ_ON_19_s1_0067` | EQ_ON / 19 | `NONOOpNNqpNOqNOpr=q` | `n(o(n(o(o(A,n(n(B))),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L68) |
| `EQ_ON_19_s1_0068` | EQ_ON / 19 | `NONOOpNNqpNOqNOrp=q` | `n(o(n(o(o(A,n(n(B))),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L69) |
| `EQ_ON_19_s1_0069` | EQ_ON / 19 | `NONONOpNqrNOONqrp=r` | `n(o(n(o(n(o(A,n(B))),C)),n(o(o(n(B),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L70) |
| `EQ_ON_19_s1_0070` | EQ_ON / 19 | `NONONOpNqrNOOprNq=r` | `n(o(n(o(n(o(A,n(B))),C)),n(o(o(A,C),n(B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L71) |
| `EQ_ON_19_s1_0071` | EQ_ON / 19 | `NONONOpNqpNOqNOpr=q` | `n(o(n(o(n(o(A,n(B))),A)),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L72) |
| `EQ_ON_19_s1_0072` | EQ_ON / 19 | `NONONOpNqpNOqNOrp=q` | `n(o(n(o(n(o(A,n(B))),A)),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L73) |
| `EQ_ON_19_s1_0073` | EQ_ON / 19 | `NONONNpOqpNOqNOpr=q` | `n(o(n(o(n(n(A)),o(B,A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L74) |
| `EQ_ON_19_s1_0074` | EQ_ON / 19 | `NONONNpOqpNOqNOrp=q` | `n(o(n(o(n(n(A)),o(B,A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L75) |
| `EQ_ON_19_s1_0075` | EQ_ON / 19 | `NONONNpOqrNOqNOrp=q` | `n(o(n(o(n(n(A)),o(B,C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L76) |
| `EQ_ON_19_s1_0076` | EQ_ON / 19 | `NONOpONNqpNOqNOpr=q` | `n(o(n(o(A,o(n(n(B)),A))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L77) |
| `EQ_ON_19_s1_0077` | EQ_ON / 19 | `NONOpONNqpNOqNOrp=q` | `n(o(n(o(A,o(n(n(B)),A))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L78) |
| `EQ_ON_19_s1_0078` | EQ_ON / 19 | `NONOpONNqrNOqNOrp=q` | `n(o(n(o(A,o(n(n(B)),C))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L79) |
| `EQ_ON_19_s1_0079` | EQ_ON / 19 | `NONOpOqOppNOqNOpr=q` | `n(o(n(o(A,o(B,o(A,A)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L80) |
| `EQ_ON_19_s1_0080` | EQ_ON / 19 | `NONOpOqOppNOqNOrp=q` | `n(o(n(o(A,o(B,o(A,A)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L81) |
| `EQ_ON_19_s1_0081` | EQ_ON / 19 | `NONOpOqOprNOqNOpr=q` | `n(o(n(o(A,o(B,o(A,C)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L82) |
| `EQ_ON_19_s1_0082` | EQ_ON / 19 | `NONOpOqOprNOqNOrp=q` | `n(o(n(o(A,o(B,o(A,C)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L83) |
| `EQ_ON_19_s1_0083` | EQ_ON / 19 | `NONOpOqOqpNOqNOpr=q` | `n(o(n(o(A,o(B,o(B,A)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L84) |
| `EQ_ON_19_s1_0084` | EQ_ON / 19 | `NONOpOqOqpNOqNOrp=q` | `n(o(n(o(A,o(B,o(B,A)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L85) |
| `EQ_ON_19_s1_0085` | EQ_ON / 19 | `NONOpOqOrpNOqNOpr=q` | `n(o(n(o(A,o(B,o(C,A)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L86) |
| `EQ_ON_19_s1_0086` | EQ_ON / 19 | `NONOpOqOrpNOqNOrp=q` | `n(o(n(o(A,o(B,o(C,A)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L87) |
| `EQ_ON_19_s1_0087` | EQ_ON / 19 | `NONOpOqOrqNOrNOpq=r` | `n(o(n(o(A,o(B,o(C,B)))),n(o(C,n(o(A,B))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L88) |
| `EQ_ON_19_s1_0088` | EQ_ON / 19 | `NONOpOqOrrNOqNOpr=q` | `n(o(n(o(A,o(B,o(C,C)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L89) |
| `EQ_ON_19_s1_0089` | EQ_ON / 19 | `NONOpOqOrrNOqNOrp=q` | `n(o(n(o(A,o(B,o(C,C)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L90) |
| `EQ_ON_19_s1_0090` | EQ_ON / 19 | `NONOpNNOqpNOqNOpr=q` | `n(o(n(o(A,n(n(o(B,A))))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L91) |
| `EQ_ON_19_s1_0091` | EQ_ON / 19 | `NONOpNNOqpNOqNOrp=q` | `n(o(n(o(A,n(n(o(B,A))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L92) |
| `EQ_ON_19_s1_0092` | EQ_ON / 19 | `NONOpNNOqrNOqNOpr=q` | `n(o(n(o(A,n(n(o(B,C))))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L93) |
| `EQ_ON_19_s1_0093` | EQ_ON / 19 | `NONOpNNOqrNOqNOrp=q` | `n(o(n(o(A,n(n(o(B,C))))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L94) |
| `EQ_ON_19_s1_0094` | EQ_ON / 19 | `NONNNOOpqpNOqNOpr=q` | `n(o(n(n(n(o(o(A,B),A)))),n(o(B,n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L95) |
| `EQ_ON_19_s1_0095` | EQ_ON / 19 | `NONNNOOpqpNOqNOrp=q` | `n(o(n(n(n(o(o(A,B),A)))),n(o(B,n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L96) |
| `EQ_ON_19_s1_0096` | EQ_ON / 19 | `NONONOpqrNOONNprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(n(n(A)),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L97) |
| `EQ_ON_19_s1_0097` | EQ_ON / 19 | `NONONOpqrNOONNqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(n(n(B)),C),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L98) |
| `EQ_ON_19_s1_0098` | EQ_ON / 19 | `NONONOpqrNOONNqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(n(n(B)),C),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L99) |
| `EQ_ON_19_s1_0099` | EQ_ON / 19 | `NONONOpqrNONONrpp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(o(n(C),A)),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L100) |
| `EQ_ON_19_s1_0100` | EQ_ON / 19 | `NONONOpqrNONONrqq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(o(n(C),B)),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L101) |
| `EQ_ON_19_s1_0101` | EQ_ON / 19 | `NONONOpqrNONNOprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(o(A,C))),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L102) |
| `EQ_ON_19_s1_0102` | EQ_ON / 19 | `NONONOpqrNONNOprq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(o(A,C))),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L103) |
| `EQ_ON_19_s1_0103` | EQ_ON / 19 | `NONONOpqrNONNOqrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(o(B,C))),A))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L104) |
| `EQ_ON_19_s1_0104` | EQ_ON / 19 | `NONONOpqrNONNOqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(n(n(o(B,C))),B))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L105) |
| `EQ_ON_19_s1_0105` | EQ_ON / 19 | `NONONOpqrNOOppOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,A),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L106) |
| `EQ_ON_19_s1_0106` | EQ_ON / 19 | `NONONOpqrNOOppOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,A),o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L107) |
| `EQ_ON_19_s1_0107` | EQ_ON / 19 | `NONONOpqrNOOpqOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,B),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L108) |
| `EQ_ON_19_s1_0108` | EQ_ON / 19 | `NONONOpqrNOOpqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,B),o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L109) |
| `EQ_ON_19_s1_0109` | EQ_ON / 19 | `NONONOpqrNOOprOpp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),o(A,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L110) |
| `EQ_ON_19_s1_0110` | EQ_ON / 19 | `NONONOpqrNOOprOpq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),o(A,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L111) |
| `EQ_ON_19_s1_0111` | EQ_ON / 19 | `NONONOpqrNOOprOqp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),o(B,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L112) |
| `EQ_ON_19_s1_0112` | EQ_ON / 19 | `NONONOpqrNOOprOqq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),o(B,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L113) |
| `EQ_ON_19_s1_0113` | EQ_ON / 19 | `NONONOpqrNOOprOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L114) |
| `EQ_ON_19_s1_0114` | EQ_ON / 19 | `NONONOpqrNOOqpOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,A),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L115) |
| `EQ_ON_19_s1_0115` | EQ_ON / 19 | `NONONOpqrNOOqpOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,A),o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L116) |
| `EQ_ON_19_s1_0116` | EQ_ON / 19 | `NONONOpqrNOOqqOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,B),o(C,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L117) |
| `EQ_ON_19_s1_0117` | EQ_ON / 19 | `NONONOpqrNOOqqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,B),o(C,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L118) |
| `EQ_ON_19_s1_0118` | EQ_ON / 19 | `NONONOpqrNOOqrOpp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),o(A,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L119) |
| `EQ_ON_19_s1_0119` | EQ_ON / 19 | `NONONOpqrNOOqrOpq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),o(A,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L120) |
| `EQ_ON_19_s1_0120` | EQ_ON / 19 | `NONONOpqrNOOqrOqp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),o(B,A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L121) |
| `EQ_ON_19_s1_0121` | EQ_ON / 19 | `NONONOpqrNOOqrOqq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),o(B,B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L122) |
| `EQ_ON_19_s1_0122` | EQ_ON / 19 | `NONONOpqrNOOprNNp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(A,C),n(n(A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L123) |
| `EQ_ON_19_s1_0123` | EQ_ON / 19 | `NONONOpqrNOOqrNNp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(o(B,C),n(n(A))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L124) |
| `EQ_ON_19_s1_0124` | EQ_ON / 19 | `NONONOpqrNOpOOqrq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(o(B,C),B)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L125) |
| `EQ_ON_19_s1_0125` | EQ_ON / 19 | `NONONOpqrNOqOOprp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(o(A,C),A)))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L126) |
| `EQ_ON_19_s1_0126` | EQ_ON / 19 | `NONONOpqrNOpOrNNp=r` | `n(o(n(o(n(o(A,B)),C)),n(o(A,o(C,n(n(A)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L127) |
| `EQ_ON_19_s1_0127` | EQ_ON / 19 | `NONONOpqrNOqOrNNq=r` | `n(o(n(o(n(o(A,B)),C)),n(o(B,o(C,n(n(B)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L128) |
| `EQ_ON_19_s1_0128` | EQ_ON / 19 | `NONOpOqNrNOqNONrp=q` | `n(o(n(o(A,o(B,n(C)))),n(o(B,n(o(n(C),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L129) |
| `EQ_ON_19_s1_0129` | EQ_ON / 19 | `NONONpOqrNOqNOrNp=q` | `n(o(n(o(n(A),o(B,C))),n(o(B,n(o(C,n(A)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L130) |
| `EQ_ON_19_s1_0130` | EQ_ON / 19 | `NONONOpqrNNNOpOrp=r` | `n(o(n(o(n(o(A,B)),C)),n(n(n(o(A,o(C,A)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L131) |
| `EQ_ON_19_s1_0131` | EQ_ON / 19 | `NONONOpqrNNNOqOrq=r` | `n(o(n(o(n(o(A,B)),C)),n(n(n(o(B,o(C,B)))))))=C` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L132) |
| `EQ_ON_19_s1_0132` | EQ_ON / 19 | `NONOpOqpNONNqNOpr=q` | `n(o(n(o(A,o(B,A))),n(o(n(n(B)),n(o(A,C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L133) |
| `EQ_ON_19_s1_0133` | EQ_ON / 19 | `NONOpOqpNONNqNOrp=q` | `n(o(n(o(A,o(B,A))),n(o(n(n(B)),n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L134) |
| `EQ_ON_19_s1_0134` | EQ_ON / 19 | `NONOpOqrNONNqNOrp=q` | `n(o(n(o(A,o(B,C))),n(o(n(n(B)),n(o(C,A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L135) |
| `EQ_ON_19_s1_0135` | EQ_ON / 19 | `NONOpOqrNOqNOOprs=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(A,C),D))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L136) |
| `EQ_ON_19_s1_0136` | EQ_ON / 19 | `NONOpOqrNOqNOOpsr=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(A,D),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L137) |
| `EQ_ON_19_s1_0137` | EQ_ON / 19 | `NONOpOqrNOqNOOrps=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(C,A),D))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L138) |
| `EQ_ON_19_s1_0138` | EQ_ON / 19 | `NONOpOqrNOqNOOrsp=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(C,D),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L139) |
| `EQ_ON_19_s1_0139` | EQ_ON / 19 | `NONOpOqrNOqNOOspr=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(D,A),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L140) |
| `EQ_ON_19_s1_0140` | EQ_ON / 19 | `NONOpOqrNOqNOOsrp=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(o(D,C),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L141) |
| `EQ_ON_19_s1_0141` | EQ_ON / 19 | `NONOOpqpNOqNONNpr=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(n(n(A)),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L142) |
| `EQ_ON_19_s1_0142` | EQ_ON / 19 | `NONOOpqpNOqNONNrp=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(o(n(n(C)),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L143) |
| `EQ_ON_19_s1_0143` | EQ_ON / 19 | `NONOpOqpNOqNOpNNr=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(A,n(n(C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L144) |
| `EQ_ON_19_s1_0144` | EQ_ON / 19 | `NONOpOqpNOqNOrNNp=q` | `n(o(n(o(A,o(B,A))),n(o(B,n(o(C,n(n(A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L145) |
| `EQ_ON_19_s1_0145` | EQ_ON / 19 | `NONOpOqrNOqNOrNNp=q` | `n(o(n(o(A,o(B,C))),n(o(B,n(o(C,n(n(A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L146) |
| `EQ_ON_19_s1_0146` | EQ_ON / 19 | `NONOOpqpNOqNNNOpr=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(n(n(o(A,C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L147) |
| `EQ_ON_19_s1_0147` | EQ_ON / 19 | `NONOOpqpNOqNNNOrp=q` | `n(o(n(o(o(A,B),A)),n(o(B,n(n(n(o(C,A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L148) |
| `EQ_ON_19_s1_0148` | EQ_ON / 19 | `NONOOpqpNNNOqNOpr=q` | `n(o(n(o(o(A,B),A)),n(n(n(o(B,n(o(A,C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L149) |
| `EQ_ON_19_s1_0149` | EQ_ON / 19 | `NONOOpqpNNNOqNOrp=q` | `n(o(n(o(o(A,B),A)),n(n(n(o(B,n(o(C,A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L150) |
| `EQ_ON_19_s1_0150` | EQ_ON / 19 | `NONONpqNOONOrNpqp=q` | `n(o(n(o(n(A),B)),n(o(o(n(o(C,n(A))),B),A))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L151) |
| `EQ_ON_19_s1_0151` | EQ_ON / 19 | `NONONpqNONONprOqp=q` | `n(o(n(o(n(A),B)),n(o(n(o(n(A),C)),o(B,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L152) |
| `EQ_ON_19_s1_0152` | EQ_ON / 19 | `NONONpqNONONqrOqp=q` | `n(o(n(o(n(A),B)),n(o(n(o(n(B),C)),o(B,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L153) |
| `EQ_ON_19_s1_0153` | EQ_ON / 19 | `NONONpqNONOrNpOqp=q` | `n(o(n(o(n(A),B)),n(o(n(o(C,n(A))),o(B,A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L154) |
| `EQ_ON_19_s1_0154` | EQ_ON / 19 | `NONONpqNOOpqNONpr=q` | `n(o(n(o(n(A),B)),n(o(o(A,B),n(o(n(A),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L155) |
| `EQ_ON_19_s1_0155` | EQ_ON / 19 | `NONONpqNOOpqNONqr=q` | `n(o(n(o(n(A),B)),n(o(o(A,B),n(o(n(B),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L156) |
| `EQ_ON_19_s1_0156` | EQ_ON / 19 | `NONONpqNOpOqNOrNp=q` | `n(o(n(o(n(A),B)),n(o(A,o(B,n(o(C,n(A))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L157) |
| `EQ_ON_19_s1_0157` | EQ_ON / 19 | `NONOpqNOONONrpqNp=q` | `n(o(n(o(A,B)),n(o(o(n(o(n(C),A)),B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L158) |
| `EQ_ON_19_s1_0158` | EQ_ON / 19 | `NONOpqNOONOpNrqNp=q` | `n(o(n(o(A,B)),n(o(o(n(o(A,n(C))),B),n(A)))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L159) |
| `EQ_ON_19_s1_0159` | EQ_ON / 19 | `NONOpqNONONqrOqNp=q` | `n(o(n(o(A,B)),n(o(n(o(n(B),C)),o(B,n(A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L160) |
| `EQ_ON_19_s1_0160` | EQ_ON / 19 | `NONOpqNONONrpOqNp=q` | `n(o(n(o(A,B)),n(o(n(o(n(C),A)),o(B,n(A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L161) |
| `EQ_ON_19_s1_0161` | EQ_ON / 19 | `NONOpqNONOpNrOqNp=q` | `n(o(n(o(A,B)),n(o(n(o(A,n(C))),o(B,n(A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L162) |
| `EQ_ON_19_s1_0162` | EQ_ON / 19 | `NONOpqNOONpqNONqr=q` | `n(o(n(o(A,B)),n(o(o(n(A),B),n(o(n(B),C))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L163) |
| `EQ_ON_19_s1_0163` | EQ_ON / 19 | `NONOpqNOONpqNONrp=q` | `n(o(n(o(A,B)),n(o(o(n(A),B),n(o(n(C),A))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L164) |
| `EQ_ON_19_s1_0164` | EQ_ON / 19 | `NONOpqNOONpqNOpNr=q` | `n(o(n(o(A,B)),n(o(o(n(A),B),n(o(A,n(C)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L165) |
| `EQ_ON_19_s1_0165` | EQ_ON / 19 | `NONOpqNONpOqNONrp=q` | `n(o(n(o(A,B)),n(o(n(A),o(B,n(o(n(C),A)))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L166) |
| `EQ_ON_19_s1_0166` | EQ_ON / 19 | `NONOpqNONpOqNOpNr=q` | `n(o(n(o(A,B)),n(o(n(A),o(B,n(o(A,n(C))))))))=B` | [row](../../results/equational_lower_bounds/survivors/BAON/length19_shard1.jsonl#L167) |
