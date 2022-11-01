# 2ch-RS232C-HAT

<!-- Badges -->
[![Last Commit](https://img.shields.io/github/last-commit/shin-sforzando/2ch-RS232C-HAT)](https://github.com/shin-sforzando/2ch-RS232C-HAT/graphs/commit-activity)
[![CI](https://github.com/shin-sforzando/2ch-RS232C-HAT/actions/workflows/ci.yml/badge.svg)](https://github.com/shin-sforzando/2ch-RS232C-HAT/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/shin-sforzando/2ch-RS232C-HAT/branch/main/graph/badge.svg?token=TDCVLUJ4RF)](https://codecov.io/gh/shin-sforzando/2ch-RS232C-HAT)
[![GitHub Pages](https://github.com/shin-sforzando/2ch-RS232C-HAT/actions/workflows/pages.yml/badge.svg)](https://shin-sforzando.github.io/2ch-RS232C-HAT/)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<!-- Screenshots -->
| ![Screenshot 1](https://placehold.jp/32/3d4070/ffffff/720x480.png?text=Screenshot%201) | ![Screenshot 2](https://placehold.jp/32/703d40/ffffff/720x480.png?text=Screenshot%202) |
|:--------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
|                                      Screenshot 1                                      |                                      Screenshot 2                                      |

<!-- Synopsis -->
Create a useful tools for debugging RS-232C serial communications using [2ch-RS232C-HAT](https://www.waveshare.com/2-ch-rs232-hat.htm).

![2022-11-01 21 41 26 www waveshare com e47b434a2467](https://user-images.githubusercontent.com/32637762/199235202-9040a621-a715-46f6-afad-e3b84a7620e7.png)

## *Use this template*

<!-- TOC -->
- [*Use this template*](#use-this-template)
- [Prerequisites](#prerequisites)
- [How to](#how-to)
  - [Setup Raspberry Pi](#setup-raspberry-pi)
  - [First time preparation](#first-time-preparation)
    - [Init](#init)
    - [Reveal Secrets](#reveal-secrets)
    - [Setup Git Hooks (Lefthook)](#setup-git-hooks-lefthook)
  - [Develop](#develop)
    - [`.env`](#env)
    - [Start](#start)
    - [Format](#format)
    - [Lint](#lint)
    - [Test](#test)
  - [Document](#document)
    - [API Document](#api-document)
    - [CHANGELOG](#changelog)
  - [Clean](#clean)
- [Misc](#misc)
- [Notes](#notes)
  - [LICENSE](#license)
  - [Contributors](#contributors)

## Prerequisites

- [Python](https://www.python.org) (Version 3.10 or higher)
  - Production Dependencies
    - (T. B. D.)
  - Development Dependencies
    - [black](https://github.com/psf/black) as *Python Formatter*
    - [flake8](https://pypi.org/project/flake8/) as *Python Code Linter*
    - [Sphinx](https://www.sphinx-doc.org/) as *Python Document Generator*
    - [loguru](https://github.com/Delgan/loguru) as *Application Logger*
    - [pytest](https://pypi.org/project/pytest/) for *Application Test*
      - [pytest-xdist](https://pypi.org/project/pytest-xdist/) for *Parallel Testing*
- [Lefthook](https://github.com/evilmartians/lefthook) as *Git Hooks Manager*
- [git-secret](https://git-secret.io/) as *Secret File Manager*
- [direnv](https://direnv.net) as *`.env` Loader*

## How to

```shell
$ make help
default              常用
init                 初期
open                 閲覧
hide                 秘匿
reveal               暴露
start                開始
format               整形
lint                 検証
test                 試験
pytest               試験
doc                  文書
sphinx               文書
clean                掃除
help                 助言
```

### Setup Raspberry Pi

(T. B. D.)

### First time preparation

#### Init

It is recommended that everything be done in a virtual environment.

```shell
python3 -m venv venv
source venv/bin/activate
```

To install some development commands, run below.

```shell
make init
```

#### Reveal Secrets

To install [git-secret](https://git-secret.io/) via [Homebrew](https://brew.sh) manually, `brew install git-secret`.
To install [direnv](https://direnv.net) via [Homebrew](https://brew.sh) manually, `brew install direnv`.

Developers who share a GPG key with their team can decrypt confidential information.

To reveal the secret information (= `*.secrets`), run below.

```shell
make reveal
```

If there are `.env` -like files included in `*.secrets`, [direnv](https://direnv.net) try to load them automatically.
`direnv allow` to approve it.

On the other hand, to encrypt the updated secret information, run below.

```shell
make hide
```

#### Setup Git Hooks (Lefthook)

To install [Lefthook](https://github.com/evilmartians/lefthook) via [Homebrew](https://brew.sh), `brew install lefthook`.

```shell
lefthook install
```

Thereafter, each commit will validate by `make format` and `make lint`, and each push will validate by `make test` and [secretlint](https://github.com/secretlint/secretlint).

### Develop

Commands that are often used during development should be prepared in `default`.

```shell
make
```

#### `.env`

Make sure there is `.env` like below before starting development.

```.env
DEBUG=True
```

Usually, `.env` is prepared by [Reveal Secrets](#reveal-secrets) action.
Don't forget that it needs to run `direnv allow` every time the `.env` is changed.

#### Start

(T. B. D.)

#### Format

To format Python source codes using [Black](https://github.com/psf/black) manually, run below.

```shell
make format
```

#### Lint

To lint Python source codes using [flake8](https://pypi.org/project/flake8/) manually, run below.

```shell
make lint
```

#### Test

To test Python source codes using [pytest](https://docs.pytest.org/) manually, run below.

```shell
make test
```

### Document

#### API Document

When the main branch is updated, `pages.yml` will update the [API Document](https://shin-sforzando.github.io/2ch-RS232C-HAT/).

To generate API Documents using [Sphinx](https://www.sphinx-doc.org/) manually, run below.

```shell
make doc
```

#### CHANGELOG

To install [git-cliff](https://github.com/orhun/git-cliff) via [Homebrew](https://brew.sh) manually, `brew install git-cliff`.

To update `CHANGELOG.md` manually, run [git-cliff](https://github.com/orhun/git-cliff) like below.

```shell
git cliff --output CHANGELOG.md
```

### Clean

To clean up miscellaneous files, run below.

```shell
make clean
```

## Misc

## Notes

This repository is [Commitizen](https://commitizen.github.io/cz-cli/) friendly, following [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow).
See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

### LICENSE

See [LICENSE](LICENSE).

### Contributors

- [sforzando LLC. and Inc.](https://sforzando.co.jp/)
  - [Shin'ichiro Suzuki](https://github.com/shin-sforzando)
