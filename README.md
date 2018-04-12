# jyson
Command-Line JSON Parser for Python3

## Usage
### Examples
#### Input
`echo '{"key":"value"}' | ./jyson.py`
#### Output
`{'key': 'value'}`

#### Input
`echo '{"key":"value"}' | ./jyson.py key`
#### Output
`value`

### In general
#### Input 
`command | ./jyson.py key1 key2 ... keyn`

#### Output 
`commands_json_output['key1']['key2'][...]['keyn']`

