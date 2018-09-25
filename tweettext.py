#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from util import *
from misc import *
from generators import *
from names import *
from people import *
from texttoimg import *



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

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets
	
class TweetTxtGen():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def SetPriority(self, sText, List, iPriority):
		for x in range(iPriority):
			List.append(sText)
	
	def GenerateTweet(self):
		self.BookSeller = BookSellers()
		self.Hashtag = Hashtags()
		self.SexyAdj = SexyAdjs()
		
		return ""
		
class TweetTxtGen1(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	ID = 1
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = "The " + SexyAdj.GetWord() + " " + WordList(["read", "book", "ebook"]).GetWord() + " that was " + WordList(["BANNED on", "TOO HOT for", "TOO FILTHY for", "too much for"]).GetWord() + " Amazon! Now available on " + BookSeller.GetWord(NotList = ["Amazon", "Kindle Unlimited"]) 
		if CoinFlip():
			sText += " (from " + AuthorBuilder() + ")"
		#=============================
		
		return sText
		
class TweetTxtGen2(TweetTxtGen):
	# Available soon on Amazon and Smashwords. By Ben Dover
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Coming soon on", "Available soon on", "Look for this soon on", "Get it now on", "Download it today on"]).GetWord() + " " + sBookSeller 
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		
		return sText
		
class TweetTxtGen3(TweetTxtGen):
	# Watch for this naughty ebook on Wattpad and Kobo. By Ben Dover 
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Watch for this", "Look for this", "Keep an eye out for this"]).GetWord() + " " + self.SexyAdj.GetWord() + " ebook on " + sBookSeller
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		#=============================
		
		return sText
		
class TweetTxtGen4(TweetTxtGen):
	# Coming soon to discerning readers on Amazon and Smashwords. By Ben Dover 
	ID = 4
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sBookSeller = self.BookSeller.GetWord()
		
		sText = WordList(["Available soon", "Coming soon", "On its way soon"]).GetWord() + " to " + WordList(["discerning", "discrete", "discriminating"]).GetWord() + " readers on " + sBookSeller 
		if CoinFlip():
			sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
		if CoinFlip():
			sText += ". By " + AuthorBuilder()
		
		return sText
		
class TweetTxtGen5(TweetTxtGen):
	# Ben Dover's Patreon supporters get instant access to all his filthy reads!
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		Supporters = WordList(["Patreon supporters", "supporters on Patreon"])
		Access = WordList(["instant access", "free access", "access"])
		Reads = WordList(["reads", "books", "stories"])
		
		if CoinFlip():
			# male
			sText = AuthorBuilder(Gender = Gender.Male) + "'s "
			sText += Supporters.GetWord() + " get " + Access.GetWord() + " to all his " + self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"
		else:
			# female
			sText = AuthorBuilder(Gender = Gender.Female) + "'s "
			sText += Supporters.GetWord() + " get " + Access.GetWord() + " to all her " + self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"

		
		return sText
		
class TweetTxtGen6(TweetTxtGen):
	# Get excited! The wait is over for Ben Dover's latest sexy release!
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["At last!","At last!","At last!", "Finally!","Finally!", "Get excited!", "It's here!"]).GetWord() + " The wait is over for " + AuthorBuilder() + "'s " + WordList(["newest", "latest"]).GetWord() + " " + self.SexyAdj.GetWord() + " " + WordList(["book","book","book","release","novel","ebook", "release"]).GetWord() + "!"
		
		return sText
		
class TweetTxtGen7(TweetTxtGen):
	# Out soon from Ben Dover
	ID = 7
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Available soon", "Coming soon", "On its way soon", "Out soon", "Arriving soon"]).GetWord() + " from " + AuthorBuilder() 
		
		return sText
		
