# Instructions

## Setting up your keys

1. Log in to [OpenAI](https://platform.openai.com/)
2. Go to [API Keys](https://platform.openai.com/api-keys)
3. Click on `Create new secret key`
4. Name your key
5. Set permissions to `All`
6. Click on `Create secret key`
7. Copy the key and paste it in an `environment variable` named exactly `OPENAI_API_KEY`:

    ```bash
    # Linux/MacOS/Bash on Windows
    export OPENAI_API_KEY="your-api-key-here"
    ```

    ```bash
    # Windows Command Prompt
    set OPENAI_API_KEY=your-api-key-here
    ```

    ```bash
    # Windows PowerShell
    $env:OPENAI_API_KEY="your-api-key-here"
    ```

8. Check if you have the variable set up correctly by running the following command in your terminal:

    ```bash
    # Linux/MacOS/Bash on Windows
    echo $OPENAI_API_KEY
    ```

    ```bash
    # Windows Command Prompt
    echo %OPENAI_API_KEY%
    ```

    ```bash
    # Windows PowerShell
    echo $env:OPENAI_API_KEY
    ```

9. To check if the key is set up correctly without revealing your key in your terminal, you can display it partially by running the following command:

    ```bash
    # Linux/MacOS/Git Bash on Windows
    echo ${OPENAI_API_KEY:0:3}...
    ```

    ```bash
    # Windows Command Prompt
    echo %OPENAI_API_KEY:~0,3%...
    ```

    ```bash
    # Windows PowerShell
    echo ($env:OPENAI_API_KEY).Substring(0,3) + "..."
    ```

10. Check if you have `sk-...` and not just `...`

>For more instructions on how to complete this in different Operational Systems, go to <https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key>

## Setup Virtual Environment
1. Setup a `Virtual Environment` for the project
   * [Tutorial](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
   * Run `python -m venv venv/` (Linux/MacOS) or `py -m venv venv/` (Windows) to create a virtual environment in your project's folder
2. Activate the virtual environment
   * venv [docs](https://docs.python.org/3/library/venv.html)
   * Run `source venv/bin/activate` or `. venv/bin/activate` (Linux/MacOS) or `source venv/scripts/activate` (Windows) to activate the virtual environment
3. Install the `transformers` package with `pip`
   * pip [docs](https://pip.pypa.io/en/stable/)
   * Run `pip install transformers` to install the `transformers` package
4. Install one of the Machine Learning frameworks compatible with `transformers`
   * Run `pip install 'transformers[torch]'`, `pip install 'transformers[tf-cpu]'` or `pip install 'transformers[flax]'` to install `PyTorch`, `TensorFlow 2.0` or `Flax` respectively
5. Test if your installation was successful
   * Run `python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I love you'))"` to test if the installation was successful
     * You should get an output similar to this: `[{'label': 'POSITIVE', 'score': 0.9998704791069031}]`
   * Run `python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I must confess: I have put pineapple on pizza'))"` to test if your model is thinking correctly
     * If you don't get a `NEGATIVE` sentiment from this, your model is definitely not thinking correctly (in my opinion)
6. Setup keys for recently created `Virtual Environment` (as needed).

>You can check more details about the installation process at <https://huggingface.co/docs/transformers/installation>
