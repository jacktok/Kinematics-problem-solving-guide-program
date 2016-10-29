from wordcut.wordGroup import WordGroup
import pprint
a=WordGroup()
pp = pprint.PrettyPrinter(indent=10)
pp.pprint(a.dumpGrammar())