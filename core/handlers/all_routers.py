all_routers = []

from core.handlers.admin.admin_routers import routers

all_routers += routers

from core.handlers.user.user_routers import routers

all_routers += routers

from core.handlers.other.other_routers import routers

all_routers += routers


