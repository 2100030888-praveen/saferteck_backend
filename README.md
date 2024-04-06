# saferteck_backend
File Manager 

DESCRIPTION
	In this project, I handle files with specific names, using Django to store provided content that can be modified and viewed as needed. The interface is designed to be user-friendly, ensuring a seamless and enjoyable experience while interacting with the stored data.

Installation
	Clone the repository: git clone <repository_url>
	Navigate to the project directory: cd <project_directory>

Setup
	Create a virtual environment: python3 -m venv env
	Activate the virtual environment:
	On Windows: .\env\Scripts\activate
	On macOS and Linux: source env/bin/activate
	Install dependencies: pip install django
	Apply migrations: python manage.py migrate

Usage
	Start the development server: python manage.py runserver 8080
	Access the application in your web browser at http://127.0.0.1:8080/

Uploading Files
	On the homepage, we offer the option to create and upload files. By clicking on the "Create" button, users can generate a file with a specific name and content of their choice. This feature provides flexibility and convenience, allowing users to tailor their files according to their needs.

Viewing Files
	At home, there's this neat option called "Get Files." Clicking on it lets you see all the files that have been made up until now.

Updating Files
	Navigate to the view file then we have a modify the option so we can easily modify the content

