#!/usr/bin/python3.6
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
		#self.Girls = BookGirls()
		#self.GirlsBasic = BookGirlsBasic()
		#self.GirlAdjs = BookGirlAdjs()
		#self.GirlCompAdjs = BookGirlCompAdjs()
		#self.Masters = BookMasters()
		#self.MastersBasic = BookMastersBasic()
		#self.MasterGangs = BookMasterGangs()
		#self.MasterAdjs = BookMasterAdjs()
		#self.MasterCompAdjs = BookMasterCompAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()
		self.Gerunds = BookGerunds()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		self.SubtitleCoda = SubtitleCoda()
		
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
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(bAddArticle = True)
	
		sTweet = self.VerbsBy.GetWord() + " By\n" + Master.Desc
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace"]) + " by\n" + Master.Desc
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(bAddArticle = True, sPosArticle = "My")
			
		sTweet = self.VerbsTo.GetWord() + " To " + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "An Erotic"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 2
	
	Master = MaleChar()
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ['BDSM'])
		Master = MaleChar(iNumMaxCBits = 3, NotList = ['BDSM'], bAllowGang = False)
			
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM " + self.SubtitleCoda.GetWord()
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
		
		NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", "Gifted", "Pledged", "Bed", "Sex Dungeon"]
		
		Master = MaleChar(bAllowGang = False, NotList = NotList, bAddArticle = True)
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		else:
			sTweet = self.VerbsBy.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		
		return sTweet
		
class Generator7(Generator):
	# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master1 = MaleChar(iNumMaxCBits = 2, bAllowGang = False)
		Master2 = MaleChar(bAddArticle = True)
		Girl = FemaleChar(iNumMaxCBits = 2)
		sTweet = "The " + Girl.Desc + ",\nThe " + Master1.Desc + ",\n& " + Master2.Desc + ":\n"
		if CoinFlip():
			sTweet += "A Hot Ménage"
		else:
			sTweet += "A " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator8(Generator):
	# My Boyfriend is a Secret Daddy Dom 
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(bAllowGang = False, NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single"])
		sTweet = "My " + WordList(["Boyfriend", "Hot Date", "Fiancé", "Blind Date", "Kidnapper"]).GetWord() + " is a\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + AddArticles(Girl.Desc) + " " + self.SubtitleCoda.GetWord()
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
		
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = ["BDSM"])
		Master = MaleChar(iNumMaxCBits = 3, NotList = ["BDSM"])
		
		sTweet = "The " + Girl.Desc + "\nand\nThe " + Master.Desc 
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM " + self.SubtitleCoda.GetWord()
			else:
				sTweet += ":\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(bAddArticle = True)

		sTweet = "Baby For " + Master.Desc
		if CoinFlip():
			sTweet += ":\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator11(Generator):
	# The Millionaire Sherrif's Virgin
	ID = 11
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		Master = MaleChar()
		
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc

		return sTweet
		
class Generator12(Generator):
	# Babysitter to the Billionaire Uniporn
	ID = 12
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		Master = MaleChar(bAddArticle = True)
		
		sTweet = Girl.Desc + "\nto\n" + Master.Desc
		
		return sTweet
		
class Generator13(Generator):	
	# Babysitter for the Billionaire Uniporn
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		Master = MaleChar(bAddArticle = True)
		
		sTweet = Girl.Desc + "\nfor\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(),"A BDSM","A Forbidden"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, bAddArticle = True)
		MasterGang = MaleGangChar()

		if CoinFlip():
			sTweet = Girl.Desc + "'s\nGang Bang:\nA " + self._getFMs_() + " Romance"
		else:
			if CoinFlip():
				sTweet = "Gang-Banged By\nThe " + MasterGang.Desc
			else:
				sTweet = "Shared By\nThe " + MasterGang.Desc
			if CoinFlip():
				sTweet += ":\nAn " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator15(Generator):
	# The Small-Town Virgin's First Porno
	ID = 15
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True)
		
		sTweet = Girl.Desc + "'s\nFirst Porno"
		if CoinFlip():
			sTweet += ":\nAn " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator16(Generator):
	# The Small-Town Virgin's First Time
		
	ID = 16
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["MILF", "Concubine", "Wife", "Pregnant", "Mom", "Sex", "Divorced"], bAddArticle = True)

		sTweet = Girl.Desc + "'s\nFirst Time"
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Secret", "An S&M", "A Rough Sex", "An Anal"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Duke 
	ID = 17
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Subtitles = []
		
		Master = MaleChar(iNumMaxCBits = 3)
		Gang = MaleGangChar()
		
		sTweet = self.VerbsBy.GetWord() + ":\n"
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Master.Desc)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Gang.Desc)
		Subtitles.append(Girl.Desc + "\nfor the\n" + Master.Desc)
		Girl = FemaleChar()
		Subtitles.append("The " + Master.Desc + "'s\n" + Girl.Desc)
		Subtitles.append(AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord())
		
		sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Sex", "Lesbian","BDSM", "Anal", "MILF"], iNumMaxCBits = 3)
		sTweet += "\"" + WordList(["S@*#!", "Oh No!", "Uh Oh!", "Whoops!", "WTF?!?", "Oh F*@%!"]).GetWord() + " " 
		sTweet += "My\n" + Girl.Desc + "\nIs " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", "An Anal Porn Star", "An Erotic Model", "A Fetish Model"]).GetWord() + "!\""
		
		return sTweet
		
