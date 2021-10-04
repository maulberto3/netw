import asyncio
import aioftp
import ssl
import uvloop
uvloop.install()

# ctx = ssl.create_default_context()
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)


async def main():
    server = aioftp.Server(ssl=ctx)  #  [user], path_io_factory=path_io_factory
    await server.run()


asyncio.run(main())