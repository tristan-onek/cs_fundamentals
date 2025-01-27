section .data
    fizz db "Fizz", 0
    buzz db "Buzz", 0
    fizzbuzz db "FizzBuzz", 0
    newline db 10, 0 ; Newline character
    fmt db "%d", 0 ; Format for printing numbers

section .bss
    num resb 4 ; Temporary buffer for storing numbers

section .text
    global _start

_start:
    ; Initialize counter
    mov ecx, 1 ; Counter starts at 1

loop_start:
    ; Check if counter > 100
    cmp ecx, 101
    jge end_program ; Exit loop if ecx > 100

    ; Check divisibility by 3 and 5
    mov eax, ecx
    xor edx, edx
    mov ebx, 15 ; Divisibility by 15 (3 * 5)
    div ebx
    cmp edx, 0
    je print_fizzbuzz

    ; Check divisibility by 3
    mov eax, ecx
    xor edx, edx
    mov ebx, 3
    div ebx
    cmp edx, 0
    je print_fizz

    ; Check divisibility by 5
    mov eax, ecx
    xor edx, edx
    mov ebx, 5
    div ebx
    cmp edx, 0
    je print_buzz

    ; Otherwise, print the number
    mov eax, ecx
    call print_number
    jmp next_iteration

print_fizzbuzz:
    mov esi, fizzbuzz
    call print_string
    jmp next_iteration

print_fizz:
    mov esi, fizz
    call print_string
    jmp next_iteration

print_buzz:
    mov esi, buzz
    call print_string
    jmp next_iteration

next_iteration:
    ; Print newline
    mov esi, newline
    call print_string

    ; Increment counter
    inc ecx
    jmp loop_start

end_program:
    ; Exit program
    mov eax, 60 ; syscall: exit
    xor edi, edi ; status: 0
    syscall

print_string:
    ; Print string at ESI
    mov eax, 1 ; syscall: write
    mov edi, 1 ; file descriptor: stdout
    mov edx, 5 ; Max length of string
    syscall
    ret

print_number:
    ; Print number in EAX
    ; Converts to string and prints
    push rdx
    push rcx
    push rbx

    mov rbx, 10
convert_loop:
    xor edx, edx
    div rbx
    add dl, '0'
    push rdx
    test eax, eax
    jnz convert_loop

print_digits:
    pop rax
    mov esi, rax
    call print_string
    loop print_digits

    pop rbx
    pop rcx
    pop rdx
    ret
