from psychopy import core, visual, sound, event

class ToneGenerator:
    def __init__(self,num_trials_per_state=4,states=['Squeeze right hand','Red']):
        win = visual.Window([400,400])
        fixation = visual.TextStim(win, text='+')
        tone = sound.Sound('A')

        self.num_trials_per_state = num_trials_per_state
        self.num_blocks = len(states)
        self.states = states

        self.win = win
        self.fixation = fixation
        self.tone = tone
    
    def start_block(self,block_state):
        self.fixation.draw()
        message = f"Press the spacebar to start block.\n State: {block_state}."
        visual.TextStim(self.win, text=message,pos=(0,-.25)).draw()
        self.win.flip()

        event.waitKeys(keyList='space')
        core.wait(1.0)

    def play_tone(self):
        self.fixation.draw()
        self.win.flip()
        self.tone.play()
        core.wait(1.5)
        self.tone.stop()

    def run_block(self,block_num):
        block_state = self.states[block_num]
        self.start_block(block_state)
        for trial_num in range(self.num_trials_per_state):
            self.play_tone()
        
    def _end(self):
        self.win.close()
        core.quit()
    
    def run_experiment(self):
        for block_num in range(self.num_blocks):
            self.run_block(block_num)
        self._end()

toneGen = ToneGenerator()
toneGen.run_experiment()