# How to merge two repos

Just imagine we have two git repos and one of them haven’t update a lot of time. We want to merge it.
How we should to do it the situation.
Don’t forget exists lasted changes in repo

```bash
$ git fetch -ap 
$ git pull
```

First of all we need add remote source

```bash
$ git remote add gerrit ssh://gerrit.com:29418/XXX/XXX
```

Check it. Should be two remotes origin and second remote url gerrit

```bash
$ git remote -v

# Output
gerrit	ssh://gerrit.com:29418/XXX/XXX (fetch)
gerrit	ssh://gerrit.com:29418/XXX/XXX (push)
origin	https://github.com/YYYY/YYYY (fetch)
origin	https://github.com/YYYY/YYYY (push)
```

Call master branch from other remote with prefix. That action to do more easy to filter in git log and merge branch in future

```bash
$ git checkout -b gerrit gerrit/master
```

Now need choice branch with missing changes

```bash
$ git checkout gerrit
```

Merge changes from origin repo which contain lasted changes

```bash
$ git merge origin/master
```

Add new commit

```bash
$ git commit -a -m "Sync"
```

I recommend to use squash, if we wouldn’t like add each commit separately

```bash
$ git rebase -i gerrit/master
```

Finally push to gerrit repo

```bash
$ git push gerrit HEAD:refs/for/master
```

It is all.
