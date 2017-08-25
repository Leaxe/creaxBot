#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, pi, floor

# Optional Information. Fill out only if you wish.

# Your real name:
# Contact Email:
# Can this bot's code be shared publicly (Default: No):
# Can non-tournment gameplay of this bot be displayed publicly (Default: No):

oldSteeringError = 0;
proportionalConst = 32767 / (2 * pi);
integralConst = 0;
derivativeConst = 0;



ballZ = 0
ballX = 0
turn = 16383

playerZ = -1
playerX = -1
playerRot1 = .2
playerRot4 = 0.8

# Need to handle atan2(0,0) case, aka straight up or down, eventually

playerFrontDirection = atan2(playerRot1, playerRot4)
ballDirection = atan2(ballX - playerX, ballZ - playerZ)
#        print ('playerRot1 = ', playerRot1)
#        print ('playerRot1 = ', playerRot1)

steeringError = pi / 2 + playerFrontDirection - ballDirection

turn = floor(steeringError * proportionalConst)
print(steeringError)
print(ballDirection)
print(turn)
