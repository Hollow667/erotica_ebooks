#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from util import *
from misc import *
from names import *
from people import *
from texttoimg import *

PromoHistoryQ = HistoryQ(2)

def GetTweet(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
	Generator = None
	GenType = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	#print("GetTweet() Generator Type is " + str(GenType))
	
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if not gen == None:
			Generator = gen
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)

		if not gen == None:
			Generator = gen
		
	return Generator

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets

class Generator():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def SetPriority(self, sText, List, iPriority):
		for x in range(iPriority):
			List.append(sText)
	
	def GetMaster(self, NotList = None, bNonBasic = True, bBasic = True, bGangs = True, bComplex = True):
		if NotList is None:
			NotList = []
			
		Masters = []
		
		sBMaster = self.MastersBasic.GetWord(NotList = NotList)
		sNBMaster = self.Masters.GetWord(NotList = NotList)
		sGang = self.MasterGangs.GetWord(NotList = NotList)

		if bNonBasic:		
			NotList.append(sNBMaster)
			# non-basic master, no adjs
			self.SetPriority(sNBMaster, Masters, 4)
			# ========================================

			# non-basic master, 1 reg adj
			sAdj = self.MasterAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sNBMaster, Masters, 3)
			# ========================================
			
			#non-basic master, 1 comp adj
			sAdj = self.MasterCompAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sNBMaster, Masters, 2)
			# ========================================

			#non-basic master, 1 reg adj & 1 comp adj
			sAdj1 = self.MasterAdjs.GetWord(NotList = NotList)
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sAdj1] + NotList)
			self.SetPriority(sAdj1 + " " + sAdj2 + " " + sNBMaster, Masters, 2)
			# ========================================

			if bComplex:
				#non-basic master, 2 comp adjs 
				sAdj1 = self.MasterAdjs.GetWord(NotList = NotList)
				sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sAdj1] + NotList)
				self.SetPriority(sAdj1 + " " + sAdj2 + " " + sNBMaster, Masters, 1)
				# ========================================
			
			NotList.pop()

		if bBasic:
			NotList.append(sBMaster)
			
			#basic master, 1 reg adj
			sAdj = self.MasterAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sBMaster, Masters, 4)
			# ========================================

			#basic master, 1 comp adj
			sAdj = self.MasterCompAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sBMaster, Masters, 3)
			# ========================================

			#basic master, 1 reg adj & 1 comp adj 
			sAdj1 = self.MasterAdjs.GetWord(NotList = NotList)
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sAdj1] + NotList)
			self.SetPriority(sAdj1 + " " + sAdj2 + " " + sBMaster, Masters, 2)
			# ========================================

			if bComplex:
				#basic master, 2 comp adjs 
				sAdj1 = self.MasterCompAdjs.GetWord(NotList = NotList)
				sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sAdj1] + NotList)
				self.SetPriority(sAdj1 + " " + sAdj2 + " " + sBMaster, Masters, 1)
				# ========================================
			
			NotList.pop()

		if bGangs:
			NotList.append(sGang)
		
			#gang, no adjs
			self.SetPriority(sGang, Masters, 3)
			# ========================================

			#gang, 1 reg adj 
			sAdj = self.MasterAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sGang, Masters, 2)
			# ========================================

			#gang, 1 comp adj
			sAdj = self.MasterCompAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sGang, Masters, 2)
			# ========================================

			#gang, 1 reg adj & 1 comp adj 
			sAdj1 = self.MasterAdjs.GetWord(NotList = NotList)
			sAdj2 = self.MasterCompAdjs.GetWord(NotList = [sAdj1] + NotList)
			self.SetPriority(sAdj1 + " " + sAdj2 + " " + sGang, Masters, 1)
			# ========================================
			
			NotList.pop()
	
		return Masters[randint(0, len(Masters) - 1)]
		
	def GetGirl(self, NotList = None, bNonBasic = True, bBasic = True, bComplex = True):
		sGirl = ""
		
		if NotList is None:
			NotList = []
		
		Girls = []
		
		sBGirl = self.GirlsBasic.GetWord(NotList = NotList)
		sNBGirl = self.Girls.GetWord(NotList = NotList)

		if bNonBasic:
			NotList.append(sNBGirl)
			
			# non-basic girl, no adjs
			self.SetPriority(sNBGirl, Girls, 4)
			# ========================================
			
			# non-basic girl, 1 reg adj
			self.SetPriority(self.GirlAdjs.GetWord(NotList = NotList) + " " + sNBGirl, Girls, 3)
			# ========================================

			# non-basic girl, 1 comp adj 
			sAdj = self.GirlCompAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sNBGirl, Girls, 3)
			# ========================================
			
			# non-basic girl, 1 reg and 1 comp adj 
			sAdj1 = self.GirlAdjs.GetWord(NotList = NotList)
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sAdj1] + NotList)
			self.SetPriority(sAdj1 + " " + sAdj2 + " " + sNBGirl, Girls, 2)
			# ========================================

			if bComplex:
				# non-basic girl, 2 comp adjs
				sAdj1 = self.GirlCompAdjs.GetWord(NotList = NotList)
				sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sAdj1] + NotList)
				self.SetPriority(sAdj1 + " " + sAdj2 + " " + sNBGirl, Girls, 1)
				# ========================================
			
			NotList.pop()

		if bBasic:
			NotList.append(sBGirl)
			
			# basic girl, 1 reg adj 
			sAdj = self.GirlAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sBGirl, Girls, 4)
			# ========================================

			# basic girl, 1 comp adj 
			sAdj = self.GirlCompAdjs.GetWord(NotList = NotList)
			self.SetPriority(sAdj + " " + sBGirl, Girls, 3)
			# ========================================

			# basic girl, 1 reg adj and 1 comp adj 
			sAdj1 = self.GirlAdjs.GetWord(NotList = NotList)
			sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sAdj1] + NotList)
			self.SetPriority(sAdj1 + " " + sAdj2 + " " + sBGirl, Girls, 3)
			# ========================================

			if bComplex:
				# basic girl, 2 comp adjs
				sAdj1 = self.GirlCompAdjs.GetWord(NotList = NotList)
				sAdj2 = self.GirlCompAdjs.GetWord(NotList = [sAdj1] + NotList)
				self.SetPriority(sAdj1 + " " + sAdj2 + " " + sBGirl, Girls, 1)
				# ========================================
			
			NotList.pop()
			
		return Girls[randint(0, len(Girls) - 1)]
		
	def _getFMs_(self):
		FMs = ""
		
		iRandLen = randint(4,10)
		for x in range(1, iRandLen):
			iRandChoice = randint(1,3)
			if iRandChoice == 1:
				FMs += "F"
			else:
				FMs += "M"
				
		if "M" not in FMs:
			FMs += "M"
		elif "F" not in FMs:
			FMs += "F"
		
		return FMs
	
	def GenerateTweet(self):
		self.Girls = BookGirls()
		self.GirlsBasic = BookGirlsBasic()
		self.GirlAdjs = BookGirlAdjs()
		self.GirlCompAdjs = BookGirlCompAdjs()
		self.Masters = BookMasters()
		self.MastersBasic = BookMastersBasic()
		self.MasterGangs = BookMasterGangs()
		self.MasterAdjs = BookMasterAdjs()
		self.MasterCompAdjs = BookMasterCompAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		
		return ""
		
