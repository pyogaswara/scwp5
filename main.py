import prob_calculator

hat = prob_calculator.Hat(black=6, red=8, green=3)
probability = prob_calculator.experiment(hat=hat,
                  expected_balls={"red":1,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