class Generator19(Generator):
	# Full Frontal for the Shy Amish Virgin: A BDSM Romance
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Naked", "Nude", "Nudist"], bAddArticle = True)
		Master = MaleChar()
		
		if CoinFlip():
			sTweet = "Full Frontal Nudity for\n" + Girl.Desc
		else:
			if CoinFlip():
				sTweet = WordList(["Naked in Public", "Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["For\nThe", "For\nMy"]).GetWord() + " " + Master.Desc
			else:
				sTweet = WordList(["Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["By\nThe", "By\nMy"]).GetWord() + " " + Master.Desc
		
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "A Submissive"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Master = MaleChar(bAllowGang = False, bAddArticle = True)
		Gang = MaleGangChar(bAddArticle = True)
		
		sTweet = ""

		sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
		sTweet = "\"I Was " + sVerbBy
		if not "in public" in sVerbBy.lower():
			sTweet += " By\n"
			if CoinFlip():
				sTweet += Master.Desc
			else:
				sTweet += Gang.Desc
		sTweet += ",\nAnd I Liked It\""

		return sTweet
		
class Generator21(Generator):
	# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
	ID = 21
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = self.VerbsBy.GetWord()  + " By\n"
		sTweet += Master.Desc + ":\nA " + Girl.Desc + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
	ID = 22
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlGood = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good)
		GirlLes = LesbianChar()
		GirlBad = LesbianChar(Type = GirlType.Bad)

		
		if CoinFlip():
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlLes.Desc
		else:
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlBad.Desc
		sTweet += ":\n" + WordList(["A Lesbian","A Secret Lesbian","A Taboo Lesbian","A Forbidden",  "An FF",]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator23(Generator):
	# The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
	ID = 23
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar(iNumMaxCBits = 2).Desc)
		GayTitles.append("The " + GayChar(iNumMaxCBits = 2).Desc + "\nand\nThe " + GayChar().Desc) 
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + GayChar().Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret Gay","A Taboo","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator24(Generator):
	# Deflowered Live on the Internet: An Amish Futa Princess Experience 
	ID = 24
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Pregnant", "Mom", "MILF", "Concubine", "Wife", "Divorced"])
		
		sTweet = "Deflowered Live"
		if CoinFlip():
			sTweet += "!\n"
		else:
			if CoinFlip():
				sTweet += " on the Interet:\n"
			else:
				sTweet += " on Television:\n"
		sTweet += AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord()
		return sTweet
		
class Generator25(Generator):
	# Greg Gets Pounded In The Butt By The Motorcycle Gang
	ID = 25
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("Pounded In The Butt By\nThe Gay " + MaleGangChar().Desc)
		GayTitles.append("Pounded In The Butt By\n" + GayChar(bAddArticle = True).Desc)
		GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + WordList(["Well-Hung", "Well-Endowed"]).GetWord() + " " + GayChar(iNumMaxCBits = 2, NotList = ["Well-Hung", "Well-Endowed"]).Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret","A Taboo Gay","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator26(Generator):
	# Hotwife for Daddy: A BDSM Romance 
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		
		sTweet = AddArticles(Girl.Desc) + "\nFor Daddy:\n"
		sTweet += WordList(["A BDSM","An " + self._getFMs_() + "", "A Taboo", "A Forbidden", "A Forbidden", "A Naughty"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator27(Generator):
	# The Shy Lesbian Gymnast Wore Black
	ID = 27
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"], bAddArticle = True)
		
		sTweet = Girl.Desc + "\nWore " + WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "A Strap-On"]).GetWord() + ":\n"
		sTweet += "A " + WordList(["FemDom", "Dominatrix", "BDSM", "Cuckold"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet

class Generator28(Generator):
	#Cuckolded By My Nudist Babysitter
	ID = 28
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		
		sTweet = "Cuckolded By My\n" + Girl.Desc 
		
		return sTweet
		
class Generator29(Generator):
	# Blackmailing My Step-Dad's Busty Ballerina
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ["Girlfriend", "Mom", "Dad" "Sister"])
		
		sTweet = WordList(["Dating", "Sleeping With", "Blackmailing", "Secretly Dating", "Sharing", "Watching", "Filming", "Claiming", "Spanking", "Tying Up", "Dominating", "Exposing", "Undressing", "Hypnotizing", "Impregnating", "Owning", "Punishing", "Spanking", "Paddling", "Training", "Pleasuring"]).GetWord() + " "
		sTweet += "My " + WordList(["Father's", "Dad's", "Step-Dad's", "Boyfriend's", "Best Friend's", "Neighbor's", "Boss's", "Son's", "Step-Son's"]).GetWord() + "\n"
		sTweet += Girl.Desc

		return sTweet
		
class Generator30(Generator):
	# Hot Ménage a Trois: Dick and Lily and The Well-Hung Bodyguard Sumo-Wrestler
	ID = 30
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName1 = NamesMale().FirstName()
		sHisName2 = NamesMale().FirstName()
		sHerName1 = NamesFemale().FirstName()
		sHerName2 = NamesFemale().FirstName()
		sLastName = LastNames().GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		Lesbo = LesbianChar(iNumMaxCBits = 3)
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
		Gay = GayChar(iNumMaxCBits = 3)
		
		Menages = []
		
		sTweet = SexyAdjs().GetWord().capitalize() + " " + WordList(["Ménage", "Ménage a Trois", "Threesome", "Three-Way"]).GetWord() + ":\n"
		
		Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Girl.Desc)
		Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Master.Desc)
		Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Lesbo.Desc)
		Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Master.Desc)
		Menages.append(sHisName1 + " and " + sHisName2 + "\nand\nthe " + Gay.Desc)
		Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Girl.Desc)
		Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Master.Desc)
		
		sTweet += Menages[randint(0, len(Menages) -1)]

		return sTweet
		
