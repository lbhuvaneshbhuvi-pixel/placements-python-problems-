def most_frequent_word(text):
    words = [w.lower() for w in text.split()]
    if not words:
        return ""
    from collections import Counter
    counts = Counter(words)
    max_count = max(counts.values())
    candidates = [w for w in counts if counts[w] == max_count]
    return min(candidates)


