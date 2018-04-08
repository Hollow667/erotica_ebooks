# Text-to-Image module

import os, sys, time
from PIL import Image, ImageDraw, ImageFont
from random import *
from util import *

PATH = "resources/"
FONT = "NoticiaText-Regular.ttf"
MAX_IMG_NUM = 37

BGImgQ = HistoryQ(iQSize = 5)

def SaveImg(img, filename = ""):
	try:
		if filename == "":
			img.save('test' + str(time.time()) + '.png')
		else:
			img.save(filename)
	except IOError as e:
		print("***ERROR***\nFile save failed in SaveImg()\n" + e.reason)
		
		
def WrapText(sText, font, offset_width):
	# break string into multi-lines that fit base_width
	Lines = []
	
	bEndOfText = False
	iLastWhtSpc = 0
	iLineStart = 0
	while not bEndOfText:
		width_of_line = 0
		iLastWhtSpc = iLineStart
		
		for x in range(iLineStart, len(sText)):
			if sText[x].isspace() or sText[x] == "-":
				iLastWhtSpc = x
			#print("WrapText() x = " + str(x) + ", iLastWhtSpc = " + str(iLastWhtSpc))
			#print("WrapText() sTest[" + str(x) + "] is '" + sText[x] + "'")
			char_size = font.getsize(sText[x])
			width_of_line += char_size[0]
			
			if sText[x] == "\n" or width_of_line >= offset_width:
				if iLastWhtSpc >= iLineStart:
					#print("WrapText() iLastWhtSpc > iLineStart and line is too wide. Break and append to Lines[]")
					Lines.append(sText[iLineStart:iLastWhtSpc])
					#print("WrapText() current line is [" + sText[iLineStart:iLastWhtSpc] + "]")
					iLineStart = iLastWhtSpc + 1
					break
				else:
					#print("WrapText() iLastWhtSpc <= iLineStart and line is too wide. Break and append to Lines[]")
					iLastWhtSpc = int((x - iLineStart)/2) 
					Lines.append(sText[iLineStart:iLastWhtSpc])
					#print("WrapText() current line is [" + sText[iLineStart:iLastWhtSpc] + "]")
					iLineStart = iLastWhtSpc + 1
					break
			else:
				#print("WrapText() line is not too wide.")
				if x == len(sText) - 1:
					bEndOfText = True
					Lines.append(sText[iLineStart:len(sText)])
					#print("WrapText() current line is [" + sText[iLineStart:len(sText)] + "]")
					break 
	
	return Lines
	
def CalcTotalLineHeight(Lines, font):
	iTotLineHeight = 0
	for line in Lines:
		if line.isspace() or line == "":
			iTotLineHeight += font.getsize("a")[1] / 2
		else:
			iTotLineHeight += font.getsize(line)[1]
		#print("CalcTotalLineHeight() iTotLineHeight is now " + str(iTotLineHeight))
		
	return iTotLineHeight
		
