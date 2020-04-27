       .global main
main:
        movabs $0x68732f6e69622fff, %rax
        shr $8, %rax
        pushq %rax
        movq %rsp, %rdi
        xorl %eax, %eax
        movb $59, %al
        syscall	
