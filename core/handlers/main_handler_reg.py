from aiogram import Dispatcher
from core.handlers.user.user_handlers_reg import registration_user_handlers
from core.handlers.admin.admin_handlers_reg import registration_admin_handlers
from core.handlers.other.other_handlers_reg import registration_other_handlers

def registration_handlers(dp:Dispatcher):
    registration_admin_handlers(dp)
    registration_user_handlers(dp)
    registration_other_handlers(dp) 