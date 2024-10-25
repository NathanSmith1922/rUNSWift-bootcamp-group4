from BehaviourTask import BehaviourTask
from body.skills.FindBall import FindBall
from body.skills.Pass import Pass


class FindBallThenPass(BehaviourTask):
    """
    Description:
    Find the ball, and pass it to 
    another robot detected on the field 
    """

    def _initialise_sub_tasks(self):
        self._sub_tasks = {
            "FindBall": FindBall(self),
            "Pass": Pass(self),
        }

    def _reset(self):
        self._current_sub_task = "FindBall"

    def _transition(self):
        # If the current task is to find the ball
        if self._current_sub_task == "FindBall":
            # Transition to "Pass" once the ball has been located and approached
            if ballDistance() < 500:  # Check if robot is close enough to the ball
                self._current_sub_task = "Pass"
        
        # Once the ball has been passed, reset to FindBall
        elif self._current_sub_task == "Pass":
            if self._sub_tasks["Pass"].has_finished_kick:
                self._current_sub_task = "FindBall"


    def _tick(self):
        self._tick_sub_task()

