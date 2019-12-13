#Enigma Simulator By Sumit Uttam


# A function for shifting list
def shift(l, n):
	return l[n:] + l[:n]

# Class Representing The Cogs	
class cog:
	def create(self,rotorPattern):
		self.transformation=rotorPattern
		return 
	def passthrough(self,i):                    
		return self.transformation[i]
	def passthroughrev(self,i):
		return self.transformation.index(i)
	def rotate(self):
		self.transformation=shift(self.transformation, 1)
	def setcog(self,a):
		self.transformation=a


class enigma:	
	def __init__(self, noCogs,printspecialchars,rotorPatterns):
		self.printspecialchars=printspecialchars
		self.noCogs=noCogs
		self.cogs=[]
		self.oCogs=[]
		
		for i in range(0,self.noCogs):
			self.cogs.append(cog())
			self.cogs[i].create(rotorPatterns[i])
			self.oCogs.append(self.cogs[i].transformation)
	
		self.reflector=rotorPatterns[i+1]

	def print_setup(self): # To print the enigma setup for debugging/replication
		print ("Enigma Setup:\nCogs: ",self.noCogs,"\nCog arrangement:")
		for i in range(0,self.noCogs):
			print (self.cogs[i].transformation)
		print ("Reflector arrangement:\n",self.reflector,"\n")
		
	def reset(self):
		for i in range(0,self.noCogs):
			self.cogs[i].setcog(self.oCogs[i])
			
	def encode(self,text):
		ln=0
		cipherText=str()
		for l in text.lower():
			num=ord(l)%97
			if (num>25 or num<0):
				if (self.printspecialchars):
					cipherText+=l 
				else:
					pass
			else:
				ln+=1
				for i in range(0,self.noCogs):
					num=self.cogs[i].passthrough(num)
					
				num=self.reflector[num]
				
				for i in range(0,self.noCogs):
					num=self.cogs[self.noCogs-i-1].passthroughrev(num)
				cipherText+=""+chr(97+num)
				
				for i in range(0,self.noCogs):
					if ( ln % ((i*6)+1) == 0 ):
						self.cogs[i].rotate()
		return cipherText.upper()

