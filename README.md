# Virscape E-commerce Django

Virscape E-commerce is a fully functional e-commerce store built using the Django Framework. It features a secure payment checkout system implemented with the Stripe API.

## Technologies Used

- Django
- SQLite
- HTML
- Tailwind CSS
- JavaScript
- Stripe API

## Cloning the Repository

#1 Clone the repository using the command below :

```bash
git clone https://github.com/3N-VOY/Virscape_ecommerce_Django.git
```
#2 Move into the directory where we the project files are :

```bash
cd Virscape_ecommerce_Django-main
```
#3 Create a virtual environment :

-->First Install virtualenv
```bash
pip install virtualenv
```
-->Then create the virtual environment:
```bash
virtualenv envname
```
-->Activate the virtual environment :
```bash
envname\scripts\activate
```
4# Install the requirements :
 ```bash
pip install -r requirements.txt
```
#5 Replace STRIPE API Keys in settings.py:
 ```bash
STRIPE_PUB_KEY = 'INCLUDE YOUR KEY HERE'

STRIPE_PRIVATE_KEY = 'INCLUDE YOUR PRIVATE KEY HERE'
```
#6 Replace Stripe Key in cart/templates/checkout.html:
 ```bash
 var stripe = Stripe('INCLUDE YOUR KEY HERE');
```

#7 Run the App

 ```bash
python manage.py runserver
```

> The development server will run at: http://127.0.0.1:8000/
>
## App Preview:
![virscape_preview1](https://github.com/3N-VOY/Virscape_ecommerce_Django/assets/128035289/d3be4351-5e2f-4f96-92e3-1a7b83bb0f72)

![virscape_preview2](https://github.com/3N-VOY/Virscape_ecommerce_Django/assets/128035289/f9afe2ce-adc1-49e6-b88e-d3417bb7ab0f)

![virscape_preview3](https://github.com/3N-VOY/Virscape_ecommerce_Django/assets/128035289/721b5ed6-44e2-4b7c-986d-8988681a9a7f)

![virscape_preview4](https://github.com/3N-VOY/Virscape_ecommerce_Django/assets/128035289/cee0ad60-a361-4ca7-8137-0453fc70870e)

![virscape_preview5](https://github.com/3N-VOY/Virscape_ecommerce_Django/assets/128035289/d4f3a954-ed41-4767-8e13-c6e38ee75ca4)



