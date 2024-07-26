from litestar.middleware.rate_limit import RateLimitConfig

rate_limit_config = RateLimitConfig(rate_limit=("minute", 1))
