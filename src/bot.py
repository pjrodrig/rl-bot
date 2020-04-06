import math
import random

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from util.orientation import Orientation
from util.vec import Vec3

class MyBot(BaseAgent):

    def initialize_agent(self):
        # This runs once before the bot starts up
        self.controller_state = SimpleControllerState()
        self.throttle = {
            'til': 0,
           'value': 0
        }

        #debug
        self.setThrottle = True

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        secondsElapsed = packet.game_info.seconds_elapsed
        myCar = packet.game_cars[self.index]

        # if self.setThrottle:
        #     self.setThrottle = False
        #     self.throttle['til'] = secondsElapsed + 3
        #     self.throttle.value = 1
        #     print(myCar.physics.location)
        #     print(secondsElapsed)
        
        


        # if self.throttle['til'] > secondsElapsed:
        #     self.controller_state.throttle = self.throttle['value']
        # else:
        #     if self.controller_state.throttle > 0:
        #         print(myCar.physics.location)
        #         print(secondsElapsed)
        #     self.controller_state.throttle = 0

        # if self.steer.til > secondsElapsed:
        #     self.controller_state.steer = self.steer.value
        # else:
        #     self.controller_state.steer = 0


        loc = packet.game_cars[0].physics.location
        curve = [loc]
        for i in range(0, 200):
            curve += []


        # car_location = Vec3(my_car.physics.location)
        # car_to_target = self.target - car_location

        # # print(car_location.dist(self.target))
        # if car_location.dist(self.target) < 30:
        #     pick_random_target(self, self.get_field_info().boost_pads)
        
        # # Find the direction of our car using the Orientation class
        # car_orientation = Orientation(my_car.physics.rotation)
        # car_direction = car_orientation.forward

        # steer_correction_radians = find_correction(car_direction, car_to_target)
        # if steer_correction_radians > 1:
        #     turn = -1
        # elif steer_correction_radians < -1:
        #     turn = 1
        # else:
        #     turn = -1 * steer_correction_radians

        # self.controller_state.throttle = 1.0
        # self.controller_state.steer = turn
        # path = predictBallPath(packet.game_ball)
        # draw_debug(self.renderer, my_car, packet.game_ball, "", self.target, path)

        return self.controller_state



def find_correction(current: Vec3, ideal: Vec3) -> float:
    # Finds the angle from current to ideal vector in the xy-plane. Angle will be between -pi and +pi.

    # The in-game axes are left handed, so use -x
    current_in_radians = math.atan2(current.y, -current.x)
    ideal_in_radians = math.atan2(ideal.y, -ideal.x)

    diff = ideal_in_radians - current_in_radians

    # Make sure that diff is between -pi and +pi.
    if abs(diff) > math.pi:
        if diff < 0:
            diff += 2 * math.pi
        else:
            diff -= 2 * math.pi

    return diff

def draw_debug(renderer, car, ball, action_display, target, path):
    renderer.begin_rendering()
    # draw a line from the car to the ball
    renderer.draw_line_3d(car.physics.location, ball.physics.location, renderer.white())
    # print the action that the bot is taking
    renderer.draw_string_3d(car.physics.location, 2, 2, action_display, renderer.white())
    renderer.draw_string_3d(target, 2, 2, "*", renderer.white())
    renderer.draw_polyline_3d(path, renderer.black())
    renderer.end_rendering()

def pick_random_target(self, targets):
    target_location = targets[random.randrange(0, len(targets))].location
    self.target = Vec3(target_location.x, target_location.y, target_location.z)
    print(self.target)

def predictBallPath(ball):
    gravity = -6.5
    floor = 93

    x = ball.physics.location.x
    y = ball.physics.location.y
    z = ball.physics.location.z

    xVel = ball.physics.velocity.x/10
    yVel = ball.physics.velocity.y/10
    zVel = ball.physics.velocity.z/10
    path = [(x, y, z)]

    a = 0.5 * gravity 
    b = zVel
    c = z - floor
    t = -1 * (-1 * b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print(math.floor(t))
    for time in range(0, math.floor(t)):
        path += [(x + xVel * time, y + yVel * time, z + zVel * time + 0.5 * gravity * time * time)]

    # x = x + xVel * t
    # y = y + yVel * t
    # z = floor
    # path += [(x, y, z)]
    # zVel = -0.5 * zVel

    # b = zVel
    # c = 0
    # t = -1 * (-1 * b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    # print(math.floor(t))
    # for time in range(0, math.floor(t)):
    #     path += [(x + xVel * time, y + yVel * time, z + zVel * time + 0.5 * gravity * time * time)]

    # x = x + xVel * t
    # y = y + yVel * t
    # z = floor
    # path += [(x, y, z)]
    # zVel = -1 * zVel

    # b = zVel
    # t = -1 * (-1 * b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    # print(math.floor(t))
    # for time in range(0, math.floor(t)):
    #     path += [(x + xVel * time, y + yVel * time, z + zVel * time + 0.5 * gravity * time * time)]

    return path
    
