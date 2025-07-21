import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls_drawn)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn
import copy

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        
        copied_hat = copy.deepcopy(hat)

        
        drawn = copied_hat.draw(num_balls_drawn)

        
        drawn_counts = {}
        for ball in drawn:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments
