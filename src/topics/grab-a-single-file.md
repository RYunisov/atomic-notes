# Grap

## Description

If you heard about a monorepo.
You have to know there aren't the easy way to grab a single file from that.

As an experiment and process of learning Golang `grab` is small tool to resolve that.

Link: [Grab](https://github.com/RYunisov/grab)

Current version only for the linux distributives.

TODO:

* Implement TestCases
* Check on different environments as MacOS, Windows

## How to build

```bash
$ go build cmd/grab/*
```

## How to use

Use by default:

* Current username and `id_rsa`
* Branch `main`
* File `README.md` from root directory

To get a help information

```bash
$ ./grab --help

Usage of ./grab:
  -commit string
    	Example CommitId
  -file string
    	Example FilePath (default "README.md")
  -pk string
    	Example PrivateKey (default "/home/<username>/.ssh/id_rsa")
  -refs string
    	Example Refs (default "refs/heads/main")
  -repo string
    	Example RepoAddr (default "https://github.com/RYunisov/atomic-notes.git")
  -skip-auth
    	Skip Auth by Default (default true)
  -user string
    	Example Username (default "<username>")
```

To get a specific file from a specific commit from `master` branch

```bash
$ ./grab -repo=ssh://<any-repo.git> \
         -user=<username> \
         -refs=refs/heads/master \
         -file=<full-path-to-file> \
         -commit=<commit-hash> \
         -skip-auth=false

```