class TweetTxtGen8(TweetTxtGen):
	# The fisting scene is really surprisingly tasteful!
	ID = 8
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "The " + WordList(["anal", "anal", "orgy", "gangbang", "fisting", "reverse gangbang", "double gangbang", "triple penetration", "deep throat", "incest", "foursome", "fivesome", "MILF orgy", "lesbian orgy", "gay bathhouse", "bukkake", "forced feminization", "choking", "twincest", "Dirty Sanchez", "pee drinking", "wife swapping"]).GetWord() + " scene is " 
		sText += WordList(["surprisingly", "actually surprisingly", "really surprisingly", "actually very", "really quite", "actually unexpectedly", "unexpectedly"]).GetWord() + " " 
		sText += WordList(["tasteful", "tasteful", "loving", "affectionate", "sweet", "heartfelt", "classy", "subdued", "discrete", "charming", "endearing", "thoughtful", "tactful", "wistful"]).GetWord() + "!"
		
		return sText
		
class TweetTxtGen9(TweetTxtGen):
	# If you only read one book this year about clown bukkake, make sure it is this one!
	ID = 9
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "If you only read one book this " + WordList(["year", "year", "year", "month", "month", "decade", "week", "week", "century"]).GetWord() + " about "
		sText += WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat man", "dwarf", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur"]).GetWord() + " "
		sText += WordList(["nipple play", "incest", "threesomes", "fisting", "foursomes", "fivesomes", "bukkake", "bukkake", "forced feminization", "spanking", "rope play", "water-sports", "wife swapping", "69ing", "choking play", "orgies", "gangbangs", "reverse gangbangs", "harems", "lactation"]).GetWord() + ", " 
		sText += WordList(["it should be", "make sure it is", "I heartily recommend"]).GetWord() + " this one!" 

		
		return sText
		
class TweetTxtGen10(TweetTxtGen):
	# Who will Emily choose, the rodeo clown or her step-dad? I was on the edge of my seat! #teamstepdad
	ID = 10
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sSuitor1 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True).Desc.lower()
		sSuitor2 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True).Desc.lower()
		sText = "Who will " + NamesFemale().FirstName() + " choose, " + sSuitor1 + " or " + sSuitor2 + "? I was on the edge of my seat! " 
		if CoinFlip():
			if CoinFlip():
				sText += "#team" + sSuitor1.replace(" ", "").replace("the", "").replace("her", "").replace("-", "")
			else:
				sText += "#team" + sSuitor2.replace(" ", "").replace("the", "").replace("her", "").replace("-", "")
		
		return sText
		
class TweetTxtGen11(TweetTxtGen):
	# Include one little sumo wrestler fisting scene and they ban you from Amazon for life!
	ID = 11
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Include one little "
		sText += WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat-man", "dwarf", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur", "velociraptor", "pro-wrestler"]).GetWord() + " "
		sText += WordList(["anal", "double anal", "nipple play", "fisting", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "bukkake", "feminization", "paddling", "rope play", "water-sports", "wife swapping", "69", "choking", "orgy", "gangbang", "reverse gangbang", "lactation", "double penetration", "triple penetration", "pee-drinking", "Dirty Sanchez"]).GetWord() + " scene, " 
		sText += "and they ban you from Amazon" 
		if CoinFlip():
			sText += " for life"
		sText += "!"
		
		return sText
		