def FormatText(sText, size, color):
	Lines = []
	base_width = size[0]
	base_height = size[1]
	
	xOffset = .018
	yOffset = .018
	
	offset_width = round(base_width - (base_width * xOffset * 2), 0)
	offset_height = round(base_height - (base_height * yOffset * 2), 0)
	
	iFontSize = 30
	
	#print("FormatText() sText length: " + str(len(sText)))
	iTextLen = len(sText)
	if iTextLen <= 140:
		iFontSize = 95
	elif iTextLen <= 185:	#(+  45)
		iFontSize = 80
	elif iTextLen <= 255:	#(+  70)
		iFontSize = 70
	elif iTextLen <= 335:	#(+  80)
		iFontSize = 60
	elif iTextLen <= 520:	#(+ 185)
		iFontSize = 50
	elif iTextLen <= 685:
		iFontSize = 44
	elif iTextLen <= 1000:
		iFontSize = 36
	elif iTextLen <= 1400:
		iFontSize = 34
	else: 
		iFontSize = 30

		
	#print("FormatText() Starting font size is " + str(iFontSize))
	
	font = ImageFont.truetype(PATH + FONT, size = iFontSize, layout_engine = ImageFont.LAYOUT_RAQM)
	
	iTotLineHeight = 0
	
	Lines = WrapText(sText, font, offset_width)
	
	iTotLineHeight = CalcTotalLineHeight(Lines, font)
	
	#if the height of our lines exceeds the height of the image area, reduce font and try again
	while iTotLineHeight > offset_height:
		print("FormatText() offset_height exceeded for font size " + str(iFontSize) + ", shrinking font by 3 and trying again")
		iFontSize += (-3)
		
		font = ImageFont.truetype(PATH + FONT, size = iFontSize, layout_engine = ImageFont.LAYOUT_RAQM)
		
		Lines = WrapText(sText, font, offset_width)
		
		iTotLineHeight = CalcTotalLineHeight(Lines, font)
		
	print("FormatText() Final font size is " + str(iFontSize))
	#print(Lines)
			
	ImgTxt = Image.new('RGBA', (base_width, base_height), (0,0,0,95))
	draw = ImageDraw.Draw(ImgTxt)
			
	#print("FormatText() Base Height = " + str(base_height) + ", Total Line Height = " + str(iTotLineHeight))
	#print("FormatText() Vertical offset = " + str(round(((offset_height - iTotLineHeight)/2))))
																		#47.952
																		#1284.048
	y_text = 0
	for x in range(0, len(Lines)):
		width, height = (0, 0)
		if Lines[x].isspace() or Lines[x] == "":
			width, height = font.getsize("a")
			height = height / 2
			#print("FormatText() Empty line found, adding height of " + str(width) + " to vertical offset")
		else:
			width, height = font.getsize(Lines[x])

			draw.text((int(base_width * xOffset), round((offset_height - iTotLineHeight)/2) + y_text), Lines[x], font=font, fill=color)
		y_text += height
		
	# y_text = 0
	# for line in Lines:
		# if line.isspace() or line == "":
			# width, height = font.getsize(".")
		# else:
			# width, height = font.getsize(line)
		# draw.text(((base_width - width) / 2, y_text), line, font=font, fill=color)
		# y_text += height
	
	return ImgTxt

def DrawText(size, sText, color): 
	bck_width = size[0]
	bck_height = size[1]
	
	stest = "d e"
	#print(stest[1].isspace())
	ImgTxt = FormatText(sText, (bck_width - int(bck_width * .075), bck_height - int(bck_height * .075)), color)
	
	ImgFrame = Image.new('RGBA', size, (255,255,255,0))
	
	ImgFrame.paste(ImgTxt, (int((bck_width - ImgTxt.size[0])/2), int((bck_height - ImgTxt.size[1])/2)))

	return ImgFrame
	
def GetBGImg(iPicNo = 0):
	BGImg = None 
	
	if iPicNo == 0:
		iPicNo = randint(1, MAX_IMG_NUM)

		while not BGImgQ.PushToHistoryQ(iPicNo):
			iPicNo = randint(1, MAX_IMG_NUM)

	try:
		BGImg = Image.open(PATH + "bg_" + str(iPicNo) + ".png").convert('RGBA')
	except IOError as e:
		print("***ERROR***\nFile save failed in SaveImg()\n" + e.reason)
	
	return BGImg

def CreateImg(sText):
	# create Image object with the input image
	
	#for i in range(1, MAX_IMG_NUM + 1):
	#ImgBase = GetBGImg(iPicNo = i)
	ImgBase = GetBGImg()
	
	color = 'rgb(255, 255, 255)' # black color
	
	ImgTxt = DrawText(ImgBase.size, sText, color)
	 
	# composite the text and base images

	ImgOut = Image.alpha_composite(ImgBase, ImgTxt)
	 
	# save the edited image
	 
	return ImgOut