class GeneratorPromo(Generator):
	ID = 0
	Priority = 0
	Type = GeneratorType.Promo
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#sTweet = "Blue Diamond: \U0001F539 Eggplant: \U0001F346 Fire: \U0001F525 Laughing: \U0001F923 Robot: \U0001F916 Green Heart: \U0001F49A Blue Heart: \U0001F499 Purple Heart: \U0001F49C No one under 18: \U0001F51E Winking kiss face: \U0001F618 Star: \U00002B50"

		iRand = randint(1,7)
		while not PromoHistoryQ.PushToHistoryQ(iRand):
			iRand = randint(1,7)

		if iRand == 1:
			sTweet = "Reply to " + WordList(["one of my tweets", "an @bot_lust tweet", "a Flaming Lust Bot tweet"]).GetWord() + " for a fun surprise! " + GetEmoji()
			sTweet += "\n\n\U0001F539Reply \"#book\" and I'll respond with a made-up smutty book title."
			sTweet += "\n\U0001F539Reply \"#lovescene\" to get your own custom love scene!"
		elif iRand == 2:
			sTweet = "Tell your family, friends and lovers to follow " + WordList(["@bot_lust", "Flaming Lust Bot", "me", "this bot"]).GetWord() + " for all the steamy, sweaty, silly action!\n" + GetEmoji(randint(1,3))
		elif iRand == 3:
			sTweet = WordList(["@bot_lust", "Flaming Lust Bot", "this bot"]).GetWord() + " is very naughty, and NOT appropriate for anyone under 18! \U0001F51E\n\nThat includes you, " + WordList(["kid who is hiding their phone behind their math book while they check twitter", str(randint(6,11)) + "th grader who is supposed to be doing homework", str(randint(6,11)) + "th grader who is supposed to be reading"]).GetWord() + "!"
			if CoinFlip(): 
				sTweet += " \U0001F928"
		elif iRand == 4:
			sTweet = "I am a twitter bot\U0001F916 designed to automatically generate " + WordList(["hot", "sexy", "naughty", "steamy"]).GetWord() + "\U0001F525, " + WordList(["filthy", "dirty"]).GetWord() + "\U0001F346, and " + WordList(["funny", "hilarious", "ridiculous", "silly"]).GetWord() + "\U0001F923 scenes from the world's worst smutty romance novel!\n\nReply to one of my tweets " + WordList(["and get a surprise!", "if you want more.", "if you're impatient for my next terrible love scene!"]).GetWord()
		elif iRand == 5:
			if CoinFlip():
				sTweet = "Full disclosure: "
			sTweet += "I am a bot\U0001F916!\n\nBut not the Russian kind of bot, the " + WordList(["funny", "sexy", "naughty", "silly", "dirty"]).GetWord() + " kind of bot!" 
			if CoinFlip():
				sTweet += " " + GetEmoji()
			if CoinFlip():
				sTweet += "\n#botlife #twitterbot"
		elif iRand == 6:
			sTweet = "Look what " + WordList(["my followers are", "people are ", "other twitter users are", "the internet is"]).GetWord() + " saying:\n\n\U00002B50'I am hooked on this ridiculous account!'\n\U00002B50'The stuff this bot comes up with is hysterical. XD'\n\U00002B50'[S]imultaneously hilarious, nauseating, and inspiring'\n\n" + WordList(["Thank you!", "Thanks!", "Thank you all!", "Big bot love to everyone!"]).GetWord() 
			sTweet += " " + GetEmoji(randint(1,3))
		else:
			sTweet = WordList(["I love you", "You're the best", "Big Bot Love", "I \U00002764 you"]).GetWord() + ", followers!"
			if CoinFlip():
				sTweet = "*" + sTweet + "*"
			sTweet += "\n\n" + GetHeartEmoji(randint(1,5))
			
		return sTweet
		
