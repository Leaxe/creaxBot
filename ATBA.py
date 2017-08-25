#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


# Optional Information. Fill out only if you wish.

# Your real name:
# Contact Email:
# Can this bot's code be shared publicly (Default: No):
# Can non-tournment gameplay of this bot be displayed publicly (Default: No):

class agent:

    def __init__(self, team):
        self.team = team  # use self.team to determine what team you are. I will set to "blue" or "orange"

    def get_bot_name(self):

        # This is the name that will be displayed on screen in the real time display!

        return 'ATBA'

    def get_output_vector(self, input):

        ballZ = input[0][2]
        ballX = input[0][7]
        turn = 16383

        if self.team == 'blue':
            playerZ = input[0][1]
            playerX = input[0][5]
            playerRot1 = input[0][8]
            playerRot4 = input[0][11]
        else:
            playerZ = input[0][3]
            playerX = input[0][18]
            playerRot1 = input[0][19]
            playerRot4 = input[0][22]

        # Need to handle atan2(0,0) case, aka straight up or down, eventually

        playerFrontDirectionInRadians = math.atan2(playerRot1,
                playerRot4)
        relativeAngleToBallInRadians = math.atan2(ballX
                - playerX, ballZ - playerZ)

        if not abs(playerFrontDirectionInRadians
                   - relativeAngleToBallInRadians) < math.pi:

            # Add 2pi to negative values

            if playerFrontDirectionInRadians < 0:
                playerFrontDirectionInRadians += 2 * math.pi
            if relativeAngleToBallInRadians < 0:
                relativeAngleToBallInRadians += 2 * math.pi

        if relativeAngleToBallInRadians \
            > playerFrontDirectionInRadians:
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
