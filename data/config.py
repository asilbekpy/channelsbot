from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "6792619983:AAGmllbnG2U5NpAHlOuLdZloIpQalR6xz1o"#env.str("BOT_TOKEN")  # Bot toekn
ADMINS = [1024522810,1680816082]#env.list("ADMINS")  # adminlar ro'yxati
IP = "localhost"#env.str("ip")  # Xosting ip manzili
