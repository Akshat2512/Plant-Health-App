
       

const video = document.querySelector('video');

const n = navigator.mediaDevices;
var camId=[];
ls=null;
let i=0;


var t=document.getElementById("cameraList");

t.onchange = ()=>{
    stop()
    startCamera()
 }


function get_camera_list(){
    camId = []
    n.enumerateDevices().then(devices => {

        var videoDevices = devices.filter(function(device) {
                                        return device.kind === 'videoinput';
                                        });
        
        
        videoDevices.forEach(function(device) {
        if(device.label != '')
        {camId.push(device.deviceId);
        camId.push(device.label);}
    
        });
    
        for(let i = camId.length;i>0;i=i-2)
        {
            var x=document.getElementById("cameraList").innerHTML;
            document.getElementById("cameraList").innerHTML = x+"<option>"+camId[i-1]+"</option>";
        }
        startCamera();
    }); 
}

async function checkCameraAccess() {
    try {
        const stream = await n.getUserMedia({ video: true });
        // User granted access to the camera
        stream.getTracks().forEach(track => track.stop()); // Release the camera stream
        return true;
    } catch (error) {
        // User denied access or no camera available
        return false;
    }
}

checkCameraAccess().then(hasAccess => {
    if (hasAccess) {
        console.log('Camera access granted!');
        get_camera_list();
       

    } else {
        console.log('Camera access denied or not available.');
    }
});

function startCamera()
{   

    var changecamera = document.getElementById("cameraList").value;

     let index= camId.indexOf(changecamera);

     n.getUserMedia({video:{deviceId:{exact:camId[index-1]}, width: {ideal:256}, height:{ideal:256}}}).then(stream => {
                 video.srcObject = stream;
                 video.play();
                }).catch(error => { console.error('Error accessing media devices.', error); });
    return changecamera
} 


async function stop() {

    video.srcObject.getTracks().forEach(function(track) {
    video.pause();
    track.stop();
    });
    }
    
function stopCamera() {
    
        stop();
        var x = document.getElementById('st');
        x.onclick=() => { playCamera() };
        x.innerHTML = "<i class='fa-solid fa-play'></i>";
    
}
    
function playCamera() {

        startCamera();
        var x = document.getElementById('st');
        x.onclick = () => { stopCamera() };
        x.innerHTML = "<i class='fa-solid fa-stop'></i>";
}
    


$('#view').on('click', (e)=>{
    e.target.hidden = 'hidden';
    $('#close_results').eq(0)[0].hidden = false;
    $('#results').eq(0)[0].style.display = 'block';
})



$('#close_results').eq(0)[0].onclick = (e) => {
        $('#view').eq(0)[0].hidden = false;
        $('#close_results').eq(0)[0].hidden = 'hidden';
        $('#results').eq(0)[0].style.display = 'none';
    };

 
    


function update_data(data, dataURL, i)
{

let width=video.videoWidth;
let height=video.videoHeight;

var list_data = $('#results').eq(0)[0];


var input = `<div class="species">
                     <div><img src='${dataURL}' height = '${height/3}' width = '${width/3}'></img></div>
                     <div>
                        <div>Species: </div><div>${data['Species']}</div>
                        <div>Health Status: </div><div>${data['Health Status']}</div>
                        <div>Confidence: </div><div>${data['Confidence']}%</div>
                     </div>
             </div>`;

list_data.innerHTML = input + list_data.innerHTML;

hide_loading();

document.getElementById('cap').disabled = false;

list_data.style.display = 'flex';

$('#close_results').eq(0)[0].hidden = false;
$('#view').eq(0)[0].hidden = 'hidden';

}
     
function predict_disease(dataURL, i)
{  
    
   $.ajax({
            type: "POST",
            url: "api/script.php",
            data: {url1 : dataURL, val : i},
            success: function(response){
        
                show_loading('receiving');
                
                response = response.slice(1,-1);

                data = JSON.parse(response);
                console.log(data);
                update_data(data, dataURL, i);
            },
            error: function(xhr, status, error) {
                   console.error("Error executing Python script:", error);
            }

        })
       
}

function show_loading(t){
    var ld =document.getElementById("loading");
    ld.style.opacity='1';
    ld.style.transform = 'translateY(-70px)';
    ld.innerHTML = `<i class="fa-solid fa-spinner fa-spin-pulse"></i> ${t} ...&nbsp`;

    document.getElementById("cap").disabled = true;

}

function hide_loading(){
    var ld =document.getElementById("loading");
        ld.style.opacity='0';
        ld.style.transform = 'translateY(0px)';
        ld.innerHTML = `<i class="fa-solid fa-spinner fa-spin-pulse"></i> success ...&nbsp`;

        document.getElementById("cap").disabled = false;

}



function capture()
{       
        
        show_loading('sending data');
        
         $("#c").attr('width',256);
         $("#c").attr('height',256);
        var canvas = document.getElementById("c");
        canvas.getContext('2d').drawImage(video,0,0,256,256);
        const dataURL = canvas.toDataURL("image/png");
      
        predict_disease(dataURL, 0);    // call ajax to run CNN model using server side scripting (PHP)
       
           
}

document.getElementById('file-upload').onchange = (e) => {
     var files = e.target.files;
     
     show_loading('sending data');
     if(files)
     {
        [... files].forEach( (f, i) => {
            
          const reader = new FileReader();
          reader.onload = function(e){
               const imgURL = e.target.result;
               predict_disease(imgURL, i);
          }
          reader.readAsDataURL(f);

        })
     }
     console.log(files);

}


