#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

import people
import verbs
import names 

from random import *
from util import *
		
class Events(WordList):
	def __init__(self):
		super().__init__(['Ash Wednesday',
		'Christmas Eve',
		'Easter Sunday',
		'Friday',
		'Halloween',
		'Highschool Graduation',
		'Homecoming',
		'Hump Day',
		'Independence Day',
		'International Women\'s Day',
		'Junior Prom',
		'Mardis Gras',
		'Mother\'s Day',
		'my anniversary',
		'my birthday',
		'my wedding day',
		'New Year\'s Eve',
		'Spring Break',
		'St. Patrick\'s Day',
		'Superbowl Sunday',
		'teacher planning day',
		'Valentine\'s Day'])
		
	def RemoveMy(self, sWord):
		return sWord.replace('my ','')
		
	def GetWord(self, bRemoveMy = False):
		sEvent = ""
		
		sEvent = super().GetWord()
			
		if bRemoveMy:
			sEvent = self.RemoveMy(sEvent)
			
		return sEvent
		
class MaleSO(WordList):
	def __init__(self):
		super().__init__(['boyfriend',
			'fiancé',
			'hubby',
			'husband'])
			
class FemaleSO(WordList):
	def __init__(self):
		super().__init__(['bride',
			'girlfriend',
			'fiancé',
			'wife'])
		
class Hashtags(WordList):
	def __init__(self):
		super().__init__(['50shades',
			'amwriting',
			'BDSM',
			#'bitcoin',
			#'blockchain',
			'bot',
			'botally'
			'botlife',
			'botlove',
			'eartg',
			'eartg',
			'erotica',
			'erotica',
			'fantasy',
			'fiftyshades',
			'filthy',
			#'litecoin',
			'lovestory',
			'lprtg',
			'lprtg',
			'mrbrtg',
			'naughty',
			'nsfw',
			'PleaseRT',
			'scifi',
			'romance',
			'smut',
			'sorrynotsorry',
			'ssrtg',
			'ssrtg',
			'taboo',
			'truelove',
			'twitterbot',
			'twitterbot',
			'wprtg'])
		
class BadGirlNames(NounAdjList):
	DefaultNoun = 'slut'
	DefaultAdj = 'little'
	
	NounList = ['hussy',
		'minx',
		'nympho',
		'skank',
		'slut',
		'slut',
		'slut',
		'tart',
		'tramp',
		'trollop',
		'whore',
		'whore']
		
	AdjList = ['brazen',
		'cheeky',
		'filthy',
		'little',
		'nasty',
		'outrageous',
		'saucy',
		'shameless',
		'wanton']
		
class SexyAdjs(WordList):
	def __init__(self):
		super().__init__(['dirty',
		'erotic',
		'filthy',
		'hot',
		'kinky',
		'naughty',
		'sexy',
		'sensual',
		'steamy',
		'taboo'])

class BookSellers(WordList):
	def __init__(self):
		super().__init__(['Apple Books',
			'Amazon',
			'B&N',
			'Kindle Unlimited',
			'Kobo',
			'Radish Fiction',
			'Smashwords',
			'WattPad'])
			
# mature, young, teenager, MILF, etc
class AgeFemaleNoun(WordList):
	def __init__(self):
		super().__init__(['College Girl',
			'Maiden',
			'Mature Woman',
			'MILF',
			'Older Woman',
			'Schoolgirl',
			'Teen',
			'Teenager',
			'Virgin'])
			
# mature, young, teenager, MILF, etc
class AgeFemaleAdj(WordList):
	def __init__(self):
		super().__init__(['Co-ed',
			'Maiden',
			'Mature',
			'MILF',
			'Nubile',
			'Older',
			'Schoolgirl',
			'Teen',
			'Teenage',
			'Virgin',
			'Young'])
		
# bashful, innocent, etc 
class AttitudeGoodFemale(WordList):
	def __init__(self):
		super().__init__(['Anal Virgin',
			'Bashful',
			'Chaste',
			'Conservative',
			'Innocent',
			'Innocent',
			'Sassy',
			'Sexy',
			'Shy',
			'Virginal'])
		
# kinky, slutty, etc 
class AttitudeBadFemale(WordList):
	def __init__(self):
		super().__init__(['Desperate',
			'Kinky','Kinky',
			'Naughty','Naughty',
			'Nympho','Nympho',
			'Promiscuous',
			'Slutty','Slutty','Slutty',
			'Wanton','Wanton',
			'Willing','Willing'])
			
