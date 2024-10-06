# mdtWrangler
An http-fileserver implementation to get around Microsoft's silly implementations of filesharing, particularly with respect to serving the results of MDT to a netboot.xyz server from a Windows 10 (Pro) host

---

## Why:
After being annoyed and frustrated with the inability to easily serve files via http on Windows, and having tried just about every possible option via docker, I came to the conclusion that I would just write my own http fileserver in python
### Background:
We have an MDT server that is on a Windows 10 Pro virtual machine, and I was having a bear of a time getting it to serve the files to netboot.xyz as netboot doesn't **really** support SMB or NFS. So I just said screw it and wrote my own 

---

## Instructions:

Put the files of this repo into the parent directory of whichever directory has the "Boot" files the MDT creates. Technically you can put it anywhere but this is just where I put it because I felt like it.

You need python to run python files, and the easiest way to install it is by opening up `CMD` and running `python`.
- If python is installed, it'll drop you into the python shell. If not, it will open up the Microsoft store and prompt you to download a python version. I went with Python 3.12

Once you have python installed, the only other dependency is `fasthtml`. You can install this with `pip install fasthtml`.

The next Step is to run in `CMD` `python serve.py`

Copy `.env.example` to `.env` and make sure to correct the variables to correct paths on your filesystem

Point the `windows.ipxe` file at the correct paths as well, and then you should be able to select windows from your boot server.
