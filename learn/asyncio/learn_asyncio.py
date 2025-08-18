import asyncio
import random

class AsyncioLearn():
    async def say_hello(self, i, segundo):
        print(f"Hola {i} en {segundo} segundos")
        await asyncio.sleep(segundo)
        print(f"Hola {i} despues de {segundo} segundos")

    async def main(self, n):
        tasks = []
        for i in range(n):
            task = asyncio.create_task(self.say_hello(i, random.randint(1, 5)))
            tasks.append(task)
        await asyncio.gather(*tasks)

asyncio_obj = AsyncioLearn()
asyncio.run(asyncio_obj.main(10)) 


# async def say_hello(i, segundos):
#     print(f"Hello, world!!! -> Indice: {i}")
#     await asyncio.sleep(segundos)
#     print(f"Goodbye, world!!! -> Indice: {segundos}")

# async def lista_say_hello(n):
#     lista_tareas = []
#     for i in range(n):
#         segundo = 0 if i==0 else random.randint(1, 5)
#         print(i)
#         lista_tareas.append(say_hello(i, segundo))
#         print(f"Executado {i+1} de {n}")

#     await asyncio.gather(*lista_tareas)
    

# asyncio.run(lista_say_hello(500))