# Temperature State Converter (Problem 1)

A Python script designed to convert Fahrenheit temperatures to Celsius and determine the physical state of water (Ice, Liquid, or Gas) based on the result.

---

## Features
*   **Unit Conversion:** Converts temperature from Fahrenheit to Celsius using the standard formula: $C = (F - 32) \times \frac{5}{9}$.
*   **State Analysis:** Evaluates the resulting Celsius value to identify the phase of water.
*   **Precise Input:** Uses floating-point conversion to allow for decimal temperature values.

---

## Physical State Logic
The program categorizes the state of water based on the following Celsius thresholds:

| Celsius Range | Physical State |
| :--- | :--- |
| **0°C or below** | Ice (Solid) |
| **Above 0°C up to 100°C** | Liquid |
| **Above 100°C** | Gas (Vapor) |

---

## Technical Details

### Script Logic
1.  **User Input:** Prompts for a Fahrenheit value and converts it to a `float`.
2.  **Mathematical Conversion:** Applies the subtraction and multiplication factors to calculate Celsius.
3.  **Nested & Sequential If-Statements:** 
    *   Checks for freezing point (less than or equal to 0).
    *   Uses a nested condition to verify if the temperature falls between 0 and 100.
    *   Checks for boiling point (greater than 100).

### Example Workflow
*   **Input:** `32`
*   **Calculation:** $(32 - 32) \times \frac{5}{9} = 0$
*   **Output:** `Temperature in Celsius: 0.0`, `Ice`

---

## How to Run

### Prerequisites
*   **Python 3.x**
*   No external dependencies required.

### Execution
1.  Save the code to a file named `temp_converter.py`.
2.  Run the script via terminal:
    ```bash
    python temp_converter.py
    ```
3.  Enter the temperature when prompted to see the conversion and the state of water.
