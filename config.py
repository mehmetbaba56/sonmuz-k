from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", BAE3xB4AHqae8q9OR2AIQRyzjpUW15N0AjkayWmH65dC97LR_D8w005l7NfeAZdz3XD-OlGJEbBvUDux57qu5V2WYOTMofMvznUKEoXmcyRc2Pz2_Gong_UUYZLvKcfNNsGOYN3kmxtQgO0oyog7rKAIiivvEAAG6uoVkra-FG30a7gkQy6Z_s1nmmas8iVEPeJCRwbLe7kQZQlC58IpTS9qTbnDx31T8bWX6CZzvvwHVbxkgjU-w-GURh3wKGlbFtv0gz-4vIedanzL_TencSzscsKB7RSLp_kfOHv0-v66Io6w-RFaH3g-IZSuA8e_4UXmKD5i6NfC1hATvgUTse9xz48d4AAAAAGdozS4AA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TSGCheckerChat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TSGChecker")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
