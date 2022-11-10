import random

from aiohttp import web

routes = web.RouteTableDef()

users = {}


@routes.get('/randomcoins')
async def index(request):
	data = {
		"coins": random.randint(1, 100)
	}
	return web.json_response(data)


@routes.get('/user/{user_id:\d+}')
async def user(request):
	user_id = int(request.match_info['user_id'])
	user = users.get(user_id)
	if user is None:
		return web.json_response({
			"error": "User not found"
		}, status=404)
	return web.json_response(user)


@routes.post('/user/{user_id:\d+}')
async def update_user(request):
	user_id = int(request.match_info['user_id'])
	data = await request.json()
	users[user_id] = data
	return web.json_response(data)


if __name__ == '__main__':
	app = web.Application()
	app.add_routes(routes)
	web.run_app(app)
