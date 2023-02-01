## Package Deployment Tool

This is a tool for deploying python packages to PyPI. The script does the following:
```
1. Reads the package version from pyproject.toml
2. Increments the patch version number of the package
3. Removes any previous build files
4. Builds the new package
5. Uploads the package to PyPI
6. Offers the option to install the new version of the package
```

### How to use
```
1. Clone or download this repository
2. Make sure you have the required packages installed: dotenv, shutil, subprocess. You can install them by using the command pip install -r requirements.txt
3. make a token that has access to all your projects (scope) https://pypi.org/manage/account/token/, if you do not want to use a token replace "__token__" at the top to your username, and put your password where your_pypi_token would go.
4. Create a .env file in the root directory and add the following line:
TOKEN=<your_pypi_token>
5. Replace <your_pypi_token> with your PyPI token.
6. Run the script in the terminal by using the command python main.py
7. Enter the directory where your package is located
8. Choose whether you want to install the new version of the package or not.
```

## Note
Make sure that the package you want to deploy is in the same directory as pyproject.toml
The script assumes that you have already created a PyPI account and have your token ready.
you can see example supported packages in my other packages