class Generator31(Generator):
	#Wanton & Willing: My Naked Lesbian Futa Princess
	ID = 31
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ListAdjs = WordList(misc.AttitudeFemale().List + misc.PhysCharFemale().List)
		sAdj1 = ListAdjs.GetWord()
		sAdj2 = ListAdjs.GetWord(NotList = [sAdj1])
		sHerName = NamesFemale().FirstName()
		
		sTweet = sAdj1 + " & " + sAdj2 + ":\n"
		
		if CoinFlip():
			Girl = FemaleChar(iNumMinCBits = 2)
			sTweet += "My " + Girl.Desc
		else:
			Girl = FemaleChar()
			sTweet += sHerName + " the " + Girl.Desc

		return sTweet
		
class Generator32(Generator):
	ID = 32
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		#print(misc.RelateMale().List + misc.MaritalStatusMale().List)
		if CoinFlip():
			Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ['Single', 'Man', 'Dad', 'Father', 'Brother', 'Son'], bAllowMaritalStatus = False, bAllowRelate = False)
			if Master.Desc[-3:] == "Man":
				sMaster = Master.Desc[0:-4]
			else:
				sMaster = Master.Desc
			sTweet = WordList(["Sleeping With", "Hooking Up With", "Tempting", "Seducing", "Bedding", "Stripping For", "Secretly Watching", "Showering With", "Spying On", "Sharing", "Playing With", "Claimed By", "Taken By", "Deflowered By", "Dominated By", "Blackmailed By", "Stripped By", "Tied to the Bed By", "Pleasured By", "Spanked By", "Ravished By", "Taken Hard By", "Massaged By", "Going Down On", "Impregnated By"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Daughter", "Sister", "Step-Sister", "Step-Daughter"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Boyfriend", "Fiancé", "Husband", "Hubby"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Step-Mom", "Mom", "Mother"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Brother", "Boyfriend", "Boyfriend", "Step-Brother"]).GetWord()
			else:	
				sTweet += "My Best Friend's\n"
				sTweet += sMaster + " " + WordList(["Son", "Brother", "Boyfriend", "Fiancé", "Husband", "Dad", "Father", "Hubby", "Step-Dad"]).GetWord()
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, NotList = ['Single','Virgin', 'Girl', 'Woman', 'Mom', 'Sister', 'Mother', 'Daughter', 'Lesbian', 'Maiden', 'Wife'], bAllowMaritalStatus = False, bAllowRelate = False, bAllowTitle = False)
			if Girl.Desc[-4:] == "Girl":
				sGirl = Girl.Desc[0:-5]
			elif Girl.Desc[-5:] == "Woman":
				sGirl = Girl.Desc[0:-6]
			else:
				sGirl = Girl.Desc
			sTweet = WordList(["Sleeping With", "Seducing", "Massaging", "Bedding", "Undressing", "Secretly Watching", "Spying On", "Sharing", "Showering With", "Stripping", "Playing With", "Claiming", "Spanking", "Punishing", "Deflowering", "Going Down On", "Blackmailing", "Pleasuring", "Impregnating"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Brother", "Step-Brother", "Step-Son", "Son"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Girlfriend", "Fiancé", "Wife"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Father", "Dad", "Step-Dad"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Girlfriend", "Step-Sister"]).GetWord()
			else:
				sTweet += "My Best Friend's\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Step-Sister", "Daughter", "Step-Daughter", "Fiancé", "Wife", "Step-Mom", "Mom", "Mother"]).GetWord()
			
		return sTweet
		
