import os
class Config:
    API_ID=25206101
    API_HASH="2135724a8fdecb737f31d22ec8e6894b"
    TOKEN="7657159740:AAHjfaLL2CTyJKqsJqXQl55Fk5NY9EuhR3c"
    SUDO = list(int(i) for i in os.environ.get("SUDO", "7601457849").split(" "))
    START_IMG="https://graph.org/file/4308dcc94aacbdc3ed0c9-c04a9611c927588ddc.jpg"
    BOT_ID=7657159740
    BOT_USERNAME="@Copyrightremover213bot"
    BOT_NAME="copyright remover bot"
