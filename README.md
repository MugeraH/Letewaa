## Letewaa

## Description
This is a delivery App where the users can place a pizza order. The seller gets a notification when the buyer places an order. The seller then notifies the buyer that their order is being processed and will be delivered once done. The app consumes a weather API that notifies the app users on the day's weather. 

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* Sign up or sign in.
* Get a weather report and possible suggestions.
* Choose a supplier and get a menu.
* Be able to make an order and be notified once my order has been placed.


## Supplier Stories
These are the behaviours/features that the application implements for use by a supplier.

As a supplier I would like to:
* Sign up or sign in.
* Get notified of incoming orders.
* Be able to accept orders and notify the user.
* Be able to update the catalogue.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Customer/Supplier Authentication | **On demand** | Access Home Page |
| Display Suppliers | **Home page** | Clickable links to open the specific supplier |
| Display profile | **Click profile page** | Redirected to a page with your profile |
| Order | **On button click** | Item added to cart |
| Checkout | **Cart page** | Confirm order and get total |
| Supplier Page | **Home page** | Clickable links of incoming orders and catalogue update |
| Incoming Orders | **On button click** | Accept incoming orders and notify customer |
| Update Catalogue | **On button click** | Add items to catalogue and upload image |


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/MugeraH/Letewaa.git
        $ cd Letewaa

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test

## Technologies Used
* Python3.6
* Flask

## License & Copyright
© Hughes Mugera, Alice Githui, Dunstan Mmbehero, Bernice Twili
Licensed under [MIT License](LICENSE)