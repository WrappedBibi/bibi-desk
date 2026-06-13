# Roadmap

Near term:
- [x] single-symbol desk loop (forecast, signal, size, execute)
- [x] event-driven backtester with R-multiple accounting
- [x] Rust execution engine (order router + paper fill sim)
- [ ] portfolio layer: gross risk budget + per-cluster caps
- [ ] correlation-aware sizing so correlated legs share a cap
- [ ] live venue adapters past the paper stub
- [ ] walk-forward retraining cadence for the Kronos checkpoint

Research:
- [ ] risk parity vs half-Kelly on the 1h book (see feature/risk-parity)
- [ ] confidence floor sweep per symbol
