  //
  // // Initialize Firebase
  // var config = {
  //   apiKey: "AIzaSyAc6xANvMdWV2TTJA_Z0Bnb26JYxySKSS8",
  //   authDomain: "smart-spirometer.firebaseapp.com",
  //   databaseURL: "https://smart-spirometer.firebaseio.com",
  //   projectId: "smart-spirometer",
  //   storageBucket: "smart-spirometer.appspot.com",
  //   messagingSenderId: "846679117231"
  // };
  // firebase.initializeApp(config);
  //
  function get_data(page,count){
   $.ajax({
          type: "POST",
          url: "http://localhost:8080/get_data",
          data: {
              page: page,
              count: count,
          }
      }).done(function (data) {
          console.log('get returned data');
          console.log(data);
          let obj_data = JSON.parse(data)
          // console.log(type(data));
          // console.log(data_return.name);
          let messageDiv = document.getElementById("value");
          messageDiv.innerHTML = obj_data.breath + '<br>' + obj_data.label + '<br>' + obj_data.timestamp;
          console.log(obj_data.breath);
          // handle_response(data);
      });
  }

  function handle_response(data){

  }

  get_data('page_user',1)
