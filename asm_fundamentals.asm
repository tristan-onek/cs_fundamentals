section .data
    array db 10, 20, 30, 40, 50 ; Static array
    array_size equ 5            ; Size of the array

    stack resb 16               ; Stack space (4 elements, 4 bytes each)
    stack_pointer dq 0          ; Stack pointer

    linked_list_head dq 0       ; Linked list head pointer
    node1 db 1, 0, 0, 0, 0, 0, 0, 0 ; First node value
    node2 db 2, 0, 0, 0, 0, 0, 0, 0 ; Second node value

section .bss
    buffer resb 256             ; General-purpose buffer for output

section .text
global _start

_start:
    ; Array Example
    mov rsi, array             ; Load array base address
    mov rcx, array_size        ; Set loop counter
print_array:
    mov al, [rsi]              ; Load current array element
    call print_byte            ; Print the element
    add rsi, 1                 ; Move to next element
    loop print_array           ; Loop until end of array

    ; Stack Example
    ; Push elements
    mov rax, 10
    call stack_push
    mov rax, 20
    call stack_push
    ; Pop element
    call stack_pop
    call print_byte            ; Print popped element

    ; Linked List Example
    ; Add nodes manually
    mov rax, node1
    call linked_list_add
    mov rax, node2
    call linked_list_add
    ; Traverse and print
    mov rdi, linked_list_head
traverse_linked_list:
    test rdi, rdi
    jz done
    mov rax, [rdi]             ; Get node value
    call print_byte
    mov rdi, [rdi + 8]         ; Move to next node
    jmp traverse_linked_list
done:

    ; Exit program
    mov rax, 60                ; Exit syscall
    xor rdi, rdi               ; Return code 0
    syscall

; Stack Push
stack_push:
    mov rbx, stack_pointer
    mov [stack + rbx], al
    inc rbx
    mov stack_pointer, rbx
    ret

; Stack Pop
stack_pop:
    mov rbx, stack_pointer
    dec rbx
    mov al, [stack + rbx]
    mov stack_pointer, rbx
    ret

; Linked List Add
linked_list_add:
    mov rbx, linked_list_head
    mov [rax + 8], rbx         ; Link current head as next node
    mov linked_list_head, rax  ; Update head to new node
    ret

; Print a single byte as a number
print_byte:
    mov rbx, rax               ; Backup value
    add al, '0'                ; Convert to ASCII
    mov [buffer], al
    mov rsi, buffer
    mov rdx, 1                 ; Print 1 byte
    mov rax, 1                 ; Write syscall
    mov rdi, 1                 ; File descriptor (stdout)
    syscall
    mov rax, rbx               ; Restore original value
    ret
