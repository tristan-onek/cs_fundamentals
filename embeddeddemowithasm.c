#include <stdint.h>
#include <stdio.h>

volatile uint32_t GPIO_PORTA_DATA = 0;
volatile uint32_t GPIO_PORTA_DIR = 0;
volatile uint32_t GPIO_PORTA_DEN = 0;

volatile uint32_t TIMER0_CTRL = 0;
volatile uint32_t TIMER0_LOAD = 0;
volatile uint32_t TIMER0_VALUE = 0;
volatile uint32_t TIMER0_INTCLR = 0;

volatile uint32_t UART0_DR = 0;
volatile uint32_t UART0_FR = 0; // Flag register
#define UART_FR_TXFF 0x20 // Transmit FIFO Full Flag


#define PIN_LED 0x01 // PA0

void GPIO_Init(void);
void LED_Toggle(void);
void Timer_Init(uint32_t load_value);
void UART_SendChar(char c);
void UART_SendString(const char *str);
void delay_ms(uint32_t ms);

int main() 
{
    // Initialize GPIO and Timer
    GPIO_Init();
    Timer_Init(1000000); // Load value for ~1 second delay (simulated)

    // Main Loop
    while (1) {
        LED_Toggle();             // Toggle the LED
        UART_SendString("LED toggled!\n"); // Send message via UART
        delay_ms(1000);           // Delay ~1 second
    }

    return 0;
}

// Initialize GPIO
void GPIO_Init(void) 
{
    GPIO_PORTA_DIR |= PIN_LED;   // Set PA0 as output
    GPIO_PORTA_DEN |= PIN_LED;   // Enable digital function on PA0
    printf("GPIO Initialized.\n");
}

// Toggle LED
void LED_Toggle(void) 
{
    // Inline assembly to toggle GPIO data register
    __asm__ volatile (
        "movl %0, %%eax\n"       // Load GPIO_PORTA_DATA into eax
        "xorl %1, %%eax\n"       // XOR eax with PIN_LED
        "movl %%eax, %0\n"       // Store back to GPIO_PORTA_DATA
        : "+m" (GPIO_PORTA_DATA) // Output operand
        : "r" (PIN_LED)          // Input operand
        : "eax"                  // Clobbered register
    );
}

// Initialize Timer
void Timer_Init(uint32_t load_value) 
{
    // Inline assembly to set timer load value and enable
    __asm__ volatile (
        "movl %1, %%eax\n"       // Load load_value into eax
        "movl %%eax, %0\n"       // Store eax into TIMER0_LOAD
        "movl $0x1, %2\n"        // Set TIMER0_CTRL to enable (value 1)
        : "+m" (TIMER0_LOAD), "+m" (TIMER0_CTRL)
        : "r" (load_value)
        : "eax"
    );
    printf("Timer Initialized.\n");
}

// Send a character over UART
void UART_SendChar(char c) 
{
    // Inline assembly to wait for UART FIFO availability and send a character
    __asm__ volatile (
        "1: movl %1, %%eax\n"    // Load UART0_FR into eax
        "testl %2, %%eax\n"      // Check UART_FR_TXFF flag
        "jnz 1b\n"               // If FIFO full, loop back
        "movb %0, %3\n"          // Send character to UART0_DR
        : "+m" (UART0_DR)
        : "m" (UART0_FR), "r" (UART_FR_TXFF), "r" ((uint32_t)c)
        : "eax"
    );
}

// Send a string over UART
void UART_SendString(const char *str) 
{
    while (*str) 
    {
        UART_SendChar(*str++);
    }
}

// use caution below
void delay_ms(uint32_t ms) 
{
    volatile uint32_t count = ms * 1000; // Assume 1 ms = 1000 iterations
    __asm__ volatile (
        "1: decl %0\n"           // Decrement count
        "jnz 1b\n"               // If not zero, loop
        : "+r" (count)           // Input and output operand
    );
}
