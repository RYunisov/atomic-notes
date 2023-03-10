# How to use GitHub Actions and GitHub Pages

GitHub provide an oppotinuty to hosting static site from Markdown documentation  

* Create structure like as `.github/workflows` in your project
* Create file with content as described below

> Repository contain `book.yaml, src/SUMMARY.md and etc` because I use `mdbook` to serve static page.

```yaml
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: Checkout project
        uses: actions/checkout@v3
        with:
          path: docs

      # Runs a set of commands using the runners shell
      - name: Install MDBook
        run: cargo install mdbook mdbook-emojis

      - name: Build docs
        run: mdbook build docs

      - name: Upload artifact
        uses: actions/upload-artifact@master
        with:
          name: page
          path: docs/book
          if-no-files-found: error

  deploy:
    runs-on: ubuntu-latest
    needs: build

    permissions:
      pages: write      # to deploy to Pages
      id-token: write   # to verify the deployment originates from an appropriate source

    environment:
      name: github-pages
      url: ${{steps.deployment.outputs.page_url}}
    
    steps:
      - name: Download artifacts
        uses: actions/download-artifact@master
        with:
          name: page
          path: .

      - name: GitHub Pages configuration
        uses: actions/configure-pages@v1

      - name: GitHub Pages upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: .

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```
