from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
import pandas as pd



class ArabicNLP(object):

    def __init__(self):
        self.mle_dis = MLEDisambiguator.pretrained()
        self.db = MorphologyDB.builtin_db()
        self.analyzer = Analyzer(self.db)

    def get_diacratics(self, sentence):
        sentence = simple_word_tokenize(sentence)
        disambig = self.mle_dis.disambiguate(sentence)
        diacritized =' '.join([d.analyses[0].analysis['diac'] for d in disambig])
        return diacritized

    def get_properties(self, word):
        show_keys = {'diac':'اعراب','lex':'ریشه','d3tok':'تجزیه','gen':'جنس','num':'عدد','stemgloss':'معنی'}
        analyses = self.analyzer.analyze(word)
        results = []
        for analysis in analyses:
            temp = dict()
            for k,v in analysis.items():
                if k in show_keys:
                    temp[show_keys[k]]=v
            results.append(temp)
        df = pd.DataFrame(results)
        return df.to_html(index=False)
