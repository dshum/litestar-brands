from litestar.events import listener


@listener("refresh")
async def refresh_brands() -> None:
    print("before refresh_brands")
    try:
        # state = State()
        # scope = HTTPScope()
        # async with remote_sqlalchemy_config.provide_session(state, scope) as remote_session:
        #     remote_service = RemoteBrandService(session=remote_session)
        #     statement = (select(RemoteBrand)
        #                  .order_by(RemoteBrand.name.asc()))
        #     remote_brands = await remote_service.list(statement=statement)
        #     print("remote brands received")
        # data = [brand.to_dict() for brand in remote_brands]
        # session = sqlalchemy_config.get_session()
        # async with BrandService.new(session=db_session) as service:
        #     await service.upsert_many(data=data, match_fields=["name"])
        # await redis_store.delete_all()
        print("brands refreshed")
    except Exception as err:
        print(err)
