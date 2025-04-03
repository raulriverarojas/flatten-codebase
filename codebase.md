### DIRECTORY . FOLDER STRUCTURE ###
./
    .DS_Store
    flatten.py
    README.md
    .gitignore
    codebase.md
    .git/
        config
        HEAD
        description
        index
        packed-refs
        objects/
            pack/
                pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.idx
                pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.pack
            info/
        info/
            exclude
        logs/
            HEAD
            refs/
                heads/
                    main
                remotes/
                    origin/
                        HEAD
        hooks/
            commit-msg.sample
            pre-rebase.sample
            pre-commit.sample
            applypatch-msg.sample
            fsmonitor-watchman.sample
            pre-receive.sample
            prepare-commit-msg.sample
            post-update.sample
            pre-merge-commit.sample
            pre-applypatch.sample
            pre-push.sample
            update.sample
            push-to-checkout.sample
        refs/
            heads/
                main
            tags/
            remotes/
                origin/
                    HEAD
### DIRECTORY . FOLDER STRUCTURE ###

### DIRECTORY . FLATTENED CONTENT ###
### ./.DS_Store BEGIN ###
[Error reading file: 'utf-8' codec can't decode byte 0xaf in position 563: invalid start byte]
### ./.DS_Store END ###

### ./flatten.py BEGIN ###
import os
import argparse

def printFolderStructure(directory, output_file, skip_folders=None):
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        # Skip directories in the skip_folders list
        if skip_folders:
            directories[:] = [d for d in directories if d not in skip_folders]
            
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder, skip_folders=None):
    for dirpath, dirnames, filenames in os.walk(folder):
        # Skip directories in the skip_folders list
        if skip_folders:
            # This modifies dirnames in-place to prevent os.walk from recursing into skipped directories
            dirnames[:] = [d for d in dirnames if d not in skip_folders]
            
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', help='Base folders to process')
    parser.add_argument('--skip_folders', nargs='*', default=[], help='Folders to skip during processing')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')
    parser.add_argument('--output', default='codebase.md', help='Output file name (default: codebase.md)')

    system_instructions = """## System Instructions for Language Model Assistance in Code Debugging
    ### Role Definition:
    - **Act as a software engineer** tasked with assisting in debugging code.
    - Provide insights, explanations, and solutions based on the provided codebase information.

    ### Codebase Markdown File Structure:
    - The codebase markdown file represents the actual codebase structure and content.
    - It begins with a directory tree representation:
      ```
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      (file tree representation)
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      ```
    - Following the directory tree, the contents of each file are displayed:
      ```
      ### path/to/file1 BEGIN ###
      (content of file1)
      ### path/to/file1 END ###
      
      ### path/to/file2 BEGIN ###
      (content of file2)
      ### path/to/file2 END ###
      ```

    ### Guidelines for Interaction:
    - Respond to queries based on the explicit content provided within the markdown file.
    - Avoid making assumptions about the code without clear evidence presented in the file content.
    - When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
      ```
      ### folder1/folder2/myfile.ts BEGIN ###
      (specific implementation details)
      ### folder1/folder2/myfile.ts END ###
      ```

    ### Objective:
    - The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file."""
    args = parser.parse_args()
    if args.system_instructions:
      print(system_instructions)
      if not args.folders:
          return
  
    if args.folders:
      base_folders = args.folders
      skip_folders = args.skip_folders
      
      with open(args.output, 'w') as output_file:
          for base_folder in base_folders:
              printFolderStructure(base_folder, output_file, skip_folders)
              
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
              for filepath in walkFolderTree(base_folder, skip_folders):
                  content = f"### {filepath} BEGIN ###\n"
                  
                  try:
                      with open(filepath, "r") as f:
                          content += f.read()
                      content += f"\n### {filepath} END ###\n\n"
                  except Exception as e:
                      # Better error handling
                      content += f"[Error reading file: {str(e)}]\n"
                      content += f"### {filepath} END ###\n\n"
                  
                  output_file.write(content)
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
    else:
      print("usage: main.py [-h] --folders FOLDERS [FOLDERS ...] [--skip_folders SKIP_FOLDERS [SKIP_FOLDERS ...]] [--system_instructions] [--output OUTPUT]")
      print("Error: the following arguments are required: --folders")

