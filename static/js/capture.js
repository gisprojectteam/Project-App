
    function startup() {
        video = document.getElementById('video');
        navigator.getUserMedia =( navigator.getUserMedia ||
                               navigator.webkitGetUserMedia ||
                               navigator.mozGetUserMedia ||
                               navigator.msGetUserMedia);
      if (navigator.getUserMedia){navigator.getUserMedia({
            video: true,
            audio: false
          },
          function(stream) {
              window.URL = window.URL || window.webkitURL;
              
              video.srcObject=stream;
  video.play();;
           
            video.play(); 
          }, function (error){
                console.warn(error);
            });
          }
      
      }
            
          
  window.addEventListener('load', startup);