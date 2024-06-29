from litestar.stores.redis import RedisStore

from app.config import settings

redis_store = RedisStore.with_client(
    url=settings.redis.location,
    namespace=settings.redis.namespace,
)
