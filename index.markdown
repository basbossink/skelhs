---
layout: default
title: Skelhs
---

#  Skelhs

## Introduction

Skelhs is a simple code generator utilising [PasteScript][1] to generate the boilerplate contents of a Haskell module and the assoctiated test module. 

## Installation requirements

- [Python 2.6][2]
- [PasteScript][1] installation should be as simple as:

        $ easy_install PasteScript

- [Cheetah][3] is a dependency of PasteScript so it should have been
  installed automagically in the previous step. It's listed here for
completeness only.

[1]: http://pythonpaste.org/script/
[2]: http://www.python.org
[3]: http://www.cheetahtemplate.org/

## Installation
1. get the sources and install using:

        $ git clone git://github.com/basbossink/skelhs.git
        $ cd skelhs.basicmodule
        $ python setup.py install

1. Verify your install with:

        $ paster create --list-templates

   The list of available templates should contain the following line:

        skelhs_basic_module:  A haskell module with a test environment

## Usage

    $ paster create -t skelhs_basic_module <target_dir_name> 

Note that the `target_dir_name` directory will be created if it does not exist.