class AttitudeFemale(WordList):
	def __init__(self):
		super().__init__(AttitudeGoodFemale().List + AttitudeBadFemale().List)		
		
class ClothingFemale(WordList):
	def __init__(self):
		super().__init__(['High-Heeled',
			'Latex-Clad',
			'Leather-Clad'])

class GenModFemale(WordList):
	def __init__(self):
		super().__init__(['Anal','Anal',
		'BDSM','BDSM','BDSM',
		'Erotic',
		'Horny',
		'Nudist','Nudist','Nudist',
		'Sex',
		'Taboo','Taboo'])
		
# single, single mom, married, engaged
class MaritalStatusFemale(WordList):
	def __init__(self):
		super().__init__(['Recently-Divorced',
			'Concubine',
			'Harem','Harem',
			'Married','Married','Married',
			'Single','Single','Single','Single'])

# french, italian, etc
class NationFemale(WordList):
	def __init__(self):
		super().__init__(['Amish','Amish','Amish',
			'Asian','Asian',
			'Christian','Christian','Christian',
			'Country',
			'Czech',
			'French',
			'German',
			'Island Girl',
			'Latina',
			'Russian',
			'Small-Town',
			'Swedish'])
		
# big-titty, etc
class PhysCharFemale(WordList):
	def __init__(self):
		super().__init__(['Attractive',
			'Beautiful',
			'Big Titty',
			'Busty',
			'Buxom',
			'Curvy',
			'Gorgeous',
			'Hot',
			'Leggy',
			'Naked',
			'Nubile',
			'Nude',
			'Petite',
			'Skinny',
			'Voluptuous',
			'Young'])
			
class PregState(WordList):
	def __init__(self):
		super().__init__(['Fertile','Fertile','Fertile',
			'Lactating',
			'Pregnant',
			'Nursing'])

# nurse, flight-attendant, etc
class ProfGoodFemale(WordList):
	def __init__(self):
		super().__init__(['Airline Stewardess',
			'Babysitter',
			'Ballerina',
			'Bikini Model',
			'Bridesmaid',
			'Cheerleader',
			'Co-ed',
			'College Girl',
			'Dancer',
			'Fashion Model',
			'Gymnast',
			'House Maid',
			'Housewife',
			'Flight Attendant',
			'Governess',
			'Handmaiden',
			'French Maid',
			'Librarian',
			'Life Drawing Model',
			'Lingerie Model',
			'Masseuse',	
			'Maid',
			'Milk Maid',
			'Nanny',
			'Nurse',
			'Pastor\'s Wife',
			'Secretary','Secretary',
			'Servant',
			'Schoolgirl',
			'Starlet',
			'Supermodel',
			'Teacher',
			'Waitress',
			'Wet Nurse'])
			
# porn star, call girl, escort, etc
class ProfBadFemale(WordList):
	def __init__(self):
		super().__init__(['Amateur Porn Star',
			'Anal Whore',
			'Call-Girl',
			'Dominatrix',
			'Escort',
			'Fetish Model',
			'Porn Star',
			'Slave',
			'Stripper',
			'Whore',
			'Witch'])
			
class ProfFemale(WordList):
	def __init__(self):
		super().__init__(ProfGoodFemale().List + ProfBadFemale().List)

# step-daughter, mom
class RelateFemale(WordList):
	def __init__(self):
		super().__init__(['Concubine',
			'Cousin',
			'Daughter','Daughter',
			'Daughter\'s Best Friend',
			'Girlfriend','Girlfriend','Girlfriend',
			'Mistress',
			'Mommy',
			'Mommy',
			'Sister',
			'Step-Daughter','Step-Daughter',
			'Step-Mom','Step-Mom','Step-Mom',
			'Step-Sister','Step-Sister',
			'Wife','Wife'])

class SexualityFemale(WordList):
	def __init__(self):
		super().__init__(['Bi-Curious',
			'Lesbian'])
	
# black, ebony
class SkinHairColorFemale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'Ebony','Ebony',
			'Pale',
			'Blonde',
			'Brunette',
			'Dark-Haired',
			'Redhead'])

