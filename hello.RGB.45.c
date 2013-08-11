//
//
// hello.RGB.45.c
//
// RGB LED software PWM hello-world
//
// Neil Gershenfeld
// 11/10/10
//
// (c) Massachusetts Institute of Technology 2010
// Permission granted for experimental and personal use;
// license for commercial sale available from MIT.
//
// MIXED BY FRANCISCO WITH
//
// hello.bus.45.c
//
// 9600 baud serial bus hello-world
//
// Neil Gershenfeld
// 11/24/10
//
// (c) Massachusetts Institute of Technology 2010
// Permission granted for experimental and personal use;
// license for commercial sale available from MIT.
//




#include <avr/io.h>
#include <util/delay.h>
// FROM NETWORK
#include <avr/pgmspace.h>
#include <string.h>
#include <stdlib.h> 

#define output(directions,pin) (directions |= pin) // set port direction for output
// FROM NETWORK
#define input(directions,pin) (directions &= (~pin)) // set port direction for input

#define set(port,pin) (port |= pin) // set port pin
#define clear(port,pin) (port &= (~pin)) // clear port pin
#define pin_test(pins,pin) (pins & pin) // test for port pin
#define bit_test(byte,bit) (byte & (1 << bit)) // test for bit set
#define PWM_delay() _delay_us(25) // PWM delay

#define led_port PORTB
#define led_direction DDRB
#define blue (1 << PB1)
#define green (1 << PB0)
#define red (1 << PB2)

// FROM NETWORK

#define bit_delay_time 100 // bit delay for 9600 with overhead
#define bit_delay() _delay_us(bit_delay_time) // RS232 bit delay
#define half_bit_delay() _delay_us(bit_delay_time/2) // RS232 half bit delay
#define led_delay() _delay_ms(100) // LED flash delay

//#define led_port PORTB
//#define led_direction DDRB
//#define led_pin (1 << PB0)

#define serial_port PORTB
#define serial_direction DDRB
#define serial_pins PINB
#define serial_pin_in (1 << PB3)
#define serial_pin_out (1 << PB4)

#define node_id '5'

void get_char(volatile unsigned char *pins, unsigned char pin, char *rxbyte) {
   //
   // read character into rxbyte on pins pin
   //    assumes line driver (inverts bits)
   //
   *rxbyte = 0;
   while (pin_test(*pins,pin))
      //
      // wait for start bit
      //
      ;
   //
   // delay to middle of first data bit
   //
   half_bit_delay();
   bit_delay();
   //
   // unrolled loop to read data bits
   //
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 0);
   else
      *rxbyte |= (0 << 0);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 1);
   else
      *rxbyte |= (0 << 1);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 2);
   else
      *rxbyte |= (0 << 2);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 3);
   else
      *rxbyte |= (0 << 3);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 4);
   else
      *rxbyte |= (0 << 4);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 5);
   else
      *rxbyte |= (0 << 5);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 6);
   else
      *rxbyte |= (0 << 6);
   bit_delay();
   if pin_test(*pins,pin)
      *rxbyte |= (1 << 7);
   else
      *rxbyte |= (0 << 7);
   //
   // wait for stop bit
   //
   bit_delay();
   half_bit_delay();
   }



void flash() {
   //
   // LED flash delay
   //
   clear(led_port, green);
   led_delay();
   set(led_port, green);
   }
void flash_blue() {
  //
  // LED flash delay
  //
  clear(led_port, blue);
  led_delay();
  set(led_port, blue);
  }
void flash_red() {
//
// LED flash delay
//
clear(led_port, red);
led_delay();
set(led_port, red);
}

int main(void) {
   //
   // main
   //
   unsigned char count, pwm;
   // FROM NETWORK
   static char chr; // was static char chr;
   //
   // set clock divider to /1
   //
   CLKPR = (1 << CLKPCE);
   CLKPR = (0 << CLKPS3) | (0 << CLKPS2) | (0 << CLKPS1) | (0 << CLKPS0);
   //
   // initialize LED pins
   //
   set(led_port, blue);
   output(led_direction, blue);
   set(led_port, green);
   output(led_direction, green);
   set(led_port, red);
   output(led_direction, red);
   //
   // initialize output pins FROM NETWORK
   //
   set(serial_port, serial_pin_out);
   input(serial_direction, serial_pin_out);
   set(led_port, green);
   output(led_direction, green);
   //
   // main loop
   //
   while (1) {
		  get_char(&serial_pins, serial_pin_in, &chr);
		  if (chr == 45) {  // -
      			clear(led_port, red);}
		  else if (chr == 46) { // .
		        clear(led_port, green);}
		  else if (chr == 47) {  // /
				clear(led_port, blue);}
	  	  else if (chr == 36) {  // $
	  			set(led_port, red);
				set(led_port, blue);
				set(led_port, green);
			}
			
	
      }
   }
 
