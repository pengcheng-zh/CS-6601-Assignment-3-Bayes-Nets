import unittest
from numpy import random

from submission import *
"""
Contains various local tests for Assignment 3.
"""

class ProbabilityTests(unittest.TestCase):

    #Part 1a͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    def test_network_setup(self):
        """Test that the power plant network has the proper number of nodes and edges."""
        security_system = make_security_system_net()
        nodes = security_system.nodes()
        self.assertEqual(len(nodes), 7, msg="incorrect number of nodes")
        total_links = security_system.number_of_edges()
        self.assertEqual(total_links, 6, msg="incorrect number of edges between nodes")

    #Part 1b͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    def test_probability_setup(self):
        """Test that all nodes in the power plant network have proper probability distributions.
        Note that all nodes have to be named predictably for tests to run correctly."""
        # test H distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        security_system = set_probability(make_security_system_net())
        H_node = security_system.get_cpds('H')
        self.assertTrue(H_node is not None, msg='No H node initialized')

        H_dist = H_node.get_values()
        self.assertEqual(len(H_dist), 2, msg='Incorrect H distribution size')
        test_prob = H_dist[0]
        self.assertEqual(round(float(test_prob*100)), 50, msg='Incorrect H distribution')

        # test C distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        security_system = set_probability(make_security_system_net())
        C_node = security_system.get_cpds('C')
        self.assertTrue(C_node is not None, msg='No C node initialized')

        C_dist = C_node.get_values()
        self.assertEqual(len(C_dist), 2, msg='Incorrect C distribution size')
        test_prob = C_dist[0]
        self.assertEqual(round(float(test_prob*100)), 70, msg='Incorrect C distribution')

        # test M distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        security_system = set_probability(make_security_system_net())
        M_node = security_system.get_cpds('M')
        self.assertTrue(M_node is not None, msg='No M node initialized')

        M_dist = M_node.get_values()
        self.assertEqual(len(M_dist), 2, msg='Incorrect M distribution size')
        test_prob = M_dist[0]
        self.assertEqual(round(float(test_prob*100)), 20, msg='Incorrect M distribution')

        # test B distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        security_system = set_probability(make_security_system_net())
        B_node = security_system.get_cpds('B')
        self.assertTrue(B_node is not None, msg='No B node initialized')

        B_dist = B_node.get_values()
        self.assertEqual(len(B_dist), 2, msg='Incorrect B distribution size')
        test_prob = B_dist[0]
        self.assertEqual(round(float(test_prob*100)), 50, msg='Incorrect B distribution')


        # Q distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        # can't test exact probabilities because͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        # order of probabilities is not guaranteed͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        Q_node = security_system.get_cpds('Q')
        self.assertTrue(Q_node is not None, msg='No Q node initialized')
        [cols, rows1, rows2] = Q_node.cardinality
        self.assertEqual(rows1, 2, msg='Incorrect Q distribution size')
        self.assertEqual(rows2, 2, msg='Incorrect Q distribution size')
        self.assertEqual(cols,  2, msg='Incorrect Q distribution size')

        # K distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        K_node = security_system.get_cpds('K')
        self.assertTrue(K_node is not None, msg='No K node initialized')
        [cols, rows1, rows2] = K_node.cardinality
        self.assertEqual(rows1, 2, msg='Incorrect K distribution size')
        self.assertEqual(rows2, 2, msg='Incorrect K distribution size')
        self.assertEqual(cols,  2, msg='Incorrect K distribution size')

        # D distribution͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        D_node = security_system.get_cpds('D')
        self.assertTrue(D_node is not None, msg='No D node initialized')
        [cols, rows1, rows2] = D_node.cardinality
        self.assertEqual(rows1, 2, msg='Incorrect D distribution size')
        self.assertEqual(rows2, 2, msg='Incorrect D distribution size')
        self.assertEqual(cols,  2, msg='Incorrect D distribution size')
        try:
            security_system.check_model()
        except:
            self.assertTrue(False, msg='Sum of the probabilities for each state is not equal to 1 or CPDs associated with nodes are not consistent with their parents')


    #Part 2a Test͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    def test_games_network(self):
        """Test that the games network has the proper number of nodes and edges."""
        games_net = get_game_network()
        nodes = games_net.nodes()
        self.assertEqual(len(nodes), 6, msg='Incorrect number of nodes')
        total_links = games_net.number_of_edges()
        self.assertEqual(total_links, 6, 'Incorrect number of edges')

        # Now testing that all nodes in the games network have proper probability distributions.͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        # Note that all nodes have to be named predictably for tests to run correctly.͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆

        # First testing team distributions.͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        # You can check this for all teams i.e. A,B,C (by replacing the first line for 'B','C')͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆

        A_node = games_net.get_cpds('A')
        self.assertTrue(A_node is not None, 'Team A node not initialized')
        A_dist = A_node.get_values()
        self.assertEqual(len(A_dist), 4, msg='Incorrect distribution size for Team A')
        test_prob = A_dist[0]
        test_prob2 = A_dist[2]
        self.assertEqual(round(float(test_prob*100)),  15, msg='Incorrect distribution for Team A')
        self.assertEqual(round(float(test_prob2*100)), 30, msg='Incorrect distribution for Team A')

        # Now testing match distributions.͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        # You can check this for all matches i.e. AvB,BvC,CvA (by replacing the first line)͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
        AvB_node = games_net.get_cpds('AvB')
        self.assertTrue(AvB_node is not None, 'AvB node not initialized')

        AvB_dist = AvB_node.get_values()
        [cols, rows1, rows2] = AvB_node.cardinality
        self.assertEqual(rows1, 4, msg='Incorrect match distribution size')
        self.assertEqual(rows2, 4, msg='Incorrect match distribution size')
        self.assertEqual(cols,  3, msg='Incorrect match distribution size')

        flag1 = True
        flag2 = True
        flag3 = True
        for i in range(0, 4):
            for j in range(0,4):
                x = AvB_dist[:,(i*4)+j]
                if i==j:
                    if x[0]!=x[1]:
                        flag1=False
                if j>i:
                    if not(x[1]>x[0] and x[1]>x[2]):
                        flag2=False
                if j<i:
                    if not (x[0]>x[1] and x[0]>x[2]):
                        flag3=False

        self.assertTrue(flag1, msg='Incorrect match distribution for equal skill levels')
        self.assertTrue(flag2 and flag3, msg='Incorrect match distribution: teams with higher skill levels should have higher win probabilities')

    #Part 2b Test͏︅͏︀͏︋͏︋͏󠄌͏󠄎͏󠄋͏󠄏͏󠄄͏󠄆
    def test_posterior(self):
        posterior = calculate_posterior(get_game_network())

        self.assertTrue(abs(posterior[0]-0.25)<0.01 and abs(posterior[1]-0.42)<0.01 and abs(posterior[2]-0.31)<0.01, msg='Incorrect posterior calculated')

    # Part 2c Test
    def test_gibbs_sampler(self):
        # init_state = [random.choice(range(0, 4)), random.choice(range(0, 4)), random.choice(range(0, 4)), 0, 0, 2]
        new_state = Gibbs_sampler(get_game_network(), None)
        print(new_state)

    def test_MH_sampler(self):
        sample = MH_sampler(get_game_network(), None)
        print(sample)

    def test_compare_sampling(self):
        Gibbs_convergence, MH_convergence, Gibbs_count, MH_count, MH_rejection_count = compare_sampling(get_game_network(), None)

        print(Gibbs_convergence, MH_convergence, Gibbs_count, MH_count, MH_rejection_count)

    def test_sampling_question(self):
        sampling_question()
if __name__ == '__main__':
    unittest.main()