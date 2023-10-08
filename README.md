# Background_Changer_Assistant
## This is a python code that you can randomly change your pc background photo with!

1. For using this repository, firstly, you need to clone or download the python code on your system!

2. Then, you need to sign up for an Unsplash account and start an app.
   - To get an API access key from Unsplash, you need to follow these steps:
   1. Register as a developer on the [Unsplash website](https://unsplash.com/documentation).
   2. Once you have registered, go to your apps and click on "New Application".
   3. Fill in the required details for your application.
   4. Initially, your application will be in demo mode and will be rate-limited to 50 requests per hour. This is perfect for demo apps, trying out the API, and for educational purposes.
   5. If you're ready to move to production mode, follow the "Apply for Production" instructions. If approved, your rate limit will be increased to the full amount.
   6. To authenticate requests, pass your application's access key via the HTTP Authorization header: `Authorization: Client-ID YOUR_ACCESS_KEY`. You can also pass this value using a 
 `client_id` query parameter: `https://api.unsplash.com/photos/?client_id=YOUR_ACCESS_KEY`.
  
 - For more information on how to use the Unsplash API, please refer to their [API documentation](https://unsplash.com/documentation).

3. In the next step, you need to embed your `YOUR_ACCESS_KEY` and the `path` that you want to store your image in the `background_changer.py` file.
   - Alternatively, you can change the time for changing the photo in the end of the code(it is set to 12 hours).

4. If you want the code to be run in the background follow these steps:
   - In the terminal, go to the directory where the code is saved.
   - Then, run this command `pythonw.exe background_changer.py`.

5. Also, if you want the code to be run every time you start your computer, follow these steps:
   1. Press **Windows key + R** to open the Run dialog box.
   2. Type **shell:startup** and press **Enter**. This will open the Startup folder.
   3. Right-click on an empty area in the folder and select **New > Shortcut**.
   4. In the "Create Shortcut" window, type the path to your Python script (e.g., "C:\path\to\your\script.py") and click **Next**.
   5. Give your shortcut a name (e.g., "My Python Script") and click **Finish**.

## Hope you have a lot of fun!
