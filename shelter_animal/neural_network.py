"""
Kaggle - Shelter Animal Outcomes
Neural network example using Keras

To run on GPU:
THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python2 neural_network.py

Author: Cosmo Harrigan

This is a neural network model that only uses these 4 features as input: 
animal type, gender, age, hour. Breed, color and name are completely 
disregarded (but would likely improve the score if added to the model in 
an appropriate way). The animal type and gender are categorical features
and are converted into binary indicator variables, and the age and hour 
are real-valued features and are centered and scaled to unit variance. 
The neural network employs batch normalization and dropout regularization.
The training proceeds until validation loss stops improving (early stopping),
and then a checkpoint of the model with the best validation loss is used for
prediction.
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.optimizers import Adam

def calc_age_in_years(x):
    x = str(x)
    if x == 'nan': return 0
    age = int(x.split()[0])
    if x.find('year') > -1: return age
    if x.find('month')> -1: return age / 12.
    if x.find('week')> -1: return age / 52.
    if x.find('day')> -1: return age / 365.
    else: return 0

animals = pd.read_csv('train.csv')

# --- Extract the target and features:
'''
Target: 
- outcome type, indicator variables

Features:
(1) animal type, indicator variables
(2) gender, indicator variables
(3) age, real-valued, scaled
(4) hour, real-valued, scaled
'''

y = pd.get_dummies(animals.OutcomeType)
X = pd.get_dummies(animals.AnimalType)
X = pd.concat((X, pd.get_dummies(animals.SexuponOutcome)), axis=1)

animals.DateTime = pd.to_datetime(animals.DateTime)

X['years_old'] = animals.AgeuponOutcome.apply(calc_age_in_years)
X['hour'] = animals.DateTime.dt.hour

# --- Define the model:
'''
- ReLU activation function
- Batch Normalization
- Dropout Regularization
'''
model = Sequential()
model.add(Dense(512, input_dim=9, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

for i in range(3):
    model.add(Dense(512, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

model.add(Dense(5, activation='softmax'))

opt = Adam()
model.compile(loss='categorical_crossentropy', optimizer=opt)

# --- Train model:
X_train, X_test, y_train, y_test =\
    train_test_split(X, y, test_size=0.05, random_state=42)

# Centered and scale to unit variance
mean_age = X_train.years_old.mean()
std_age = X_train.years_old.std()

X_train.years_old -= mean_age
X_train.years_old /= std_age
X_test.years_old -= mean_age
X_test.years_old /= std_age

mean_hour = X_train.hour.mean()
std_hour = X_train.hour.std()

X_train.hour -= mean_hour
X_train.hour /= std_hour
X_test.hour -= mean_hour
X_test.hour /= std_hour

X_train, X_test, y_train, y_test =\
    X_train.values, X_test.values, y_train.values, y_test.values

# Save the model with the best validation loss, and stop training when the 
# validation loss stops improving
checkpointer = ModelCheckpoint(filepath="/tmp/weights.hdf5", verbose=1,
                               save_best_only=True)
early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=0,
                               mode='auto')

h = model.fit(X_train, y_train, nb_epoch=200, batch_size=128,
              show_accuracy=True, validation_data=(X_test, y_test),
              callbacks=[checkpointer, early_stopping])

plt.plot(h.history['loss'])
plt.plot(h.history['val_loss'])
plt.legend(['training loss', 'validation loss'])
plt.savefig('training.png')

print('Min validation loss achieved: {}'.format(np.min(h.history['val_loss'])))

# --- Generate submission:
model.load_weights('/tmp/weights.hdf5')

submission = pd.read_csv('test.csv')

X_submission = pd.get_dummies(submission.AnimalType)
X_submission =\
    pd.concat((X_submission, pd.get_dummies(submission.SexuponOutcome)), axis=1)

X_submission['years_old'] = submission.AgeuponOutcome.apply(calc_age_in_years)
X_submission.years_old -= mean_age
X_submission.years_old /= std_age

submission.DateTime = pd.to_datetime(submission.DateTime)
X_submission['hour'] = submission.DateTime.dt.hour
X_submission.hour -= mean_hour
X_submission.hour /= std_hour

print('Generating submission...')
proba = model.predict_proba(X_submission.values)
ids = submission['ID'].values

with open('submission.csv', 'w') as f:
    f.write('ID,Adoption,Died,Euthanasia,Return_to_owner,Transfer\n')
    for i, probs in zip(ids, proba):
        probas = ','.join([str(i)] + [str(p) for p in probs.tolist()])
        f.write(probas)
        f.write('\n')
    print('Wrote submission to file')

