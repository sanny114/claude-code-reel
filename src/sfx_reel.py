# Sound for reel.html. Times = 絵コンテ.md (120 BPM, beat 0.5 s).
import sys; sys.path.insert(0, "C:/Users/yuzuk/.claude/skills/motion-video/scripts")
from sfx import *
dry, wet = init(15.0)
F, C_, G, Am = CHORDS['F'], CHORDS['C'], CHORDS['G'], CHORDS['Am']
# 0-3: pad + cursor ticks + typing
put(wet, 0.0, pad([f/2 for f in F], 3.0, .25))
for b in (0.0, 0.5): put(dry, b, tick(1800, .5))
for i in range(11): put(dry, 1.0 + i*.125, key(.7), pan=(i%3-1)*.2)
put(dry, 1.75, riser(1.25, 200, 2400, .35))
# 3.0 enter: zoom-through
put(dry, 3.0, kick(1.3)); put(dry, 3.0, sub(.9)); put(dry, 2.9, whoosh(.45, 400, 9000, .6, -.5, .5))
put(dry, 3.45, blip(500, 1300, .5, .14))                     # mascot pops
put(dry, 3.5, kick(1.1)); put(wet, 3.5, stab(F, .6, .55)); put(dry, 3.5, crash(.35, 1.2))
# 4.0-9.0 tasks: kick + wipe on each head, backbeat hats
for i in range(5):
    t0 = 4.0 + i
    put(dry, t0, kick(1.0)); put(dry, t0 - .05, whoosh(.25, 800, 7000, .35, -.7, .7))
    put(dry, t0 + .5, clap(.35))
    for k in range(8): put(dry, t0 + k*.125, hat(.12 if k%2 else .06), pan=.3)
    put(dry, t0, bass([87.3, 110, 98, 130.8, 87.3][i], .4, .6))
for i in range(6): put(dry, 4.0 + i*.035, key(.4))            # request typing (fast)
for i in range(14): put(dry, 4.58 + i*.025, snap(.18), pan=[-.6, 0, .6][i%3])  # files into folders
for i in range(6): put(dry, 5.22 + i*.05, pluck([262, 294, 330, 392, 440, 523][i], .35, .3))  # bars
put(dry, 5.62, blip(700, 1600, .45, .12))                     # +32%
for i in range(8): put(dry, 6.3 + i*.04, key(.35))            # summary
put(dry, 6.5, snap(.5))
for k, t in enumerate((7.18, 7.28, 7.33, 7.38, 7.46, 7.52, 7.58)): put(dry, t, blip(900 - k*40, 350, .3, .08))  # web parts land
for i in range(8): put(dry, 8.2 + i*.03, key(.35))            # mail typing
put(dry, 8.62, pluck(784, .5, .5)); put(dry, 8.64, pluck(1047, .45, .6))   # check mark
# 9.0 tiles
put(dry, 9.0, kick(1.1)); put(dry, 9.0, sub(.7)); put(wet, 9.0, stab(C_, .8, .5))
for i in range(4): put(dry, 9.1 + i*.06, snap(.3), pan=-.6 + i*.4)
# 10-12 statement
put(dry, 10.0, kick(1.1)); put(wet, 10.0, stab(Am, .8, .45))
put(dry, 11.0, kick(1.2)); put(dry, 11.0, clap(.6)); put(wet, 11.0, stab(G, .8, .45))
for i in range(17): put(dry, 11.0 + i*.0625, tick(1200 + (i%2)*300, .15, .02), pan=-.8 + i*.1)  # footsteps
for k in range(4): put(dry, 10.0 + k*.25, hat(.08)); put(dry, 11.0 + k*.25, hat(.1))
# 12.0 collapse -> cursor
put(dry, 11.95, whoosh(.5, 9000, 300, .45, .6, -.2))
for i in range(13): put(dry, 12.5 + i*.0625, key(.5))
put(dry, 13.0, kick(1.0)); put(dry, 13.0, blip(1300, 500, .45, .16))  # mascot lands
put(wet, 13.0, pad(F, 2.0, .4)); put(dry, 13.0, sub(.5, 2.0))
for b in (13.5, 14.0, 14.5): put(dry, b, tick(1800, .3))
write("audio.wav")
