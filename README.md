# face_recognition
face recognition service used to identify people from a know data set

# Setup
after cloning the Repo just install the dependices first
<br>
<code>pip install -r requirments.txt </code> 
<br>
# How to use
to use it just run the command
<br>
<code>python app.py </code>
<br>
this will run the server and then u could use postman or curl for example to make a <strong>POST</strong> request to <code>localhost:5001/ </code> 
<br>if u change the port in the code for any reason then ofc change it in the url of the request.
<br>
the request should look something like this.
<br>
<code>curl --location --request POST 'localhost:5001/' \
--header 'Content-Type: multipart/form-data; boundary=--------------------------149287528197819264576957' \
--form 'original=@example_images/obama.jpg' \
--form 'captured=@example_images/obama.jpg'
</code>
<br> 
and this return a response
<code>
{
  "same_person": true
}
</code><br> if the two pics are of the same person ofcourse