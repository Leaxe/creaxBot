#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, pi, floor
from numpy import zeros

# Optional Information. Fill out only if you wish.

# Your real name:
# Contact Email:
# Can this bot's code be shared publicly (Default: No):
# Can non-tournment gameplay of this bot be displayed publicly (Default: No):

class agent:

    def __init__(self, team):
        self.team = team  # use self.team to determine what team you are. I will set to "blue" or "orange"
        self.oldSteeringError = 0;
        self.proportionalConst = 1;
        self.integralConst = 1;
        self.derivativeConst = 0;
        self.integralSize = 30;
        self.pastError = zeros(self.integralSize)
        self.pastErrorSum = 0

    def get_bot_name(self):

        # This is the name that will be displayed on screen in the real time display!

        return 'ATBA2'

    def get_output_vector(self, input):
        self.pastErrorSum = 0
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

        playerFrontDirection = atan2(playerRot1, playerRot4)
        ballDirection = atan2(ballX - playerX, ballZ - playerZ)
#        print ('playerRot1 = ', playerRot1)
#        print ('playerRot1 = ', playerRot1)
        
        steeringError = playerFrontDirection - ballDirection
        if steeringError < 0:
            steeringError += 2*pi
        
        if steeringError > pi:
            steeringError -= 2*pi
        print(floor(steeringError * 100/pi))
        turningFactor = 5
        steeringError *= turningFactor
        steeringError += pi
        steeringError = floor(steeringError * (32767 / (2*pi)))
        
        propComp = floor(self.proportionalConst * steeringError)
        intComp = floor(self.integralConst * self.pastErrorSum)
        derComp = floor(self.derivativeConst * (self.oldSteeringError - steeringError))
        
        turn = propComp + intComp + derComp
        
        self.oldSteeringError = steeringError
        
        for i in range(self.integralSize - 1):
            self.pastError[i] = self.pastError[i + 1]
        self.pastError[self.integralSize - 1] = steeringError
        for i in range(self.integralSize):
            self.pastErrorSum += self.pastError[i]
        self.pastErrorSum /= self.integralSize
            
#        steeringError = pi / 2 + playerFrontDirection - ballDirection

#        turn = floor(steeringError * self.proportionalConst)
#        print(steeringError)
#        print(turn)

        return [
            turn,
            16383,
            32767,
            0,
            0,
            0,
            0,
            ]
