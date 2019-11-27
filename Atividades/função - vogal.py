def vogal(letra):
	v = 0
	c = 0
    
	if letra == "a":
		v = 1
	else:
		if letra == "e":
			v = 1
		else:
			if letra == "i":
				v = 1
			else:
				if letra == "o":
					v = 1
				else:
					if letra == "u":
						v = 1
					else:
						if letra == "A":
							v = 1
						else:
							if letra == "E":
								v = 1
							else:
								if letra == "I":
									v = 1
								else:
									if letra == "O":
										v = 1
									else:
										if letra == "U":
											v = 1
										else:
											c = 1
    
	if v == 1:
		return True
	else:
		return False