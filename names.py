#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Names module

from random import *
from util import *

class Names:
	def __init__(self):
		self.FirstNamesList = []
		self.LastNamesList = []
	
	def FirstName(self):
		sFirstName = ""
		iRandIndex = 0
		
		iRandIndex = randint(0, len(self.FirstNamesList) - 1)
		
		sFirstName = self.FirstNamesList[iRandIndex]
		
		return sFirstName

class NamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.FirstNamesList = ['Adam',
			'Adonis',
			'Alex',
			'Alistair',
			'Ambrose',
			'Andre',
			'Archer',
			'Ben','Ben',
			'Bill',
			'Blake',
			'Brad',
			'Bradford',
			'Bradley',
			'Brody',
			'Burt',
			'Buster',
			'Cal',
			'Chad',
			'Christopher',
			'Clint',
			'Clive',
			'Connor',
			'Cullen',
			'Dallas',
			'Dante',
			'Darius',
			'Deacon',
			'Desmond',
			'Dewey',
			'Dick','Dick',
			'Dirk',
			'Dominic',
			'Don',
			'Doug',
			'Drake',
			'Drew',
			'Duane',
			'Earl',
			'Ed',
			'Eduardo',
			'Esteban',
			'Ferdinand',
			'Finn',
			'Flint',
			'Frank',
			'Gary',
			'Gavin',
			'Geoffrey',
			'George',
			'Grant',
			'Greg',
			'Griffin',
			'Grigory',
			'Hank',
			'Harry','Harry','Harry',
			'Hudson',
			'Hugh','Hugh',
			'Hunter',
			'Iain',
			'Ivan',
			'Jack','Jack',
			'James',
			'Javier',
			'Jed',
			'Jerry',
			'Jim',
			'Jimmy',
			'Joe',
			'John',
			'Johnny',
			'Jordan',
			'Josh',
			'Juan',
			'Julian',
			'Kane',
			'Lance','Lance',
			'Larry',
			'Leon',
			'Lex',
			'Liam',
			'Lorenzo',
			'Lou',
			'Luke',
			'Mac',
			'Manuel',
			'Mark',
			'Max',
			'Melvin',
			'Michael',
			'Mike','Mike',
			'Miles',
			'Ned',
			'Nick',
			'Nicolas',
			'Oliver','Oliver',
			'Paul',
			'Pat','Pat',
			'Peter',
			'Philmore',
			'Quentin',
			'Quinn',
			'Rafael',
			'Rafe',
			'Ramon',
			'Randy',
			'Raoul',
			'Reed',
			'Reggie',
			'Reginald',
			'Remington',
			'Rex',
			'Ricardo',
			'Rich','Rich',
			'Rico',
			'Roberto',
			'Roland',
			'Rowan',
			'Royce',
			'Ruben',
			'Russell',
			'Rusty',
			'Ryder',
			'Sawyer','Sawyer',
			'Scott',
			'Sean',
			'Sebastian',
			'Seymour','Seymour','Seymour',
			'Shane',
			'Skip',
			'Stefan',
			'Steve',
			'Sterling',
			'Thad',
			'Tim',
			'Tom',
			'Tremaine',
			'Trevor',
			'Trey',
			'Tristan',
			'Tristan',
			'Tucker',
			'Valentine',
			'Vance',
			'Vaughan',
			'Vicenzo',
			'Vincent',
			'Willie','Willie',
			'Woody','Woody',
			'Xavier',
			'Zeke']	
		
