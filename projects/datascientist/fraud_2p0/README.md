# Fraud 2.0 — PR‑AUC + Threshold Tuning

**Goal (Week 3–4):** Rebuild classification with sklearn `Pipeline`, stratified CV, PR curve focus, and a clear threshold choice.

**Checklist**
- [ ] Pipeline with `ColumnTransformer`, no leakage
- [ ] Compare Logistic, Tree/Forest, XGBoost
- [ ] Handle imbalance: class weights/SMOTE, report PR‑AUC
- [ ] Calibrate and pick threshold for business cost
- [ ] `model_card.md` with data, metrics, risks

**Deliverables**
- `notebooks/`, `src/`, `models/`, `streamlit_app.py`, `model_card.md`
