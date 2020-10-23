import time


class FpsTimer:

    def __init__(self, previous_time, fps):
        self.prev_time = previous_time
        self.framerate = fps
        self.framecounter = 0
        self.waitcounter = 0

    def endFrame(self):  # Wait untill the current frame ends for the given framerate
        curr_time = time.time()
        spf = 1 / self.framerate
        wait_time = self.prev_time + spf - curr_time
        self.prev_time += spf  # This prevents fps slowdown due to overhead

        self.framecounter += 1
        self.waitcounter += wait_time
        if self.framecounter == 60:
            self.framecounter = 0
            print("Frame usage: ", wait_time / 10, "%")

        if wait_time > 0:
            time.sleep(wait_time)
