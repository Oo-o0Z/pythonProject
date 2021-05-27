Mondrian K-Anonymized
===========================
The project is modified from [Mondrian](https://github.com/qiyuangong/Mondrian)

## Usage

1. Download or Clone the project.
2. Modify `config.json` as you want.
3. At path of the project, run `python anonimized.py`.



## config.json

The project use json as the configuration file.

Example:

**WARNING**: (Don't add comments to the file, because we use python.json in the project which doesn't support json with comments)

```json
{   
    "inputData":{
        "dataPath": "data/adult.data",
        "qiIndex": [0, 1, 4, 5, 6, 8, 9, 13],
        "isCat": [false, true, false, true, true, true, true, true],
        "saIndex" : -1
    },
    "mode":{
        "model": "relax",
        "k": 10,
        "flag": ""
    }
}
```

### inputData

#### dataPath

- Type: `String`
- Default: `"data/adult.data"`

Path of the dataset prepared to anonymize.

Base path is where you put `anonymized.py`

#### qiIndex

- Type: `Array<int>`
- Default: `[]`

Index of Quasi-identifier of the dataset.

#### isCat

- Type: `Array<Boolean>`
- Default: `[]`

For each Quasi-identifier, if it is string, append true, if not, append false.

#### saIndex

- Type: `Int`
- Default: `-1`

Index of Sensative attribute.

### mode

#### model

- Type: `String, ["relax" | "strict"] `
- Default: `"relax"`

Choose anonymous model.

#### k

- Type: `Int`
- Default: `10`

Size of one anonymous group.

#### flag

- Type: `string, ["k" | "qi" | "data"]`
- Default: `""`

Choose anonymous flag.