if __name__ == "__main__":
  main()

### ./flatten.py END ###

### ./README.md BEGIN ###
# Flatten Codebase

## Overview

**Flatten Codebase** is a utility tool designed to simplify the process of preparing a codebase for analysis or processing by Language Models (LMs). It achieves this by flattening the entire codebase into a single Markdown (.md) file, making it easier for the developer to provide the codebase to the LM for various tasks such as code analysis, generation, or other natural language processing (NLP) activities.

## Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Suggested system instructions](#suggested-system-instructions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)

## Purpose

The primary goal of this tool is to streamline the workflow involved in providing a codebase to a LM for various tasks such as code analysis, generation, or other natural language processing (NLP) activities. By converting the codebase into a flat structure within a Markdown document, it allows developers to easily provide the codebase to the LM without the need for complex file handling or processing.

## Suggested system instructions
The file `system_instructions.txt` located on the project repository contains a suggestion of system instructions to be provided to the language model when using the codebase.md file generated by this tool. The argument `--system_instructions` can also be used to display these instructions in the terminal. Feel free to modify them to better fit your needs.

## Features

- **Directory Structure Representation**: Generates a structured representation of each specified folder's contents, including all nested directories and files.
- **File Content Extraction**: Extracts and includes the content of each file within the specified folders, facilitating direct analysis or processing by LMs.
- **Output in Markdown Format**: Outputs the flattened codebase in a Markdown file, ensuring compatibility with a wide range of tools and platforms that support Markdown.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This tool requires Python 3.x.

### Installation

Use the `flatten.py` script directly:
```bash
python3 flatten.py
```
You can put it in your PATH to use it as a global command.

### Usage

Run the script with the `--folders` argument followed by the paths to the base folders you wish to process. For example:
```bash
python3 flatten.py --folders /path/to/folder1 /path/to/folder2
```

This will create a `codebase.md` file in the current directory containing the flattened structure and the content of the specified folders.

## Contributing

Contributions to improve the tool's functionality, performance, or documentation are welcome. Please feel free to submit pull requests or issues through the GitHub repository.
### ./README.md END ###

### ./.gitignore BEGIN ###
build
flatten_codebase.egg-info
dist
### ./.gitignore END ###

### ./codebase.md BEGIN ###
### DIRECTORY . FOLDER STRUCTURE ###
./
    .DS_Store
    flatten.py
    README.md
    .gitignore
    codebase.md
    .git/
        config
        HEAD
        description
        index
        packed-refs
        objects/
            pack/
                pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.idx
                pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.pack
            info/
        info/
            exclude
        logs/
            HEAD
            refs/
                heads/
                    main
                remotes/
                    origin/
                        HEAD
        hooks/
            commit-msg.sample
            pre-rebase.sample
            pre-commit.sample
            applypatch-msg.sample
            fsmonitor-watchman.sample
            pre-receive.sample
            prepare-commit-msg.sample
            post-update.sample
            pre-merge-commit.sample
            pre-applypatch.sample
            pre-push.sample
            update.sample
            push-to-checkout.sample
        refs/
            heads/
                main
            tags/
            remotes/
                origin/
                    HEAD
### DIRECTORY . FOLDER STRUCTURE ###

