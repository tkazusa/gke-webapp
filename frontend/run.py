# -*- encoding: UTF-8 -*-
import os
from _config import config
from _frontend import create_app

try:
    config_fie = os.environ['APP_CONFIG_FILE']
except KeyError as e:
    KeyError("Set env APP_CONFIG_FILE")


config = config.load()
app = create_app()


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Run webapp interface')
    parser.add_argument("--host", type=str, default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()

    app.run(debug=True, host=args.host, port=args.port)
