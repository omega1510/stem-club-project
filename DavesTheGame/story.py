"""The story for the game.
"""

from choice import Choice
from situation import Situation

office = Situation("""
As you awake from troubled dreams, you find yourself in a small, brightly lit
office room. Tennis balls and cricket bats are strewn across the floor. You are
sitting at a small desk, and have the feeling that there is something you need
to do...

Still disoriented, you gaze down at your waist. Attached there is a rectangular
ID card emblazoned with the name, "Waqas Haider."

Suddenly, it all comes back to you. You are Br. Waqas, RISE Academy PE Teacher
and friend to all the students. You recall what you planned to do today: get
Dave's for the boys.

But first, you should check if you have enough free periods to get to Dave's
and back...
""")

check_schedule = Situation("""
You pull up the schedule on your phone and see that you have classes to teach
for the entire day.
""")

leave_without_schedule = Situation("""
You open the door and step outside your office into the lobby. You swiftly walk
through the gym and into the main school hallway. The school admin, Sr.
Basahat, is standing there. It's almost like she was waiting for you.

"Don't you have a class to teach?" she cries.

Reluctantly, you answer in the affirmative. The job-security-threatening stare
Sr. Basahat is giving you is evidence that the boys won't be getting Dave's
today.
""", game_over=True)

ignore_schedule = Situation("""
You decide to go to Dave's anyway, hoping that the repercussions of missing
your class won't be too devastating. Anticipating that Sr. Basahat, the school
admin, might be waiting for you in the hallway, you decide to slip out the side
entrance of the building and quickly run to your car.

You get into your sleek Tesla and punch in the address for Dave's Hot Chicken.
However, you don't think you have enough range.
""")

stay_at_school = Situation("""
Looks like the boys won't be getting Dave's today.
""", game_over=True)

take_tesla = Situation("""
You take a deep breath and make a prayer to God. Next thing you know, you're
flying down N First St with the car screeching warnings at you every few
seconds. "Fortune favors the bold," you think.

Unfortunately, you were too bold. About halfway there, you can almost see
Dave's in the distance, almost smell the spicy tenders in the air, when the car
grinds to a halt.
""")

take_minivan = Situation("""
You take a deep breath and make a prayer to God. Next thing you know, you're
flying down N First St with your heart beating loudly in your chest. "Forget
getting fired, I'll get arrested for this!" you think.

You pull into the parking lot and can almost smell the spicy tenders in the
air. A few minutes later, the Dave's has been acquired. You walk out of the
restaurant with bags of sliders and tenders in your hands, triumphant. You
can't help but smile as you pack the food into the trunk.

After a long journey, you arrive back in the school parking lot. As you walk
towards the entrance with the bags in your hands, out of the corner of your
eye, you see one of your students, Mohammad Abidi, prowling outside with a
desire for bloodshed in his eyes.

"I know you have Dave's, Br. Waqas," he cries. "And I will do anything to get
it. To get ALL of it!"

You realize your life is in danger.
""")

run = Situation("""
You begin to jog down N First St with your heart beating loudly in your chest.
You will do anything to get the boys some Dave's.

You glance at your watch. Time is running out, and you might not make it back
by lunchtime if you don't pick up the pace.
""")

admit_defeat = Situation("""
You fall to the ground, palms against the hot asphalt. You have failed the
boys. You have failed yourself. You are a man adrift in the open sea, with
nowhere to go but drown.
""", game_over=True)

run_slow = Situation("""
You decide to take your time and avoid tiring yourself out. A few minutes
later, you look at your watch and realize you might still make it in time.

You are almost enjoying the walk. Along the way, you even stop to admire the
scenery and greet people as you pass by. You arrive at the restaurant later
than planned, but still with time to spare.

A few minutes later, the Dave's has been acquired. You walk out of the
restaurant with bags of sliders and tenders in your hands, triumphant.

After a long journey, you arrive back in the school parking lot. As you walk
towards the entrance with the bags in your hands, out of the corner of your
eye, you see one of your students, Mohammad Abidi, prowling outside with a
desire for bloodshed in his eyes.

"I know you have Dave's, Br. Waqas," he cries. "And I will do anything to get
it. To get ALL of it!"

You realize your life is in danger.
""")

run_fast = Situation("""
Now you are running faster than an Olympic sprinter. At least, it feels like
you are. You think your heart might pop out of your chest. Your breaths are
heavy and frequent.

Suddenly, you feel light-headed. The world begins to spin and you fall to the
ground, palms against the hot asphalt. You cannot muster the strength to get
up.

You have failed the boys. You have failed yourself. You are a man adrift in the
open sea, with nowhere to go but drown.
""", game_over=True)

