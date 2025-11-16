#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "5537394771:AAG5OMq_gKFrFoI-mS4-blHcXGs4eAFOhDo"

    # Get from my.telegram.org
    APP_ID = int(12581928)

    # Get from my.telegram.org
    API_HASH = "9bd003806267466f904f91aa035d8991"

    # Generate a user session string
    TG_USER_SESSION = "BQC__CgAcjJlsgSl0FR27HAGc4slIg8fXRcv0Fp9ZcL5bOPT1gWHtfHyE7wwPBTpFaEVJ82wcIGKi4XjZp9IooLUTK-qSXyt8N6ogmJTHvW4kOP4A8ZHomJjlFDvlZeBVY6QsJnlkNzRULpW27TT0zNWCQrF0WcBuHGnafY9XWkCUoI1LnNe7CAmJSrE_R5oDr-aM0GqCsYhnoeVjnxD4pWCB4N-NrWqCPERZdwaDOJIm-_QDoouB10wvr6kshP6gil6KlQ5SpZmdBq_x-PJbeoT1wborBOqLwg9w464o3vwpXMuB_nb5mZnv2wEAzmlPamUA6CSazfRrvqggbEkwDUX6_ewFAAAAABgpBXkAA"

    # Database URI
    DB_URI = "mongodb+srv://freakboy:freakboy@cluster0.qhvex0i.mongodb.net/?appName=Cluster0"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
