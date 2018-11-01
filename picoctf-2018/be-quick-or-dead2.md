

**be-quick-or-be-dead-2**

Points: 275

Tags: reversing 

Poll rating:

As you enjoy this music even more, another executable be-quick-or-be-dead-2 shows up. Can you run this fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-2_2_7e92e9cc48bad623da1c215c192bc919.

Solution:

It is a easy problem but costs me about 5 hours to find the tools and get the key. :D

first, I use gdb to run the program. And I use IDA pro to help me to read some functions in the program. It looks quite clear that the reason why program run so solwly is because of the recursion version of calculating fib number. So what we need to do is just skip the functions and modify the data of the register and we can get the flag immediately.

I try to use gdb but failed. In other peoples' writeup, I find that they use a tool named radare2. I install it quickly.

Here is the steps.

Write a .py to get the `fib(0x43c)`

oh, unsigned int is used in the function so we can use `a=a%(1<<32)`

```
[0x004005a0]> aaaa
//analyse the program
[0x004005a0]> ood
//run the program
[0x7f797b9f1090]> s sym.calculate_key
//jump to this function
[0x0040074b]> pdf
//print the infomation of the function
/ (fcn) sym.calculate_key 16
|   sym.calculate_key ();
|           ; CALL XREF from sym.get_key (0x4007e1)
|           0x0040074b      55             push rbp
|           0x0040074c      4889e5         mov rbp, rsp
|           0x0040074f      bf2b040000     mov edi, 0x42b              ; 1067
|           0x00400754      e8adffffff     call sym.fib
|           0x00400759      5d             pop rbp
\           0x0040075a      c3             ret
[0x0040074b]> db 0x0040074b
//breakpoint
[0x7f5ca266c090]> dc
//continue
Be Quick Or Be Dead 2
=====================

Calculating key...
hit breakpoint at: 40074b
[0x0040074b]> dr rip=0x0040075a
//modify the rip
0x0040074b ->0x0040075a
[0x0040074b]> dr eax=0x2e8e4d99
// extremely likely to the above one
0x00000000 ->0x2e8e4d99
[0x0040074b]> dc
child stopped with signal 14
[+] SIGNAL 14 errno=0 addr=0x00000000 code=128 ret=0
Done calculating key
Printing flag:
picoCTF{the_fibonacci_sequence_can_be_done_fast_ec58967b}
[+] signal 14 aka SIGALRM received 0
```
