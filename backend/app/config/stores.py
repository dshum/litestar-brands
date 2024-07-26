from litestar.stores.redis import RedisStore

from app.config import settings

redis_store = RedisStore.with_client(
    url=settings.redis.LOCATION,
    namespace=settings.redis.NAMESPACE,
)