# futa			
class SpeciesFemale(WordList):
	def __init__(self):
		super().__init__(['Green-Skinned Alien',
			'Fairy',
			'Futa','Futa',
			'Mermaid','Mermaid',
			'Vampire'])
	
# princess	
class TitlesFemale(WordList):
	def __init__(self):
		super().__init__(['Baroness',
			'Duchess',
			'Princess','Princess','Princess','Princess',
			'Queen','Queen'])
		
# Amish maiden, BBW, Farmer's Daughter
class TropesGoodFemale(WordList):
	def __init__(self):
		super().__init__(['Amish Maiden','Amish Maiden',
			'BBW','BBW',
			'Blonde',
			'Bride',
			'Brunette',
			'Farmer\'s Daughter',
			'Prom Queen','Prom Queen',
			'Redhead',
			'Single Mom',
			'Small-Town Girl',
			'Soccer Mom',
			'Virgin','Virgin','Virgin',
			'Wallflower'])
		
# bad girl, bimbo, brat
class TropesBadFemale(WordList):
	def __init__(self):
		super().__init__(['Bad Girl',
			'Bad Girl',
			'Bimbo','Bimbo',
			'Brat',
			'Goth Girl',
			'Harem Girl',
			'Hotwife','Hotwife',
			'MILF','MILF','MILF',
			'Nymphomaniac','Nymphomaniac',
			'Submissive',
			'Witch'])
			
class TropesFemale(WordList):
	def __init__(self):
		super().__init__(TropesGoodFemale().List + TropesBadFemale().List)	
			
class BookGirlsBasic(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Sisters'])
			
class BookGirls(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__([
			'Twin Sisters',
			])
		
class BookMastersBasic(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha',
			'Artist',
			'Athlete',
			'Boyfriend',
			'Dad',
			'Daddy',
			'Family Man',
			'Father-in-Law',
			'Freshman',
			'Gentleman',
			'Hipster',
			'Husband',
			'Preacher',
			'President',
			'Prince',
			'Step-Dad',
			'Widower'])

class BookMasters(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha Male',
			'Alpha Wolf',
			'Astronaut',
			'Assassin',
			'Bachelor',
			'Barbarian',
			'BBC',
			'Biker',
			'Billionaire',
			'Bitcoin Billionaire',
			'Bodyguard',
			'Boss',
			'Boxer',
			'Breeding Stud',
			'Bull Rider',
			'CEO',
			'Centaur',
			'Centaur',
			'Count',
			'Cop',
			'Cowboy',
			'Dad',
			'Daddy',
			'Daddy Dom',
			'Defensive Lineman',
			'Dildo Designer',
			'Dinosaur',
			'Doctor',
			'Dom',
			'Dominatrix',
			'Duke',
			'Duke',
			'Fire Fighter',
			'Futanari',
			'Gangsta',
			'Gay-for-Pay Porn Star',
			'Gazillionaire',
			'Gentleman',
			'Gladiator',
			'Goat Man',
			'Guitar Player',
			'Hitman',
			'Incubus',
			'Jet Fighter Pilot',
			'Jock',
			'Killer-for-Hire',
			'King',
			'King',
			'King',
			'Kingpin',
			'Knight',
			'Lawyer',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lesbian MILF',
			'Lipstick Lesbian',
			'Lumberjack',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Stripper',
			'Man-o-taur',
			'Manor Lord',
			'Man-telope',
			'Man-ticore',
			'Marquis',
			'Mer-man',
			'MMA Fighter',
			'Millionaire',
			'Mob Boss',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Pirate Captain',
			'Playboy Billionaire',
			'Pope',
			'Porn Star',
			'President',
			'Prime Minister',
			'Prince',
			'Prince',
			'Prince',
			'Professor',
			'Quarterback',
			'Rock Star',
			'Shah',
			'Secret Agent',
			'Sex Addict',
			'Sex Warlock',
			'Sheikh',
			'Sheriff',
			'Single Dad',
			'Sorcerer',
			'Spy',
			'Stallion',
			'Sugar Daddy',
			'Sultan',
			'Surfer',
			'Heart Surgeon',
			'Tentacle Monster',
			'Trillionaire',
			'Viking',
			'Uniporn',
			'Vampire',
			'Violinist',
			'Voyeur',
			'Warrior',
			'Werewolf'])
			