class Generator33(Generator):
	ID = 33
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = sVerb + " " + self.HerName + ":\n"
		sTweet += "A " + Girl.Desc + "\n" + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator34(Generator):
	ID = 34
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True)
			sTweet = sVerb + " " + Girl.Desc
		else:
			sTweet = sVerb + " " + self.HerName
		
		sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 'Twin Sister', 'Best Friend', 'Lesbian Lover']).GetWord()

		return sTweet
		
class Generator35(Generator):
	ID = 35
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = WordList(['Arousing',
			'Bedding',
			'Bending Over For',
			'Cuckolding',
			'Deep-Throating',
			'Dominating',
			'Fellating',
			'Gagging On',
			'Going Down On',
			'Massaging',
			'Playing With',
			'Pleasing',
			'Riding',
			'Rimming',
			'Seducing',
			'Sharing',
			'Showering With',
			'Smothering',
			'Stripping For',
			'Submitting To',
			'Swallowing',
			'Teaching',
			'Teasing',
			'Tempting',
			'Touching Myself For',
			'Whipping']).GetWord()
		
		Master = MaleChar(iNumMinCBits = 2, bAllowGang = False)
		sTweet = sVerb + " Mr. " + LastNames().GetWord() + ":\n"
		sTweet += "My " + self.SubtitleCoda.GetWord(NotList = ['Story']) + " With A\n" + Master.Desc

		return sTweet
		
class Generator36(Generator):
	#Turned Gay
	ID = 36
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good)
			
			if CoinFlip():
				Lesbian = LesbianChar(bAddArticle = True, NotList = ['wife','girlfriend', 'married'])
				sTweet = "Turned Lesbo by " + Lesbian.Desc
			else:
				Lesbian = LesbianChar(NotList = ['wife','girlfriend', 'married', 'lesbian'])
				sTweet = "Straight " + Girl.Desc + "\nfor the \nLesbian " + Lesbian.Desc 
			
		else:
			Man = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
			
			if CoinFlip():
				Gay = GayChar(bAddArticle = True, NotList = ['husband','boyfriend', 'married'])
				sTweet = "Turned Gay by " + Gay.Desc
			else:
				Gay = GayChar(NotList = ['husband','boyfriend', 'married', 'gay'])
				sTweet = "Straight " + Man.Desc + "\nfor the\nGay " + Gay.Desc 

		return sTweet
		
# class Generator57(Generator):
	# ID = 57
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator58(Generator):
	# ID = 58
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator59(Generator):
	# ID = 59
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
def LastNameBuilder(NotList = None):
	sLName = ""
	
	Names = []
	
	if NotList == None:
		NotList = []
	
	sName1 = LastNames().GetWord(NotList = NotList)
	sName2 = LastNames().GetWord(NotList = [sName1] + NotList)
	
	for _ in range(4):
		Names.append(sName1)
	
	Names.append(sName1 + "-" + sName2)
	
	sLName = Names[randint(0, len(Names) - 1)]
	
	return sLName
		
