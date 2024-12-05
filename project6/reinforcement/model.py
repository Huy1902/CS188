import nn

class DeepQNetwork():
    """
    A model that uses a Deep Q-value Network (DQN) to approximate Q(s,a) as part
    of reinforcement learning.
    """

    def __init__(self, state_dim, action_dim):
        self.num_actions = action_dim
        self.state_size = state_dim

        self.learning_rate = 0.5
        self.numTrainingGames = 1000
        self.batch_size = 1000

        self.num_hidden_node = 2**14
        self.num_hidden_node2 = 2**12

        # Define the neural network layers
        self.w1 = nn.Parameter(state_dim, self.num_hidden_node)
        self.w2 = nn.Parameter(self.num_hidden_node, self.num_hidden_node2)
        self.w5 = nn.Parameter(self.num_hidden_node2, action_dim)

        # Collect all parameters
        self.parameters = [self.w1, self.w2, self.w5]

    def set_weights(self, layers):
        self.parameters = layers

    def get_loss(self, states, Q_target):
        """
        Returns the Squared Loss between Q values currently predicted
        by the network, and Q_target.
        Inputs:
            states: a (batch_size x state_dim) numpy array
            Q_target: a (batch_size x num_actions) numpy array, or None
        Output:
            loss node between Q predictions and Q_target
        """
        if Q_target is None:
            return 0
        return nn.SquareLoss(self.run(states), Q_target)

    def run(self, states):
        """
        Runs the DQN for a batch of states.
        The DQN takes the state and returns the Q-values for all possible actions
        that can be taken. That is, if there are two actions, the network takes
        as input the state s and computes the vector [Q(s, a_1), Q(s, a_2)]
        Inputs:
            states: a (batch_size x state_dim) numpy array
            Q_target: a (batch_size x num_actions) numpy array, or None
        Output:
            result: (batch_size x num_actions) numpy array of Q-value
                scores, for each of the actions
        """
        hidden_node = nn.ReLU(nn.Linear(states, self.parameters[0]))
        for _ in range(1, len(self.parameters)):
            hidden_node = nn.ReLU(nn.Linear(hidden_node, self.parameters[_]))
        return hidden_node

    def gradient_update(self, states, Q_target):
        """
        Update your parameters by one gradient step with the .update(...) function.
        Inputs:
            states: a (batch_size x state_dim) numpy array
            Q_target: a (batch_size x num_actions) numpy array, or None
        Output:
            None
        """
        loss = self.get_loss(states, Q_target)
        update = nn.gradients(loss, self.parameters)
        for _ in range(len(self.parameters)):
            self.parameters[_].update(update[_], -self.learning_rate)
