<h3>
Config
</h3>

<p>
First you need to create venv for this project.
Therefore, in the root of your project, you must type this command in your terminal to create and activate a venv environment for you.
</p>
<pre>
pipenv shell
</pre>

<p>
After activating venv you should install the <b>requirements.txt</b> packages. So type this command in your Terminal: 
</p>
<pre>
pip install -r requirements.txt
</pre>

<h3>
Run the project
</h3>

<p>
First of all, please enter the following command in the Terminal to make sure the project is configured correctly:
</p>
<pre>
python manage.py check
</pre>
<p>
You should see This message:
  <strong>
    <i>
      "System check identified no issues (0 silenced)."
    </i>
  </strong>
  <br>
</p>

<p>
You should run project. So type this command in Terminal:
</p>
<pre>
python manage.py grpcrunserver --dev
</pre>

<p>
Enter the following commands in the terminal to access the admin panel of the website:
</p>
<pre>
python manage.py createsuperuser
</pre>
<pre>
python manage.py runserver
</pre>

<p>
Now copy/paste this address in your browser URL bar:
</p>
<pre>
http://127.0.0.1:8000/
</pre>

<p>
After creating a superuser you can login into your admin panels.
</p>
<pre>
http://127.0.0.1:8000/admin/login/?next=/admin/
</pre>

<h4>
Congratulations, you ran the project correctly ✅
</h4>