class Generator1(Generator):
	# Blackmailed by the Billionaire Mountain Man 
	ID = 1
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.VerbsBy.GetWord() + " by the " + self.GetMaster()
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord() + " by the " + self.GetMaster()
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = self.VerbsTo.GetWord() + " to the " + self.GetMaster(NotList = ["BDSM"])
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_() + " Romance", "A BDSM Romance", "A Taboo Affair", "A Forbidden Romance", "A Secret Affair", "A " + self._getFMs_() + " Encounter", "An Erotic Encounter"]).GetWord()
		
		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to the " + self.GetMaster()
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "The " + self.GetMaster(bComplex = False, bNonBasic = False, bGangs = False, NotList = ["BDSM"]) + "'s " + self.GetGirl(NotList = ["BDSM"])
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM Romance"
			else:
				sTweet += ":\nA Hot Ménage"
		
		return sTweet
		
class Generator6(Generator):
	# Seduced in the Bed of the Billionaire	
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", "Gifted", "Pledged"]
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord(NotList = NotList) + " in the Bed of the " + self.GetMaster(bGangs = False)
		else:
			sTweet = self.VerbsBy.GetWord(NotList = NotList) + " in the Bed of the " + self.GetMaster(bGangs = False)
		
		return sTweet
		
class Generator7(Generator):
	# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl(bComplex = False) + ", The " + self.GetMaster(bComplex = False, bGangs = False) + ", & The " + self.GetMaster() + ":\n"
		if CoinFlip():
			sTweet += "A Hot Ménage"
		else:
			sTweet += "A " + self._getFMs_() + " Romance"
		
		return sTweet

