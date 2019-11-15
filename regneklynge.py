class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
	def __init__(self, noderPerRack):
		pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		pass

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		pass
