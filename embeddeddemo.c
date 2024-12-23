#include <stdint.h>
#include <stdio.h>

// Mock GPIO Registers:
volatile uint32_t GPIO_PORTA_DATA = 0;
volatile uint32_t GPIO_PORTA_DIR = 0;
volatile uint32_t GPIO_PORTA_DEN = 0;

// Timer:
volatile uint32_t TIMER0_CTRL = 0;
volatile uint32_t TIMER0_LOAD = 0;
volatile uint32_t TIMER0_VALUE = 0;
volatile uint32_t TIMER0_INTCLR = 0;

//UART:
volatile uint32_t UART0_DR = 0;
volatile uint32_t UART0_FR = 0; // Flag register
#define UART_FR_TXFF 0x20 // Transmit FIFO Full Flag

// GPIO Pin:
#define PIN_LED 0x01 // PA0

// Function Prototypes:
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

    return 0;//end
}

// Initialize
void GPIO_Init(void) 
{
    GPIO_PORTA_DIR |= PIN_LED;   // Set PA0 as output
    GPIO_PORTA_DEN |= PIN_LED;   // Enable digital function on PA0
    printf("GPIO Initialized.\n");
}

// Toggle LED
void LED_Toggle(void) 
{
    GPIO_PORTA_DATA ^= PIN_LED; // Toggle PA0
}

// Initialize Timer
void Timer_Init(uint32_t load_value) 
{
    TIMER0_CTRL = 0;            // Disable timer
    TIMER0_LOAD = load_value;   // Set load value
    TIMER0_CTRL |= 0x01;        // Enable timer
    printf("Timer Initialized.\n");
}
void UART_SendChar(char c) 
{
    while (UART0_FR & UART_FR_TXFF) {
        // Wait until Transmit FIFO is not full
    }
    UART0_DR = c; // Send character
}
void UART_SendString(const char *str) 
{
    while (*str) {
        UART_SendChar(*str++);
    }
}
void delay_ms(uint32_t ms) 
{
    volatile uint32_t count = ms * 1000; // Assume 1 ms = 1000 iterations
    while (count--) {
        __asm__("nop"); // No operation, just burn cycles
    }
}