class Generator8(Generator):
	# My Boyfriend is a Secret Daddy Dom 
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#sTweet = "The " + self.GetGirl() + "'s " + self.GetMaster()
		sTweet = "My " + WordList(["Boyfriend", "Hot Date", "Fiancé"]).GetWord() + " is a " + self.GetMaster(NotList = ["Boyfriend", "Hot Date", "Fiancé"], bGangs = False)
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\n" + AddArticles(self.GetGirl()) + " Romance"
			else:
				sTweet += ":\n" + AddArticles(self.GetGirl()) + " Adventure"
		else:
			sTweet += "!"
			
		return sTweet
		
class Generator9(Generator):
	# The Secretary and the Space Werewolf 
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "The " + self.GetGirl(NotList = ["BDSM"]) + " & the " + self.GetMaster(NotList = ["BDSM"])
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM Romance"
			else:
				sTweet += ":\nA " + self._getFMs_() + " Romance"
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "Baby for the " + self.GetMaster() 
		if CoinFlip():
			sTweet += ":\nA " + self._getFMs_() + " Romance"
		
		return sTweet
		
class Generator11(Generator):
	# The Millionaire Sherrif's Virgin
	ID = 11
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetMaster() + "'s " + self.GetGirl(bComplex = False)

		return sTweet
		
class Generator12(Generator):
	# Babysitter to the Billionaire Uniporn
	ID = 12
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl(bComplex = False) + " to the " + self.GetMaster()
		
		return sTweet
		
class Generator13(Generator):	
	# Babysitter for the Billionaire Uniporn
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl() + " for the " + self.GetMaster()
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_() + " Adventure","A BDSM Romance","A Forbidden Romance"]).GetWord()
		
		return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		if CoinFlip():
			sTweet = "The " + self.GetGirl() + "'s Gang Bang:\nA " + self._getFMs_() + " Romance"
		else:
			sTweet = "Gang-Banged by the " + self.GetMaster(bBasic = False, bNonBasic = False)
			if CoinFlip():
				sTweet += ":\nAn " + self._getFMs_() + " Adventure"
		
		return sTweet
		
class Generator15(Generator):
	# The Small-Town Virgin's First Porno
	ID = 15
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl(NotList = ["Porn Star"], bComplex = False) + "'s First Porno"
		if CoinFlip():
			sTweet += ":\nAn " + self._getFMs_() + " Adventure"

		return sTweet
		
