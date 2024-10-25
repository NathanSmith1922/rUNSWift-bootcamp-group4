import robot
from importlib import import_module

from BehaviourTask import BehaviourTask
from body.skills.FindBallThenPass import FindBallThenPass

class FieldPlayer(BehaviourTask):
    def _initialise_sub_tasks(self):
        self._sub_tasks = {
            "FindBallThenPass": FindBallThenPass(self),
        }

    def _reset(self):
        self._current_sub_task = "FindBallThenPass"

    def _tick(self):
        self._tick_sub_task()


    



