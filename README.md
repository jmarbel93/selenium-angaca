# selenium-angaca

Repo for selenium learning for Agaca

## Steps to Set Up

1. **Clone the Remote Repo**  
   We may start by cloning the remote repo like this:  
   ```bash  
   git clone https://github.com/jmarbel93/selenium-angaca.git  
   ```

2. **Install Python**  
   We're gonna need to install Python, which by default includes **Pip** that will come in handy later for installing some Python-related stuff:  
   ```bash  
   winget install Python.Python  
   ```

3. **Install Virtualenv**  
   Then we'll be needing to install **Virtualenv**:  
   ```bash  
   pip install virtualenv  
   ```

4. **Check Virtualenv Version**  
   And we can check the version:  
   ```bash  
   virtualenv --version  
   ```

5. **Create a Virtual Environment**  
   Then we create a virtual environment in the current folder like this:  
   ```bash  
   python -m venv venv  
   ```

6. **Activate the Virtual Environment**  
   And we activate it:  
   ```bash  
   venv\Scripts\activate  
   ```

7. **Install Dependencies**  
   Then we install **Selenium** and **Pytest** from our `requirements.txt`:  
   ```bash  
   pip install -r requirements.txt  
   
