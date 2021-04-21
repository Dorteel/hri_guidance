#!/usr/bin/env python

import argparse

import rospy

import intera_interface
import intera_external_devices

from std_msgs.msg import String

from intera_interface import CHECK_VERSION



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    map_keyboard(limb, data.data)

def listener():


    rospy.init_node('asr_listener', anonymous=True)

    rospy.Subscriber('voice_control/speech2text', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def map_keyboard(limb, text):
    angle = 0.5
    has_gripper = False	
    joints = limb.joint_names()

    def set_j(limb, joint_name, delta):
        current_position = limb.joint_angles()
        current_position[joint_name] += delta
        limb.move_to_joint_positions(current_position)
    
    def text_mapping(text, words):
	for word in words:
	    if word in text: return word
	return 'Nothing'

    text = text_mapping(text, ['up','down','left','right', 'exit', 'quit', 'venstre'])
    print(text)
    bindings = {
	'right':  (set_j, [limb, joints[0],  0.5], joints[0]+" increase"),
	'venstre':   (set_j, [limb, joints[0], -0.5], joints[0]+" increase"),
	'left':   (set_j, [limb, joints[0], -0.5], joints[0]+" increase"),
	'down':   (set_j, [limb, joints[1],  0.2], joints[0]+" increase"),		
	'up':     (set_j, [limb, joints[1], -0.2], joints[0]+" increase"),
     }

    done = False
    print("Controlling joints. Press ? for help, Esc to quit.")

    c = text#intera_external_devices.getch()
    if c:
        #catch Esc or ctrl-c
        if c in ['exit', 'quit']:
            done = True
            rospy.signal_shutdown("Example finished.")
        elif c in bindings:
            cmd = bindings[c]
            cmd[0](*cmd[1])
            
            print("command: %s" % (cmd[2],))
            
        else:
            print("key bindings: ")
            print("  Esc: Quit")
            print("  ?: Help")
            for key, val in sorted(bindings.items(),
                           key=lambda x: x[1][2]):
            	print("  %s: %s" % (key, val[2]))





if __name__ == '__main__':

    epilog = """
See help inside the example with the '?' key for key bindings.
    """
    rp = intera_interface.RobotParams()
    valid_limbs = rp.get_limb_names()
    if not valid_limbs:
        rp.log_message(("Cannot detect any limb parameters on this robot. "
                        "Exiting."), "ERROR")
        exit()
    arg_fmt = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=arg_fmt,
                                     epilog=epilog)
    parser.add_argument(
        "-l", "--limb", dest="limb", default=valid_limbs[0],
        choices=valid_limbs,
        help="Limb on which to run the joint position keyboard example"
    )
    args = parser.parse_args(rospy.myargv()[1:])

    print("Initializing node... ")
    rospy.init_node("sdk_joint_position_keyboard")
    print("Getting robot state... ")
    
    
    rs = intera_interface.RobotEnable(CHECK_VERSION)
    init_state = rs.state().enabled

    def clean_shutdown():
        print("\nExiting example.")

    rospy.on_shutdown(clean_shutdown)
    
    rospy.loginfo("Enabling robot...")
    limb = intera_interface.Limb('right')
    rs.enable()
    rospy.Subscriber('voice_control/speech2text', String, callback)
    print("Initializing subscriber...")

    rospy.spin() 
    
    print("Done.")
