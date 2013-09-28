
// FAB 9000 mkII
// Maker Faire European Edition
// Rome 2013

// Francisco Sanchez Arroyo

//***************************

#include <AccelStepper.h>

// Define parameters
#define stepsPerRev      1600

// Define pins
#define ledPin           13 // LED on the board

#define rot_step         12
#define rot_dir          11

#define sho_step         12
#define sho_dir          12

#define elb_step         12
#define elb_dir          12

#define wri_step         12
#define wri_dir          12

// Analog inputs
# define joy_h           15
# define joy_v           16
# define throttle        17

// Create steppers
AccelStepper stepper1(1, rot_step, rot_dir); 
AccelStepper stepper2(2, sho_step, sho_dir); 
AccelStepper stepper3(3, elb_step, elb_dir); 
AccelStepper stepper4(4, wri_step, wri_dir); 