class Generator16(Generator):
	# The Small-Town Virgin's First Time
		
	ID = 16
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "The " + self.GetGirl(bComplex = False, NotList = ["Slut", "Whore", "Escort", "Call-Girl", "Dominatrix", "Promiscuous", "Pregnant", "Mom", "Sex", "Kinky", "Bimbo", "MILF", "Concubine", "Wife", "Porn Star", "Divorced"]) + "'s First Time"
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_() + " Romance", "A BDSM Romance", "A Secret Romance"]).GetWord()

		return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Duke 
	ID = 17
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Subtitles = []
		
		sTweet = self.VerbsBy.GetWord() + ":\n"
		
		Subtitles.append("The " + self.GetGirl(bComplex = False) + " & The " + self.GetMaster(bComplex = False))
		Subtitles.append("The " + self.GetGirl(bComplex = False) + " & The " + self.GetMaster(bBasic = False, bNonBasic = False))
		Subtitles.append(self.GetGirl(bComplex = False) + " for the " + self.GetMaster())
		Subtitles.append("The " + self.GetMaster(bComplex = False) + "'s " + self.GetGirl())
		Subtitles.append(AddArticles(self.GetGirl()) + " Romance")
		
		sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet += "\"" + WordList(["S@*#!", "Oh No!", "Uh Oh!", "Whoops!", "WTF?!?", "Oh F*@%!"]).GetWord() + " My " + self.GetGirl(NotList = ["Porn Star", "Sex", "Lesbian", "Bad Girl", "Call-Girl", "Stripper", "Escort", "Whore", "Slut", "Promiscuous", "Hotwife", "Dominatrix", "BDSM", "Anal"]) + " Is " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", "An Anal Porn Star", "An Erotic Model"]).GetWord() + "!\""
		
		return sTweet
		
class Generator19(Generator):
	# Full Frontal for the Shy Amish Virgin: A BDSM Romance
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			sTweet = "Full Frontal Nudity for the " + self.GetGirl(NotList = ["Escort", "Call-Girl", "Dominatrix", "Kinky", "Porn Star", "BDSM", "Submissive", "Naked", "Nude", "Nudist"])
		else:
			sTweet = WordList(["Naked in Public", "Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["For The", "For My", "By The", "By My"]).GetWord() + " " + self.GetMaster()
		
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_() + " Adventure", "A BDSM Adventure", "A Taboo Affair", "A Forbidden Affair", "A Secret Affair", "A Submissive Romance"]).GetWord()
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
		sTweet = "\"I Was " + sVerbBy
		if not "in public" in sVerbBy.lower():
			sTweet += " By "
			if CoinFlip():
				sTweet += AddArticles(self.GetMaster(bGangs = False))
			else:
				sTweet += "The " + self.GetMaster(bBasic = False, bNonBasic = False)
		sTweet += ", And I Liked It\""

		return sTweet
		
class Generator21(Generator):
	# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
	ID = 21
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.VerbsBy.GetWord()  + " by "
		sTweet += "the " + self.GetMaster(bComplex = False) + ":\nA " + self.GetGirl(bComplex = False) + " Story"
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo MILF: A Lesbian Love Story 
	ID = 22
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = WordList(["The " + self.GetGirl(bComplex = False) + " and the " + self.GetGirl(bComplex = False), "The " + self.GetGirl() + " and the " + self.GetGirl(bComplex = False), "The " + self.GetGirl(bComplex = False) + " and the " + self.GetGirl()]).GetWord()
		if CoinFlip():
			sTweet += ":\n" + WordList(["A Lesbian Love Story","A Secret Lesbian Affair","A Taboo Lesbian Affair","A Forbidden Love Story", "A Lesbian Romance"]).GetWord()
		
		return sTweet
		
class Generator23(Generator):
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	# The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
	ID = 23
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("The " + self.GetMaster(bComplex = False, bGangs = False) + " and the " + self.GetMaster(bComplex = False, bGangs = False))
		GayTitles.append("The " + self.GetMaster(bGangs = False) + " and the " + self.GetMaster(bComplex = False, bGangs = False)) 
		GayTitles.append("The " + self.GetMaster(bComplex = False, bGangs = False) + " and the Gay " + self.GetMaster(bGangs = False))
		GayTitles.append(sHisName + " and the Gay " + self.GetMaster())
		GayTitles.append("Pounded In The Butt By My " + self.GetMaster())
		GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By The " + self.GetMaster())
		GayTitles.append(sHisName + " and the " + WordList(["Well-Hung", "Well-Endowed"]).GetWord() + " " + self.GetMaster(bComplex = False, bGangs = False, NotList = ["Well-Hung", "Well-Endowed"]))
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay Love Story","A Secret Gay Affair","A Taboo Gay Affair","A Forbidden Love Story", "A Gay Romance", "An MM Romance", "An MM Love Story"]).GetWord()
		
		return sTweet
		
