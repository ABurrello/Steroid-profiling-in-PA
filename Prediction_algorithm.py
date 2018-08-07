from sklearn.ensemble import RandomForestClassifier
import scipy.io
import numpy as np
import pickle
filename = 'Forest_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print '\nWelcome to the prediction tool: please use points in decimal numbers (3.7 and not 3,7)'
print'-------------------------\n'
for i in [1,2,3]:
    Password = raw_input('Please insert password and press enter:\n')
    if Password == 'MicroAPA_JBAB':
        Steroids= ['Aldosterone [ng/mL]',
                '18-Oxocortisol [ng/mL]',
                '18-Hydroxycortisol [ng/mL]',
                '21-Deoxycortisol [ng/mL]',
                'Corticosterone [ng/mL]',
                '11-Deoxycorticosterone [ng/mL]',
                'Progesterone [ng/mL]',
                'Cortisol [ng/mL]',
                'Cortisone [ng/mL]',
                '11-Deoxycortisol [ng/mL]',
                '17-Hydroxyprogesterone [ng/mL]',
                'Pregnenolone [ng/mL]',
                'Androstenedione [ng/mL]',
                'DHEA [ng/mL]',
                'DHEA sulphate [ng/mL]']
        Query = np.zeros((1,15))
        Prediction_type = ['Micro-APA',
        'Macro-APA',
        'Bilateral Adrenal Hyperplasia']
        for i in range(len(Steroids)):
            String_to_print = 'Insert value of ' +Steroids[i]+' and press enter:\n'
            Query[0,i] = input(String_to_print)
        Prediction = loaded_model.predict(Query)
        print '------------'
        print 'The patient is predicted as ' + Prediction_type[Prediction[0]-1]
        break
    else:
        print 'Wrong password.'
