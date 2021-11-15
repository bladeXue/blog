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

Now that you have an initialization file, you can add customization options to tailor Emacs for Python development. There are a few ways you can customize Emacs, but the one with the fewest steps is adding [Emacs packages](https://www.gnu.org/software/emacs/manual/html_node/emacs/Packages.html). These come from a variety of sources, but the primary package repository is [MELPA](https://melpa.org/#/), or the **Milkypostman’s Emacs Lisp Package Archive**.

Think of MELPA as [PyPI](https://pypi.org/) for Emacs packages. Everything you need and will use in this tutorial can be found there. To begin using it, expand the code block below and copy the configuration code to your `init.el` file:

```lisp
;; .emacs.d/init.el

;; ===================================
;; MELPA Package Support
;; ===================================
;; Enables basic packaging support
(require 'package)

;; Adds the Melpa archive to the list of available repositories
(add-to-list 'package-archives
             '("melpa" . "http://melpa.org/packages/") t)

;; Initializes the package infrastructure
(package-initialize)

;; If there are no archived package contents, refresh them
(when (not package-archive-contents)
  (package-refresh-contents))

;; Installs packages
;;
;; myPackages contains a list of package names
(defvar myPackages
  '(better-defaults                 ;; Set up some better Emacs defaults
    material-theme                  ;; Theme
    )
  )

;; Scans the list in myPackages
;; If the package listed is not already installed, install it
(mapc #'(lambda (package)
          (unless (package-installed-p package)
            (package-install package)))
      myPackages)

;; ===================================
;; Basic Customization
;; ===================================

(setq inhibit-startup-message t)    ;; Hide the startup message
(load-theme 'material t)            ;; Load material theme
(global-linum-mode t)               ;; Enable line numbers globally

;; User-Defined init.el ends here
```

As you read through the code, you’ll see that `init.el` is broken into sections. Each section is separated by comment blocks that begin with two semicolons (;;). The first section is titled `MELPA Package Support`:

```lisp
;; .emacs.d/init.el

;; ===================================
;; MELPA Package Support
;; ===================================
;; Enables basic packaging support
(require 'package)

;; Adds the Melpa archive to the list of available repositories
(add-to-list 'package-archives
             '("melpa" . "http://melpa.org/packages/") t)

;; Initializes the package infrastructure
(package-initialize)

;; If there are no archived package contents, refresh them
(when (not package-archive-contents)
  (package-refresh-contents))
```

This section begins by setting up the packaging infrastructure:

- **Line 7** tells Emacs to use packages.
- **Lines 10 and 11** add the MELPA archive to the list of package sources.
- **Line 14** initializes the packaging system.
- **Lines 17 and 18** build the current package content list if it doesn’t already exist.

The first section continues from line 20:

```lisp
;; Installs packages
;;
;; myPackages contains a list of package names
(defvar myPackages
  '(better-defaults                 ;; Set up some better Emacs defaults
    material-theme                  ;; Theme
    )
  )

;; Scans the list in myPackages
;; If the package listed is not already installed, install it
(mapc #'(lambda (package)
          (unless (package-installed-p package)
            (package-install package)))
      myPackages)
```

At this point, you’re all set to programmatically install Emacs packages:

- **Lines 23 to 27** define a list of package names to install. You’ll add more packages as you progress through the tutorial:
  - **Line 24** adds [better-defaults](http://melpa.org/#/better-defaults). This is a collection of minor changes to the Emacs defaults that make it more user-friendly. It’s also a great base for further customization.
  - **Line 25** adds the [material-theme](http://melpa.org/#/material-theme) package, which is a nice dark style found in other environments.
- **Lines 31 to 34** traverse the list and install any packages that are not already installed.

> Note: You don’t need to use the Material theme. There are many different [Emacs themes](http://melpa.org/#/?q=theme) available on MELPA for you to choose from. Pick one that suits your style!

After you install your packages, you can move on to the section titled `Basic Customization`:

```lisp
;; ===================================
;; Basic Customization
;; ===================================

(setq inhibit-startup-message t)    ;; Hide the startup message
(load-theme 'material t)            ;; Load material theme
(global-linum-mode t)               ;; Enable line numbers globally

;; User-Defined init.el ends here
```

Here, you add a few other customizations:

- **Line 40** disables the initial Emacs screen containing the tutorial information. You may want to leave this commented out by using a double semicolon (;;) until you’re more comfortable with Emacs.
- **Line 41** loads and activates the Material theme. If you want to install a different theme, then use its name here instead. You can also comment out this line to use the default Emacs theme.
- **Line 42** displays line numbers in every buffer.

Now that you have a complete basic configuration file in place, you can save the file using `Ctrl`+`X` `Ctrl`+`S`. Then, close and restart Emacs to see the changes.

The first time Emacs runs with these options, it may take a few seconds to start as it sets up the packaging infrastructure. When that’s finished, you’ll see that your Emacs window looks a bit different:

![emacsv2-themed](./images/emacsv2-themed.png "emacsv2-themed")

After the restart, Emacs skipped the initial screen and instead opened the last active file. The Material theme is applied, and line numbers have been added to the buffer.

> Note: You can add packages interactively after the packaging infrastructure is set up. Hit `Alt`+`X`, then type `package-show-package-list` to see all the packages available to install in Emacs. As of this writing, there are over 4300 available.
> 
> With the list of packages visible, you can:
> 
> - Quickly filter the list by package name by hitting `F`.
> - View the details of any package by clicking its name.
> - Install the package from the package view by clicking the *Install* link.
> - Close the package list using `Q`.

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
























































































































