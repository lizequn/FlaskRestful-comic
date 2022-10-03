import logging
from app.main import app


def recommend(scripts):
    logging.debug(f"do recommendation scripts:{scripts}")
    return [{'href': 'address', 'title': 'article title'}, {'href': 'address', 'title': 'article title'}], 'test'
