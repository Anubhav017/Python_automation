from functools import lru_cache

import gevent.ssl
from locust import FastHttpUser, constant, task

import config


@lru_cache(maxsize=1)
def shared_ssl_context(cafile=None):
    # built once: loading CA certs per user costs so much CPU (Windows cert store)
    # that 1000 users starve the load generator. Each user still does its own TLS handshake.
    return gevent.ssl.create_default_context(cafile=cafile)


class HomepageVisitor(FastHttpUser):
    """A new visitor: opens its own connection, loads the homepage once, then stays idle."""

    host = config.LOAD_BASE_URL
    insecure = False
    ssl_context_factory = staticmethod(shared_ssl_context)
    # far longer than the test, so every user makes exactly one visit
    wait_time = constant(3600)

    @task
    def homepage(self):
        headers = {"User-Agent": config.USER_AGENT, "Accept": "text/html"}
        with self.client.get("/", headers=headers, name="GET /", catch_response=True) as resp:
            # a 200 is not enough, an error page can come back as 200 too
            if resp.status_code != 200:
                resp.failure(f"status {resp.status_code}")
            elif config.LOAD_EXPECT_TEXT not in resp.text:
                resp.failure("expected homepage text missing")
