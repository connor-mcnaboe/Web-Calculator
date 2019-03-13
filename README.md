# Web Calculator 

### About Web Calculator 

Web Calculator is a web based calculator that performs simple arithmetic operations. It is built using the Flask framework, which enables python-based web development. 

### Download

```
git clone https://github.com/zerodarkbirdy/Web-Calculator.git
```

### Installation

If you would like to install the required dependencies directly to your machine, change your directory to Web-Calculator/ and run: 

```
python3 setup.py
```

If you wish to create a virtual environment from which you will run the application, change your directory to Web-Calculator/ and run:
 

```
python3 -m venv wcvenv
```

If python 3.x is your defualt python ($PATH points to python 3.x), then drop the 3 in all pythonX commands. To activate the virtual environment you just created, jump to the documentation on the system you are using (below).

#### Unix Systems

To activate the virtual environment on a Unix system (Mac OSX or Linux), run: 

```
source wcvenv/bin/activate
```

Once the environment is activated then execute the setup file:
 
```
python3 setup.py
```

#### Windows Systems

To activate the virtual environment on a Windows system, run: 

```
wcvenv\Scripts\activate
```

Once the environment is activated then execute the setup file:
 
```
python3 setup.py
```

### Running the server 

To start the server, run (in the Web-Calculator directory): 

```
flask run 
```

### Troubleshooting 

For any errors or issues, please contact [connor.mcnaboe@uconn.edu](mailto:connor.mcnaboe@uconn.edu)
