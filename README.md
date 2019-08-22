# vsco-dl
> Download all of the images and videos from a VSCO user

<p align="center">
<a href="https://asciinema.org/a/196264">
<img src="https://asciinema.org/a/196264.png" width="595px" height="auto">
</a>
</p>

## :floppy_disk: Installation

```bash
# clone the repo
$ git clone https://github.com/boomaa23/vsco-dl.git

# install the requirements
$ pip install requests
```

## :hammer: Usage
```
usage: vsco-dl.py [-h] [--content CONTENT] username pages

Download all of the images and videos from a VSCO user

positional arguments:
  username           Username of VSCO user
  pages              Number of pages the user has

optional arguments:
  -h, --help         show this help message and exit
  --content CONTENT  Option to download only videos (video) or photos (photo)

```

## :scroll: License
MIT License

Modifications (C) 2019 Boomaa23
Copyright (c) 2018 Siddharth Dushantha
