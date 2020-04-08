# face_recognition
face recognition service used to identify people from a know data set

# Setup
after cloning the Repo just install the dependices first
<br>
<code>pip install -r requirments.txt </code> 
<br>
if it fails cuz of dlib - just excute these commands <br>
<code> sudo apt-get install build-essential cmake </code> <br>
<code> sudo apt-get install libgtk-3-dev </code> <br>
<code> sudo apt-get install libboost-all-dev </code>
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
<code>
curl --location --request POST 'https://fr-api.herokuapp.com//verify' \
--header 'Content-Type: application/json' \
--data-raw '{
	"original_face": "http://psce.pw/PTZZB", 
	"captured_face": "http://psce.pw/R82RD"
}'
</code>
<br> 
and this return a response
<code>
{
  "same_person": false
}
</code><br> if the two pics are of the same person ofcourse
