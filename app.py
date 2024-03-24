import g4f
from g4f.api import Api
import os

list_ignored_providers = [
    # "RetryProvider",
    "GptForLove",
    "ChatBase",
    "Chatgpt4Online",
    "ChatAnywhere",
    "GptGo",
    "You",
]
self_port = os.environ.get('PORT', '1337')

if __name__ == "__main__":
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')
    port=self_port
    app = Api(engine=g4f,list_ignored_providers=list_ignored_providers, debug=True)
    app.run(f"0.0.0.0:{port}", use_colors=True)
