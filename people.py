#!/usr/bin/env python
# -*- coding: utf-8 -*-
# People module

from random import *
from util import *

import misc

FemCBitHistoryQ = HistoryQ(10)

class CharBit():
	def __init__(self):
		self.val = ""
		self.part = ""

class Character():
	def __init__(self):
		self.Gender = Gender.Neuter
		
class AgeFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if CoinFlip():
			self.val = misc.AgeFemaleNoun().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			self.part = "noun"
		else:
			self.val = misc.AgeFemaleAdj().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			self.part = "adj"
		return self.val
		
class AttitudeFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = misc.AttitudeGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = misc.AttitudeBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = misc.AttitudeFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class ClothingFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.ClothingFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class GenModFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.GenModFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class MaritalStatusFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.MaritalStatusFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class NationFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.NationFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class PhysCharFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.PhysCharFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class PregState(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.PregState().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class ProfFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = misc.ProfGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = misc.ProfBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = misc.ProfFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			
		self.part = "noun"
		return self.val
		
class RelateFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.RelateFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "noun"
		return self.val

class SexualityFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.SexualityFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class SkinHairColorFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.SkinHairColorFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class SpeciesFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.SpeciesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class TitleFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = misc.TitlesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class TropeFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = misc.TropesGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = misc.TropesBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = misc.TropesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)	
			
		self.part = "noun"
		
		return self.val
		
class FemaleChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 4, Type = GirlType.Neutral, NotList = None):
		super().__init__()
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		
		CharBitList = []
		
		CharBitList.append(AttitudeFemale(Type = Type))
		CharBitList.append(AttitudeFemale(Type = Type))
		CharBitList.append(PhysCharFemale())
		CharBitList.append(PhysCharFemale())
		CharBitList.append(SkinHairColorFemale())
		if Type != GirlType.Good:
			CharBitList.append(GenModFemale())
		CharBitList.append(ClothingFemale())
		CharBitList.append(PregState())
		CharBitList.append(MaritalStatusFemale())
		CharBitList.append(NationFemale())
		CharBitList.append(AgeFemale())
		CharBitList.append(SexualityFemale())
		CharBitList.append(ProfFemale(Type = Type))
		CharBitList.append(ProfFemale(Type = Type))
		CharBitList.append(ProfFemale(Type = Type))
		CharBitList.append(SpeciesFemale())
		CharBitList.append(TropeFemale(Type = Type))
		CharBitList.append(TropeFemale(Type = Type))
		CharBitList.append(TropeFemale(Type = Type))
		CharBitList.append(RelateFemale())
		CharBitList.append(TitleFemale())
			
		BitGetList = []
		bFoundNoun = False 
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		if irand1 > irand2:
			iNumCBits = irand1
		else:
			iNumCBits = irand2 
			
		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits)):
			sBit = CharBitList[x].Get(NotList = NotList)
			if CharBitList[x].part == "noun":
				bFoundNoun = True 
			NotList.append(sBit)
			BitGetList.append(sBit)
			
		if not bFoundNoun:
			BitGetList.append(WordList(["Girl","Woman"]).GetWord(NotList = NotList))
		
		self.Desc = ""
		for x in range(0, len(BitGetList)):
			if x > 0:
				self.Desc += " "
			self.Desc += BitGetList[x]

class Person(WordList):
	def GetPerson(self):
		sPerson = ""
		
		sPerson = self.GetWord()
		
		return sPerson
		
class MaleSO(Person):
	def __init__(self):
		super().__init__(['boyfriend','boyfriend',
			'fiancé',
			'hubby',
			'husband'])
			
class FemaleSO(Person):
	def __init__(self):
		super().__init__(['bride',
			'girlfriend','girlfriend',
			'fiancé',
			'wife'])
		
