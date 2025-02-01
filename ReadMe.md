# CafeWeb

CafeWeb is a full stack comprehensive web application designed to manage and streamline the operations of a cafe. This project includes various modules to handle different aspects of the cafe's operations, such as managing food and beverage items, handling delivery information, and view sold itmes.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Cafe Management**: Manage cafe operations adding food and beverage items.
- **Sold Item Model**:Admins can view items purchased by users, including payment price, payment mode, and user name.
- **Delivery Information**: A model for users to add their address, which is saved for each user. Admins can view the addresses in the default Django admin panel.
- **Add to Cart Feature**: Users can add items to their cart before proceeding to checkout.
- **Payment Feature**: Users can make payments with various payment modes.
- **User Authentication**: Secure user authentication and authorization.
- **Admin Interface**: Easy-to-use Django admin interface for managing the application.
## Project Structure

- [CafeWeb](http://_vscodecontentref_/1): Main project directory
  - [CafeApp/](http://_vscodecontentref_/2): Contains the cafe-related models, views, and templates
    - [admin.py](http://_vscodecontentref_/3): Admin configuration for the Cafe model
    - [apps.py](http://_vscodecontentref_/4): Application configuration
    - [migrations/](http://_vscodecontentref_/5): Database migrations
    - [models.py](http://_vscodecontentref_/6): Cafe model definition
    - [tests.py](http://_vscodecontentref_/7): Unit tests for the cafe app
    - [views.py](http://_vscodecontentref_/8): Views for handling cafe-related requests
  - [DeliveryInfo/](http://_vscodecontentref_/9): Contains the delivery-related models
    - [admin.py](http://_vscodecontentref_/10): Admin configuration for the Delivery model
    - [apps.py](http://_vscodecontentref_/11): Application configuration
    - [migrations/](http://_vscodecontentref_/12): Database migrations
    - [models.py](http://_vscodecontentref_/13): Delivery model definition
  - [Food_App/](http://_vscodecontentref_/16): Contains the food-related models
  - [Other_Beverage/](http://_vscodecontentref_/17): Contains the other beverage-related models
  - [SoldApp/](http://_vscodecontentref_/18): Contains the sold items-related models
  - [Tea_App/](http://_vscodecontentref_/19): Contains the tea-related models
  - `static/`: Contains static files (CSS, JavaScript)
  - `templates/`: Contains HTML templates
  - [CafeWeb](http://_vscodecontentref_/20): Contains project settings, URLs, and views
    - [settings.py](http://_vscodecontentref_/21): Project settings
    - [urls.py](http://_vscodecontentref_/22): URL routing for the project
    - [views.py](http://_vscodecontentref_/23): Views for handling user authentication and all pages
    - [wsgi.py](http://_vscodecontentref_/24): WSGI configuration for deployment
    - [asgi.py](http://_vscodecontentref_/25): ASGI configuration for deployment
  - [manage.py](http://_vscodecontentref_/26): Django's command-line utility for administrative tasks
  - [db.sqlite3](http://_vscodecontentref_/27): SQLite database file

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/CafeWeb.git
    cd CafeWeb
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv myenv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage

- **Admin Interface**: Access the admin interface at `http://127.0.0.1:8000/admin/` to manage the application.
- **User Interface**: Access the main application at `http://127.0.0.1:8000/`.

## Contributing

We welcome contributions to improve this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/4) file for more details.