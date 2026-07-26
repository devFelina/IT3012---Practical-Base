def __init__(self, width=10, height=10, num_food=10, num_opponents=2, num_traps=3, custom_walls=None):
        self.width = width
        self.height = height
        self.agent_pos = [0, 0]  # Starting position (x, y)

        if custom_walls is not None:
            self.walls = set(custom_walls)
        else:
            # Generate some default scattered walls for a larger grid
            self.walls = {(2, 2), (2, 3), (5, 5), (6, 5), (3, 7)}

        # Dynamically generate random food positions avoiding walls and agent start
        self.food_positions = set()
        while len(self.food_positions) < num_food:
            fx = random.randint(0, self.width - 1)
            fy = random.randint(0, self.height - 1)
            pos_tuple = (fx, fy)
            if pos_tuple != (0, 0) and pos_tuple not in self.walls:
                self.food_positions.add(pos_tuple)

        # Dynamically generate toxic traps avoiding (0, 0), walls, and food positions
        self.toxic_traps = set()
        while len(self.toxic_traps) < num_traps:
            tx = random.randint(0, self.width - 1)
            ty = random.randint(0, self.height - 1)
            trap_pos = (tx, ty)
            if (
                trap_pos != (0, 0) 
                and trap_pos not in self.walls 
                and trap_pos not in self.food_positions
            ):
                self.toxic_traps.add(trap_pos)

        # Generate adversarial opponents avoiding start, walls, food, and traps
        self.opponents = []
        while len(self.opponents) < num_opponents:
            ox = random.randint(0, self.width - 1)
            oy = random.randint(0, self.height - 1)
            op_pos = [ox, oy]
            op_tuple = tuple(op_pos)
            if (
                op_tuple != (0, 0) 
                and op_tuple not in self.walls 
                and op_tuple not in self.food_positions
                and op_tuple not in self.toxic_traps
            ):
                self.opponents.append(op_pos)

        self.score = 0
        self.steps = 0
        self.collision = False