from naoqi import ALProxy
import qi
ip = "192.168.1.3"
tts = ALProxy("ALTextToSpeech", ip, 9559)
#tts.say("Hello, world!")
motion = ALProxy("ALMotion", ip, 9559)

motion.wakeUp()

motion.setStiffnesses("Body", 1.0)
motion.moveInit()
i = 1
id = motion.post.moveTo(-0.2, 0, 0)
print(id)
motion.wait(id, 0)
tts.say("I'm walking")

id = motion.post.moveTo(-0.2, 0, 0)
    
print(id)
#motion.rest()
