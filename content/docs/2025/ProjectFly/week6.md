---
title: "Week #6"
---

# **Week #6**

## Team

### **Team Members**

| Team Member							| Telegram Alias	| Email Address   					| Track												| Responsibilities   |
|---------------------------------------|-------------------|-----------------------------------|---------------------------------------------------|--------------------|
| Dmitriy Vizitei (Lead)				| @otkisaev			| d.vizitei@innopolis.university 	| Low level (embedded) + Electric circuit engineer + testing  | Project coordination, task delegation, programming and testing prototypes |
| Senea Belykh							| @SenyaZenya		| s.belykh@innopolis.university		| Low level (embedded) + Electric circuit engineer	| Programming and testing prototypes |
| Dmitry Ryabov							| @theDioxider		| d.ryabov@innopolis.university 	| Low level (embedded) 								| Programming |
| Anas Hamrouni							| @reachnasta		| a.hamrouni@innopolis.university   | Design engineer 									| Designing 3D models |
| Andrew Pavlov							| @chaleshka_0		| and.pavlov@innopolis.university	| Tech writer 										| Document the work and write reports |

## Links

*Specify here all the necessary links to your website, application installer, final demo, etc.*

- **Deployment**: [Setup instructions](#Setup-instructions)
- **API Docs**: [API Docs](#API-Docs)
- **Documentation**: [Documentation](#Documentation)
- **Demo**: https://drive.google.com/file/d/1RMR0l2JPTSWMmnUTkXt8X2qB1T35l_1s/view?usp=drive_link

## Final deliverables

### API Docs
```C
/**
 * Convert a raw ADC measurement to real voltage.
 *
 * @param adc: Raw ADC measurement
 * @return Voltage
 */
double adcToVolts(uint32_t adc)

/**
 * Convert voltage to index number of a triggered reed sensor.
 *
 * @param v: Voltage
 * @param N: Total number of sensors in the line
 * @return Index number of a triggered reed sensor in range [1, N]
 */
int voltToLineNumber(double v, int N)

/**
 * Pretty-print current measurement state of water level into the serial port.
 */
void printMeasurements()
```

### Documentation

Electrical Circuit
The electrical circuit of the device consists of six normally closed (NC) reed switches (4x28 mm) that connect power and signal lines. A 10 kΩ resistor is placed between each reed switch to detect which one is closed using the voltage divider rule. A current-limiting resistor is placed before the first reed switch to prevent a short circuit. A separating resistor is placed after the last reed switch to distinguish between the last reed switch being closed and no switch being closed. A 100 kΩ resistor is connected between the signal line and ground to suppress contact bouncing. The circuit operates at 3.3 V.

PCB Design
The printed circuit board (PCB) has a length matching the tank length (234 mm), which fits six reed switches with 0.85 mm spacing between leads, and a minimum possible width of 11 mm. The trace width is 1 mm for reliability and ease of manufacturing. The final device consists of two identical PCBs, but with the reed switches offset by 14 mm (half the length of a reed switch) relative to each other. This allows dual verification of magnet position and eliminates blind spots between reed switches on the opposite PCB.

Assembly\
\- The two PCBs are stacked together with the reed switches facing outward and a dielectric spacer in between.\
\- They are then placed inside a rod.\
\- Power (VCC), ground (GND), and two signal lines are connected to a microcontroller board mounted on the top cover.

### Project overview

This project is a request to develop a solution for the use of unmanned aerial vehicles in agriculture. The task was to develop a system for measuring the liquid level in the tank of an unmanned aerial vehicle for spraying crops.

### Features

- Custom sensor of liquid level solution for a tank of complicated form
- The sensor has an easy production and support abilities 
- The custom pcb with stm micro controller
- The reliable way to measure liquid level
- The custom easy to understand progress bar (visualization) of liquid level
- Isolation of electric parts exposed to liquids
- The smart step by step installation and uninstallation system of sensor rod and float configuration

### Tech stack

| Field					| Stack							|
|-----------------------|-------------------------------|
| Embeded programming	| C/C++, Cube IDE, Arduino IDE	|
| Design engineer		| NX Seimens					|
| Sensors Mechanics		| Math + physics				|

### Setup instructions

1. Assemble the tool
2. Assemble the float
3. Attach the 'bottomCap' to the tool
4. Place the float on the 'bottomCap'
5. Enter the tool into the tank through the filling neck
6. Enter the rod into the tank from the top
7. Align the rod with Float and the 'bottomCap'
8. Hold the tool and turn the rod to screw together the rod and the 'bottomCap' 
9. Pull the tool from the filling neck
10. Fix the rod with screws and place in the PCB


#### How to assemble the tool:
1. Glue the short side of toolHandler with toolHandler2
2. Align the 'tool' part with 'toolhandler2' so they fit and glue them together

#### How to assemble the float:
1. Put some glue inside the groove of the float
2. Attach both parts

## Presentation draft

https://docs.google.com/presentation/d/1ErlLMnh_HFSRYw7ifzSZqWEL7AQgV6kYaB8lmL1xhwc/view

# Weekly commitments

## Individual contribution of each participant

| Member					| Contribution					|
|---------------------------|-------------------------------|
| Dmitriy Vizitei			| Board assembly, testing |
| Senea Belykh				| Board assembly, testing |
| Dmitry Ryabov				| Code for calculating ADC, code for visualizing and interpreting the reed switch signal |
| Anas Hamrouni				| Updated version of the models |
| Andrew Pavlov				| 6nd week report, presentation draft |


## Plan for Next Week

- Calibrate the sensor's work to make it more reliable in magnet field 
- Update the demo presentation
- Improve the materials used in assembly- 
- Complete assembly with custom pcb with stm32 controller
- Test final assembly

## Confirmation of the code's operability

We confirm that the code in the main branch:
- [X] In working condition.
- [X] Run via docker-compose (or another alternative described in the `README.md`).
