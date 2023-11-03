# Webpage

[![Project Status](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)

My personal web page

## About

This repository hosts my personal webpage with some case studies, notebooks,
and things that keep my mind busy.

## Dependencies

Download [Minicoda](https://docs.conda.io/en/latest/miniconda.html) first and install everything like this

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

conda create -n web python=3.9
echo "source ~/miniconda3/bin/activate web" >> ~/.bashrc

source ~/miniconda3/bin/activate web
conda install -y nodejs
```

## Installation

Running the following on the command line install all dependencies, builds
the distributable and starts an express server that listens to port 4000

```bash
npm install
npm run build
npm run preview
```

## Development

For development, run this:

```bash
npm install
npm run dev
```

## Author

Simon Dirmeier <a href="mailto:sfyrbnd @ pm me">sfyrbnd @ pm me</a>
