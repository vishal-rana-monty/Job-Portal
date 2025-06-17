# JobPortal by Vishal Rana 
🚀 Project Setup Guide 

 Follow these steps to set up the project and run it locally:

🐍 1. Create a Virtual Environment: python -m venv venv

       

▶️ 2. Activate the Virtual Environment:
   -On Windows:
      venv\Scripts\activate


   -On macOS/Linux:
      source venv/bin/activate

📦 3. Install Required Packages: pip install -r requirements.txt
       

🛠 4. Apply Database Migrations:
       -python manage.py makemigrations
       -python manage.py migrate


💾 5. Load Initial Fixture Data:
       -python manage.py loaddata jobs/fixtures/jobcategory.json
       -python manage.py loaddata jobs/fixtures/skills.json

👤 6. Create a Superuser (Admin Access):  python manage.py createsuperuser
      

    You can access the admin panel at: http://127.0.0.1:8000/admin



🖥 7. Run the Development Server:  python manage.py runserver
      

    Visit http://127.0.0.1:8000 in your browser to view the project.
