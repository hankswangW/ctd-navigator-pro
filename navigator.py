"""Search and presentation logic independent of Streamlit."""

import re
import unicodedata
from difflib import SequenceMatcher

from ctd_data import RECORDS


def normalize(text):
    text = unicodedata.normalize("NFKC", (text or "")).lower().strip()
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", " ", text).strip()


def _score(query, record):
    q = normalize(query)
    if not q:
        return 0.0
    candidates = [record["name"], record["zh"]] + record["aliases"]
    best = 0.0
    q_tokens = set(q.split())
    for candidate in candidates:
        c = normalize(candidate)
        if q == c:
            score = 1.0
        elif q in c or c in q:
            score = 0.88 + 0.08 * min(len(q), len(c)) / max(len(q), len(c))
        else:
            c_tokens = set(c.split())
            overlap = len(q_tokens & c_tokens) / max(1, len(q_tokens | c_tokens))
            sequence = SequenceMatcher(None, q, c).ratio()
            score = max(0.78 * sequence, 0.82 * overlap)
        best = max(best, score)
    return best


def search_records(query, scope, limit=8):
    """Return relevant records for DS/DP, highest-confidence first."""
    eligible = [r for r in RECORDS if scope in r["scope"]]
    if not normalize(query):
        return []
    ranked = sorted(((round(_score(query, r), 3), r) for r in eligible), key=lambda x: x[0], reverse=True)
    return [(score, record) for score, record in ranked[:limit] if score >= 0.24]


def confidence_label(score):
    if score >= 0.86:
        return "高匹配"
    if score >= 0.58:
        return "可能匹配"
    return "探索结果"

