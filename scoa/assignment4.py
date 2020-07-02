import numpy as np
import pandas as pd

class MCPNeuron(object):
    """McCulloch-Pitts Neuron model
    
    Creates a logic gate using a set of weights and 
    an activation threshold. 
    
    Parameters
    ----------
        w : array-like, shape = [1, m_signals]
            Input weights, either -1, 0 or 1.
        t : int 
            Activation threshold.
    
    """
    
    def __init__(self, w = [1,1], t = 1):
        self.w = np.array(w)
        self.t = t
        
    
    def decide(self, message):
        """ Heaviside activation function.
        
        Returns 1 if the weighted sum of the input signals,
        passed as a message, exceeds the threshold value. 
        
        Returns 0, otherwise.
        
        Parameters
        ----------
            message : array-like, shape = [1, m_signals] 
                Array of input signals, either 0 or 1.
        
        Returns
        -------
            y : int
                Output signal, either 0 or 1.
        
        """
        
        x = message # consistency with function notation above
        sum_ = np.inner(self.w,x)
        
        if sum_ >= self.t:
            return 1
        else:
            return 0
        
        
    def TruthTable(self, in_signals, in_labels, out_label):
        """
        Generates a truth table (dataframe) of n messages
        for a logic gate object constructed using the MCPNeuron 
        class, where a message is a 1-D array of m signals.
        
        Parameters
        ----------
            in_signals : array-like, shape = [n_messages, m_signals]
                Set of input signals, each 0 or 1.
            in_labels : list, length = m_signals
                Column labels, as strings, for the input signals
            out_label : str
                Column label for the output signal
            
        Returns
        -------
            table: dataframe, shape = [n_messages, m_signals + 1]
                Truth table showing relationship between in and out
                signals.
        
        """
        
        table = pd.DataFrame(in_signals, columns = in_labels)
        
        out_signals = []
        for row in in_signals:
            signal = self.decide(message = row)
            out_signals.append(signal)
            
        table[out_label] = pd.Series(out_signals)
        return table

in_signals = np.array([[0,0], [0,1], [1,0], [1,1]])
in_labels = ['x1', 'x2']
out_label = 'y'

# instantiate OR gate as an MCP Neuron class
OR = MCPNeuron(w = [1,1], t = 1)
OR_table = OR.TruthTable(in_signals, in_labels = in_labels, out_label = out_label)
print(OR_table)

in_signals = np.array([[0,0], [0,1], [1,0], [1,1]])
# instantiate AND gate as an MCP Neuron class
AND = MCPNeuron(w = [1,1], t = 2)
AND_table = AND.TruthTable(in_signals, in_labels = in_labels, out_label = out_label)
print(AND_table)

NOT_signals = np.array([[0], [1]])
# instantiate NOT gate as an MCP Neuron class
NOT = MCPNeuron(w = [-1], t = 0)
NOT_table = NOT.TruthTable(NOT_signals, in_labels = ['x1'], out_label = 'y')
print(NOT_table)

in_signals = np.array([[0,0], [0,1], [1,0], [1,1]])
# instantiate AND gate as an MCP Neuron class
NAND = MCPNeuron(w = [-1,-1], t = -1)
NAND_table = NAND.TruthTable(in_signals, in_labels = in_labels, out_label = out_label)
print(NAND_table)

in_signals = np.array([[0,0], [0,1], [1,0], [1,1]])
# instantiate AND gate as an MCP Neuron class
NOR = MCPNeuron(w = [-1,-1], t = 0)
NOR_table = NOR.TruthTable(in_signals, in_labels = in_labels, out_label = out_label)
print(NOR_table)


