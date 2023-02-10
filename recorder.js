var buttonRecord = document.getElementById("record");
var buttonStop = document.getElementById("stop");
var buttonClick = document.getElementById("Click")
var buttonpreview = document.getElementById("preview")

var myImage = document.getElementById("myImage");

//var image = document.getElementById("myImage");


buttonStop.disabled = true;
buttonpreview.disabled = true;

buttonRecord.onclick = function() {
    // var url = window.location.href + "record_status";
    buttonRecord.disabled = true;
    buttonStop.disabled = false;
    
    // disable download link
    var downloadLink = document.getElementById("download");
    downloadLink.text = "";
    downloadLink.href = "";

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "true" }));
};

buttonStop.onclick = function() {
    buttonRecord.disabled = false;
    buttonStop.disabled = true;    

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);

            // enable download link
            var downloadLink = document.getElementById("download");
            downloadLink.text = "localhost:5000//static/video.avi";
            downloadLink.href = "/static/video.avi";
            //downloadLink.href = "localhost:5000//static/video.avi"
        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};

buttonClick.onclick = function() {
    buttonClick.disabled = false;
    buttonRecord.disabled = false;
    buttonpreview.disabled = false;
        

    // XMLHttpRequest
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // alert(xhr.responseText);
            console.log("Hello");

            // enable download link
            //document.write("Hello");
            var downloadLink = document.getElementById("download");
            downloadLink.text = "localhost:5000/static/saved_img.jpg";
            downloadLink.href = "/static/saved_img.jpg";


            //document.getElementById("myImage").style.display = "block";
            //myImage.src="/static/saved_img.jpg"
            //myImage.src="/static/saved_img.jpg"

        }
    }
    xhr.open("POST", "/record_status");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status:""}));
};




document.getElementById("preview").addEventListener("click", function(){
    //alert("Button was clicked!");
    var myImage = document.getElementById("myImage");
    myImage.src="/static/saved_img.jpg";
    buttonpreview.disabled = true;
});




  

