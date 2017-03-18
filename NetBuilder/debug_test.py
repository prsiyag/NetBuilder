#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 00:25:09 2017

@author: andresberejnoi
"""

from NeuralNet import Network, mean_squared_error
import numpy as np

#Some tests
def random_training_set():
    
    #Define input and output layer neurans
    numIn = 2
    numOut = 3
    #create random inputs and outputs
    np.random.seed(50)
    input_set = np.random.rand(1000,numIn)   #1000 samples where each sample has numIn features
    target_set = np.random.rand(1000,numOut)   
    
    net = Network(topology=[numIn,3,numOut])
    net.train(input_set=input_set,
              target_set=target_set,
              batch_size=0,
              epochs=10000)
    
def test_AND():
    
    #Define input and output layer neurans
    numIn = 2
    numOut = 1
    
    #num_samples = 4
    
    #Create training sets
    T,F = 1.,0.
    input_set = np.array([[F,F],
                          [F,T],
                          [T,F],
                          [T,T]])
    
    target_set = np.array([[F],
                           [F],
                           [F],
                           [T]])

    
    
    net = Network(topology=[numIn,3,numOut])
    net.set_outActivation_fun(func='sigmoid')
    net.train(input_set=input_set,
              target_set=target_set,
              batch_size=4,
              epochs=100)
    
    
    test_out = net.feedforward(input_set)
    print('TEST OUTPUT:')
    print(test_out)
    
    error = mean_squared_error(target=target_set,actual=test_out)
    print('ERROR:',error)
    
def test_XOR():
    
    #Define input and output layer neurans
    numIn = 2
    numOut = 1
    
    #num_samples = 4
    
    #Create training sets
    T,F = 1.,-1.
    input_set = np.array([[F,F],
                          [F,T],
                          [T,F],
                          [T,T]])
    
    target_set = np.array([[F],
                           [T],
                           [T],
                           [F]])

    
    
    net = Network(topology=[numIn,1,numOut])
    net.train(input_set=input_set,
              target_set=target_set,
              batch_size=4,
              epochs=200)
    
    
    test_out = net.feedforward(input_set)
    print('\nTEST OUTPUT:')
    print(test_out)
    
    error = mean_squared_error(target=target_set,actual=test_out)
    print('ERROR:',error)
    
if __name__=='__main__':
    #random_training_set()
    test_AND()
    #test_XOR()