#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt, hypot, sin, cos, acos, atan2
from numpy import sign, cross, pi

# Optional Information. Fill out only if you wish.

# Your real name:
# Contact Email:
# Can this bot's code be shared publicly (Default: No):
# Can non-tournment gameplay of this bot be displayed publicly (Default: No):

    
class agent:
    
    
    def __init__(self, team):
        self.team = team  # use self.team to determine what team you are. I will set to "blue" or "orange"
        self.ballOldZ = 0
        self.ballOldX = 0

    def get_bot_name(self):

        # This is the name that will be displayed on screen in the real time display!

        return "goodBot"

    def get_output_vector(self, input):
        ballZ = input[0][2]
        ballX = input[0][7]
        ballVelZ = ballZ - self.ballOldZ
        ballVelX = ballX - self.ballOldX
        turn = 16383
        
        print(ballVelZ)
        print(ballVelX)

        if self.team == "blue":
            playerZ = input[0][1]
            playerX = input[0][5]
            player_rot1 = input[0][8]
            player_rot4 = input[0][11]
        else:
            playerZ = input[0][3]
            playerX = input[0][18]
            player_rot1 = input[0][19]
            player_rot4 = input[0][22]

        ###PREDICT BALL###

        #playerX = 1
        #playerZ = 1
        #ballX = 1
        #ballZ = 4
        #ballVelX = 0
        #ballVelZ = 1
    
        carVel = 30
    
        C = atan2(ballVelZ, ballVelX) + atan2(ballX - playerX, ballZ
                - playerZ) + pi / 2  # angle between ball path and direction to car
        R = hypot(ballVelX, ballVelZ) / carVel  # ratio between ball velocity and car velocity
        b = hypot(ballX - playerX, ballZ - playerZ)  # distance between ball and car
        print("b = ", b)
        if ((2 * R * b * cos(C)) ** 2 + 4 * (1 - R ** 2) * b ** 2) < 0 or R == 0 or R == 1:
            intersectX = ballX
            intersectZ = ballZ
            print("bad determinant")
        else:
            c = (-2 * R * b * cos(C) + sqrt((2 * R * b * cos(C)) ** 2 + 4
                 * (1 - R ** 2) * b ** 2)) / (2 * (1 - R ** 2))  # distance from car to meeting point
            a = c * R  # distance between ball and meeting point
            print("c = ", c)
            print("a = ", a)
            Asign = sign(cross([ballVelX, ballVelZ], [playerX - ballX,
                         playerZ - ballZ]))  # figures out which way angle A goes, counterclockwise (negative) or clockwise (positive)
            A = Asign * acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # angle made from ball > car > meeting point
    
            D = atan2(ballZ - playerZ, ballX - playerX) + A  # angle between the x axis and line from car to meeting point
    
            intersectX = playerX + c * cos(D)
            intersectZ = playerZ + c * sin(D)
    
            # Need to handle atan2(0,0) case, aka straight up or down, eventually
    
        player_front_direction_in_radians = atan2(player_rot1,
                player_rot4)
        relative_angle_to_ball_in_radians = atan2(intersectX - playerX,
                intersectZ - playerZ)
    
        if not abs(player_front_direction_in_radians
                   - relative_angle_to_ball_in_radians) < pi:
    
            # Add 2pi to negative values
    
            if player_front_direction_in_radians < 0:
                player_front_direction_in_radians += 2 * pi
            if relative_angle_to_ball_in_radians < 0:
                relative_angle_to_ball_in_radians += 2 * pi

        if relative_angle_to_ball_in_radians > player_front_direction_in_radians:
            turn = 0
        else:
            turn = 32767
    
        return [
            turn,
            16383,
            32767,
            0,
            0,
            0,
            0,
            ]
