from pprint import pprint
import asyncio
import aioftp
import ssl
import uvloop
uvloop.install()

ctx = ssl.create_default_context()
# ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# netstat -lp listening and processes

async def main():
    async with aioftp.Client.context(host='0.0.0.0', port=41175) as client:
        pprint([x for x in dir(client) if "_" not in x])
        # res = await client.list()
        # pprint(res)
        # # res = await client.command('RETR')
        # # pprint(res)
        res = await client.download(source='README',
                destination='README2')
        pprint(res)


# async def main():
#     tasks = [
#         asyncio.create_task(get_mp3("server1.com", 21, "login", "password")),
#         asyncio.create_task(get_mp3("server2.com", 21, "login", "password")),
#         asyncio.create_task(get_mp3("server3.com", 21, "login", "password")),
#     ]
#     await asyncio.wait(tasks)


asyncio.run(main())