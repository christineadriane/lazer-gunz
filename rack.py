from node import Node

## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self, maxNoder):
		self._listNoder = []
		self._maxNoder = maxNoder

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self._listNoder.append(node)

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self._listNoder)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		antProsRack = 0
		# her skal vi gå gjennom hvert objekt i lista. Programmet "vet" at lista er full
		# av objekter av Node-klassen. Når vi da bruker "for e in lista", itererer gjennom
		# selve elementet og ikke plasseringen (indeksen). Derfor bruker vi e.antProsessorer()
		# etterpå. Da skjønner den at metoden hører til Node-klassen. 
		for e in self._listNoder:
			antallProsPerNode = e.antProsessorer()
			antProsRack += antallProsPerNode
		return antProsRack

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass
