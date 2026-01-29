# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at <https://github.com//dsci_524_group_30_data_validation/issues>.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

DSCI_524_Group_30_Data_Validation could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com//dsci_524_group_30_data_validation/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com//dsci_524_group_30_data_validation/issues>. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started

Ready to contribute? Here's how to set up DSCI_524_Group_30_Data_Validation for
local development.

1. Fork the <https://github.com//dsci_524_group_30_data_validation>
   repository on GitHub.
2. Clone your fork locally (*if you want to work locally*)

    ```shell
    git clone git@github.com:your_name_here/dsci_524_group_30_data_validation.git
    ```

3. [Install hatch](https://hatch.pypa.io/latest/install/).

4. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `feat` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b fix-name-of-your-bugfix
    ```

    Now you can make your changes locally.

5. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

6. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

7. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.
3. Your pull request will automatically be checked by the full test suite.
   It needs to pass all of them before it can be considered for merging.

### Development tools, GitHub infrastructure, and organizational practices

In this course, and throughout development of this project, we have utilized many new tools, and learned many new practices related to github infrastructure, collaboration, and package development. Below, we discuss some of the practices and tools we learned that we will bring forward into future projects, or if we choose to scale this project up.

Some of our favorites as a group were:

* deploying documentation using quartodoc on Github Pages - ended up being a simple, constantly updating, and aesthetic way to show our function documentation. Additionally, the fact that building locally was possible was a huge help when creating the quartodoc website, as we could preview changes without needing to push.
* GitHub actions workflow for continuous integration - allowed us to continually run the test suite and style checkers on pushes and pull requests to your project’s repository’s main branch (our deployment branch, in this case). Although this presented a cost up front in terms of workload, it later helped us to keep everything running smoothly.
* Iteratively programming using LLMs, as documented in issues related to Milestone 2 - when creating tests got repetitive, when it was difficult to find where there wasn't enough branch coverage, or when code just did not want to run, working with an LLM could be very helpful. We compared experiences with Claude compared to ChatGPT, and found that prompt engineering was absolutely make or break.

If we were to scale up, we'd utilize these new tools, as well as some older classics:

* Github Flow - absolutely essential for collaboration, reproducbility, and record-keeping.
* Unit tests - illuminated a lot of potential problems in our functions, and helped to refine and improve functions.
* Defensive programming - no explanation needed
* Linking issues to pull requests to milestones to releases - this ended up being super useful for record-keeping and general wayfinding around the project.
