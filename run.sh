#!/usr/bin/env sh

set -ex

# if [ ! $(command -v uv) ]; then
# 	curl -LsSf https://astral.sh/uv/install.sh | sh
# fi

# uv got installed here
export PATH=$PATH:$HOME/.cargo/bin
if [ ! -d .venv ]; then
	uv venv
fi
uv pip sync requirements.txt
.venv/bin/python viam_module.py $@
