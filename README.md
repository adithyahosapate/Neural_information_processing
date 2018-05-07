# Methods to estimate Entropy rate in Neural Data
Implementation of some  algorithms to estimate entropy rate of neural data as well as modelling neuronal data in various ways.

##  Generating synthetic data

```
python3 generate_data.py
```

## Empirical Bayesian estimator

```
python3 empirical_bayesian_estimator.py <dataset in .txt format>
```

## Block Entropy estimator

```
python3 empirical_bayesian_estimator.py <dataset in .txt format> <outputfile name(with no extension)>
```

## Lempel Ziv estimator

```
python3 lz_estimator.py <dataset in .txt> <output image path>
```
## Modelling Neural Spike Trains

## Estimation of beta parameters

```
python3 beta_parameter_estimator.py <dataset in .mat> <prior alpha> <prior beta>
```


## LSTM

### Training the LSTM 

To train the LSTM from scratch on a dataset in the .mat format, run the following command 

```
python3 LSTM.py  -epochs <no. of epochs> -data <path to .mat file>
```

To retrain the LSTM with trained weights, run 

```
python3 LSTM.py  -weights <path to trained weights> -epochs <no. of epochs> -data <path to .mat file>
```

### Testing the LSTM

To test the LSTM with a particular dataset, run the following command

```
python3 test.py  -weights <path to trained weights> -d <path to .mat file>
```




