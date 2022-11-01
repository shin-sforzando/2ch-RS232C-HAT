# -*- coding: utf-8 -*-

TIMESTAMP := $(shell date +%Y%m%d%H%M%S)
MAKEFILE_DIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
OS_NAME := $(shell uname -s)

OPTS :=
.DEFAULT_GOAL := default
.PHONY: default init open hide reveal start format lint test pytest doc sphinx clean help

default: ## 常用
	make start

init: ## 初期
ifeq ($(OS_NAME),Darwin)
	brew install git-cliff
	brew install git-secret
	brew install direnv
	brew install lefthook
endif
	make reveal
	direnv allow
	lefthook install
	pip install -r requirements.txt
	@if [ $(OS_NAME) = "Darwin" ]; then say "The initialization process is complete." ; fi

open: ## 閲覧
	@if [ $(OS_NAME) = "Darwin" ]; then open ${OPEN_TARGET} ; fi

hide: ## 秘匿
	git secret hide -vm

reveal: ## 暴露
	git secret reveal -vf

start: ## 開始
	@if [ $(OS_NAME) = "Darwin" ]; then say "Start the application." ; fi
	python src/main.py

format: ## 整形
	black $(OPTS) .
	@if [ $(OS_NAME) = "Darwin" ]; then say "The format process is complete." ; fi

lint: ## 検証
	flake8 $(OPTS)
	@if [ $(OS_NAME) = "Darwin" ]; then say "The lint process is complete." ; fi

test: ## 試験
	pytest $(OPTS)
	@if [ $(OS_NAME) = "Darwin" ]; then say "The test process is complete." ; fi

pytest: ## 試験
	pytest $(OPTS)

doc: sphinx ## 文書

sphinx: format ## 文書
	sphinx-apidoc --force --output-dir docs .
	sphinx-build -a -b html docs docs/_build/
	@if [ $(OS_NAME) = "Darwin" ]; then say "The document generation is complete." ; fi
	make open OPEN_TARGET="./docs/_build/index.html"

clean: ## 掃除
	rm -rfv logs/*
	find . -type f -name "*.log" -prune -exec rm -rf {} +
	rm -rfv .mypy_cache
	rm -rfv .pytest_cache
	rm -rfv .coverage.*
	@if [ $(OS_NAME) = "Darwin" ]; then say "The cleanup process is complete." ; fi

help: ## 助言
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
