from main import * 
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LEDs and servo motor
green_led_pin = 17
red_led_pin = 18
servo_pin = 23

# Set up GPIO pins
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

# Function to control servo motor to a specific angle
def set_angle(angle):
    duty = angle / 18.0 + 2.5  # Map angle (0 to 180) to duty cycle (approximately 2.5 to 12.5)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Adjust this sleep time as needed for your servo

try:
    # Turn off both LEDs initially
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.output(red_led_pin, GPIO.LOW)

    # Wait for the result from main.py
    # Read the result from the file
    with open("result.txt", "r") as file:
        result = file.read().strip()

    # Check the result
    if result == "Allow":
        # Turn on green LED
        GPIO.output(green_led_pin, GPIO.HIGH)

        # Move the servo to the 90-degree position
        pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)
        pwm.start(0)
        set_angle(90)
        # Wait for 10 seconds
        time.sleep(10)
        # Move the servo back to the 0-degree position
        set_angle(0)
        pwm.stop()  # Stop PWM after use
        GPIO.output(green_led_pin, GPIO.LOW)

    else:
        # Turn on red LED
        GPIO.output(red_led_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(red_led_pin, GPIO.LOW)

except KeyboardInterrupt:
    # Clean up GPIO
    GPIO.cleanup()