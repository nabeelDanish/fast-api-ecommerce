# FastAPI E-Commerce Application

This is a learning project where I have built a simple e-commerce application using FastAPI and SQLite database.

## Overview
The FastAPI E-Commerce Application is a web-based application that simulates an e-commerce platform. It provides basic functionalities such as browsing products, adding items to the cart, and placing orders. The application is built using the FastAPI framework, which is known for its high performance and ease of use. SQLite database is used to store the product and order information.

## Features
- User registration and authentication
- Product browsing and searching
- Product details display
- Shopping cart functionality
- Placing orders
- Order history

## Installation
1. Clone the repository: `git clone https://github.com/your-username/fastapi-ecommerce.git`
2. Navigate to the project directory: `cd fastapi-ecommerce`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate.bat`
   - For Unix or Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Run the application: `uvicorn main:app --reload`
7. Open your web browser and visit `http://localhost:8000`

## Usage
- Register a new user account or log in with an existing account.
- Browse the available products by navigating through different categories or using the search functionality.
- Click on a product to view its details.
- Add items to your cart by specifying the desired quantity.
- Review the items in your cart and proceed to checkout.
- Place an order by providing the necessary information.
- View your order history and track the status of your orders.

## Technologies Used
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- SQLite: A lightweight and self-contained database engine used for storing product and order information.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)