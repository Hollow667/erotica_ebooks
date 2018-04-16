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
			'Pregnant','Pregnant',
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
			'Bride',
			'Farmer\'s Daughter',
			'Prom Queen','Prom Queen',
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
		
class AgeMaleAdj(WordList):
	def __init__(self):
		super().__init__(['College',
			'Older','Older','Older',
			'Middle-Aged',
			'Silver Fox',
			'Teenage',
			'Young'])
		
class AttitudeMale(WordList):
	def __init__(self):
		super().__init__(['Brooding',
			'Charming',
			'Cocky',
			'Dominant',
			'Horny',
			'Highly Eligible',
			'Famous',
			'Kinky',
			'Playboy',
			'Powerful',
			'Rebel',
			'Reckless',
			'Renegade',
			'Savage',
			'Shameless',
			'Slick',
			'Smooth','Smooth',
			'Wicked'])
		
class GenModMale(WordList):
	def __init__(self):
		super().__init__(['Barbarian',
			'BDSM',
			#'Chain-Gang',	
			'Gang-Bang',
			'Heart-Throb',
			#'Leather',
			'Masked','Masked','Masked',
			'Nudist',
			'Royal',
			'Secret',
			'Sex Addict',
			'Sorcerer',
			'Stay-at-Home',	
			'Studly',
			'Taboo',
			'S.W.A.T. Team',
			'Virile',
			'Wealthy'])
		
class MaritalStatusMale(WordList):
	def __init__(self):
		super().__init__(['Bachelor','Bachelor','Bachelor',
			'Divorced',
			'Married','Married','Married',
			'Single','Single',
			'Widowed'])
		
class NationMale(WordList):
	def __init__(self):
		super().__init__(['Australian',
			'French',
			'Highlander',
			'Irish',
			'Italian',
			'Japanese',
			'Norwegian',
			'Scottish',
			'Space',
			'Spanish'])
		
class PhysCharMale(WordList):
	def __init__(self):
		super().__init__(['Athletic',
			'Bald',
			'Bare-Chested',
			'Bearded','Bearded',
			'Beefcake',
			'Beefy',
			'Buff',
			'Chiseled',
			'Clean-Shaven','Clean-Shaven',
			'Dad-Bod',
			'Fine',
			'Fit',
			'Hairy','Hairy',
			'Handsome','Handsome',
			'Hung',
			'Hunky',
			'Muscled',
			'Muscular',
			'Mustachioed',
			'Naked',
			'Pantsless',
			'Rock-Hard',
			'Sexy',			
			'Shape-Shifting',
			'Strapping',
			'Strong',
			'Tall','Tall',
			'Tattooed',
			'Visibly Erect',
			'Well-Built',
			'Well-Hung','Well-Hung',
			'Well-Endowed'])
		
class ProfMale(WordList):
	def __init__(self):
		super().__init__(['Artist',
			'Astronaut',
			'Assassin',
			'Athlete',
			'Bodyguard',
			'Boxer',
			'Breeding Stud',
			'Bull Rider',
			'Cop',
			'Cowboy',
			'Defensive Lineman',
			'Dildo Designer',
			'Doctor',
			'Dom',
			'Fire Fighter',
			'Freshman',	
			'Gladiator',
			'Ghost',
			'Guitar Player',
			'Heart Surgeon',
			'Hitman',
			'Investment Banker',
			'Jet Fighter Pilot',
			'Killer-for-Hire',
			'Knight',
			'Lawyer',
			'Lumberjack',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Stripper',
			'MMA Fighter',
			'Navy Seal',
			'Pirate',
			'Pirate Captain',
			'Preacher',
			'Professor',
			'Quarterback',
			'Sailor',
			'Secret Agent',
			'Sex Warlock',
			'Sheriff',
			'Spy',
			'Stockbroker',
			'Surfer',
			'Heart Surgeon',
			'Violinist'])
		
class RelateMale(WordList):
	def __init__(self):
		super().__init__([
			'Brother',
			'Boyfriend',
			'Dad',
			'Father-in-Law',
			'Fiancé',
			'Husband',
			'Step-Brother',
			'Step-Dad',
			'Widower'])
		
class SkinHairColorMale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'Black-Bearded',
			'Blonde',
			'Bronzed',
			'Copper-Skinned',
			'Curly-Haired',
			'Ebony',
			'Red-Headed',
			'Tanned','Tanned'])
		
class SpeciesMale(WordList):
	def __init__(self):
		super().__init__(['Alien',
			'Alpha Wolf',
			'Centaur','Centaur',
			'Cyborg',
			'Dinosaur',
			'Futanari',
			'Goat Man',
			'Incubus',
			'Man-o-taur',
			'Man-telope',
			'Man-ticore',
			'Mer-man',
			'Tentacle Monster',
			'Uniporn',
			'Vampire',
			'Werewolf'])
		
class TitlesMale(WordList):
	def __init__(self):
		super().__init__(['CEO',
			'Count',
			'Duke','Duke',
			'King','King','King',
			'Marquis',
			'Pope',
			'President',
			'Prime Minister',
			'Prince','Prince','Prince',
			'Shah',
			'Sheikh','Sheikh',
			'Sultan',
			])
		
class TropesMale(WordList):
	def __init__(self):
		super().__init__(['Alpha',
			'Alpha Male',
			'Bad Boy',
			'Barbarian',
			'BBC',
			'Biker',
			'Billionaire',
			'Bitcoin Billionaire',
			'Boss',
			'Daddy',
			'Daddy Dom',
			'DILF',
			'Ex-Con',
			'Family Man',
			'Gangsta',
			'Gay-for-Pay Porn Star',
			'Gazillionaire',
			'Gentleman',
			'Hipster',
			'Hunk',
			'Jock',
			'Kingpin',
			'Ladies Man',
			'Ladykiller',
			# 'Lesbian Cheerleader',
			# 'Lesbian Dominatrix',
			# 'Lesbian MILF',
			# 'Lipstick Lesbian',
			'Loverboy',
			'Manor Lord',
			'Millionaire',
			'Mob Boss',
			'Mountain Man',
			'Multi-Millionaire',
			'Older Man',
			'Playboy Billionaire',
			'Porn Star',
			'Rock Star',
			'Single Dad',
			'Silver Fox',
			'Stallion',
			'Stud',
			'Sugar Daddy',
			'Trillionaire',
			'Viking',
			'Voyeur',
			'Warrior'])
			
class GangsMale(WordList):
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

			
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowered',
			'Annally Deflowered in Public',
			'Bared',
			'Beaten',
			'Blackmailed',
			'Bound',
			'Bound in the Dungeon',
			'Bred',
			'Broken',
			'Captured',
			'Caught on Tape',
			'Caught on Video',
			'Claimed',
			'Claimed',
			'Claimed Hard',
			'Claimed in Public',
			'Collared',
			'Conquered',
			'Chained Up',
			'Chained in the Sex Dungeon',
			'Charmed',
			'Cuddled',
			'Cuddled Hard',
			'Deflowered','Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Dominated in the Dungeon',
			'Enslaved',
			'Exposed in Public',
			'Hotwifed',
			'Humiliated',
			'Hunted For Food',
			'Hypnotized',
			'Impregnated',
			'Imprisoned in the Sex Dungeon',
			'Knocked Up',
			'Leashed',
			'Mastered',
			'Mind-Controlled',
			'Owned',
			'Paddled',
			'Pleasured',
			'Pleasured in Public',
			'Publically Humiliated',
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
			'Tied Up',
			'Tied Up in the Basement',
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
			