class BookMasterGangs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Baby Daddies',
			'Bandits',
			'Barbarians',
			'Basketball Team',
			'Biker Gang',
			'Billionaires Club',
			'Boy\'s School',
			'Brothers',
			'Cops',
			'Cowboys',
			'Football Team',
			'Gangstas',
			'Goat Men',
			'Herd of Centaurs',
			'Hockey Team',
			'Identical Twin Brothers',
			'Lesbian Harem',
			'Mer-men',
			'Mongol Horde',
			'Mountain Men',
			'Navy Seals',
			'Pirates',
			'Rock Band',
			'Seal Team Six',
			'S.W.A.T. Team',
			'Scottsmen',
			'Viking Hoard',
			'Vampire Coven',
			'Werewolf Pack'])
			
class BookMasterAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha',
			'Athletic',
			'Australian',
			'Bad Boy',
			'Bald',
			'Bearded',
			'Beefcake',
			'Black',
			'BDSM',
			'Brooding',
			'Charming',
			'Cocky',
			'Dominant',
			'Ebony',
			'Highly Eligible',
			'Famous',
			'French',
			'Gang-Bang',
			'Ghost',
			'Hairy',
			'Handsome',
			'Handsome',
			'Highlander',
			'Horny',
			'Hung',
			'Irish',
			'Italian',
			'Kinky',
			'Leather',
			'Mustachioed',
			'Naked',
			'Norwegian',
			'Nudist',
			'Older',
			'Pantsless',
			'Playboy',
			'Rebel',
			'Reckless',
			'Renegade',
			'Rock-Hard',
			'Royal',
			'Savage',
			'Scottish',
			'Secret',
			'Sexy',
			'Shape-Shifting',
			'Shameless',
			'Silver Fox',
			'Space',
			'Spanish',
			'Stay-at-Home',
			'Strapping',
			'Strong',
			'Tall',
			'Tattooed',
			'Visibly Erect',
			'Wealthy',
			'Well-Hung',
			'Well-Endowed',
			'Wicked',
			'Widowed'])
			
class BookMasterCompAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Astronaut',
			'Bitcoin Billionaire',
			'Biker',
			'Billionaire',
			'Boxer',
			'Centaur',
			'Cowboy',
			'Defensive Lineman',
			'Dinosaur',
			'Fire Fighter',
			'Futanari',
			'Gazillionaire',
			'Goat Man',
			'Guitar Player',
			'Hitman',
			'Lawyer',
			'Mer-man',
			'Millionaire',
			'MMA Fighter',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Pirate',
			'Porn Star',
			'Rock Star',
			'Sex Addict',
			'Single Dad',
			'Stripper',
			'Surfer',
			'Heart Surgeon',
			'S.W.A.T. Team',
			'Trillionaire',
			'Viking',
			'Violinist',
			'Voyeur',
			'Werewolf'])
			
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowered',
			'Annally Deflowered in Public',
			'Bared',
			'Beaten',
			'Blackmailed',
			'Bound',
			'Bred',
			'Broken',
			'Captured',
			'Caught on Video',
			'Claimed',
			'Claimed',
			'Claimed Hard',
			'Claimed in Public',
			'Collared',
			'Conquered',
			'Chained',
			'Charmed',
			'Cuckolded',
			'Cuddled',
			'Cuddled Hard',
			'Deflowered',
			'Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Enslaved',
			'Exposed in Public',
			'Forced',
			'Hotwifed',
			'Humiliated',
			'Hunted For Food',
			'Hypnotized',
			'Impregnated',
			'Knocked Up',
			'Leashed',
			'Mastered',
			'Mind-Controlled',
			'Owned',
			'Paddled',
			'Pleasured',
			'Pleasured in Public',
			'Punished',
			'Punished in Public',
			'Ravished',
			'Ruled',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Sold',
			'Sold',
			'Spanked',
			'Spanked in Public',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Taken',
			'Taken',
			'Taken Hard',
			'Taken Hard in Public',
			'Taken in Public',
			'Tamed',
			'Tempted',
			'Trained',
			'Secretly Watched',
			'Violated',
			'Whipped'])
			
class BookVerbsTo(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Bared',
				'Bound',
				'Bred',
				'Chained',
				'Engaged',
				'Enslaved',
				'Gifted',
				'Hotwifed',
				'Married',
				'Mated',
				'Pledged',
				'Sold',
				'Surrendered'])
			