class FemaleFWB(Person):
	def __init__(self):
		super().__init__(['aunt',
		'babysitter',
		'barista',
		'boss',
		'boss\'s wife',
		'CEO',
		'co-ed student',
		'hot cousin',
		'cute roommate',
		'dad\'s girlfriend',
		'daughter',
		'daughter\'s best friend',
		'daughter-in-law',
		'dominatrix',
		'eighth-grade teacher',
		'English teacher',
		'ex',
		'fashion model',
		'flight attendant',
		'French maid',
		'girlfriend',
		'girlfriend\'s mom',
		'girlfriend\'s sister',
		'guidance counselor',
		'hot best friend',
		'intern',
		'land lady',
		'librarian',
		'life drawing model',
		'English lit student',
		'maid',
		'math teacher',
		'marriage counselor',
		'masseuse',
		'math tutor',
		'mom\'s best friend',
		'mother-in-law',
		'next-door neighbor',
		'niece',
		'nurse',
		'parole officer',
		'pastor\'s wife',
		'personal trainer',
		'roommate\'s girlfriend',
		'secretary',
		'sister',
		'sister-in-law',
		'sister\'s hot friend',
		'soccer mom',
		'son\'s principal',
		'step-daughter',
		'step-mom',
		'step-sister',
		'Sunday School teacher',
		'teacher',
		'twin sister',
		'wedding planner',
		'wife',
		'wife\'s Avon Lady',
		'wife\'s pregnancy surrogate'])
		
class MaleFWB(Person):
	def __init__(self):
		super().__init__(['attorney',
			'attractive male masseuse',
			'baby daddy',
			'bank teller',
			'barista',
			'best friend\'s fiancé',
			'billionaire fiancé',
			'bodyguard',
			'boss',
			'boy toy',
			'boyfriend',
			'brother',
			'brother-in-law',
			'celebrity crush',
			'co-worker',
			'contractor',
			'dad\'s best friend',
			'daddy',
			'daddy dom',
			'daughter\'s boyfriend',
			'dentist',
			'dom',
			'driver',
			'drug dealer',
			'ex-boyfriend',
			'father',
			'father-in-law',
			'fiancé',
			'friend-with-benefits',
			'geography teacher',
			'girlfriend',
			'guidance counselor',
			'gynecologist',
			'hubby',
			'husband',
			'landlord',
			'life coach',
			'lifeguard',
			'lord',
			'mailman',
			'manager',
			'master',
			'minister',
			'one true love',
			'pastor',
			'pediatrician',
			'personal trainer',
			'photographer',
			'pizza delivery boy',
			'pool boy',
			'priest',
			'prince',
			'proctologist',
			'professor',
			'psychiatrist',
			'roommate',
			'shift supervisor',
			'sister\'s boyfriend',
			'son-in-law',
			'step-son',
			'tennis coach',
			'twin brother',
			'uber driver',
			'vice-principal',
			'volleyball coach',
			'yoga teacher'])
			
class JobBlueCollar(Person):
	def __init__(self):
		super().__init__(['aluminum can recycler',
		'bag boy',
		'baggage handler',
		'ball boy',
		'bellhop',
		'bus driver',
		'Starbucks barista',
		'beat cop',
		'blogger',
		'bus driver',
		'call center worker',
		'cat box scooper',
		'cattle wrangler',
		'civil servant',
		'club bouncer',
		'Comcast technician',
		'dish washer at Applebee\'s',
		'dog walker',
		'dog groomer',
		'farm hand',
		'farmer',
		'food court worker',
		'freshman in college',
		'fry cook',
		'garbage man',
		'gas station attendant',
		'golf caddy',
		'gym coach',
		'home theater installer',
		'hot dog vendor',
		'high school history teacher',
		'janitor',
		'junk scavenger',
		'lawn maintenance man',
		'living statue',
		'Lyft driver',
		'manager at Arby\'s',
		'masseur',
		'male nurse',
		'mall santa',
		'mechanic',
		'meter maid',
		'office assistant',
		'page boy',
		'paige',
		'painter',
		'peasant',
		'pest control technician',
		'pet store clerk',
		'Pizza Hut delivery guy',
		'plumber',
		'pool boy',
		'porn set fluffer',
		'postal clerk',
		'private in the army',
		'public restroom attendant',
		'rent-a-cop',
		'roadie',
		'roadkill disposal worker',
		'sea man',
		'self-published author',
		'serf',
		'server at Applebee\'s',
		'shift supervisor',
		'short-order cook',
		'stable boy',
		'stand-up comedian',
		'starving artist',
		'Whole Foods stock boy',
		'tax payer',
		'taxidermist',
		'third-grade teacher',
		'ticket stub collector',
		'tow-truck driver',
		'tour guide',
		'truck driver',
		'used car salesman',
		'waiter',
		'Wal-Mart greeter',
		'wedding DJ',
		'writer of erotic romances',
		'zoo keeper'])
		
