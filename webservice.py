from flask import Flask
from flask import request
import json
import importlib
import sys
import csv
import os
import pandas

from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.model_factory import ModelFactory

DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

MODEL_PARAMS = {'aggregationInfo': {'days': 0,
                     'fields': [(u'timestamp', 'first'),
                                (u'heartrate', 'sum')],
                     'hours': 0,
                     'microseconds': 0,
                     'milliseconds': 0,
                     'minutes': 5,
                     'months': 0,
                     'seconds': 0,
                     'weeks': 0,
                     'years': 0},
 'model': 'HTMPrediction',
 'modelParams': {'anomalyParams': {u'anomalyCacheRecords': None,
                                   u'autoDetectThreshold': None,
                                   u'autoDetectWaitRecords': None},
                 'clParams': {'alpha': 0.050050000000000004,
                              'verbosity': 0,
                              'regionName': 'SDRClassifierRegion',
                              'steps': '1'},
                 'inferenceType': 'TemporalAnomaly',
                 'sensorParams': {'encoders': {u'raw_value': None,
                                               u'timestamp_dayOfWeek': None,
                                               u'timestamp_timeOfDay': None,
                                               u'timestamp_weekend': None,
                                               u'heartrate': {'clipInput': True,
                                                                  'fieldname': 'heartrate',
                                                                  'n': 272,
                                                                  'name': 'heartrate',
                                                                  'type': 'AdaptiveScalarEncoder',
                                                                  'w': 21
                                                                  }},
                                  'sensorAutoReset': None,
                                  'verbosity': 0
                                  },
                 'spEnable': True,
                 'spParams': {'columnCount': 2048,
                              'globalInhibition': 1,
                              'inputWidth': 0,
                              'numActiveColumnsPerInhArea': 40,
                              'potentialPct': 0.8,
                              'seed': 1956,
                              'spVerbosity': 0,
                              'spatialImp': 'cpp',
                              'synPermActiveInc': 0.05,
                              'synPermConnected': 0.1,
                              'synPermInactiveDec': 0.05015},
                 'tmEnable': True,
                 'tmParams': {'activationThreshold': 14,
                              'cellsPerColumn': 32,
                              'columnCount': 2048,
                              'globalDecay': 0.0,
                              'initialPerm': 0.21,
                              'inputWidth': 2048,
                              'maxAge': 0,
                              'maxSegmentsPerCell': 128,
                              'maxSynapsesPerSegment': 32,
                              'minThreshold': 11,
                              'newSynapseCount': 20,
                              'outputType': 'normal',
                              'pamLength': 3,
                              'permanenceDec': 0.1,
                              'permanenceInc': 0.1,
                              'seed': 1960,
                              'temporalImp': 'cpp',
                              'verbosity': 0},
                 'trainSPNetOnlyIfRequested': False},
 'predictAheadTime': None,
'version': 1}

app = Flask(__name__)

@app.route("/" , methods = ['POST'])


def getData():   

    model = ModelFactory.create(MODEL_PARAMS)
    model.enableInference({"predictedField" : "heartrate"})

    contentType = request.headers.get('Content-Type')

    if 'application/json' or 'application/xml' not in contentType:
       

        splitted   =(request.data).split("\r\n")
        print"model olustu"
        print "***********************************************"        
        
        for i in splitted:           

            splitted = i.strip().split(",")
            print i
            print splitted
            
            timestamp = str(splitted[0])
            rate = float(splitted[1])






            result = model.run({
            "timestamp" : timestamp,
            "heartrate" : rate
            })
            result1 = {'prediction': result.inferences["multiStepBestPredictions"][1] , 'anomalyScore' : result.inferences["anomalyScore"]}
            print result1


    else:
        print "Not Supported Type"







    ##print timestamp + "-->"+ str(prediction) + "-->" + str(anomalyScore) + "\n"


    return json.dumps({"status" : True})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    print('asd')
