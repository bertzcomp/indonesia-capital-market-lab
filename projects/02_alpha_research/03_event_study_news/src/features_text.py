import re

POS_WORDS = {
    "menguat","membaik","naik","mengangkat","borong","katalis",
    "positif","kuat","potensi","melonjak","menaik","mendongkrak",
    "menguntungkan","mendorong","mengerek"
}

NEG_WORDS = {
    "koreksi","tertekan","jual","jatuh","melemah","penurunan",
    "ketat","tekan","terseret","ambil","panic","lemah","menurun"
}

def text_features(title: str):
    title = str(title).lower()
    words = re.findall(r"[a-zA-Z]+", title)

    pos = sum(w in POS_WORDS for w in words)
    neg = sum(w in NEG_WORDS for w in words)

    sent_score = (pos - neg) / max(1, len(words))

    return {
        "sent_score": sent_score,
        "pos_count": pos,
        "neg_count": neg,
        "title_len": len(words)
    }
