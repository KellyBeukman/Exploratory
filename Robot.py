#How to Run
#Edit input.txt to your liking
#Run : Get-Content input.txt | python martian_robots.py (Using Powershell)
#or
#Run : python martian_robots.py < input.txt (Using Command Prompt)

#Method to turn the robot 90 degrees to the left
def turn_left(orientation):
    turns = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    return turns.get(orientation, orientation)

#Method to turn the robot 90 degrees to the right
def turn_right(orientation):
    turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    return turns.get(orientation, orientation)


def main():
    # Determine the grid dimensions
    first_line = input().strip()
    grid_coords = first_line.split()
    max_x = int(grid_coords[0])
    max_y = int(grid_coords[1])
    
    # Track positions where robots were lost (scent markers)
    scent_positions = set()
    
    # Process each robot
    while True:
        try:
            position_line = ""
            while True:
                try:
                    line = input().strip()
                    if line:  # Check if line is not empty
                        position_line = line
                        break
                except EOFError:
                    raise
            
            # Skip empty lines and read instruction line
            instruction_line = ""
            while True:
                try:
                    line = input().strip()
                    if line:  # Check if line is not empty
                        instruction_line = line
                        break
                except EOFError:
                    raise
            
            # Determine the initial position
            position_coords = position_line.split()
            x = int(position_coords[0])
            y = int(position_coords[1])
            orientation = position_coords[2]
            
            lost = False
            
            # Process each instruction
            for instruction in instruction_line:
                if lost:
                    break
                
                if instruction == 'L':
                    # Turn left
                    orientation = turn_left(orientation)
                elif instruction == 'R':
                    # Turn right
                    orientation = turn_right(orientation)
                elif instruction == 'F':
                    # Move forward
                    new_x = x
                    new_y = y
                    
                    if orientation == 'N':
                        new_y += 1
                    elif orientation == 'S':
                        new_y -= 1
                    elif orientation == 'E':
                        new_x += 1
                    elif orientation == 'W':
                        new_x -= 1
                    
                    # Check if new position is out of bounds
                    if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                        # Check if there's a scent at current position
                        scent_key = f"{x},{y}"
                        if scent_key not in scent_positions:
                            # Robot is lost, leave scent
                            scent_positions.add(scent_key)
                            lost = True
                        # If scent exists, ignore the move
                    else:
                        # Move is valid
                        x = new_x
                        y = new_y
            
            # Output result
            output = f"{x} {y} {orientation}"
            if lost:
                output += " LOST"
            print(output)
            
        except EOFError:
            break


if __name__ == "__main__":
    main()

