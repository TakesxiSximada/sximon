app:
	docker run --name kageyama-app -p 6543:6543 --link kageyama-redis:redis -d kageyama/app

redis:
	docker run --name kageyama-redis -d kageyama/redis
