import copy
import random

# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        # Initialize the Hat class with specified balls and their quantities.
        self.contents = []
        for ball, quantity in args.items():
            self.contents.extend([ball] * quantity)

    def draw(self, num):
        # Randomly draw a specified number of balls from the hat.
        if num >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        result = True
        test_hat = copy.deepcopy(hat)
        drawn_balls = test_hat.draw(num_balls_drawn)

        for ball, expected_quantity in expected_balls.items():
            actual_quantity = drawn_balls.count(ball)
            if actual_quantity < expected_quantity:
                # If the actual quantity is less than expected, the experiment fails.
                result = False

        if result:
            # If all expected balls are drawn, the experiment is successful.
            success_count += 1

    # Calculate and return the probability of success.
    return success_count / num_experiments

