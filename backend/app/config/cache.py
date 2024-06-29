from litestar.config.response_cache import ResponseCacheConfig

cache_config = ResponseCacheConfig(store="redis_store")
