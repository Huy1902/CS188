from click.core import batch
from pydeck import Layer

import nn


class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        return nn.DotProduct(x, self.get_weights())

    def get_prediction(self, x):

        """
        Calculates the predicted class for a single data point `x`.
        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        # a node
        score_node = self.run(x)
        if nn.as_scalar(score_node) >= 0:
            return 1
        return -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        converged = False
        batch_size = 1
        while not converged:
            for x, y in dataset.iterate_once(batch_size):
                prediction = self.get_prediction(x)
                # binary perceptron
                if prediction != nn.as_scalar(y):
                    self.w.update(x, nn.as_scalar(y))
            converged = True
            for x, y in dataset.iterate_once(batch_size):
                prediction = self.get_prediction(x)
                if prediction != nn.as_scalar(y):
                    converged = False
                    break


class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """

    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.batch_size = 50
        self.output = 1
        self.input = 1
        self.hidden = 100

        self.w1 = nn.Parameter(self.input, self.hidden)
        self.b1 = nn.Parameter(1, self.hidden)
        self.w2 = nn.Parameter(self.hidden, self.output)
        self.b2 = nn.Parameter(1, self.output)
        self.learning_rate = 0.01
        self.loss_limit = 0.02

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"
        xw1 = nn.Linear(x, self.w1)
        hidden1 = nn.ReLU(nn.AddBias(xw1, self.b1))
        xw2 = nn.Linear(hidden1, self.w2)
        predicted_y = nn.AddBias(xw2, self.b2)
        return predicted_y

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SquareLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        print(dataset)
        converged = False
        while not converged:
            converged = True
            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x, y)
                if loss.data >= self.loss_limit:
                    grad_w1, grad_b1, grad_w2, grad_b2 = nn.gradients(loss, [self.w1, self.b1, self.w2, self.b2])
                    self.w1.update(grad_w1, -self.learning_rate)
                    self.b1.update(grad_b1, -self.learning_rate)
                    self.w2.update(grad_w2, -self.learning_rate)
                    self.b2.update(grad_b2, -self.learning_rate)
                    converged = False


