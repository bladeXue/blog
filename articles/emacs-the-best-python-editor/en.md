# Emacs: The Best Python Editor?

You can download all the files referenced in this tutorial at the link below:

> Download Code: [Click here to download the code](https://github.com/realpython/materials/tree/master/emacs-the-best-python-editor) you’ll use to learn about Emacs for Python in this tutorial.

## Installation and Basics

Before you can explore Emacs and all it has to offer a Python developer, you need to install it and learn some of the basics.

### Installation

When you install Emacs, you have to consider your platform. This [guide](http://ergoemacs.org/emacs/which_emacs.html), provided by [ErgoEmacs](http://ergoemacs.org/), provides everything you need to get up and running with a basic Emacs installation on Linux, Mac, or Windows.

Once the installation has finished, you can start Emacs:

![emacsv2-fresh-launch](./images/emacsv2-fresh-launch.png "emacsv2-fresh-launch")

You should be greeted with the default startup screen.

### Basic Emacs

First, let’s go through a quick example to cover some basic Emacs for Python development. You’ll see how to edit a program using vanilla Emacs, and how much Python support is built into the program. With Emacs open, use the following steps to create a quick Python program:

1. Hit `Ctrl`+`X` `Ctrl`+`F` to open a new file.
2. Type `sieve.py` to name the file.
2. Hit `Enter`.
4. Emacs may ask you to confirm your choice. If so, then hit `Enter` again.

Now type the following code:

```python
MAX_PRIME = 100

sieve = [True] * MAX_PRIME
for i in range(2, MAX_PRIME):
  if sieve[i]:
    print(i)
      for j in range(i * i, MAX_PRIME, i):
        sieve[j] = False
```

You may recognize this code as the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), which finds all primes below a given maximum. As you type the code, you’ll notice:

- Emacs highlights variables and constants differently from Python keywords.
- Emacs indents lines following [for](https://realpython.com/courses/python-for-loop/) and [if](https://realpython.com/courses/python-conditional-statements/) statements automatically.
- Emacs changes the indentation to appropriate locations when you hit `Tab` on an indented line.
- Emacs highlights the opening bracket or parenthesis whenever you type a closing bracket or parenthesis.
- Emacs responds as expected to the arrow keys, as well as the `Enter`, `Backspace`, `Del`, `Home`, `End`, and `Tab` keys.

There are some odd key mappings in Emacs, however. If you try to paste code into Emacs, for instance, then you may find the standard `Ctrl`+`V` keystroke doesn’t work.

The easiest way to learn which keys do what in Emacs is to follow the built-in tutorial. You can access it by positioning the cursor over the words Emacs Tutorial on the Emacs start screen and pressing `Enter`, or by typing `Ctrl`+`H` `T` at any time thereafter. You’ll be greeted with the following passage:

```text
Emacs commands generally involve the CONTROL key (sometimes labeled
CTRL or CTL) or the META key (sometimes labeled EDIT or ALT).  Rather than
write that in full each time, we'll use the following abbreviations:

 C-<chr>  means hold the CONTROL key while typing the character <chr>
          Thus, C-f would be: hold the CONTROL key and type f.
 M-<chr>  means hold the META or EDIT or ALT key down while typing <chr>.
          If there is no META, EDIT or ALT key, instead press and release the
          ESC key and then type <chr>.  We write <ESC> for the ESC key.

Important Note: to end the Emacs session, type C-x C-c.  (Two characters.)
To quit a partially entered command, type C-g.
```

When you scan the text from the passage, you’ll see that Emacs keystrokes are shown in the Emacs documentation using the notation C-x C-s. This is the command to save the contents of the current buffer. This notation indicates that the `Ctrl` and `X` keys are pressed at the same time, followed by the `Ctrl` and `S` keys.

> Note: In this tutorial, Emacs keystrokes are shown as `Ctrl`+`X` `Ctrl`+`S`.

Emacs uses some terminology that can be traced back to its text-based UNIX roots. Since these terms have different meanings now, it’s a good idea to review them, as you’ll be reading about them as the tutorial progresses:

- The window you see when you start Emacs is referred to as a [frame](https://www.gnu.org/software/emacs/manual/html_node/elisp/Frames.html#Frames). You can open as many Emacs frames as you wish, on as many monitors as you wish, and Emacs will track them all.
- The panes within each Emacs frame are referred to as [windows](https://www.gnu.org/software/emacs/manual/html_node/elisp/Windows.html#Windows). Emacs frames initially contain a single window, but you can open multiple windows in each frame, either manually or by running special commands.
- Within each window, the contents displayed are called a [buffer](http://www.gnu.org/software/emacs/manual/html_node/elisp/Buffers.html). Buffers can contain the contents of files, the output of commands, the lists of menu options, or other items. Buffers are where you interact with Emacs.
- When Emacs needs your input, it asks in a special one-line area at the bottom of the currently active frame called the [mini-buffer](https://www.gnu.org/software/emacs/manual/html_node/elisp/Minibuffers.html#Minibuffers). If you ever find yourself there unexpectedly, then you can cancel whatever got you there with `Ctrl`+`G`.

Now that you’ve covered the basics, it’s time to start customizing and configuring Emacs for Python development!

### Initialization File

One of the great benefits of Emacs is its powerful configuration options. The core of Emacs configuration is the [initialization file](http://www.gnu.org/software/emacs/manual/html_node/emacs/Init-File.html), which is processed every time Emacs is started.

This file contains commands written in [Emacs Lisp](https://www.gnu.org/software/emacs/manual/html_node/eintr/index.html), which is executed every time Emacs is started. Don’t worry, though! You don’t need to know Lisp to use or customize Emacs. In this tutorial, you’ll find everything you need to get started. (After all, this is Real Python, not Real Lisp!)

On start-up, Emacs looks for the initialization file in [three places](https://www.gnu.org/software/emacs/manual/html_node/emacs/Find-Init.html#Find-Init):

1. First, it looks in your home user folder for the file `.emacs`.
2. If it’s not there, then Emacs looks in your home user folder for the file `emacs.el`.
3. Finally, if neither is found, then it looks in your home folder for `.emacs.d/init.el`.

The last option, `.emacs.d/init.el`, is the current recommended initialization file. However, if you’ve previously used and configured Emacs, then you may already have one of the other initialization files present. If so, then continue to use that file as you read this tutorial.

When you first install Emacs, there is no `.emacs.d/init.el`, but you can create this file fairly quickly. With the Emacs window open, follow these steps:

1. Hit `Ctrl`+`X` `Ctrl`+`F`.
2. Type `~/.emacs.d/init.el` in the mini-buffer.
3. Hit `Enter`.
4. Emacs may ask you to confirm your choice. If so, then hit `Enter` again.

Let’s take a closer look at what’s happening here:

- You tell Emacs that you want to find and open a file with the keystrokes `Ctrl`+`X` `Ctrl`+`F`.
- You tell Emacs what file to open by giving it a path to the file. The path `~/.emacs.d/init.el` has three parts:
  1. The leading tilde `~` is a shortcut to your home folder. On Linux and Mac machines, this is usually `/home/<username>`. On Windows machines, it’s the path specified in the [HOME environment variable](http://www.gnu.org/software/emacs/manual/html_node/efaq-w32/Location-of-init-file.html#Location-of-init-file).
  2. The folder `.emacs.d` is where Emacs stores all its configuration information. You can use this folder to quickly set up Emacs on a new machine. To do so, copy the contents of this folder to your new machine, and Emacs is good to go!
  3. The file `init.el` is your initialization file.
- You tell Emacs, "Yes, I do want to create this new file." (This step is required since the file doesn’t exist. Normally, Emacs will simply open the file specified.)

After Emacs creates the new file, it opens that file in a new buffer for you to edit. This action doesn’t actually create the file yet, though. You must save the blank file using `Ctrl`+`X` `Ctrl`+`S` to create it on disk.

Throughout this tutorial, you’ll see initialization code snippets that enable different features. Create the initialization file now if you want to follow along! You can also find the complete initialization file at the link below:

> Download Code: [Click here to download the code](https://github.com/realpython/materials/tree/master/emacs-the-best-python-editor) you’ll use to learn about Emacs for Python in this tutorial.

### Customization Packages






















## Emacs for Python Development With elpy










## Additional Python Language Features










### Syntax Checking










### Code Formatting










### Integration With Jupyter and IPython










## Testing Support










## Debugging Support










## Git Support










## Additional Emacs Modes










## Alternatives










## Conclusion
























































































