class Generator24(Generator):
	# Deflowered Live on the Internet: An Amish Futa Princess Experience 
	ID = 24
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "Deflowered Live"
		if CoinFlip():
			sTweet += "! "
		else:
			if CoinFlip():
				sTweet += " on the Interet:\n"
			else:
				sTweet += " on Television:\n"
		sTweet += AddArticles(self.GetGirl(NotList = ["Escort", "Call-Girl", "Dominatrix", "Pregnant", "Mom", "MILF", "Concubine", "Wife", "Porn Star", "Divorced"])) + " Experience"

		return sTweet
		
class Generator25(Generator):
	# Here Cums The Bride: The Porn Star Pope & The Bi-Curious Christian Milk Maid 
	# ---!!! NEEDS WORK !!!---
	ID = 25
	Priority = 1
	Type = GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "Here Cums The Bride:\nThe " + self.GetMaster(bComplex = False) + " & The " + self.GetGirl(bComplex = False)
		
		return sTweet
		
class Generator26(Generator):
	# Hotwife for Daddy: A BDSM Romance 
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.GetGirl() + " for Daddy:\n"
		sTweet += WordList(["A BDSM Romance","An " + self._getFMs_() + " Adventure", "A Taboo Romance", "A Forbidden Affair", "A Forbidden Love", "A Taboo Gang-Bang", "A Naughty Adventure"]).GetWord()
		
		return sTweet
		
class Generator27(Generator):
	ID = 27
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "The " + self.GetGirl(NotList = ["Nude", "Naked", "Nudist", "Latex", "Leather"]) + " Wore " + WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "A Strap-On"]).GetWord() + ":\n"
		sTweet += WordList(["A FemDom Adventure", "A Dominatrix Adventure", "A BDSM Romance", "A Cuckold Experience"]).GetWord()

		return sTweet

class Generator28(Generator):
	ID = 28
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "Cuckolded By My " + self.GetGirl()
		
		return sTweet
		
# class Generator56(Generator):
	# ID = 56
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator57(Generator):
	# ID = 57
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator58(Generator):
	# ID = 58
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator59(Generator):
	# ID = 59
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
def GetImgTweetText(gen):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	TweetText = []
	BookSeller = BookSellers()
	Hashtag = Hashtags()
	SexyAdj = SexyAdjs()
	
	sText = "Coming soon on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================

	sText = "Available soon on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Look for this " + SexyAdj.GetWord() + " ebook on " + BookSeller.GetWord()  
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Watch for this " + SexyAdj.GetWord() + " read on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Available soon to discerning readers on " + BookSeller.GetWord() 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "My Patreon supporters get access to all my " + SexyAdj.GetWord() + " reads!"
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Reply to this tweet and " 
	if CoinFlip():
		sText += "I'll tweet a randomly-generated erotica ebook title @ you!"
	else:
		sText += "get a custom erotic ebook title of your very own in response!"
	sText += " " + GetEmoji()
	for _ in range(2):
		TweetText.append(sText)
	#=============================

	# it seems that adding any kind of hashtag at all to a bot may lead to shadowbans. so for now I'm not using this.
	# if CoinFlip():
		# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	# else:
	sText = TweetText[randint(0, len(TweetText) - 1)] 
	while IsTweetTooLong(sText):
		sText = TweetText[randint(0, len(TweetText) - 1)] 
	
	return sText 
				
class GeneratorSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in Generator.__subclasses__():
			item = subclass()
			for x in range(0, item.Priority):
				self.GeneratorList.append([item.ID, item])
			
	def RandomGenerator(self, bAllowPromo = True, Type = None):
		Generator = None
		AllowedTypes = []
		
		if not Type is None:
			AllowedTypes = [Type] 
		else:
			AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(GeneratorType.Promo)
			
		#print("RandomGenerator() Allowed types: " + str(AllowedTypes))
		if len(self.GeneratorList) > 0:

			Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
			while not Generator.Type in AllowedTypes:
				Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
				
		return Generator 
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		