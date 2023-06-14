import pywhatkit as pw

txt = """The classical waterfall model is the basic software development life cycle model. It is very 
simple but idealistic. Earlier this model was very popular but nowadays it is not used. But it 
is very important because all the other software development life cycle models are based on 
the classical waterfall model. 
The classical waterfall model divides the life cycle into a set of phases. This model considers 
that one phase can be started after the completion of the previous phase. That is the output 
of one phase will be the input to the next phase. Thus the development process can be 
considered as a sequential flow in the waterfall. Here the phases do not overlap with each 
other."""

pw.text_to_handwriting(txt,"demotext.png",[0,0,138])
print("End")