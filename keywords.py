import re
# from urllib import urlopen
from calais import Calais #https://code.google.com/p/python-calais/

CALAIS_API_KEY = "an5duh4ktc5twbfysaakjhxs"

#need to espace any question marks from URLs

testUrls = [
"https://twitter.com/sannabh", 
"http://www.gardenista.com/posts/closet-cleanout-the-only-10-pieces-of-clothing-you-need-organize", 
"http://www.dianaantohe.com/",
"http://www.apartmenttherapy.com/beyond-the-bachelorette-pad-bl-136827",
"https://medium.com/matter/miss-american-dream-31c823ad0e5a",
"http://www.culturemachine.net/index.php/cm/issue/view/24",
"http://canopycanopycanopy.com/issues/14/contents/the_venus_problem",
"http://www.buzzfeed.com/melissaharrison/vegetable-noodle-recipes",
"http://www.refinery29.com/best-coffees",
"http://www.buzzfeed.com/food",
"http://www.buzzfeed.com/candacelowry/bakeries-around-the-world-you-should-visit-before-you-die",
"http://stackoverflow.com/questions/3215830/extract-meta-keywords-from-webpage"
]

for url in testUrls:
	print "   "
	print url
	calais = Calais(CALAIS_API_KEY, submitter="historySnooper test")
	result = calais.analyze_url(url)
	result.print_summary()
	print "--"
	result.print_topics()
	print "--"
	result.print_entities()
	print "--"
	result.print_relations()
	# f = urlopen( "http://www.w3schools.com/XPath/xpath_syntax.asp" ).read()
	# print re.search( "<meta name=\"Keywords\".*?content=\"([^\"]*)\"", f ).group( 1 )