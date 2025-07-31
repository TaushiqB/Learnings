import asyncio

async def main():
    print("Start of Main Coroutine")


asyncio.run(main()) # We pass a coroutine funcion and this will return a coroutine object and that is passed to asyncio.run
# Asyncio is gonna start our event loop, 
# We cant simply run the function-as running the function will generate a co routine object, this coroutine object needs to be awaited inorder to actually
# get the result of its execution
# Await keyword is used to await a coroutine and allow it to execute and get the result
# We can use this await keyword inside an asynch func or inside a coroutine 
