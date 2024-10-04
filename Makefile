SSH_TARGET ?= pi@turbopi.local

requirements.txt: requirements.in
	uv pip compile $^ > $@

turbopi.zip: __main__.py src/*.py
	# python can run this because it has a __main__
	rm -f $@
	7z a $@ $^

deploy: turbopi.zip
	scp $^ $(SSH_TARGET):~
