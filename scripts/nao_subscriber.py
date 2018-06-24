#! /usr/bin/env python

import rospy
from nao_mind_controlled.msg import facial_expressions
from naoqi import ALProxy
import time

robot_ip ="192.168.2.100"
port = 9559
tts = ALProxy ("ALTextToSpeech",robot_ip,port )
motion = ALProxy("ALMotion",robot_ip,port)
stopper = 0
forwardever =0
dizzyright =0
dizzyleft=0
greeting =0
def callback(msg):
    global stopper,forwardever,dizzyright,dizzyleft,greeting
    if greeting == 0:
        tts.say("Hello professors and my developers")
        time.sleep(1)
        tts.say("before starting I would like to say something ")
        time.sleep(1)
        tts.say("please listen to me professors")
        time.sleep(1)
        tts.say("these guys are amazing and can do lot of things")
        time.sleep(1)
        tts.say ("now you can control me with your mind")
        time.sleep(1)
        greeting +=1
    rospy.loginfo("the Subscriber is working at the moment")
    if msg.expression == 'smile':
        rospy.loginfo("the expression is smile now ")
        threadMove = motion.post.moveTo(0.5,0.0,0.0)
        tts.say("going Forward")
        motion.wait(threadMove,0)
        forwardever +=1
        if forwardever == 3:
            tts.say("you want me to travel to nicosia on my feets or what ? ")
            forwardever = 0
        stopper = 0
        dizzyleft = 0
        dizzyright = 0
    elif msg.expression == 'clench':
        rospy.loginfo("the expression is clench now ")
        threadMove = motion.post.moveTo(0.0,0.0,0.0)
        tts.say("stopping.")
        motion.wait(threadMove,0)
        stopper = stopper + 1
        time.sleep(1)
        if stopper == 3:
            tts.say("Come on I wanna to move around and show the rector how fit I am")
            stopper = 0
        forwardever = 0
        dizzyleft = 0
        dizzyright =0
    elif msg.expression == 'eyebrow':
        rospy.loginfo("the expression is eyebrow now ")
        threadMove = motion.post.moveTo(0.0,0.0,0.5)
        tts.say("rotating left")
        motion.wait(threadMove,0)
        dizzyright +=1
        if dizzyright == 3:
            tts.say("I am getting dizzy please stop ? ")
            dizzyright = 0
        stopper = 0
        dizzyleft = 0
        forwardever = 0

    elif msg.expression == 'furbrow':
        rospy.loginfo("the expression is furbrow now ")
        threadMove = motion.post.moveTo(0.0,0.0,-0.5)
        tts.say("rotating right.")
        motion.wait(threadMove,0)
        dizzyleft +=1
        if dizzyleft == 3:
            tts.say("seriously that is it you want me  vomit or what? ")
            dizzyleft = 0
        stopper = 0
        forwardever = 0
        dizzyright = 0



rospy.init_node('nao_commander')
sub = rospy.Subscriber('/emoState',facial_expressions,callback,queue_size=1)
rospy.spin()
