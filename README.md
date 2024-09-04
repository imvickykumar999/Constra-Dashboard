># `Vicks Constra` : [`Dashboard`](https://vicksconstra.pythonanywhere.com/frest-html-admin-template/html/vertical-menu-template/index.html)
>
> `Me` : Just like github pages, if i add index.html in repo, it makes webpage, is this feature available in pythonanywhere.com without using any framework?
>
> Like this : [`Deployed Main Page`](https://vicksconstra.pythonanywhere.com/)
>
>![image](https://github.com/user-attachments/assets/ed3e7537-7fab-46a7-887c-426cda64686e)
>
>`ChatGPT` : Yes, **PythonAnywhere** allows you to host simple static websites, similar to how GitHub Pages works, without the need for a web framework like Flask, Django, etc.

### Steps to Host a Static Website on PythonAnywhere:

1. **Upload your `index.html` file**:
   - Log in to PythonAnywhere.
   - Go to the **Files** section.
   - Upload your `index.html` (and any other files like CSS, JavaScript, images) directly to a directory in your PythonAnywhere account.

2. **Set up the Web App**:
   - Go to the **Web** tab.
   - Click **Add a new web app**.
   - Choose **Manual configuration** (this option is for setting up a static site without a framework).
   - Select **Python 3.x**, even though you're not using Python for a static website (this is a requirement, but you won't use it).
   - In the configuration, set the directory where your `index.html` and other static files are located as the root directory for the site.

3. **Configure Static Files**:
   - In the **Static files** section of the Web tab, add a new entry:
     - URL: `/` (this makes your `index.html` file accessible at the root URL).
     - Path: The directory where your `index.html` and other static files are located (e.g., `/home/yourusername/yourproject/`).

4. **Reload the Web App**:
   - After setting everything up, click the **Reload** button to activate the configuration.
   - Your static website should now be live, and you can access it at the URL provided by PythonAnywhere (usually `yourusername.pythonanywhere.com`).

### Summary:
On **PythonAnywhere**, you can easily host static HTML files without using any frameworks like Flask or Django. You just need to upload your files and configure the web app to serve static content, much like GitHub Pages.

> `Version 1.0` : [Released](https://github.com/imvickykumar999/vicksconstra/releases/tag/StaticDeployment)
>
>      unzip /home/vicksconstra/mysite/ConstraStaticDashboard.zip
>      find /home/vicksconstra -type d -exec chmod 755 {} +
>
>![image](https://github.com/user-attachments/assets/b64f6763-94b9-42a1-ab58-f0f324d8ff19)
