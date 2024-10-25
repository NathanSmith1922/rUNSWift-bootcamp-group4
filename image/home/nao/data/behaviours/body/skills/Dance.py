from BehaviourTask import BehaviourTask
from body.skills.Walk import Walk
from body.skills.RaiseArm import RaiseArm

from util.Timer import Timer

class Dance(BehaviourTask):

	"""
	Description:
	A skill that can be used to test if the calculation for walking
	in a circle is done correct. The robot should walk in a circle
	of given radius, at given forward speed, facing forwards (along
	the tangent).
	"""

	def _initialise_sub_tasks(self):
		self._sub_tasks = {"Walk": Walk(self), "RaiseArm" : RaiseArm(self)}

	def _reset(self):
		self._current_sub_task = "Walk"
		self.has_finished_kick = False
		self.walk_timer = Timer(5000000).start()

	def _transition(self):
		if self._current_sub_task == "Walk" and self.walk_timer.finished(self.walk_timer):
			self._current_sub_task = "RaiseArm"
			self.walk_timer.restart(self.walk_timer)
		elif self._current_sub_task == "RaiseArm" and self.walk_timer.finished(self.walk_timer):
			self._current_sub_task = "RaiseArm"
			self.walk_timer.restart(self.walk_timer)

	def _tick(self):
		if self._current_sub_task == "Walk":
			self._tick_sub_task(forward=50)
		if self._current_sub_task == "RaiseHand":
			self._tick_sub_task()