---
layout: post
authors: ["Mark Woodbridge"]
title: "My Favorite Tool - Docker"
date: 2018-02-15
time: "00:00:00"
tags: [ "Research tools", "Virtualization", "Containers", "Software Testing", "Software Carpentry"]
---

<h2>This post originally appeared on the [Software Carpentry website](https://software-carpentry.org/)</h2>

### What kind of tool is it?
[Docker](https://www.docker.com/) is a virtualization tool.

### Why I like it

I use [Docker](https://www.docker.com/) every day - it's the one piece of software that has changed the way I work in recent years. There are many other approaches to virtualisation but its versatility and ubiquity is compelling. I use it for many purposes - for rapidly obtaining and executing other open source software, for providing a predictable environment in which to test code that I've written, and for building and deploying my own and third-party applications. We use it in the RSE team at [Imperial College](https://www.imperial.ac.uk/) to ensure that others can rapidly install and evaluate our work.


#### How does the tool help you in your work?

It makes the implicit explicit. Software provided with a Dockerfile is self-describing in the sense that you know the environment in which it expects to be run, i.e. the operating system and dependencies. Alongside versioned code and data this provides reproducibility - which is vital for research software. The ephemeral nature of containers also encourages immutability, simplifying deployment and maintenance. For further information, I recommend the article "An introduction to Docker for reproducible research" [https://doi.org/10.1145/2723872.2723882](https://doi.org/10.1145/2723872.2723882).

#### What do you wish someone had told you when you first started learning how to use this tool?

Containers, as provided by Docker (or Singularity), shouldn't be confused with virtual machines. Both can help with portability but containers should have a single purpose and package a discrete tool or application. This ensures that they can be independently versioned and re-used.

-- *Mark Woodbridge, Research Software Engineering Team Lead, Imperial College, London*

---

Have you got a favourite tool you would like to tell us about?
Please use this [form](https://docs.google.com/forms/d/e/1FAIpQLSeiu5NzJsLxYueaQrNn_qKbaa5JR2Sz12CeCRyedKQxwb54Dw/viewform)
to add a bit of detail and we will do the rest. You can read the [background to these posts](https://software-carpentry.org/blog/2017/10/fave-tools.html) here.
