# qfinder
Helps you find available username

### Prerequisites

You need to install Python 3.6 or up


### Getting the project

1. Create project folder:
```
mkdir qfinderproject
cd qfinderproject
```
2. Clone the project:
```
git clone https://github.com/GokhanYilmaz44/qfinder.git
```
3. Create a virtual environment:
```
python3 -m venv env

if you are using MAC or Linux:
source env/bin/activate

or Windows OS:
.\env\Scripts\activate
```
4. Install all dependencies:
```
pip install -r requirements.txt
```
5. Create migration files:
```
cd qfinder
python manage.py makemigrations
```
6. Apply the migrations:
```
python manage.py migrate
```
7. Provide Initial Website data:
```
python manage.py loaddata categories.json
python manage.py loaddata websites.json
```
8. Run the project server:
```
python manage.py runserver 0:<any port you want to use>
[by default port is 8000]
```

## Authors
* **Gokhan YILMAZ** [profile](https://github.com/GokhanYilmaz44)

