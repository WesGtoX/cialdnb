<h1 align="center">
  CIALdnb
  <br />
</h1>

<p align="center">
  <a href="#about-the-project">About</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#overview">Overview</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#technology">Technology</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#roadmap">Roadmap</a>&nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/wesgtox/cialdnb?style=plastic" />
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/wesgtox/cialdnb?style=plastic" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/wesgtox/cialdnb?style=plastic" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/wesgtox/cialdnb?style=plastic" />
  <img alt="License" src="https://img.shields.io/github/license/wesgtox/cialdnb?style=plastic" />
</p>


## About the Project

CIALdnb is a command line application, which through a list of URL's, extracts the `logo` data, all the `phone` numbers on the page, and the link of the visited `website`.


## Overview
- [CHANGELOG](CHANGELOG.md)


## Technology 

This project was developed with the following technologies:

- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)
- [Docker](https://www.docker.com/)


## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started/)
- [Python](https://www.python.org/downloads/) _`(Only if you are going to run via Python)`_

1. Clone the repository:
```bash
git clone https://github.com/WesGtoX/cialdnb.git
cd cialdnb
```

### Install and Run via Docker

2. Build the docker image:
```bash
docker build . -t run_cialdnb
```
3. Run:
```bash
cat websites.txt | docker run -i run_cialdnb
```
4. Can also be run via Makefile:
```bash
make build
make run
```

### Install and run via Python

2. Install the dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run:
```bash
cat websites.txt | python -m run_cialdnb
```


## Roadmap

See the [open issues](https://github.com/WesGtoX/cialdnb/issues) for a list of proposed features (and known issues).


## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Made with ♥ by [Wesley Mendes](https://wesleymendes.com/) :wave:
