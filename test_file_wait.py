import os
import logging
import asyncio


async def read_timestamp(COUNTER_FILE):
    logging.info("[Counter object]: Read last timestamp from %s" % COUNTER_FILE)
    while 1:

        while not os.path.exists(COUNTER_FILE):
            logging.info("[Counter object]: Timestamp file is not exists")
            yield "No File"

        with open(COUNTER_FILE) as f:
            stamp = f.read()

        if not len(stamp):
            logging.info("[Counter object]: Empty timestamp file")
            yield "No timestamp"

        logging.info("[Counter object]: Last timestamp %s" % stamp)
        yield stamp


# reader = read_timestamp("test_file.txt")
async def timestamp_reader():
    async for resp in read_timestamp("test_file.txt"):
        print(resp)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(timestamp_reader())
    loop.run_forever()
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
