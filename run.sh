#!/usr/bin/env sh

set -ex

# uv gets installed here
export PATH=$PATH:$HOME/.cargo/bin

if [ ! $(command -v uv) ]; then
	if [ ! $(command -v curl) ]; then
		echo need curl to install UV. please install curl on this system.
		exit 1
	fi
	curl -LsSf https://astral.sh/uv/install.sh | sh
fi

if [ ! -d .venv ]; then
	uv venv
fi
uv pip sync requirements.txt
.venv/bin/python viam_module.py $@