### DIRECTORY . FLATTENED CONTENT ###
### ./.DS_Store BEGIN ###
[Error reading file: 'utf-8' codec can't decode byte 0xaf in position 563: invalid start byte]
### ./.DS_Store END ###

### ./flatten.py BEGIN ###
import os
import argparse

def printFolderStructure(directory, output_file, skip_folders=None):
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        # Skip directories in the skip_folders list
        if skip_folders:
            directories[:] = [d for d in directories if d not in skip_folders]
            
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder, skip_folders=None):
    for dirpath, dirnames, filenames in os.walk(folder):
        # Skip directories in the skip_folders list
        if skip_folders:
            # This modifies dirnames in-place to prevent os.walk from recursing into skipped directories
            dirnames[:] = [d for d in dirnames if d not in skip_folders]
            
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', help='Base folders to process')
    parser.add_argument('--skip_folders', nargs='*', default=[], help='Folders to skip during processing')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')
    parser.add_argument('--output', default='codebase.md', help='Output file name (default: codebase.md)')

    system_instructions = """## System Instructions for Language Model Assistance in Code Debugging
    ### Role Definition:
    - **Act as a software engineer** tasked with assisting in debugging code.
    - Provide insights, explanations, and solutions based on the provided codebase information.

    ### Codebase Markdown File Structure:
    - The codebase markdown file represents the actual codebase structure and content.
    - It begins with a directory tree representation:
      ```
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      (file tree representation)
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      ```
    - Following the directory tree, the contents of each file are displayed:
      ```
      ### path/to/file1 BEGIN ###
      (content of file1)
      ### path/to/file1 END ###
      
      ### path/to/file2 BEGIN ###
      (content of file2)
      ### path/to/file2 END ###
      ```

    ### Guidelines for Interaction:
    - Respond to queries based on the explicit content provided within the markdown file.
    - Avoid making assumptions about the code without clear evidence presented in the file content.
    - When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
      ```
      ### folder1/folder2/myfile.ts BEGIN ###
      (specific implementation details)
      ### folder1/folder2/myfile.ts END ###
      ```

    ### Objective:
    - The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file."""
    args = parser.parse_args()
    if args.system_instructions:
      print(system_instructions)
      if not args.folders:
          return
  
    if args.folders:
      base_folders = args.folders
      skip_folders = args.skip_folders
      
      with open(args.output, 'w') as output_file:
          for base_folder in base_folders:
              printFolderStructure(base_folder, output_file, skip_folders)
              
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
              for filepath in walkFolderTree(base_folder, skip_folders):
                  content = f"### {filepath} BEGIN ###\n"
                  
                  try:
                      with open(filepath, "r") as f:
                          content += f.read()
                      content += f"\n### {filepath} END ###\n\n"
                  except Exception as e:
                      # Better error handling
                      content += f"[Error reading file: {str(e)}]\n"
                      content += f"### {filepath} END ###\n\n"
                  
                  output_file.write(content)
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
    else:
      print("usage: main.py [-h] --folders FOLDERS [FOLDERS ...] [--skip_folders SKIP_FOLDERS [SKIP_FOLDERS ...]] [--system_instructions] [--output OUTPUT]")
      print("Error: the following arguments are required: --folders")

if __name__ == "__main__":
  main()

### ./flatten.py END ###

### ./README.md BEGIN ###
# Flatten Codebase

## Overview

**Flatten Codebase** is a utility tool designed to simplify the process of preparing a codebase for analysis or processing by Language Models (LMs). It achieves this by flattening the entire codebase into a single Markdown (.md) file, making it easier for the developer to provide the codebase to the LM for various tasks such as code analysis, generation, or other natural language processing (NLP) activities.

## Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Suggested system instructions](#suggested-system-instructions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)

## Purpose

The primary goal of this tool is to streamline the workflow involved in providing a codebase to a LM for various tasks such as code analysis, generation, or other natural language processing (NLP) activities. By converting the codebase into a flat structure within a Markdown document, it allows developers to easily provide the codebase to the LM without the need for complex file handling or processing.

## Suggested system instructions
The file `system_instructions.txt` located on the project repository contains a suggestion of system instructions to be provided to the language model when using the codebase.md file generated by this tool. The argument `--system_instructions` can also be used to display these instructions in the terminal. Feel free to modify them to better fit your needs.

## Features

- **Directory Structure Representation**: Generates a structured representation of each specified folder's contents, including all nested directories and files.
- **File Content Extraction**: Extracts and includes the content of each file within the specified folders, facilitating direct analysis or processing by LMs.
- **Output in Markdown Format**: Outputs the flattened codebase in a Markdown file, ensuring compatibility with a wide range of tools and platforms that support Markdown.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This tool requires Python 3.x.

### Installation

Use the `flatten.py` script directly:
```bash
python3 flatten.py
```
You can put it in your PATH to use it as a global command.

### Usage

Run the script with the `--folders` argument followed by the paths to the base folders you wish to process. For example:
```bash
python3 flatten.py --folders /path/to/folder1 /path/to/folder2
```

This will create a `codebase.md` file in the current directory containing the flattened structure and the content of the specified folders.

## Contributing

Contributions to improve the tool's functionality, performance, or documentation are welcome. Please feel free to submit pull requests or issues through the GitHub repository.
### ./README.md END ###


### ./codebase.md END ###

