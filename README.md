# EXCHANGE RATES

Interact with the NBP API to retrieve exchange rate data using Python, Django (including Tests) and Swagger.

## Functions

Provides exchange rate in dependency for a given currency code, date and number of the last N quotations.

## Install

1. Download or clone
2. Run using Docker:  
  
   docker-compose up --build  
  
   or  
  
   Run manually:  
  * Create environment in source folder:  
   python -m venv venv  
  * Activate environment:  
   source venv/Scripts/activate  
  * Install requirements in source folder:  
   pip install -r requirements.txt  
  * Run app in source folder:  
   python manage.py runserver 8000  

3. Use browser for the next query example:  
   http://127.0.0.1:8000/paraphrase?tree=(S(NP(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter))(,%20,)(CC%20or)(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)))(,%20,)(VP(VBZ%20has)(NP(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets))(VP(VBN%20filled)(PP(IN%20with)(NP(NP%20(JJ%20trendy)%20(NNS%20bars))(,%20,)(NP%20(NNS%20clubs))(CC%20and)(NP%20(JJ%20Catalan)%20(NNS%20restaurants))))))))&limit=20
 
4. Run tests:  
   python manage.py test rephrase_api  
