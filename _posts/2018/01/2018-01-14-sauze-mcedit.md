---
layout: post
authors: ["Colin Sauze"]
title: "My Favorite Tool - Midnight Commander"
date: 2018-01-14
time: "00:00:00"
tags: [ "Research tools", "Text", "Text editors"]
---

### What kind of tool is it?

A text editor and file manager.

### Why I like it

My favourite tool is [Midnight Commander](https://midnight-commander.org/) and its text editor 
(which also works as a standalone tool) Mcedit. These two utilities are powerful yet easy to use. 
They both run on the command line in Unix operating systems, but instead of typing commands, 
they work mostly by using menus and selecting things with arrow keys or a mouse. This makes them a 
kind of halfway house between a traditional command line and a GUI utility and in my opinion they 
bring together the best of both worlds.

**Mcedit**

I've always hated the *Vi vs Emacs* holy war that many Unix users like to wage and I find that both editors have serious 
shortcomings and definitely aren't something I'd recommend a beginner use. Pico and Nano are certainly easier to use, 
but they always a feel a bit lacking in features and clunky to me. Mcedit runs from the command line but has a colourful 
GUI-like interface, you can use the mouse if you want, but I generally don't. If you're old enough to have used DOS, 
then it's very reminiscent of the "edit" text editor that was built into MS-DOS 5 and 6, except it's full of powerful 
features that still make it a good choice in 2018. It has a nice intuitive interface based around the `F` keys on the 
keyboard and a pull-down menu which can be accessed by pressing `F9`.

It's really easy to use and you're told about all the most important key combinations on screen and the rest can 
all be discovered from the menus. I find this far nicer than Vi or Emacs where I have to constantly look up key 
combinations or press a key by mistake and then have the dreaded *"what did I just press and what did it do?"* thought. 
Underneath it's got lots of powerful features like syntax highlighting, bracket matching, regular expression search and replace, 
and spell checking. I use Mcedit for most of my day-to-day text editing, although I do switch to heavier weight GUI-based 
editors when I need to edit lots of files at once. I just wish more people knew about it and then it might be installed by 
default on more of the shared systems and HPCs that I have to use!

**Midnight Commander (MC)**

The Midnight Commander or MC file manager is usually bundled with Mcedit and it makes navigating through filesystems very easy. 
It's based on an old DOS utility called Norton Commander. Like Mcedit, it runs on the command line but presents a GUI-like interface. 
You get shown two panes with two directory listings, one on the left and one of the right side of the screen, 
you can set these to be any directory on your system. Anyone who uses the Filezilla or WinSCP utilities to copy files 
will find this layout very familiar. Using a set of `F` keys, you can copy files, move/rename files, make directories or 
delete files very easily. But it also lets you type in any Unix command you like and have it executed in the directory 
you've selected. In addition to showing local files, it can also connect to a remote file server, FTP server or SFTP 
server and show you the files on there or open a .tar archive, zip file or compressed .tar file. Mcedit can be brought 
up to edit any file quickly by pressing the `F4` key or a simpler file viewer can be launched by pressing `F3`. 
External file viewers such as image viewers can be spawned just by pressing `Enter` when a file is selected. 

I find Midnight Commander makes looking around directories on my system much quicker and easier, it's great 
for trying to clean up a disk when you're running out of space and it's often just quicker and easier than using 
the Unix command line. One particular use case I find it shines at is copying a subset of files from one directory to 
another. This is because it lets you select a few files by a given pattern and then select a few more with another 
pattern and add them to the list of files to copy. I'll often make 5+ selections using this and then copy (or delete) 
all the files at once. The file copying screen is great too as it shows an accurate progress bar, time estimate and data 
rate, this is especially useful for copying large data files or copying stuff over a network.

#### How does the tool help you in your work?

It lets me work faster, it gives me features often only found in GUI tools on the command line and combines the 
best of working on a command line and in a GUI. This is especially useful when logging into remote systems with 
SSH where only a command line is readily available.

#### What do you wish someone had told you when you first started learning how to use this tool?

I'm not really sure there was anything, I found it really intuitive from the moment I started using it and 
figured out most of the features pretty quickly.

-- *Colin Sauze, Research Software Engineer, Aberystwyth, Wales, UK*

---

Have you got a favourite tool you would like to tell us about?
Please use this [form](https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform)
to add a bit of detail and we will do the rest. You can read the [background to these posts](https://software-carpentry.org/blog/2017/10/fave-tools.html) here.
