routers = []

from core.handlers.user.game_handler import router

routers.append(router)

from core.handlers.user.callback_handler import router

routers.append(router)

from core.handlers.user.basic_handler import router

routers.append(router)



