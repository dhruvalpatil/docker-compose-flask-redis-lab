
import os
import time
import logging
from flask import Flask
import redis

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

redis_host = os.getenv("REDIS_HOST", "redis")

# Retry connecting while Redis starts
cache = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True,
    socket_connect_timeout=2
)

@app.route("/")
def home():
    try:
        visits = cache.incr("page_visits")
        logging.info("Page visited. Total visits: %s", visits)
        return f"""
        <h1>Docker Compose Flask + Redis</h1>
        <p>Welcome to my DevOps project!</p>
        <h2>Total visits: {visits}</h2>
        """
    except redis.RedisError:
        logging.exception("Redis connection failed")
        return "Redis is temporarily unavailable. Please try again.", 503

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
