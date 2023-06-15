# src/page_tracker/app.py

import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """index method"""
    try:
        page_views = get_redis().incr("page_views")

    except RedisError:
        app.logger.exception("Redis error")  # pylint: disable=E1101
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This page has been seen {page_views} times."


@cache
def get_redis():
    """get_redis function"""
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
