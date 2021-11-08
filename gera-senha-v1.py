import array
import os
import math
import sys
import time
import string
from hashlib import md5


def fmd():
		t=([])  #sera a string com a combinacao de 4 digitos
		r="abcdefghijklmnopoqrstuxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789!@#$%&*()_-+=[]{}?/\|><"
		for a1 in range (0,85): #inicio do laco para gerar a senha de 4 digitos
			x1 = r[a1]
			for a2 in range (0,85):
				x2 = r[a2]
				for a3 in range (0,85):
					x3 = r[a3]
					for a4 in range (0,85): #fim do laco para gerar a senha de 4 digitos
						x4 = r[a4]
						t=x1+x2+x3+x4 #combinacao gerada
						print(t)
fmd()
