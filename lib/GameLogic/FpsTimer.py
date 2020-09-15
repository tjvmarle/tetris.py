import time


class FpsTimer:
    prev_time = time.time()
    framerate = 60

    def __init__(self, previous_time, fps):
        self.prev_time = previous_time
        self.framerate = fps

    def endFrame(self):  # Wait untill the current frame end for the given framerate
        curr_time = time.time()
        spf = 1 / self.framerate
        wait_time = self.prev_time + spf - curr_time
        self.prev_time += spf  # This prevents fps slowdown due to overhead
        print("Frame usage:", (1 - wait_time / spf) * 100, "%")

        if wait_time > 0:
            time.sleep(wait_time)
