# Robot Solution

A Python solution for the Robot problem - simulates robots navigating a grid on Mars, tracking their positions and handling cases where they fall off the edge.

## How to Run
1. Create or edit `input.txt` with your test data following this format (note the blank lines between robot instructions just like the example given in the solution):
   5 3
   1 1 E
   RFRFRFRF

   3 2 N
   FRRFLLFFRRFLL

   0 3 W
   LLFFFLFLFL
   
2. Run the script using one of these methods:

   **PowerShell:**
   Get-Content input.txt | python Robots.py
   

   **Command Prompt:**
   python Robots.py < input.txt

## Tech Choices

I am actually more comfortable coding in c# however for this problem, Python's simplicity and readability make it ideal. The straightforward syntax also creates less ambiguity and makes the solution easily visible. It is also easier to run on a command line with no complex imports

Making use of Dictionaries:
**Why**: Using dictionaries (`turn_left` and `turn_right`) provides minimal lookup time and makes the logic explicit and easy to verify. More maintainable than complex if-else statements.

### Set for Scent Tracking
**Why**: A `set` data structure provides O(1) average-case lookup and insertion, which is perfect for checking if a position has a scent marker. More efficient than a list for this use case.

### Procedural Approach
**Why**: For this problem, a simple procedural approach with functions is sufficient. No need for classes or complex OOP due to the problem being straightforward enough that functions provide clear, readable code.

## Problem Approach

1. **Grid Setup**: Read the grid dimensions from the first line to establish boundaries.

2. **Robot Processing Loop**: Process each robot sequentially:
   - Read initial position and orientation
   - Read instruction sequence
   - Execute each instruction (L, R, or F)

3. **Movement Logic**:
   - **Turning**: Use dictionary lookups to determine new orientation
   - **Forward Movement**: Calculate new coordinates based on current orientation
   - **Boundary Checking**: Before moving, check if the new position is within bounds

4. **Scent Marker System**:
   - When a robot would fall off the grid, check if the current position has a scent marker
   - If no scent exists: mark robot as lost and add scent to the set
   - If scent exists: ignore the move (robot is saved by previous robot's warning)

5. **Output**: After processing all instructions, output the final position and orientation, appending "LOST" if applicable.