### ./.git/config BEGIN ###
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:VictorHenrique317/flatten-codebase.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main

### ./.git/config END ###

### ./.git/HEAD BEGIN ###
ref: refs/heads/main

### ./.git/HEAD END ###

### ./.git/description BEGIN ###
Unnamed repository; edit this file 'description' to name the repository.

### ./.git/description END ###

### ./.git/index BEGIN ###
[Error reading file: 'utf-8' codec can't decode bytes in position 13-14: invalid continuation byte]
### ./.git/index END ###

### ./.git/packed-refs BEGIN ###
# pack-refs with: peeled fully-peeled sorted 
16478c0f6d16b1c41de13884bff90be67e09cb71 refs/remotes/origin/main

### ./.git/packed-refs END ###

### ./.git/objects/pack/pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.idx BEGIN ###
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
### ./.git/objects/pack/pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.idx END ###

### ./.git/objects/pack/pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.pack BEGIN ###
[Error reading file: 'utf-8' codec can't decode byte 0x98 in position 12: invalid start byte]
### ./.git/objects/pack/pack-87a73a559efa93dd7784c2e1fb97cdfae29bc72f.pack END ###

### ./.git/info/exclude BEGIN ###
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

### ./.git/info/exclude END ###

### ./.git/logs/HEAD BEGIN ###
0000000000000000000000000000000000000000 16478c0f6d16b1c41de13884bff90be67e09cb71 Raul <r.v@posteo.net> 1743688564 -0400	clone: from github.com:VictorHenrique317/flatten-codebase.git

### ./.git/logs/HEAD END ###

### ./.git/logs/refs/heads/main BEGIN ###
0000000000000000000000000000000000000000 16478c0f6d16b1c41de13884bff90be67e09cb71 Raul <r.v@posteo.net> 1743688564 -0400	clone: from github.com:VictorHenrique317/flatten-codebase.git

### ./.git/logs/refs/heads/main END ###

### ./.git/logs/refs/remotes/origin/HEAD BEGIN ###
0000000000000000000000000000000000000000 16478c0f6d16b1c41de13884bff90be67e09cb71 Raul <r.v@posteo.net> 1743688564 -0400	clone: from github.com:VictorHenrique317/flatten-codebase.git

### ./.git/logs/refs/remotes/origin/HEAD END ###

### ./.git/hooks/commit-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}

### ./.git/hooks/commit-msg.sample END ###

### ./.git/hooks/pre-rebase.sample BEGIN ###
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

### ./.git/hooks/pre-rebase.sample END ###

### ./.git/hooks/pre-commit.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

### ./.git/hooks/pre-commit.sample END ###

### ./.git/hooks/applypatch-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

### ./.git/hooks/applypatch-msg.sample END ###

### ./.git/hooks/fsmonitor-watchman.sample BEGIN ###
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

### ./.git/hooks/fsmonitor-watchman.sample END ###

### ./.git/hooks/pre-receive.sample BEGIN ###
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

### ./.git/hooks/pre-receive.sample END ###

### ./.git/hooks/prepare-commit-msg.sample BEGIN ###
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

### ./.git/hooks/prepare-commit-msg.sample END ###

### ./.git/hooks/post-update.sample BEGIN ###
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

### ./.git/hooks/post-update.sample END ###

### ./.git/hooks/pre-merge-commit.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

### ./.git/hooks/pre-merge-commit.sample END ###

### ./.git/hooks/pre-applypatch.sample BEGIN ###
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

### ./.git/hooks/pre-applypatch.sample END ###

### ./.git/hooks/pre-push.sample BEGIN ###
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

### ./.git/hooks/pre-push.sample END ###

### ./.git/hooks/update.sample BEGIN ###
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

### ./.git/hooks/update.sample END ###

### ./.git/hooks/push-to-checkout.sample BEGIN ###
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

### ./.git/hooks/push-to-checkout.sample END ###

### ./.git/refs/heads/main BEGIN ###
16478c0f6d16b1c41de13884bff90be67e09cb71

### ./.git/refs/heads/main END ###

### ./.git/refs/remotes/origin/HEAD BEGIN ###
ref: refs/remotes/origin/main

### ./.git/refs/remotes/origin/HEAD END ###

### DIRECTORY . FLATTENED CONTENT ###
