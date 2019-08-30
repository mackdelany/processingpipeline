# Processing Pipeline

This a template with which you can build your own package to clean and process tabular data. The template provides a flexible processing pipeline for easily iterating and experimenting with features, data structure and model selection. You can [check out the example data_parameters.py](https://github.com/mackdelany/processingpipeline/blob/master/processing/data_parameters.py) file to see how processing operations are mapped to features.

Take the raw data shown below as an example. Using our `data_parameters.py` file, we can encode what processes to execute on which features, and in what order. This includes multiple mechanisms for dealing with null values, renaming features, scaling, standardizing, custom functions, mapping new values and hot encoding.


| Animal | Habitat | AverageWeight  | ChineseZodiacYear | Domesticated | MaxLifespan |
| :---- |:------| :-----| :-------- |:-----|:-----|
| Dolphin | Ocean | 150 | NaN   | No | 45 |
| Whale     | Ocean     | 30000 | NaN     | No | 200  |  
| Dragon | Fantasy    | 10000 | 2012-01-01  | No      | 4500 |
| Tiger| Land | 200 | 2010-01-01  | No | 18 |
| Cat | NaN  |   4 | NaN  |    Yes |  16 |
| Unicorn | Fantasy   |  Nan | NaN | No  | 2000 |
| NaN | Land  |   120 | 2007-01-01     | No  | 60 |
| Ox| Land   |    600 | 2009-01-01 | Yes | 15 |


After encoding `data_parameters.py`, we can call `processingpipeline` to process our dataset:


``` python
import processingpipeline as pp
processed_data = pp.process_dataset('processingpipeline/data/example_raw_data.csv')
```

Which outputs our processed DataFrame as given below. Once set, we can continue to adjust our `data_parameters.py` file to output new datasets as we add features and iterate on our processed dataset over time. 

| Fantasy | Land | Ocean | AverageWeight | ChineseZodiacYear | Domesticated | MaxLifespan |
| :---- |:------| :-----| :-------- |:-----|:-----|:-----|
|    0  |   0  |    1  |    -0.569123     |     0     |        0   |      45.0 |
|    0  |   0  |    1   |    1.288061     |     0     |        0   |     200.0  |
|    1   |  0   |   0   |    0.902971   |      1       |      0     |  4500.0 |
|    0  |   1    |  0   |   -0.468284    |      1       |      0     |    18.0 |
|    0   |  1   |   0   |   -1.839539    |       0       |      1     |    16.0 |
|    1  |   0   |   0   |    0.769108     |       0       |      0     |  2000.0 |
|    0   |  1   |   0  |    -0.083195     |       1        |     1      |   15.0 |

Do note, that we can also export our processed data to a .csv file:

``` python
import processingpipeline as pp
pp.clean_and_return_dataset('processingpipeline/data/example_raw_data.csv','processed_data.csv') 
```

# Install and set up

To use processingpipeline as a template for a machine learning project; simply git clone this repo into your project folder - and edit away! 

Alternatively, if you'd like to install processingpipeline as a package, git clone the repo and execute the setup.py file from the command line while within the processingpipeline folder:

``` bash
python3 setup.py
```
