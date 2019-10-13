import asyncio
import json
import logging
import websockets
import psycopg2
from psycopg2 import sql

logging.basicConfig()

STATE = {"value": "empty"}

USERS = set()

STATES = []

def state_event():
    return json.dumps({"type": "data", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
#        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["data"] != '':
                STATE["value"] = data["data"]
                STATES.append(data["data"])
                print(STATES)
                await notify_state()
            else:
                logging.error("Massage is empty")
    finally:
        await unregister(websocket)
        if len(USERS) == 0:
            conn = psycopg2.connect(dbname='retrospective_db', user='retro_user', password='2427980baba', host='127.0.0.1', port='5432')
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM retros_session")
            x = cursor.fetchall()[-1][0]
            newState= '&'.join(STATES)
            query = "UPDATE retros_session SET oneword = '{newState}' WHERE id = '{x}'".format(newState = newState, x = x)
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()

start_server = websockets.serve(counter, "0.0.0.0", 3004)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()