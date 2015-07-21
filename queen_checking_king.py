def isCheck(Kp, Qp):
	deltaX = Qp[0] - Kp[0]
	deltaY = Qp[1] - Kp[1]

	if (Qp[0] == Kp[0]) or (Qp[1] == Kp[1]) or (abs(deltaX) == abs(deltaY)):
		return 'Check'