fight_mohammad = Situation("""
You step out in front of Mohammad. A brave decision, even by your standards.

Mohammad is foaming at the mouth and is staring daggers at the bags in your
hand.

"Daaaaaaves," he moans as he lunges at you. You step back, avoiding the attack.
Mohammad looks up. You won't beat him that easily. He tackles you with all his
body weight and you collapse to the ground.

The last thing you remember before you are knocked unconscious against the
concrete is Mohammad tearing apart the bags like someone high on cocaine
looking for his next fix.
""", game_over=True)

run_inside = Situation("""
You step out in front of Mohammad. Mohammad is foaming at the mouth and is
staring daggers at the bags in your hand. He begins to chase you down.

Once he has caught up, he lunges at you. You push him back with your foot as
you open the school's door. You quickly slip inside and lock it before Mohammad
can regain his composure.

Your breathing is hard and fast. But you seem to be OK, for the most part.

Victory is in sight. You have the Dave's, and the boys are around the corner in
the Student Hub. Unfortunately, you hear Sr. Basahat's voice boom across the
hall to your left.
""")

run_to_student_hub = Situation("""
You quickly round the corner into the hallway, but Sr. Basahat is much closer
than anticipated. She locks eyes with you. You are caught.

"Where have you been, Br. Waqas?" she asks with a threatening tone. "You missed
all your classes today!"

You begin to answer, "Uhhh--- I was sick."

She's not buying it.
""")

bathroom = Situation("""
You quickly round the corner and dash into the bathroom. Trying to stay as
quiet as possible, you can hear Sr. Basahat enter her office. The coast is
clear.

You run into the Student Hub where all the boys are eating lunch. "DAVES!" you
exclaim as you hold up the bags. The boys are ecstatic and begin to chant,
"DAVES! DAVES! DAVES!"

You look around you at the happiness you have created. You have been
successful.
""", game_won=True)

apologize = Situation("""
"Yeah, I went to Dave's to get some food for the boys," you say. "I know I
should have stayed and taught my classes. I'm sorry."

She gives you a stern look. She tells you that she understands where you're
coming from, but must enforce the rules with an iron fist.

She calls you into her office for a chat. You have failed. It looks like the
boys won't be getting Dave's anytime soon.
""", game_over=True)

argue = Situation("""
"Yeah, I went to Dave's to get some food for the boys," you say. "But it's for
a good reason. You know morale is incredibly low in the school; I just wanted
to cheer things up."

She gives you a stern look. She tells you that she understands where you're
coming from, but must enforce the rules with an iron fist.

She calls you into her office for a chat. You have failed. It looks like the
boys won't be getting Dave's anytime soon.
""", game_over=True)

bribe = Situation("""
You pull out a box from one of the bags. "I admit, I went to Dave's to get the
boys some food. I even got you some," you say. Her demeanor suddenly shifts as
soon as she sees this gesture of good will. She's still angry, but she lets you
go without reprimanding you.


You run into the Student Hub where all the boys are eating lunch. "DAVES!" you
exclaim as you hold up the bags. The boys are ecstatic and begin to chant,
"DAVES! DAVES! DAVES!"

You look around you at the happiness you have created. You have been
successful.
""", game_won=True)

office.add_choice(Choice("Check your schedule", check_schedule))
office.add_choice(Choice("Leave without checking your schedule", leave_without_schedule))

check_schedule.add_choice(Choice("Ignore the schedule", ignore_schedule))
check_schedule.add_choice(Choice("Stay at school", stay_at_school))

ignore_schedule.add_choice(Choice("Go anyway. Maybe you can make it?", take_tesla))
ignore_schedule.add_choice(Choice("Steal the school minivan", take_minivan))
ignore_schedule.add_choice(Choice("Run", run))

take_tesla.add_choice(Choice("Admit defeat", admit_defeat))
take_tesla.add_choice(Choice("Run", run))

run.add_choice(Choice("Take your time", run_slow))
run.add_choice(Choice("Speed up", run_fast))

take_minivan.add_choice(Choice("Fight Mohammad", fight_mohammad))
take_minivan.add_choice(Choice("Quickly run inside", run_inside))

run_slow.add_choice(Choice("Fight Mohammad", fight_mohammad))
run_slow.add_choice(Choice("Quickly run inside", run_inside))

run_inside.add_choice(Choice("Make the run for the Student Hub", run_to_student_hub))
run_inside.add_choice(Choice("Slip into the bathroom to avoid Sr. Basahat", bathroom))

run_to_student_hub.add_choice(Choice("Apologize", apologize))
run_to_student_hub.add_choice(Choice("Stand your ground", argue))
run_to_student_hub.add_choice(Choice("Bribe her with a chicken tender", bribe))
