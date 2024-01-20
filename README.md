# Auto-Fuzzer

## Introduction
AutoFuzzer: Smart contract auditing made efficient. It is a CLI tool integrated with ChatGPT that auto-generates Echidna test functions for automated testing. The result helps auditors and developers improve contract security. Streamline your workflow with our powerful solution.

## How to use


### Copy the example file and fill it with your OpenAI API Key
```bash
cp .env_example .env
```

### Install the project dependencies, this can be done inside a virtual environment
```bash
pip install -r requirements.txt
```

### Execute the tool on your smart contract
```bash
python main.py tests/flags.sol
```

### Outputs
You can find your smart contract with the echidna functions on the `outputs` folder of the repo


## Next steps

As a next step you can take the output of the tool and flatten that contract and execute it on Echidna to get the final result
