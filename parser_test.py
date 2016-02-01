import html5lib
with open("test_site/test.html", "rb") as f:
	element = html5lib.parse(f)
	walker = html5lib.getTreeWalker("etree")
	stream = walker(element)
	s = html5lib.serializer.HTMLSerializer()
	output = s.serialize(stream)
	for item in output:
		print("%r" % item)