class TweetTxtGen12(TweetTxtGen):
	# Ben Dover is truly the Hemmingway of triple penetration!
	ID = 12
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = AuthorBuilder() + " is truly the " + WordList(["Stephen King", "J.K. Rowling", "Jane Austen", "William Shakespeare", "Shia Lebouf", "Charles Dickens", "Hemmingway", "Agatha Christie", "Maya Angelou", "Tolstoy", "Melville", "Harper Lee", "John Grisham", "Proust", "Emily Dickinson", "Truman Capote", "James Patterson", "Dean Koontz"]).GetWord() + " of "
		sText += WordList(["gay", "lesbian", "MILF", "unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dwarf", "dragon", "orc", "goat man", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur"]).GetWord() + " "
		sText += WordList(["anal", "nipple play", "incest", "fisting", "twincest", "threesomes", "foursomes", "fivesomes", "bukkake", "bukkake", "forced feminization", "spanking", "rope play", "water-sports", "wife swapping", "69", "choking", "orgy", "gangbang", "reverse gangbangs", "lactation", "double penetration", "triple penetration", "porn", "erotica", "edging", "BDSM", "bondage", "cuckolding"]).GetWord() + "!" 

		return sText
		
class TweetTxtGen13(TweetTxtGen):
	# Honestly, these books don't really get going until the 16th book in the series.
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["You know,", "Honestly,", "To tell the truth", "In my opinion", "They say that"]).GetWord() + " these books " + WordList(["really get going after", "really hit their stride after", "don't really get good until", "really take off after", "don't really take off until", "really get good after"]).GetWord() + " the " + str(randint(4, 20)) + "th book in the series."
		
		return sText
		
class TweetTxtGen14(TweetTxtGen):
	# CONTENT WARNING: book contains graphic depictions of veganism.
	ID = 14
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["WARNING", "CONTENT WARNING", "READER WARNING", "ALERT", "READER ALERT"]).GetWord() + ": book contains " 
		sText += WordList(["explicit", "explicit", "explicit", "graphic", "graphic", "vivid"]).GetWord() + " " + WordList(["depictions", "descriptions", "scenes"]).GetWord() + " of " 
		sText += WordList(["vaping", "80's hairstyles", "mullet haircuts", "sports talk radio", "the 1970's", "trips to IKEA", "Bronies", "ferret grooming", "juice cleanses", "large animal husbandry", "women ordering ham-and-pineapple pizza", "women consuming kale smoothies", "veganism", "crossword puzzle solving", "sporks", "fish being reheated in the microwave", "men listening to Nickleback", "tax preparation", "men recording a podcast", "older women discussing their colonoscopies", "Bitcoin investing", "Jazzercize", "essential oil use", "craft-brewed beer enthusiasts", "hipster beard hygene", "bitchy soccer moms", "the music of Ariana Grande"]).GetWord() + "!"
		
		return sText
		
class TweetTxtGen15(TweetTxtGen):
	# I honestly had no idea that I was into bald centaurs until I read this book.
	ID = 15
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "I honestly had no idea that I was into " + WordList(["sexy", "sexy", "sexy", "kinky", "well-hung", "well-endowed", "naughty", "naughty", "gay", "bisexual", "bearded", "bald", "short", "mustachioed", "constantly-aroused", "repressed", "stay-at-home", "stay-at-home", "blue-collar", "Asian", "cuckolded", "lactating", "submissive", "dominant", "well-dressed", "flannel-wearing", "vegan"]).GetWord() + " "
		sText += WordList(["unicorns", "centaurs", "werewolves", "mermen", "dwarves", "dragons", "orcs", "popes", "trolls", "goat-men", "futanari", "aliens", "tentacle monsters", "pirates", "lumberjacks", "trapeze artists", "clowns", "sumo wrestlers", "were-horses", "gorillas", "dinosaurs", "dinosaurs", "blacksmiths", "Japanese businessmen", "guys named Steve"]).GetWord() + " "
		sText += "until I read this book." 
		
		return sText
		
class TweetTxtGen16(TweetTxtGen):
	# SPOILER ALERT: Amber winds up trying twincest. 
	ID = 16
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "SPOILER ALERT: at the end, " + NamesFemale().FirstName() + " " 
		sText += WordList(["does anal", "does lesbian anal", "gets fisted", "has her toes sucked", "tries nipple play", "has a threesome", "has a foursome", "has a fivesome", "gets bukkaked", "tries rope play", "tries water-sports", "becomes a cuck-quean", "tries 69", "gets choked", "tries rimming", "joins an orgy", "gets gangbanged", "tries a reverse gangbang", "tries a double gangbang", "gets double penetrated", "gets triple penetrated", "films a porno", "tries BDSM", "gets tied up", "gets a Dirty Sanchez", "tries girls", "does hot-wifing", "tries lesbian sex", "lets the guys in the gym watch", "walks naked through Times Square", "gets her ass eaten"]).GetWord() 
		
		return sText
		