class JobWhiteCollar(Person):
	def __init__(self):
		super().__init__(['accountant',
		'actuary',
		'airline pilot',
		'Apple Store genius',
		'architect',
		'astronaut',
		'banker',
		'bass guitarist',
		'bee keeper',
		'cakery owner',
		'chiropractor',
		'city councilman',
		'civil engineer',
		'classical violinist',
		'club DJ',
		'crossword puzzle writer',
		'database developer',
		'detective',
		'dive instructor',
		'executive producer',
		'first-chair flautist',
		'funeral director',
		'guru',
		'gynecologist',
		'homicide detective',
		'fashion photographer',
		'flight attendant',
		'house flipper',
		'insurance adjuster',
		'jet fighter pilot',
		'lieutenant colonel',
		'merchant',
		'middle manager',
		'motivational speaker',
		'Navy Seal',
		'neurosurgeon',
		'opthamologist',
		'orthodonist',
		'pharmacist',
		'PhD candidate',
		'photographer',
		'podiatrist',
		'porn star',
		'principal',
		'proctologist',
		'project manager',
		'public radio host',
		'published author',
		'radio DJ',
		'radiologist',
		'rancher',
		'realtor',
		'regional manager',
		'rocket scientist',
		'romance novelist',
		'sex therapist',
		'sex toy designer',
		'sherriff',
		'stay-at-home dad',
		'surgeon',
		'tax attorney',
		'tenured professor',
		'train conductor',
		'urologist',
		'veterinarian',
		'web designer',
		'Wendy\'s franchise owner',
		'yoga teacher',
		'YouTube personality'])
		
class JobWealthyMale(Person):
	def __init__(self):
		super().__init__(['archduke',
		'baron',
		'Bitcoin billionaire',
		'billionaire',
		'celebrity chef',
		'CEO',
		'count',
		'duke',
		'earl',
		'emperor',
		'film mogul',
		'general',
		'king',
		'knight',
		'marquess',
		'marquis',
		'movie star',
		'Nobel Prize winner',
		'Dalai Lama',
		'pope',
		'president',
		'prime minister',
		'prince',
		'pro football quarterback',
		'rock star',
		'senator',
		'shah',
		'sheikh',
		'sheriff',
		'sultan',
		'surgeon general',
		'titan of industry',
		'viscount'])

class JobWealthyFemale(Person): 
	def __init__(self):
		super().__init__(['actress',
		'archduchess',
		'baroness',
		'CEO',
		'contessa',
		'countess',
		'duchess',
		'heiress',
		'empress',
		'fasion designer',
		'first lady',
		'high-born lady',
		'marchioness',
		'mother superior',
		'Nobel Prize winner',
		'porn star',
		'president',
		'princess',
		'prime minister',
		'queen',
		'queen mother',
		'pop star',
		'senator',
		'social media influencer',
		'supermodel',
		'surgeon general',
		'viscountess',
		'wealthy MILF'])