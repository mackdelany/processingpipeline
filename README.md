# Processing Pipeline

This a template with which you can build your own package to clean and process tabular data. The template allows you to create a flexible processing pipeline for easily iterating and experiment with features, data structure and model selection.

Take the raw data shown below as an example. Using our `data_parameters.py` file, we can easily encode what processes to execute on which features, and in what order. This includes multiple mechanisms for dealing with null values, renaming features, scaling, standardizing, custom functions, mapping new values and hot encoding.


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

Which outputs our processed DataFrame as given below. We can continue to adjust our `data_parameters.py` file to output new datasets as we add features and iterate on our processed dataset over time. More information on how to set the `data_parameters.py` is given further down the page.

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
