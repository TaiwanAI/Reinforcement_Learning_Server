from __future__ import print_function # In python 2.7
"""
The flask application package.
"""

import sys
from flask import Flask, render_template,jsonify, request
from qlearningAgents import QLearningAgent
app = Flask(__name__)

import FlaskWebProject1.views
actionFn = lambda x: actions
learner = QLearningAgent(actionFn=actionFn)
app = Flask(__name__)

@app.route('/observeTransition', methods=['POST'])
def observeTransition():
	oldState = request.json['oldState']
	
	lastAction = request.json['lastAction']
	
	currentState = request.json['currentState']
	
	reward = request.json['reward']
	

	oldState = tuple(oldState)
	currentState = tuple(currentState)
	lastAction = tuple(lastAction)

	learner.observeTransition(oldState, lastAction, currentState, reward)
	res = dict(status_code=200)
	return jsonify(res)

@app.route('/getAction', methods=['POST'])
def getAction():
	currentState = request.json['currentState']
	currentState = tuple(currentState)
	lastAction = learner.getAction(currentState)
	print(lastAction,file=sys.stderr)
	res = dict(lastAction=lastAction)
	return jsonify(res)