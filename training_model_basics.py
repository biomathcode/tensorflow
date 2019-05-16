import tensorflow as tf
tf.enable_eager_execution()
import matplotlib.pyplot as plt

class Model(object):
    def __init__(self):
        self.W = tf.Variable(5.0)
        self.b = tf.Variable(0.0)

    def __call__(self, x):
        return self.W* x + self.b
model = Model()

assert model(3.0).numpy() == 15.0
## we will define loss function here

def loss(predicted_y, desired_y):
    return tf.reduce_mean(tf.square(predicted_y - desired_y))
# Creating dataset with some noise.

TRUE_W = 3.0

TRUE_b = 2.0

NUM_EXAMPLES = 100

inputs = tf.random_normal(shape=[NUM_EXAMPLES])
noise = tf.random_normal(shape=[NUM_EXAMPLES])
outputs = inputs * TRUE_W + TRUE_b + noise

plt.scatter(inputs, outputs, c='b')
plt.scatter(inputs, model(outputs), c="r")
plt.show()

print('current: loss'),
print(loss(model(inputs), outputs).numpy())

## Training loop
# gradient descent algorithm
def train(model, inputs, outputs, learning_rate):
    with tf.GradientTape() as t:
        current_loss = loss(model(inputs), outputs)
    dW, db = t.gradient(current_loss, [model.W, model.b])
    model.W.assign_sub(learning_rate * dW)
    model.b.assign_sub(learning_rate * db)
model = Model()

Ws, bs =[],[]
epochs = range(15)
for epoch in epochs:
    Ws.append(model.W.numpy())
    bs.append(model.b.numpy())
    current_loss = loss(model(inputs), outputs)

    train(model, inputs, outputs, learning_rate=0.1)
    print('Epoch %2d: W=%1.2f b=%1.2f, loss=%2.5f' %(epoch, Ws[-1], bs[-1], current_loss))


#Let's plot it all

plt.plot(epochs, Ws, 'r',
         epochs,bs, 'b')
plt.plot([TRUE_W] *len(epochs), 'r--',
         [TRUE_b] *len(epochs), 'b--')
plt.legend(['W','b', 'true W', 'true b'])
plt.show()

