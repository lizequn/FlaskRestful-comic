import os
import logging
from joblib import load
from scipy.sparse import load_npz
import json
from flask import g
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from ..config import MODEL_FOLDER


def get_model():
    if 'vectorizer' not in g:
        g.vectorizer = load(os.path.join(MODEL_FOLDER, 'vectorizer.joblib'))
        g.X = load_npz(os.path.join(MODEL_FOLDER, 'X_matrix.npz'))
        with open(os.path.join(MODEL_FOLDER, 'file_infos.json'), 'r') as f:
            g.file_infos = json.load(f)
    return g.vectorizer, g.X, g.file_infos


def get_nlp():
    if 'nlp' not in g:
        g.nlp = spacy.load("en_core_web_sm")
    return g.nlp


def get_topk(arr, k=3):
    return np.argpartition(arr, len(arr) - k)[-k:][::-1]


def lemma_stopword(content):
    nlp = get_nlp()
    return " ".join(token.lemma_ for token in nlp(content) if
                    token.lemma_.lower() not in nlp.Defaults.stop_words and token.is_alpha)


def lemma(content):
    nlp = get_nlp()
    return " ".join(token.lemma_ for token in nlp(content) if token.is_alpha)


def recommend(script):
    logging.debug(f"do recommendation scripts:{script}")
    vectorizer, X, file_infos = get_model()
    processed_script = lemma(script)
    y = vectorizer.transform([processed_script])
    distance = cosine_similarity(X, y)
    results= []
    for query in range(distance.shape[1]):
        for index in get_topk(distance[:, query]):
            results.append(file_infos[str(index)])
    return results,'version'