def AuthorBuilder(Gender = Gender.Neuter):
	sAName = ""
	
	Alphabet = "AAAABBBCCDDDEEEEFFFGGGGHHHIIJJJJKKLLLMNOOPPPQRRRRSSSSTTTTUVVWWWXYZ"
	
	FirstNames = []
	MaleNames = NamesMale()
	FemNames = NamesFemale()
	
	sName = ""
	for _ in range(2):
		sName += Alphabet[randint(0, len(Alphabet) - 1)] + "."
	FirstNames.append(sName)
	
	if Gender == Gender.Male or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(MaleNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(2):
			sName1 = MaleNames.FirstName()
			sName2 = MaleNames.FirstName()
			while sName2 in sName1:
				sName2 = MaleNames.FirstName()
			FirstNames.append(sName1 + " " + sName2)
			
		for _ in range(4):
			FirstNames.append(MaleNames.FirstName() + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
		
	if Gender == Gender.Female or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(FemNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(2):
			sName1 = FemNames.FirstName()
			sName2 = FemNames.FirstName()
			while sName2 in sName1:
				sName2 = FemNames.FirstName()
			FirstNames.append(sName1 + " " + sName2)
			
		for _ in range(4):
			FirstNames.append(FemNames.FirstName() + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
		
	sAName = FirstNames[randint(0, len(FirstNames) - 1)]
	
	sAName += " " + LastNameBuilder(NotList = [sAName])
	
	return sAName
		
def GetImgTweetText(gen):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	TweetText = []
	BookSeller = BookSellers()
	Hashtag = Hashtags()
	SexyAdj = SexyAdjs()
	
	sBookSeller = BookSeller.GetWord()
	
	sText = "The " + SexyAdj.GetWord() + " " + WordList(["read", "book", "ebook"]).GetWord() + " that was " + WordList(["BANNED on", "TOO HOT for", "TOO FILTHY for", "too much for"]).GetWord() + " Amazon! Now available on " + BookSeller.GetWord(NotList = ["Amazon", "Kindle Unlimited"]) 
	if CoinFlip():
		sText += " (from " + AuthorBuilder() + ")"
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = WordList(["Coming soon on", "Available soon on", "Look for this soon on", "Get it now on", "Download it today on"]).GetWord() + " " + sBookSeller 
	if CoinFlip():
		sText += " and " + BookSeller.GetWord(NotList = [sBookSeller])
	if CoinFlip():
		sText += ". By " + AuthorBuilder()
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = WordList(["Watch for this", "Look for this", "Keep an eye out for this"]).GetWord() + " " + SexyAdj.GetWord() + " ebook on " + sBookSeller
	if CoinFlip():
		sText += " and " + BookSeller.GetWord(NotList = [sBookSeller])
	if CoinFlip():
		sText += ". By " + AuthorBuilder()
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = WordList(["Available soon", "Coming soon", "On its way soon"]).GetWord() + " to " + WordList(["discerning", "discrete", "discriminating"]).GetWord() + " readers on " + sBookSeller 
	if CoinFlip():
		sText += " and " + BookSeller.GetWord(NotList = [sBookSeller])
	if CoinFlip():
		sText += ". By " + AuthorBuilder()
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = AuthorBuilder(Gender = Gender.Male) + "'s "
	sText += WordList(["Patreon supporters", "supporters on Patreon"]).GetWord() + " get " + WordList(["instant access", "free access", "access"]).GetWord() + " to all his " + SexyAdj.GetWord() + " " + WordList(["reads", "books", "stories"]).GetWord() + "!"
	for _ in range(1):
		TweetText.append(sText)
	#=============================
	
	sText = AuthorBuilder(Gender = Gender.Female) + "'s "
	sText += WordList(["Patreon supporters", "supporters on Patreon"]).GetWord() + " get " + WordList(["instant access", "free access", "access"]).GetWord() + " to all her " + SexyAdj.GetWord() + " " + WordList(["reads", "books", "stories"]).GetWord() + "!"
	for _ in range(1):
		TweetText.append(sText)
	#=============================
	
	sText = WordList(["Available soon", "Coming soon", "On its way soon", "Out soon", "Arriving soon"]).GetWord() + " from " + AuthorBuilder(Gender = Gender.Female) 
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	sText = "Reply to this tweet and " 
	if CoinFlip():
		sText += "I'll tweet a " + WordList(["randomly", "computer", "bot", "algorithmically"]).GetWord () + "-generated " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title @ you!"
	else:
		sText += "get a custom " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title of your very own in reply! " + GetEmoji()
	sText += " " + GetEmoji()
	for _ in range(3):
		TweetText.append(sText)
	#=============================
	
	sText = WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + WordList([" my sister bot", " my bot-sibbling", ""]).GetWord() + " @bot_lust " + WordList(["to read what's inside", "to read " + SexyAdjs().GetWord() + " excerpts from", "to see what's inside", "to read " + SexyAdjs().GetWord() + " bot-generated love scenes from"]).GetWord() + " this book (warning: NSFW!) " + GetEmoji()
	for _ in range(2):
		TweetText.append(sText)
	#=============================

	# it seems that adding any kind of hashtag at all to a bot may lead to shadowbans. so for now I'm not using this.
	if randint(1,5) == 5:
		sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
		while IsTweetTooLong(sText):
			sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	else:
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
		