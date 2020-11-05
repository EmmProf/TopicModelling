from ipywidgets import FloatText, Output, VBox, HBox, Layout, Button

def deTokenize(corpus):
  '''
  Detokenize a tokenized corpus.
  
  Parameters:
      corpus (list): a tokenized corpus.
  Returns:
      deTokenizedCorpus (list): the joined corpus.
  '''
  deTokenizedCorpus = list(map(" ".join,corpus))
  return deTokenizedCorpus

def corpusVisualizer(corpus,output):
  '''
  Returns a small UI which uses ipywidgets to look into the corpus.
  
  Parameters:
      corpus (list):The corpus (list of strings).
      output (Output widget): The output widget which will contain the visualization.
  
  Returns:
      docVisualizer (VBox widget):Small UI to visualize docs in the corpus.   
  '''
  n = len(corpus)
  indexSelector = FloatText(value=0,min=0,max=n,step=1)
  Show = Button(description="Show")
  Clear = Button(description="Clear")
  def showDoc(b):
    with output:
      doc_i = int(indexSelector.value)
      indexSelector.value += 1
      print("Doc " + str(doc_i) + ": ",corpus[doc_i])
  Show.on_click(showDoc)
  Clear.on_click(lambda b: output.clear_output())
  docVisualizer = VBox(children=[HBox([indexSelector,Show,Clear]),output])
  return docVisualizer
  
def compareCorpuses(corpus1,corpus2,output):
  '''
  Output a visualizer to compare corpuses.

  Parameters:
    corpus1 (list): first corpus.
    corpus2 (list): second corpus.

  Returns:
    corpusVisulazer (VBox widget): a visualizer to compare the corpuses.
  '''
  if type(corpus1[0]) is list: corpus1 = deTokenize(corpus1)
  if type(corpus2[0]) is list: corpus2 = deTokenize(corpus2)
  return corpusVisualizer([s1 + "\n " + s2 for s1,s2 in zip(corpus1,corpus2)],output)
  