class TweetTxtGen17(TweetTxtGen):
	# This was a good read, but was the lesbian anal scene really necessary?
	ID = 17
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Delightful and provcative", "Good book", "I enjoyed this", "This was a good read", "Pretty good read", "Fun book", "A real page-turner"]).GetWord() + ", but was the "
		sText += WordList(["anal", "lesbian anal", "fisting", "toe-sucking", "nipple play", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "rope play", "water-sports", "cuck-queaning", "69", "choking", "an orgy", "a gangbang", "a reverse gangbang", "a double gangbang", "double penetration", "triple penetration", "porn", "BDSM", "bondage", "Dirty Sanchez", "hot-wifing", "water-sports"]).GetWord() + " "
		sText += "scene really necessary?"
		
		return sText
		
class TweetTxtGen18(TweetTxtGen):
	# 'Delightful & provactive!' raves Dwarf Fisting Magazine 
	ID = 18
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "'" + WordList(["Delightful & provactive", "Thoughtful & heart-warming", "Heart-warming & transcendant", "Complex yet satisfying", "A real rollercoaster ride", "An emotional rollercoaster", "An edge-of-your-seat, stand-up-and-cheer page-turner", "Kept me literally glued to my Kindle", "Kept me literally nailed to my seat", "Un-put-downable", "A grand slam", "A home-run", "A modern classic"]).GetWord() + "!' "
		sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
		sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
		sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Choking", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 
			
		return sText
		
class TweetTxtGen19(TweetTxtGen):
	# 'Ben Dover's latest is a triumph!' applauds Goat-man Foursome Magazine 
	ID = 19
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "'" + AuthorBuilder() + "'s latest is " + WordList(['a triumph', 'a triumph', 'a massive success', 'a masterpiece', 'an erotic masterpiece', 'a modern classic', 'a sexual classic', 'brilliant', 'a work of genius', 'an unmatched success', 'the next Harry Potter', 'the next 50 Shades of Gray', 'the next Hunger Games', 'un-put-downable', 'heart-warming and satisfying', 'very readable']).GetWord() + "!' "
		sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
		sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
		sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Choking", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 

		
		return sText
		
class TweetTxtGen20(TweetTxtGen):
	# Reply to this tweet and I'll tweet a randomly-generated naughty ebook title @ you!
	ID = 20
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "Reply to this tweet and " 
		if CoinFlip():
			sText += "I'll tweet a " + WordList(["randomly", "computer", "bot", "algorithmically"]).GetWord () + "-generated " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title @ you!"
		else:
			sText += "get a custom " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title of your very own in reply! " + GetEmoji()
		sText += " " + GetEmoji()

		
		return sText
		
class TweetTxtGen21(TweetTxtGen):
	# Follow my sister bot @bot_lust to read naughty excerpts from this book (warning: NSFW!) ;-)
	ID = 21
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + WordList([" my sister bot", " my bot-sibbling", ""]).GetWord() + " @bot_lust " + WordList(["to read what's inside", "to read " + self.SexyAdj.GetWord() + " excerpts from", "to see what's inside", "to read " + SexyAdjs().GetWord() + " bot-generated love scenes from"]).GetWord() + " this book (warning: NSFW!) " + GetEmoji()
		
		return sText
		