class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """

    class NeuralLayer:
        def __init__(self, input_size, output_size):
            self.w = nn.Parameter(input_size, output_size)
            self.b = nn.Parameter(1, output_size)

        def update(self, gradient, learning_rate):
            self.w.update(gradient[0], learning_rate)
            self.b.update(gradient[1], learning_rate)

    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.batch_size = 200

        self.layer1 = self.NeuralLayer(784, 250)
        self.layer2 = self.NeuralLayer(250, 150)

        self.layer3 = self.NeuralLayer(150, 10)
        self.learning_rate = 0.34

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        hidden_node1 = nn.ReLU(nn.AddBias(nn.Linear(x, self.layer1.w), self.layer1.b))
        hidden_node2 = nn.ReLU(nn.AddBias(nn.Linear(hidden_node1, self.layer2.w), self.layer2.b))
        hidden_node3 = nn.AddBias(nn.Linear(hidden_node2, self.layer3.w), self.layer3.b)
        return hidden_node3

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SoftmaxLoss(self.run(x), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        print(dataset)
        converged = False
        while dataset.get_validation_accuracy() < 0.98:
            converged = True
            for x, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(x, y)
                w1, b1, w2, b2, w3, b3 = nn.gradients(loss, [self.layer1.w, self.layer1.b,
                                                             self.layer2.w, self.layer2.b,
                                                             self.layer3.w, self.layer3.b])
                self.layer1.w.update(w1, -self.learning_rate)
                self.layer1.b.update(b1, -self.learning_rate)
                self.layer2.w.update(w2, -self.learning_rate)
                self.layer2.b.update(b2, -self.learning_rate)
                self.layer3.w.update(w3, -self.learning_rate)
                self.layer3.b.update(b3, -self.learning_rate)


class LanguageIDModel(object):
    """
    A model for language identification at a single-word granularity.

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """

    class NeuralLayer:
        def __init__(self, input_size, output_size):
            self.w = nn.Parameter(input_size, output_size)
            self.b = nn.Parameter(1, output_size)

        def update(self, gradient, learning_rate):
            self.w.update(gradient[0], learning_rate)
            self.b.update(gradient[1], learning_rate)

    def __init__(self):
        # Our dataset contains words from five different languages, and the
        # combined alphabets of the five languages contain a total of 47 unique
        # characters.
        # You can refer to self.num_chars or len(self.languages) in your code
        self.learning_rate = 0.31
        self.num_chars = 47
        self.languages = ["English", "Spanish", "Finnish", "Dutch", "Polish"]

        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.layer1 = self.NeuralLayer(self.num_chars, 100)
        self.layer2 = self.NeuralLayer(100, 100)
        self.layer3 = self.NeuralLayer(100, 5)

        self.hidden_layer1 = self.NeuralLayer(100, 100)
        self.hidden_layer2 = self.NeuralLayer(100, 100)

        self.batch_size = 100

    def run(self, xs):
        """
        Runs the model for a batch of examples.

        Although words have different lengths, our data processing guarantees
        that within a single batch, all words will be of the same length (L).

        Here `xs` will be a list of length L. Each element of `xs` will be a
        node with shape (batch_size x self.num_chars), where every row in the
        array is a one-hot vector encoding of a character. For example, if we
        have a batch of 8 three-letter words where the last word is "cat", then
        xs[1] will be a node that contains a 1 at position (7, 0). Here the
        index 7 reflects the fact that "cat" is the last word in the batch, and
        the index 0 reflects the fact that the letter "a" is the inital (0th)
        letter of our combined alphabet for this task.

        Your model should use a Recurrent Neural Network to summarize the list
        `xs` into a single node of shape (batch_size x hidden_size), for your
        choice of hidden_size. It should then calculate a node of shape
        (batch_size x 5) containing scores, where higher scores correspond to
        greater probability of the word originating from a particular language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
        Returns:
            A node with shape (batch_size x 5) containing predicted scores
                (also called logits)
        """
        "*** YOUR CODE HERE ***"
        for i in range(len(xs)):
            if i == 0:
                layer1 = nn.ReLU(nn.AddBias(nn.Linear(xs[i], self.layer1.w), self.layer1.b))
                hidden = (nn.AddBias(nn.Linear(layer1, self.layer2.w), self.layer2.b))
            else:
                hidden_layer1 = nn.ReLU(nn.AddBias(
                    nn.Add(nn.Linear(xs[i], self.layer1.w), nn.Linear(hidden, self.hidden_layer1.w)),
                    self.hidden_layer1.b))
                hidden_layer2 = nn.ReLU(nn.AddBias(nn.Linear(hidden_layer1, self.hidden_layer2.w), self.hidden_layer2.b))
                hidden = hidden_layer2
        return nn.AddBias(nn.Linear(hidden, self.layer3.w), self.layer3.b)

    def get_loss(self, xs, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 5). Each row is a one-hot vector encoding the correct
        language.

        Inputs:
            xs: a list with L elements (one per character), where each element
                is a node with shape (batch_size x self.num_chars)
            y: a node with shape (batch_size x 5)
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"
        return nn.SoftmaxLoss(self.run(xs), y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        while dataset.get_validation_accuracy() < 0.85:
            for xs, y in dataset.iterate_once(self.batch_size):
                loss = self.get_loss(xs, y)
                layer1_w, layer1_b, layer2_w, layer2_b, layer3_w, layer3_b, hidden_layer1_w, hidden_layer1_b, hidden_layer2_w, hidden_layer2_b = nn.gradients(
                    loss, [self.layer1.w, self.layer1.b,
                           self.layer2.w, self.layer2.b,
                           self.layer3.w, self.layer3.b,
                           self.hidden_layer1.w, self.hidden_layer1.b,
                           self.hidden_layer2.w, self.hidden_layer2.b])
                self.layer1.w.update(layer1_w, -self.learning_rate)
                self.layer1.b.update(layer1_b, -self.learning_rate)
                self.layer2.w.update(layer2_w, -self.learning_rate)
                self.layer2.b.update(layer2_b, -self.learning_rate)
                self.layer3.w.update(layer3_w, -self.learning_rate)
                self.layer3.b.update(layer3_b, -self.learning_rate)
                self.hidden_layer1.w.update(hidden_layer1_w, -self.learning_rate)
                self.hidden_layer1.b.update(hidden_layer1_b, -self.learning_rate)
                self.hidden_layer2.w.update(hidden_layer2_w, -self.learning_rate)
                self.hidden_layer2.b.update(hidden_layer2_b, -self.learning_rate)