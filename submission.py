import sys

'''
WRITE YOUR CODE BELOW.
'''
from numpy import zeros, float32
#  pgmpy͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
import pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
#You are not allowed to use following set of modules from 'pgmpy' Library.͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
#
# pgmpy.sampling.*͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
# pgmpy.factors.*͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
# pgmpy.estimators.*͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆

def make_security_system_net():
    """
        Create a Bayes Net representation of the above security system problem. 
        Use the following as the name attribute: "H","C", "M","B", "Q", 'K",
        "D"'. (for the tests to work.)
    """
    BayesNet = BayesianNetwork()
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError
    return BayesNet


def set_probability(bayes_net):
    """
        Set probability distribution for each node in the security system.
        Use the following as the name attribute: "H","C", "M","B", "Q", 'K",
        "D"'. (for the tests to work.)
    """
    # TODO: set the probability distribution for each node͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError    
    return bayes_net


def get_marginal_double0(bayes_net):
    """
        Calculate the marginal probability that Double-0 gets compromised.
    """
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError
    return double0_prob


def get_conditional_double0_given_no_contra(bayes_net):
    """
        Calculate the conditional probability that Double-0 gets compromised
        given Contra is shut down.
    """
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError
    return double0_prob


def get_conditional_double0_given_no_contra_and_bond_guarding(bayes_net):
    """
        Calculate the conditional probability that Double-0 gets compromised
        given Contra is shut down and Bond is reassigned to protect M.
    """
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError
    return double0_prob


def get_game_network():
    """
        Create a Bayes Net representation of the game problem.
        Name the nodes as "A","B","C","AvB","BvC" and "CvA".  
    """
    BayesNet = BayesianNetwork()
    # TODO: fill this out͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError    
    return BayesNet


def calculate_posterior(bayes_net):
    """
        Calculate the posterior distribution of the BvC match given that A won against B and tied C. 
        Return a list of probabilities corresponding to win, loss and tie likelihood.
    """
    posterior = [0,0,0]
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError
    return posterior # list 


def Gibbs_sampler(bayes_net, initial_state):
    """
        Complete a single iteration of the Gibbs sampling algorithm 
        given a Bayesian network and an initial state value. 
        
        initial_state is a list of length 6 where: 
        index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
        index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)
        
        Returns the new state sampled from the probability distribution as a tuple of length 6.
        Return the sample as a tuple. 

        Note: You are allowed to calculate the probabilities for each potential variable
        to be sampled. See README for suggested structure of the sampling process.
    """
    sample = tuple(initial_state)    
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    variable_index = None # Your chosen variable

    if variable_index == 0:
        # Sample A͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        raise NotImplementedError
    elif variable_index == 1:
        # Sample B͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        raise NotImplementedError
    elif variable_index == 2:
        # Sample C͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        raise NotImplementedError

    elif variable_index == 4:
        # Sample BvC͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        raise NotImplementedError
    
    else:
        raise ValueError("Variable index out of range")


    return sample


def MH_sampler(bayes_net, initial_state):
    """
        Complete a single iteration of the MH sampling algorithm given a Bayesian network and an initial state value. 
        initial_state is a list of length 6 where: 
        index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
        index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)    
        Returns the new state sampled from the probability distribution as a tuple of length 6. 
    """
    A_cpd = bayes_net.get_cpds("A")      
    AvB_cpd = bayes_net.get_cpds("AvB")
    match_table = AvB_cpd.values
    team_table = A_cpd.values
    sample = tuple(initial_state)    
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    raise NotImplementedError    
    return sample


def compare_sampling(bayes_net, initial_state):
    """
        Compare Gibbs and Metropolis-Hastings sampling by calculating how long it takes for each method to converge.
    """    
    Gibbs_count = 0
    MH_count = 0
    MH_rejection_count = 0
    Gibbs_convergence = [0,0,0] # posterior distribution of the BvC match as produced by Gibbs 
    MH_convergence = [0,0,0] # posterior distribution of the BvC match as produced by MH
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    
    raise NotImplementedError        
    return Gibbs_convergence, MH_convergence, Gibbs_count, MH_count, MH_rejection_count


def sampling_question():
    """
        Question about sampling performance.
    """
    # TODO: assign value to choice and factor͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    
    raise NotImplementedError
    choice = 2
    options = ['Gibbs','Metropolis-Hastings']
    factor = 0
    return options[choice], factor


def return_your_name():
    """
        Return your name from this function
    """
    # TODO: finish this function͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    # Contact me with email: zhangpch666@163.com or Wechat: YSYY66
    
    raise NotImplementedError
