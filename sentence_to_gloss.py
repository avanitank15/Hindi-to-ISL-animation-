"""
Rule-based sentence → gloss converter.

- Works out of the box for English with spaCy's en_core_web_sm model.
- Can be adapted to other languages by swapping the NLP pipeline and POS tags.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List

import spacy

@dataclass
class SentenceToGloss:
    """
    Simple rule-based sentence → gloss converter.

    Attributes
    ----------
    nlp_model : str
        spaCy model name, e.g. "en_core_web_sm".
    lexicon : Dict[str, str]
        Optional mapping from token lemma (lowercase) to gloss token.
    keep_pos : set
        POS tags that are kept as content words.
    """

    nlp_model: str = "en_core_web_sm"
    lexicon: Dict[str, str] = field(default_factory=dict)
    keep_pos: set = field(default_factory=lambda: {
        "NOUN", "PROPN", "VERB", "AUX", "ADJ", "ADV", "NUM"
    })

    def __post_init__(self):
        # Load spaCy model once
        self.nlp = spacy.load(self.nlp_model, disable=["ner"])  # NER not needed

    # --------- Public API ---------
    def gloss_sentence(self, sentence: str) -> str:
        """
        Convert a spoken-language sentence into a gloss string.

        Parameters
        ----------
        sentence : str
            Input sentence (e.g. English / Indic in Roman).

        Returns
        -------
        str
            Gloss sequence (space-separated).
        """
        doc = self.nlp(sentence)
        time_tokens, location_tokens, content_tokens = [], [], []

        for token in doc:
            gloss_token = self._token_to_gloss(token)
            if not gloss_token:
                continue

            # Use dependency labels heuristically to reorder TIME / LOCATION
            if token.dep_ in {"npadvmod"} and self._looks_like_time(token):
                time_tokens.append(gloss_token)
            elif token.dep_ in {"pobj", "obl", "advmod"} and self._looks_like_location(token):
                location_tokens.append(gloss_token)
            else:
                content_tokens.append(gloss_token)

        # Basic SLish order: TIME – LOCATION – MAIN CONTENT
        gloss_sequence = time_tokens + location_tokens + content_tokens
        return " ".join(gloss_sequence)

    # --------- Internal helpers ---------
    def _token_to_gloss(self, token) -> str | None:
        """
        Map a spaCy token to a gloss token (or None to drop it).
        """
        # Skip pure punctuation
        if token.is_punct:
            return None

        lemma = token.lemma_.lower().strip()

        # 1. Lexicon override (highest priority)
        if lemma in self.lexicon:
            return self.lexicon[lemma]

        # 2. Drop obvious function words by POS or stopword flag
        if token.pos_ not in self.keep_pos or token.is_stop:
            return None

        # 3. Default: lemma in uppercase
        gloss = lemma.upper()

        # 4. Add simple tags for some POS types (optional)
        if token.pos_ in {"VERB", "AUX"}:
            gloss = f"{gloss}"  # e.g. VERBS: no suffix, or use f"{gloss}-V"
        elif token.pos_ == "ADJ":
            gloss = f"{gloss}"  # e.g. f"{gloss}-ADJ" if you want
        elif token.pos_ == "ADV":
            gloss = f"{gloss}"

        return gloss

    @staticmethod
    def _looks_like_time(token) -> bool:
        text = token.text.lower()
        time_words = {"today", "yesterday", "tomorrow",
                      "morning", "evening", "night",
                      "now", "later", "soon"}
        return text in time_words

    @staticmethod
    def _looks_like_location(token) -> bool:
        text = token.text.lower()
        loc_words = {"school", "office", "home", "house", "park",
                     "market", "village", "city"}
        return text in loc_words