class TweetTxtGen22(TweetTxtGen):
	# Features a beautiful interracial relationship between a stegosaur and a reverse merman
	ID = 22
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		Creatures = WordList(["Unicorn", "Centaur", "Man-o-taur", "Gargoyle", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-horse", "T-Rex", "Velociraptor", "Stegosaur", "Plesiosaur", "Pterodactyl", "Reverse Merman", "Cyborg", "Vampire", "Zombie", "Were-shark", "Demon", "Incubus"])
		sSpecies1 = Creatures.GetWord().lower()
		sSpecies2 = Creatures.GetWord(NotList = [sSpecies1]).lower()
		
		sText = "Features a " + WordList(['beautiful', 'tender', 'loving', 'sweet', 'touching', 'heartfelt', 'heart-warming']).GetWord() + " interracial relationship between a " + sSpecies1 + " and a " + sSpecies2 
		
		return sText
		
class TweetTxtGen23(TweetTxtGen):
	# The edging scene goes on for 97 pages
	ID = 23
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "The " + WordList(["anal", "double anal", "lesbian orgy", "reverse gangbang", "Dirty Sanchez", "fisting", "nipple play", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "rope play", "pee-drinking", "cuckolding", "69", "choking", "orgy", "gangbang", "double gangbang", "double penetration", "triple penetration", "BDSM", "bondage", "wife-swapping", "voyeurism", "water-sports", "public humiliation", "lactation", "age play", "mutual masturbation", "edging", "forced orgasm", "domination", "submission"]).GetWord() + " scene goes on for " + str(randint(3,119)) + " pages"
		
		return sText
		
class TweetTxtGen24(TweetTxtGen):
	# I had some trouble keeping the characters straight. Is Gary the blonde fireman with the 7" schlong or the brunette fireman with the 8" schlong?
	ID = 24
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sText = ""
		
		sText = "I had " + WordList(["a hard time", "some trouble", "a bit of a problem", "some difficulty"]).GetWord() + " keeping the characters straight. "
		if CoinFlip():
			sName = NamesFemale().FirstName()
			Lady = WordList(misc.TropesBadFemale().List + misc.TropesGoodFemale().List + misc.ProfFemale().List).GetWord().lower()
			iLength = WordList([32,34,36]).GetWord()
			sCupSize = WordList(['D', 'DD']).GetWord()
			BoobNames = WordList(['boobs', 'tits', 'gazongas', 'coconuts', 'melons', 'bazookas', 'hooters', 'tatas', 'jugs', 'rack', 'titties', 'cantalopes', 'grapefruits', 'pom-poms'])
			sBoobName = BoobNames.GetWord()
			
			sText += "Was " + sName + " the blonde " + Lady + " with the " + str(iLength) + sCupSize + " " + sBoobName + " or the brunette " + Lady + " with the " + str(iLength + 2) + sCupSize + "D " + sBoobName + "?"
		else:
			sName = NamesMale().FirstName()
			Dude = WordList(misc.SpeciesMale().List + misc.ProfMale().List + misc.TropesMale().List).GetWord().lower()
			iLength = randint (6, 12)
			PenisNames = WordList(['schlong', 'dick', 'bagpipe', 'rod', 'pole', 'willy', 'johnson', 'dingus', 'dong', 'package', 'prick', 'sausage', 'slim jim', 'stiffy', 'swizzle stick', 'tool', 'trouser snake', 'wiener'])
			sPenisName = PenisNames.GetWord()
			
			sText += "Was " + sName + " the blonde " + Dude + " with the " + str(iLength) + "\" " + sPenisName + " or the brunette " + Dude + " with the " + str(iLength + 1) + "\" " + sPenisName + "?"
		return sText
		
# class TweetTxtGen25(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 25
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText
		
# class TweetTxtGen26(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 26
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText
		
# class TweetTxtGen27(TweetTxtGen):
	# The sexy read that was BANNED on Amazon! Now available on Smashwords
	# ID = 27
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sText = ""
		
		# return sText
		

class TweetTxtGenSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in TweetTxtGen.__subclasses__():
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
					

		
def GetImgTweetText(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetTxtHistoryQ = None):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	Generator = None
	GenType = None 
	HistoryQ = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	#print("GetTweet() Generator Type is " + str(GenType))
	
	if not TweetTxtHistoryQ is None:
		HistoryQ = TweetTxtHistoryQ
	
	iSwitch = 999
	
	GenSel = TweetTxtGenSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if not gen == None:
			Generator = gen
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
		while not HistoryQ.PushToHistoryQ(gen.ID):
			gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
	
	if not gen is None:
		sText = gen.GenerateTweet()
	else:
		sText = ""

	# bots using hashtags can lead to shadowbans. so we have to use sparingly.
	if randint(1,5) == 5:
		sText += " #" + Hashtags().GetWord()
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	# else:
		# sText = TweetText[randint(0, len(TweetText) - 1)] 
		# while IsTweetTooLong(sText):
			# sText = TweetText[randint(0, len(TweetText) - 1)] 
	
	return sText 
	