class NamesFemale(Names):
	def __init__(self):
		super().__init__()
		
		self.FirstNamesList = ['Alana',
			'Alexis',
			'Amanda','Amanda','Amanda',
			'Amber',
			'Amelia',
			'Anastasia',
			'Angelica',
			'Anita','Anita','Anita','Anita',
			'Anna',
			'Annabel',
			'Aria',
			'Autumn',
			'Ava',
			'Bella',
			'Belle',
			'Bianca',
			'Bobbi',
			'Brielle',
			'Brigitte',
			'Brynn',
			'Calliope',
			'Candy',
			'Carmina',
			'Cecie',
			'Charity',
			'Chastity',
			'Chelsea',
			'Cherry',
			'Clarissa',
			'Colette',
			'Constance',
			'Cordelia',
			'Daisy',
			'Dani',
			'Daphne',
			'Delilah',
			'Delores',
			'Donna',
			'Eden',
			'Eliza',
			'Elizabeth',
			'Emma',
			'Ericka',
			'Esmerelda',
			'Estelle',
			'Felicia',
			'Felicity',
			'Fiona',
			'Fonda',
			'Francesca',
			'Georgina',
			'Gisele',
			'Honey',
			'Ima',
			'Indigo',
			'Inya',
			'Isabelle',
			'Issa','Issa',
			'Ivana','Ivana','Ivana','Ivana',
			'Jacinda',
			'Jackie',
			'Jaqueline',
			'Jasmine',
			'Josephine',
			'Juliette',
			'Juniper',
			'Jynx',
			'Katrina',
			'Kitty',
			'Lacey',
			'Laurel',
			'Lavinia',
			'Lelani',
			'Leslie',
			'Licorice',
			'Lilah',
			'Lola',
			'Marianna',
			'Marilyn',
			'Marsha',
			'Melina',
			'Misty',
			'Molly',
			'Morgan',
			'Natasha',
			'Nell',
			'Olive',
			'Olivia','Olivia',
			'Ophelia','Ophelia','Ophelia',
			'Paris',
			'Phillippa',
			'Phoebe',
			'Piper',
			'Raven',
			'Regina',
			'Rhoda',
			'Roanna',
			'Rosaline',
			'Rosie','Rosie',
			'Roxanne',
			'Ruby',
			'Sable',
			'Sabrina',
			'Saffron',
			'Satin',
			'Scarlett',
			'Sharon','Sharon','Sharon',
			'Simone',
			'Sophie',
			'Summer',
			'Svetlana',
			'Sydney',
			'Sylvia',
			'Tonya',
			'Tori',
			'Valentina',
			'Vanessa',
			'Veronica',
			'Viola',
			'Violet',
			'Virginia',
			'Vivienne',
			'Zenobia']
			
class LastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = ["Amalova",
			"Ambrose",
			"Avalon",
			"Bangs","Bangs",
			"Banks",
			"Bardot",
			"Beaver","Beaver","Beaver",
			"Belle",
			"Blue",
			"Blush",
			"Bodie",
			"Bradshaw",
			"Bee",
			"Bellemore",
			"Bitt",
			"Black",
			"Bravo",
			"Brest","Brest",
			"Bottoms",
			"Buhnz",
			"Butts",
			"Calderwood",
			"Canon",
			"Charlemaigne",
			"Carron",
			"Cherry",
			"Church",
			"Cox",
			"Crown",
			"Cullen",
			"Cummings",
			"Dalicia",
			"Dallas",
			"Dawn",
			"Deacon",
			"De Boest",
			"Devlyn",
			"Devonshire",
			"Dick",
			"Dix",
			"Douglass",
			"Faulk",
			"Faust",
			"Finch",
			"Fox",
			"Frost",
			"Fuchs",
			"Furrows",
			"George",
			"Goodhead",
			"Gray",
			"Greene",
			"Grotch",
			"Hancock",
			"Handler",
			"Harder",
			"Hardin",
			"Harlowe",
			"Harper",
			"Hawke",
			"Head",
			"Hill",
			"Hoar",
			"Holden",
			"Hump",
			"Hung",
			"Hunt",
			"Hyman",
			"Hunter",
			"Jakov",
			"James",
			"Janus",
			"Johnson",
			"Jones",
			"Juniper",
			"Kayne",
			"Khayler",
			"Khayler",
			"King",
			"Knight",
			"Knockers",
			"Knott",
			"Knox",
			"Knuttz",
			"Koch",
			"Kootch",
			"Kuntz",
			"Lace",
			"Lambert",
			"Lange",
			"La Vigne",
			"Le Rock",
			"Light",
			"Lipps",
			"Long",
			"Lust",
			"Mandelay",
			"Mann",
			"Marcato",
			"Meadows",
			"Mellck",
			"Michaels",
			"Milfinger",
			"Minx",
			"Moore",
			"Moorehead",
			"Morgan",
			"Mount",
			"Mountford",
			"Muncher",
			"Muff",
			"Muffin",
			"Noir",
			"Norton",
			"Onyx",
			"Osias",
			"Oxhard",
			"Peaches",
			"Pearl",
			"Peters",
			"Philmore",
			"Pohl",
			"Polk",
			"Prince",
			"Quinn",
			"Rainne",
			"Ransom",
			"Raven",
			"Ravenswood",
			"Red",
			"Rose",
			"Rhodes",
			"Rodd",
			"Sachs",
			"Scott",
			"Schaft",
			"Skye",
			"Sloan",
			"Snatch",
			"Snow",
			"Sparks",
			"St. Claire",
			"Steele",
			"Sterling",
			"Stiffington",
			"Stiles",
			"Storm",
			"Strange",
			"Stroker",
			"Swallows",
			"Swann",
			"Swift",
			"Tinto",
			"Topper",
			"Torres",
			"Vale",
			"Valentine",
			"Venter",
			"Wang",
			"Weiner",
			"White",
			"Wilde",
			"Winters",
			"Wolf",
			"Wood",
			"Zahara",
			"Zemen"]